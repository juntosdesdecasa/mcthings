import sys

import mcpi.block
import mcpi.minecraft


from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a town")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

        town = Town(mc, pos)
        town.block = mcpi.block.BEDROCK
        town.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
