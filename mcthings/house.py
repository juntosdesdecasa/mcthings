import mcpi

from .thing import Thing


class House(Thing):

    height = 3
    width = 5
    length = 5
    wall_width = 1
    door_size = 1

    def build(self):
        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        self.server.setBlocks(
            init_x, init_y, init_z,
            init_x + self.length-1, init_y + self.height-1, init_z + self.width-1,
            self.block)

        # Fill the cube with air so it becomes a kind of house
        self.server.setBlocks(
            init_x + self.wall_width, init_y, init_z + self.wall_width,
            init_x + self.length-1 - self.wall_width,
            init_y + self.height-1 - self.wall_width,
            init_z + self.width-1 - self.wall_width,
            mcpi.block.AIR)

        # Add a door
        self.server.setBlocks(
            init_x, init_y, init_z + self.wall_width,
            init_x + 1, init_y + self.door_size, init_z + self.door_size,
            mcpi.block.AIR)


