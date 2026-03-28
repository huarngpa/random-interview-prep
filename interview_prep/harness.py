from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class Case:
    name: str
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)
    expected: Any = None
    expected_exception: type[BaseException] | None = None


def assert_cases(
    solver: Callable[..., Any],
    cases: list[Case],
    *,
    normalizer: Callable[[Any], Any] | None = None,
) -> None:
    for case in cases:
        if case.expected_exception is not None:
            try:
                solver(*case.args, **case.kwargs)
            except case.expected_exception:
                continue
            except Exception as exc:  # pragma: no cover - defensive branch
                raise AssertionError(
                    f"{case.name}: expected {case.expected_exception.__name__}, "
                    f"got {type(exc).__name__}"
                ) from exc

            raise AssertionError(
                f"{case.name}: expected {case.expected_exception.__name__}, "
                "but no exception was raised"
            )

        actual = solver(*case.args, **case.kwargs)

        if normalizer is not None:
            actual = normalizer(actual)
            expected = normalizer(case.expected)
        else:
            expected = case.expected

        if actual != expected:
            raise AssertionError(
                f"{case.name}: expected {expected!r}, got {actual!r}. "
                f"args={case.args!r}, kwargs={case.kwargs!r}"
            )
