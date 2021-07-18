from __future__ import annotations


class _Counter:
    n: int

    def __init__(self: _Counter) -> None:
        self.n = 0

    def __iter__(self: _Counter) -> _Counter:
        return self

    def __next__(self: _Counter) -> int:
        result: int = self.n
        self.n += 1
        return result


class World:
    """A World object which manages entities, components, and processors."""

    _entity_counter: _Counter

    def __init__(self: World) -> None:
        """Initialize `World` with an entity counter."""
        self._entity_counter = _Counter()

    def create_entity(self: World) -> int:
        """
        Create an entity.

        :return: Entity Identifier
        """
        return next(self._entity_counter)
