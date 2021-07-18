"""Tests related to entity creation."""
from ecs import World

world: World = World()


def test_identifiers() -> None:
    """Ensure entity identifiers follow a predictable outcome."""
    entity_1 = world.create_entity()
    entity_2 = world.create_entity()

    assert entity_1 == 0
    assert entity_2 == 1
