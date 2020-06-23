# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
from mcpi.vec3 import Vec3

from mcthings.world import World
from mcthings.thing import Thing


class Sphere(Thing):

    radius = 5
    """ radius of the Sphere """

    def build(self):
        World.renderer.server.drawing.drawSphere(
            self.position.x + self.radius,
            self.position.y + self.radius - 1,
            self.position.z + self.radius,
            self.radius,
            self.block)

        end_x = self.position.x + 2 * self.radius
        end_y = self.position.y + 2 * self.radius
        end_z = self.position.z + 2 * self.radius

        self._end_position = Vec3(end_x, end_y, end_z)


class SphereHollow(Thing):

    radius = None
    """ radius of the Hollow Sphere """
    height = 0

    def build(self):
        World.renderer.server.drawing.drawHollowSphere(
            self.position.x + self.radius,
            self.position.y + self.radius - 1,
            self.position.z + self.radius,
            self.radius,
            self.block)

        end_x = self.position.x + 2 * self.radius
        end_y = self.position.y + 2 * self.radius
        end_z = self.position.z + 2 * self.radius

        self._end_position = Vec3(end_x, end_y, end_z)
