import mcpi.block


class Thing:
    """ base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    """ block type used by the thing. Default to BRICK_BLOCK"""
    block_empty = mcpi.block.AIR

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    @property
    def server(self):
        """ Minecraft Python server connection """
        return self._server

    def __init__(self, server=None, position=None):
        """
        Create a thing
        :param server: Minecraft Python server in format host:port
        :param position: build position
        """

        self._position = position
        self._server = server

    def build(self):
        """
        Build the thing and show it in Minecraft at position coordinates

        :return:
        """
        pass

    def unbuild(self):
        """
        Unbuild the thing in Minecraft

        :return:
        """

        block = self.block
        self.block = self.block_empty
        self.build()
        self.block = block
