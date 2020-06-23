#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.river import River
from mcthings.world import World
from tests.base import TestBaseThing


class TestRiver(TestBaseThing):
    """Test River Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a river")

        pos = self.pos

        pos.x += 1

        river = River(pos)
        river.width = 3
        river.depth = 3
        river.length = 5
        river.build()
        river.unbuild()

        pos = river.end_position
        river = River(Vec3(pos.x, self.pos.y, pos.z))
        river.depth = 3
        river.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
