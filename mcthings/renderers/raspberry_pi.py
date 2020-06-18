# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import math
import sys

import mcpi
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
from minecraftstuff import MinecraftDrawing

from .renderer import Renderer
from ..memory_chunk import MemoryChunk


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

    def render_equal_blocks_chunk(self, chunk, pos):
        """ Render a chunk with all blocks equal and not rotating """
        block = chunk.blocks_ids[0]

        init_pos = pos
        end_pos = Vec3(pos.x + chunk.size.x-1, pos.y + chunk.size.y-1, pos.z + chunk.size.z-1)

        self.server.mc.setBlocks(init_pos.x, init_pos.y, init_pos.z,
                                 end_pos.x, end_pos.y, end_pos.z,
                                 block)

    def render_chunk(self, chunk, pos):
        """ Render chunk rotating it if needed """

        size_x = chunk.end_pos.x - chunk.init_pos.x
        size_y = chunk.end_pos.y - chunk.init_pos.y
        size_z = chunk.end_pos.z - chunk.init_pos.z

        init_x = chunk.init_pos.x
        init_y = chunk.init_pos.y
        init_z = chunk.init_pos.z

        blocks = chunk.blocks_ids
        data = chunk.blocks_data

        cos_degrees = math.cos(math.radians(self.rotate_degrees))
        sin_degrees = math.sin(math.radians(self.rotate_degrees))

        # TODO: Rotating must be done in memory, not in the render!

        def rotate_x(pos_x, pos_z):
            return pos_x * cos_degrees - pos_z * sin_degrees

        def rotate_z(pos_x, pos_z):
            return pos_z * cos_degrees + pos_x * sin_degrees

        for y in range(0, size_y):
            for z in range(0, size_z):
                for x in range(0, size_x):
                    i = x + size_x * z + (size_x * size_z) * y
                    b = blocks[i]
                    if b != 0:
                        if self.block == self._block_empty:
                            # Cleaning the schematic
                            b = 0
                        d = data[i] & 0b00001111  # lower 4 bits

                        if b in self.change_blocks:
                            b = self.change_blocks[b]

                        if self.rotate_degrees != 0:
                            rotated_x = init_x + rotate_x(x, z)
                            rotated_z = init_z + rotate_z(x, z)
                            self.server.mc.setBlock(rotated_x, init_y + y, rotated_z, b, d)
                            # chunk.end_position = mcpi.vec3.Vec3(rotated_x, init_y + y, rotated_z)
                        else:
                            self.server.mc.setBlock(init_x + x, init_y + y, init_z + z, b, d)
                            # chunk.end_position = mcpi.vec3.Vec3(init_x + x, init_y + y, init_z + z)

    def render(self, chunk_memory, pos):
        if MemoryChunk.chunk_equal(chunk_memory):
            self.render_equal_blocks_chunk(chunk_memory, pos)
        else:
            self.render_chunk(chunk_memory, pos)
