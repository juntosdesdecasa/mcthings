# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
from datetime import datetime

import mcpi
from mcpi.vec3 import Vec3
from nbt.nbt import NBTFile, TAG_List, TAG_Int, TAG_Short, TAG_Byte_Array, TAG_String

from mcthings.world import World

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def size_region(init_pos, end_pos):
    """
    Measure (size) the cuboid between init_pos and end_pos
    :param init_pos:
    :param end_pos:
    :return:
    """

    size_x = end_pos.x - init_pos.x + 1
    size_z = end_pos.z - init_pos.z + 1
    size_y = end_pos.y - init_pos.y + 1

    return Vec3(size_x, size_y, size_z)


def extract_region(init_pos, end_pos):
    """
    Extract a Minecraft world region with the id of the blocks

    :return: bytearrays for blocks ids and block data
    """

    size = size_region(init_pos, end_pos)

    blocks = World.renderer.get_blocks(Vec3(init_pos.x, init_pos.y, init_pos.z),
                                       Vec3(end_pos.x, end_pos.y, end_pos.z))
    blocks_list = list(blocks)

    # The order in getBlocks is z, x, y and for a Schematic it must be x, z, y
    block_list_ordered = []

    for y in range(0, size.y):
        x_by_z = []  # x, z plane for y

        for x in range(0, size.x):
            z_row = []
            for z in range(0, size.z):
                z_row.append(blocks_list[(x * size.z + z) + (size.x * size.z) * y])
            x_by_z.append(z_row)

        for z in range(0, size.z):
            for x in range(0, size.x):
                block_list_ordered.append(x_by_z[x][z])

    # Create the data_bytes
    data_bytes = bytearray()
    blocks_bytes = bytearray()
    for i in range(0, len(block_list_ordered)):
        blocks_bytes.append(block_list_ordered[i])
        data_bytes.append(0)

    return blocks_bytes, data_bytes


def extract_region_with_data(init_pos, end_pos):
    """
    Extract a Minecraft world region with the id and data of the blocks

    :return: bytearrays for blocks ids and block data
    """
    size = size_region(init_pos, end_pos)

    blocks_bytes = bytearray()
    data_bytes = bytearray()

    # Use the same loop than reading Schematic format: x -> z -> y
    for y in range(0, size.y):
        for z in range(0, size.z):
            for x in range(0, size.x):
                block_pos = mcpi.vec3.Vec3(init_pos.x + x, init_pos.y + y, init_pos.z + z)
                block = World.server.getBlockWithData(block_pos.x, block_pos.y, block_pos.z)
                blocks_bytes.append(block.id)
                data_bytes.append(block.data)

    return blocks_bytes, data_bytes


def build_schematic_nbt(init_pos, end_pos, block_data=False):
    """
    Creates a NBT Object with the schematic data

    :param init_pos: initial position for extracting the Schematic
    :param end_pos: end position for extracting the Schematic
    :param block_data: extract blocks ids and data (much slower)

    :return: The NBT object with the Schematic
    """
    size = size_region(init_pos, end_pos)

    # Profiling of Schematics export
    app_init = datetime.now()
    logging.info("Schematic: Exporting blocks: %i" % (size.x * size.y * size.z))

    # Prepare the NBT Object
    nbtfile = NBTFile()
    nbtfile.name = "Schematic"
    nbtfile.tags.append(TAG_Short(name="Width", value=size.x))
    nbtfile.tags.append(TAG_Short(name="Height", value=size.y))
    nbtfile.tags.append(TAG_Short(name="Length", value=size.z))
    nbt_blocks = TAG_Byte_Array(name="Blocks")
    nbtfile.tags.append(nbt_blocks)
    nbt_data = TAG_Byte_Array(name="Data")
    nbtfile.tags.append(nbt_data)

    # Additional fields need
    nbtfile.tags.append(TAG_String(name="Materials", value="Alpha"))
    nbtfile.tags.append(TAG_Int(name="'WEOriginX'", value=0))
    nbtfile.tags.append(TAG_Int(name="'WEOriginY'", value=0))
    nbtfile.tags.append(TAG_Int(name="'WEOriginZ'", value=0))
    nbtfile.tags.append(TAG_Int(name="'WEOffsetX'", value=0))
    nbtfile.tags.append(TAG_Int(name="'WEOffsetY'", value=0))
    nbtfile.tags.append(TAG_Int(name="'WEOffsetZ'", value=0))
    entities_list = TAG_List(name="Entities", type=TAG_Int)
    nbtfile.tags.append(entities_list)
    tile_entities_list = TAG_List(name="TileEntities", type=TAG_Int)
    nbtfile.tags.append(tile_entities_list)

    # Collect all blocks
    if block_data:
        (blocks_bytes, data_bytes) = extract_region_with_data(init_pos, end_pos)
    else:
        (blocks_bytes, data_bytes) = extract_region(init_pos, end_pos)

    nbt_blocks.value = blocks_bytes
    nbt_data.value = data_bytes

    total_time_min = (datetime.now() - app_init).total_seconds()
    logging.info("Schematic export finished in %.2f secs" % total_time_min)

    return nbtfile


