"""Entity-Component System, which manages entities, components, and processors."""
from ._component import Component
from ._world import World

__all__ = ["World", "Component"]
