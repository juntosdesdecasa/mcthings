#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.schematic import Schematic
from mcthings.world import World
from integration.base import TestBaseThing


class TestRotateSchematic(TestBaseThing):
    """Test to rotate an Schematic """

    def test_build(self):
        World.renderer.post_to_chat("Loading and building a schematic")

        pos = self.pos

        pos.x += 3
        boat = Schematic(pos)
        boat.file_path = "schematics/pirate-boat.schematic"
        boat.build()

        rot_boat = Schematic(pos)
        rot_boat.file_path = "schematics/pirate-boat.schematic"
        rot_boat.create()
        rot_boat.rotate(90)
        rot_boat.render()

        rot_boat = Schematic(pos)
        rot_boat.file_path = "schematics/pirate-boat.schematic"
        rot_boat.create()
        rot_boat.rotate(180)
        rot_boat.render()

        rot_boat = Schematic(pos)
        rot_boat.file_path = "schematics/pirate-boat.schematic"
        rot_boat.create()
        rot_boat.rotate(270)
        rot_boat.render()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
