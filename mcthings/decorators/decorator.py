# TODO: at some point this must be a real Singleton

from mcpi.minecraft import Minecraft
# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block

from mcthings.blocks_memory import BlocksMemory
from mcthings.world import World


class Decorator:
    """
    A Decorator is able to decorate a Thing based on its characteristics.

    If a Thing has decorators, they will be called after the build of the Thing.
    """

    block = mcpi.block.AIR
    """ Base block for the decorator """

    def __init__(self, thing):
        self._blocks_memory = BlocksMemory()
        self._thing = thing

    def create(self):
        """
        Create the decorator

        :return:
        """

    def set_block(self, pos, block, data=None):
        self._blocks_memory.set_block(pos, block, data)

    def set_blocks(self, init_pos, end_pos, block):
        """ Add a cuboid with the same block for all blocks and without specific data"""
        self._blocks_memory.set_blocks(init_pos, end_pos, block)

    def render(self):
        """
        Renders the decorator

        :return:
        """
        World.renderer.render(self._blocks_memory)

    def decorate(self):
        """
        Decorate the thing

        :return:
        """

        self.create()
        self.render()
