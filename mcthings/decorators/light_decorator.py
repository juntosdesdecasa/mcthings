# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import math

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.block import Block
from .decorator import Decorator


class LightDecorator(Decorator):
    """
    A Light Decorator to illuminate the Thing.

    Add lights (torches) to Thing so you can see inside it
    """

    def create(self):
        """
        Add a torch in the center of the Thing

        :return:
        """

        thing_end = self._thing.end_position
        thing_start = self._thing.position

        center_pos_x = thing_start.x + math.floor((thing_end.x - thing_start.x) / 2)
        center_pos_y = thing_start.y + math.floor((thing_end.y - thing_start.y) / 2)
        center_pos_z = thing_start.z + math.floor((thing_end.z - thing_start.z) / 2)

        self.set_block(Vec3(center_pos_x, center_pos_y, center_pos_z), mcpi.block.TORCH)