def find_min_max_cuboid_vertex(vertex, vertex_opposite):
    """
    Find the min vertex and the max vertex for a given cuboid
    defined from two opposite vertexes

    :param vertex: a vertex in the cuboid
    :param vertex_opposite: the opposite vertex of the cuboid
    :return: vertex_min, vertex_max
    """

    vertex_min = vertex_max = None

    width = abs(vertex_opposite.x - vertex.x) + 1
    height = abs(vertex_opposite.y - vertex.y) + 1
    length = abs(vertex_opposite.z - vertex.z) + 1

    # Find all vertex in the up face: up1 and up3 are already known
    up1 = vertex_opposite
    up3 = Vec3(vertex.x, vertex_opposite.y, vertex.z)
    if vertex.y > vertex_opposite.y:
        up1 = vertex
        up3 = Vec3(vertex_opposite.x, vertex.y, vertex_opposite.z)
    # Now we need to find the two other vertexes up2, up4
    # Looking at up1 there are two options for up2 and up4
    up1x1 = Vec3(up1.x + (width - 1), up1.y, up1.z)
    up1x2 = Vec3(up1.x - (width - 1), up1.y, up1.z)
    up1z1 = Vec3(up1.x, up1.y, up1.z + (length - 1))
    up1z2 = Vec3(up1.x, up1.y, up1.z - (length - 1))
    # Looking at up3 there are two options for up2 and up4
    up3x1 = Vec3(up3.x + (width - 1), up3.y, up3.z)
    up3x2 = Vec3(up3.x - (width - 1), up3.y, up3.z)
    up3z1 = Vec3(up3.x, up3.y, up3.z + (length - 1))
    up3z2 = Vec3(up3.x, up3.y, up3.z - (length - 1))
    # The right vertex is the common one for up2 and up4
    if up1x1 == up3z1 or up1x1 == up3z2:
        up2 = up1x1
    elif up1x2 == up3z1 or up1x2 == up3z2:
        up2 = up1x2
    else:
        raise RuntimeError("Bad min an max vertex for cuboid")
    if up1z1 == up3x1 or up1z1 == up3x2:
        up4 = up1z1
    elif up1z2 == up3x1 or up1z2 == up3x2:
        up4 = up1z1
    else:
        raise RuntimeError("Bad min an max vertex for cuboid")

    # Now select the min and max vertex for up face
    x_min = x_max = up1.x  # init with a possible value
    z_min = z_max = up1.z  # init with a possible value
    for v in [up1, up2, up3, up4]:
        x_max = v.x if v.x > x_max else x_max
        x_min = v.x if v.x < x_min else x_min
        z_max = v.z if v.z > z_max else z_max
        z_min = v.z if v.z < z_min else z_min

    # And now select the min and max vertex
    for v in [up1, up2, up3, up4]:
        if v.x == x_min and v.z == z_min:
            vertex_min = Vec3(v.x, v.y - (height - 1), v.z)
        if v.x == x_max and v.z == z_max:
            vertex_max = Vec3(v.x, v.y, v.z)

    if vertex_min is None or vertex_max is None:
        raise RuntimeError("Bad min an max vertex for cuboid")

    return vertex_min, vertex_max


