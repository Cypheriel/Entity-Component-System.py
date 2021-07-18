"""Tests related to entity creation."""
from dataclasses import dataclass

from ecs import Component, World


@dataclass
class Position(Component):
    """Position component."""

    x: int
    y: int


def test_identifiers() -> None:
    """Ensure entity identifiers follow a predictable outcome."""
    world: World = World()

    assert world.create_entity() == 0
    assert world.create_entity() == 1


def test_component_identifiers() -> None:
    """Ensure entity component identifiers match entity identifiers."""
    world: World = World()

    world.create_entity(Position(x=0, y=0))  # Entity-0
    world.create_entity(Position(x=99, y=99))  # Entity-1

    for position in world.get_component(Position):
        predicted_position = [(0, 0), (99, 99)][position.entity_id]

        assert predicted_position == (position.x, position.y)
