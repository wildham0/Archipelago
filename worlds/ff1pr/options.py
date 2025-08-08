import logging
from dataclasses import dataclass
from typing import Dict, Any, TYPE_CHECKING

from decimal import Decimal, ROUND_HALF_UP

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections, \
                     PerGameCommonOptions, OptionGroup, Removed, Visibility, NamedRange
if TYPE_CHECKING:
    from . import FF1pixelWorld


class ShuffleGearShops(DefaultOnToggle):
    """
    Shuffle the content of all Weapon Shops together, and do the same for Armor Shops.
    """
    internal_name = "shuffle_gear_shops"
    display_name = "Shuffle Gear Shops"

@dataclass
class FF1pixelOptions(PerGameCommonOptions):
    # generation options
    shuffle_gear_shops: ShuffleGearShops

grouped_options = [
    OptionGroup("Base Options", [
        ShuffleGearShops,
    ])]

presets = {
    "Starter": {
        "shuffle_gear_shops": True,
    }}