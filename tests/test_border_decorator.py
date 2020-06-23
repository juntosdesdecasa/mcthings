#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi
import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.block import Block
from mcthings.decorators.border_decorator import BorderDecorator
from mcthings.fence import Fence
from mcthings.house import House
from mcthings.pyramid import Pyramid
from mcthings.river import River
from mcthings.scene import Scene
from mcthings.town import Town
from mcthings.world import World
from tests.base import TestBaseThing


class TestBorderDecorator(TestBaseThing):
    """ Test Border Decorator """

    def test_build(self):
        World.renderer.post_to_chat("Building a block with a border")

        pos = self.pos
        pos.x += 2

        # Add a border around an scene
        Block(pos)
        # Block(Vec3(pos.x+1,  pos.y, pos.z))
        p = Pyramid(pos)
        p.height = 5
        House(pos)
        river = River(pos)
        river.length = 5
        init_scene = World.first_scene()
        init_scene.build()

        # Add a Railway around the scene
        border = BorderDecorator
        border.block = mcpi.block.RAIL
        border.margin = 5
        init_scene.add_decorator(border)
        init_scene.decorate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
