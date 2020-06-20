#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.blocks_gallery import BlocksGallery
from mcthings.world import World
from tests.base import TestBaseThing


class TestBlocksGallery(TestBaseThing):
    """Test  Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building a blocks gallery with all available blocks")

        pos = self.pos

        pos.x += 1

        gallery = BlocksGallery(pos, self.renderer)
        gallery.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
