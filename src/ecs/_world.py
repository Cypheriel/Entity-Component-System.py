from __future__ import annotations

from typing import Generator, Type, TypeVar

from ._component import Component

T = TypeVar("T")


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
    _entities: dict[int, Component]
    _components: list[Component]

    def __init__(self: World) -> None:
        """Initialize `World` with an entity counter."""
        self._entity_counter = _Counter()
        self._entities = {}
        self._components = []

    def create_entity(self: World, *components: Component) -> int:
        """
        Create an entity.

        :return: Entity Identifier
        """
        entity_id: int = next(self._entity_counter)

        for component in components:
            component.entity_id = entity_id
            self._components.append(component)

        return entity_id

    def get_component(self: World, component_type: Type[T]) -> Generator[T, None, None]:
        """
        Query components for components of matching type. Useful in processors.

        :param component_type: Component subclass
        :return: Components of matching type
        """
        for component in self._components:
            if isinstance(component, component_type):
                yield component
