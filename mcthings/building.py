# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi

from .house import House
from .thing import Thing


class Building(Thing):

    floors = 10
    width = 10
    house_mirror = False

    def create(self):

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        house_pos = mcpi.vec3.Vec3(init_x, init_y, init_z)
        init_height = init_y

        for i in range(0, self.floors):
            house = House(house_pos, self)
            self.add_child(house)
            house_pos.y = house.height * i + init_height
            house.width = self.width
            house.block = self.block
            house.mirror = self.house_mirror
            house.create()
            self._end_position = house.end_position
