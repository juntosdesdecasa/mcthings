import mcpi

from .thing import Thing


class BlocksGallery(Thing):

    # https://www.minecraftinfo.com/idlist.htm
    MAX_BLOCK_NUMBER = 247

    def build(self):
        """
        Show all possible block types in a line
        :return:
        """

        for i in range(1, self.MAX_BLOCK_NUMBER):
            self.server.setBlock(self.position.x + i, self.position.y,
                                 self.position.z, mcpi.block.Block(i))
