# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi
from mcpi.vec3 import Vec3

from .thing import Thing


class Fence(Thing):
    """
    Build a block plane and empty it to create the fence
    """

    fence_space = 5
    """ Space between the fence and the thing fenced """
    thick = 1
    height = None
    thing = None

    def create(self):
        """
        Create a fence around the configured thing
        :return:
        """
        if self.thing is None:
            raise RuntimeError("Thing to be fenced is not defined")

        self.add_child(self.thing)

        init_x = self.thing.position.x - self.fence_space - self.thick
        init_y = self.thing.position.y
        init_z = self.thing.position.z - self.fence_space - self.thick

        self._position = Vec3(init_x, init_y, init_z)

        end_x = self.thing.end_position.x + self.fence_space + self.thick
        end_y = self.thing.end_position.y
        if self.height:
            end_y = self.thing.position.y + (self.height - 1)
        end_z = self.thing.end_position.z + self.fence_space + self.thick

        self._end_position = Vec3(end_x, end_y, end_z)

        self.set_blocks(
            Vec3(init_x, init_y, init_z),
            Vec3(end_x, end_y, end_z),
            self.block.id)

        # Fill the prism with air to became a rectangular wall
        self.set_blocks(
            Vec3(init_x + self.thick, init_y, init_z + self.thick),
            Vec3(end_x - self.thick, end_y, end_z - self.thick),
            mcpi.block.AIR.id)

        # Rebuild the thing because it is destroyed when emptying the fence
        # if we are not removing the fence
        if self.block.id != mcpi.block.AIR.id:
            self.thing.create()
