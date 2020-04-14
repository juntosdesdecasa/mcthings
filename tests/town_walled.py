import sys

import mcpi.block
import mcpi.minecraft


from mcthings.town_wall import TownWall
from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a walled town")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 10

        wall_thick = 1

        town = Town(mc, pos)
        town.block = mcpi.block.BEDROCK
        town.build()
        # Position the wall to round the town
        pos.x += wall_thick + town.space + town.house_length
        pos.z -= (town.space + wall_thick)
        town_wall = TownWall(mc, pos)
        town_wall.block = mcpi.block.BRICK_BLOCK
        town_wall.town = town
        town_wall.thick = wall_thick
        town_wall.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
