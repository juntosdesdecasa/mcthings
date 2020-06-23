# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import unittest

import mcpi

from mcthings.renderers.raspberry_pi import _Server

from mcthings.renderers.raspberry_pi import RaspberryPi
from mcthings.world import World


class TestBaseThing(unittest.TestCase):
    """ Integration tests for McThings """

    BUILDER_NAME = "ElasticExplorer"

    MC_SEVER_HOST = "localhost"
    MC_SEVER_PORT = 4711

    @classmethod
    def setUpClass(cls):

        try:
            World.renderer = RaspberryPi(cls.MC_SEVER_HOST, cls.MC_SEVER_PORT)
        except mcpi.connection.RequestError:
            logging.error("Can't connect to Minecraft server " + cls.MC_SEVER_HOST)
            sys.exit(1)

    def setUp(self):
        server = World.renderer.server
        self.pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(self.BUILDER_NAME))

