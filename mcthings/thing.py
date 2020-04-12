import mcpi


class Thing:
    """ Base class for all objects in mcthings library """

    block = None
    block_empty = mcpi.block.AIR
    position = None
    server = None

    def __init__(self, block=None, position=None, server=None):
        self.block = block
        self.position = position
        self.server = server

    def build(self):
        pass

    def clean(self):
        block = self.block
        self.block = self.block_empty
        self.build()
        self.block = block
