# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# TODO: at some point this must be a real Singleton
from mcpi.vec3 import Vec3


class BlocksMemory:
    """
    Memory of the blocks inside a Thing.

    It must include the blocks ids, blocks data and size of the thing
    """

    blocks_ids = []
    blocks_data = []
    size = Vec3()
