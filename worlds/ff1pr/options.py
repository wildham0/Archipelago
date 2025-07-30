import logging
from dataclasses import dataclass
from typing import Dict, Any, TYPE_CHECKING

from decimal import Decimal, ROUND_HALF_UP

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections, \
                     PerGameCommonOptions, OptionGroup, Removed, Visibility, NamedRange
if TYPE_CHECKING:
    from . import FF1pixelWorld


class VanillaChestPriority(DefaultOnToggle):
    """
    bla  bla
    """
    internal_name = "chest_priority"
    display_name = "Prioritize Vanilla Chests"

@dataclass
class FF1pixelOptions(PerGameCommonOptions):
    # generation options
    chest_priority: VanillaChestPriority

groups = [
    OptionGroup("Base Options", [
        VanillaChestPriority,
    ])]

presets = {
    "Vanilla-like": {
        "chest_priority": True,
    }}