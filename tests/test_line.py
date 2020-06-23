#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.line import Line
from mcthings.world import World
from tests.base import TestBaseThing


class TestLine(TestBaseThing):
    """Test Line Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a line")

        pos = self.pos

        pos.x += 1
        line = Line(pos)
        line.width = 2
        line.block = mcpi.block.SAND
        line.length = 10
        line.width = 1
        line.build()

        line = Line(line.end_position)
        line.width = 2
        line.block = mcpi.block.STONE
        line.build()

        line = Line(line.end_position)
        line.length = 10
        line.width = 2
        line.block = mcpi.block.SAND
        line.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
