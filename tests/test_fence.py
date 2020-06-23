#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi
import mcpi.block

from mcthings.block import Block
from mcthings.decorators.border_decorator import BorderDecorator
from mcthings.fence import Fence
from mcthings.house import House
from mcthings.pyramid import Pyramid
from mcthings.scene import Scene
from mcthings.town import Town
from mcthings.world import World
from tests.base import TestBaseThing


class TestFence(TestBaseThing):
    """Test Fence Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a walled town")

        pos = self.pos

        pos.x += 10

        town = Town(pos)
        town.houses = 3
        town.block = mcpi.block.WOOD
        town.house_width = 10
        town.house_length = 10
        town.house_height = 10
        town.build()

        # Build the wall to round the town
        fence = Fence(None)
        fence.block = mcpi.block.GOLD_BLOCK
        fence.thing = town
        fence.thick = 4
        fence.height = 5
        fence.build()

        pos.x += 30
        pyr = Pyramid(pos)
        pyr.build()
        fence = Fence(None)
        fence.thing = pyr
        fence.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
