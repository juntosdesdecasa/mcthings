from .thing import Thing


class Block(Thing):

    def build(self):
        self.server.setBlock(self.position.x, self.position.y,
                             self.position.z, self.block)
