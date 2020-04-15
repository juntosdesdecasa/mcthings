from .thing import Thing


class Wall(Thing):
    height = 5
    length = 10
    width = 2

    def build(self):
        self.server.setBlocks(
            self.position.x, self.position.y, self.position.z,
            self.position.x+self.length-1,
            self.position.y+self.height-1,
            self.position.z+self.width-1,
            self.block)
