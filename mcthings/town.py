import mcpi

from .thing import Thing
from .house import House


class Town(Thing):

    houses = 4
    house_width = 5
    house_length = 5
    house_height = 3
    space = 3
    """space between the town houses"""

    def build(self):
        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        house_pos = mcpi.vec3.Vec3(init_x, init_y, init_z)

        for i in range(0, self.houses):
            house = House(self.server, house_pos)
            house.width = self.house_width
            house.length = self.house_length
            house.height = self.house_height
            house.block = self.block
            house.build()
            house_pos.z += self.house_width + self.space

        # Fill the end_position
        end_x = init_x + self.house_length
        end_y = init_y + self.house_height
        end_z = house_pos.z - self.space

        self._end_position = mcpi.vec3.Vec3(end_x, end_y, end_z)
