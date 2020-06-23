#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.wall import Wall
from mcthings.world import World
from tests.base import TestBaseThing


class TestWall(TestBaseThing):
    """Test Wall Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a wall")

        pos = self.pos

        pos.x += 1

        wall = Wall(pos)
        wall.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
