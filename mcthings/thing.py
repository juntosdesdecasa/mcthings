import mcpi.block


class Thing:
    """ Base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    block_empty = mcpi.block.AIR
    server = None

    @property
    def position(self):
        return self._position

    def __init__(self, server=None, position=None):
        """
        Create a thing
        :param server: Minecraft server in format host:port
        :param position: build position
        """

        self._position = position
        self.server = server

    def build(self):
        """
        Build the thing and show it in Minecraft at position coordinates.

        :return:
        """
        pass

    def unbuild(self):
        """
        Unbuild the thing in Minecraft.

        :return:
        """

        block = self.block
        self.block = self.block_empty
        self.build()
        self.block = block
