import mcpi

from .thing import Thing
from .house import House


class Building(Thing):

    floors = 10
    width = 10

    def build(self):
        init_x = self.position.x + self.width / 1.5
        init_y = self.position.y
        init_z = self.position.z - self.width / 2

        house_pos = mcpi.vec3.Vec3(init_x, init_y, init_z)

        for i in range(0, self.floors):
            house = House( self.server, house_pos)
            house_pos.y = house.height * i
            house.width = self.width
            house.build()
