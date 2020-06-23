#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import unittest


from mcthings.house import House
from mcthings.decorators.light_decorator import LightDecorator
from mcthings.world import World
from tests.base import TestBaseThing


class TestHouse(TestBaseThing):
    """Test House Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a house")

        pos = self.pos

        pos.x += 1

        house = House(pos)
        house.build()

        # Mirror house
        pos.x -= 10   # space between both houses
        house = House(pos)
        house.mirror = True
        house.build()
        # Add lights
        house.add_decorator(LightDecorator)
        house.decorate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
