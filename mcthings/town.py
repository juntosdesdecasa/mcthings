import mcpi

from .thing import Thing
from .house import House


class Town(Thing):

    houses = 4
    house_width = 5
    house_length = 5
    house_height = 3
    space = 3  # space between houses

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
            house.build()
            house_pos.z += self.house_width + self.space
