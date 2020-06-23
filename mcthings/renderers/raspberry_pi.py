# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import math
import sys

import mcpi
from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing

from .renderer import Renderer
from ..blocks_memory import BlocksMemory


class _Server:
    """
    A Server manages the connection with the Minecraft server.

    Every World must have a Server in which built the World.
    """

    def __init__(self, host="localhost", port="4711"):
        self._host = host
        self._port = port

        self._mc = Minecraft.create(address=host, port=port)
        self._drawing = MinecraftDrawing(self._mc)

    @property
    def drawing(self):
        """ Connection to MinecraftDrawing (only used in Things built with MinecraftDrawing)"""
        return self._drawing

    @property
    def mc(self):
        """ Connection to Minecraft """
        return self._mc


class RaspberryPi(Renderer):
    """
    Renderer implemented using the Raspberry Pi Python API
    https://www.stuffaboutcode.com/p/minecraft-api-reference.html

    """

    def __init__(self, host, port):
        try:
            self.server = _Server(host, port)
        except mcpi.connection.RequestError:
            logging.error("Can't connect to Minecraft/Minetest server %s:%s" % (host, port))
            sys.exit(1)

    def render_cuboid_memory(self, memory):
        """ Render a memory with all blocks equal in a filled cuboid """
        block = memory.blocks[0]

        init_pos, end_pos = memory.find_init_end_pos()

        self.server.mc.setBlocks(init_pos.x, init_pos.y, init_pos.z,
                                 end_pos.x, end_pos.y, end_pos.z,
                                 block.id)

    def render_memory(self, memory):
        """ Render memory """

        for block in memory.blocks:
            if block.data is not None:
                self.server.mc.setBlock(block.pos.x, block.pos.y, block.pos.z, block.id, block.data)
            else:
                self.server.mc.setBlock(block.pos.x, block.pos.y, block.pos.z, block.id)

    def render(self, blocks_memory):
        if BlocksMemory.memory_equal(blocks_memory) and blocks_memory.is_cuboid():
            self.render_cuboid_memory(blocks_memory)
        else:
            self.render_memory(blocks_memory)

    def post_to_chat(self, message):
        self.server.mc.postToChat(message)

    def get_block(self, pos):
        return self.server.mc.getBlock(pos.x, pos.y, pos.z)

    def get_blocks(self, init_pos, end_pos):
        return self.server.mc.getBlocks(init_pos.x, init_pos.y, init_pos.z, end_pos.x, end_pos.y, end_pos.z)
