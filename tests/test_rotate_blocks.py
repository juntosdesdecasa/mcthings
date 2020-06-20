#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.blocks import Blocks
from mcthings.collage import Collage
from tests.base import TestBaseThing


class TestRotateBlock(TestBaseThing):
    """ Test to rotate Blocks """

    def test_build(self):
        self.renderer.server._mc.postToChat("Building two blocks")

        pos = self.pos

        pos.x += 3
        blocks = Collage(pos, self.renderer)
        blocks.width = 7
        blocks.height = 2
        blocks.length = 3
        blocks.build()

        pos.x += 15
        blocks = Collage(pos, self.renderer)
        blocks.width = 7
        blocks.height = 2
        blocks.length = 5
        blocks.create()
        blocks.rotate(90)
        blocks.render()

        # Check that the blocks start and end point are correct
        init_blocks = Blocks(blocks.position, self.renderer)
        init_blocks.height = 5
        init_blocks.width = 1
        init_blocks.length = 1
        init_blocks.build()
        end_blocks = Blocks(blocks.end_position, self.renderer)
        end_blocks.height = 5
        end_blocks.width = 1
        end_blocks.length = 1
        end_blocks.build()

        try:
            blocks.rotate(45)
        except RuntimeError:
            logging.info("Detected right Exception for invalid %s degrees", str(45))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
