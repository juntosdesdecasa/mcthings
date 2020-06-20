#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.bridge import Bridge
from mcthings.world import World
from tests.base import TestBaseThing


class TestBridge(TestBaseThing):
    """Test Bridge Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building bridges")

        pos = self.pos

        bridge = Bridge(pos, self.renderer)
        bridge.large = 10
        bridge.height = 3
        bridge.width = 3
        bridge.block = mcpi.block.WOOD
        bridge.build()

        pos = bridge.end_position
        pos.x += 1
        pos.y = bridge.position.y
        bridge1 = Bridge(pos, self.renderer)
        bridge1.large = 10
        bridge1.block = mcpi.block.BEDROCK
        bridge1.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
