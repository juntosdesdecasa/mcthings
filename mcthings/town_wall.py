import mcpi

from .thing import Thing
from .wall import Wall


class TownWall(Thing):
    """
    Build a block plane and empty it to create the wall
    """

    height = 3
    wall_space = 5
    """Space between the wall and the houses in the town"""
    thick = 1
    town = None

    def build(self):

        if self.town is None:
            raise RuntimeError("Town is not defined")

        self._position = self.town.position
        self._end_position = self.town.end_position

        init_x = self.town.position.x - self.wall_space - self.thick
        init_y = self.town.position.y
        init_z = self.town.position.z - self.wall_space - self.thick

        end_x = self.town.end_position.x + self.wall_space + self.thick
        end_y = self.town.end_position.y
        end_z = self.town.end_position.z + self.wall_space + self.thick

        self.server.setBlocks(
            init_x, init_y, init_z,
            end_x, end_y, end_z,
            self.block)

        # Fill the prism with air to became a rectangular wall
        self.server.setBlocks(
            init_x + self.thick, init_y, init_z + self.thick,
            end_x - self.thick,
            end_y,
            end_z - self.thick,
            mcpi.block.AIR)
