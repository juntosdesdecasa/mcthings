# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo


class MemoryChunk:
    """
    Blocks memory for a Thing is split in memory chunks. Each chunk is a cuboid
    with a initial and end position, and the blocks to be drawn. The renderer will
    render each chunk independently.

    Blocks in memory are organized in width, length, height order.
    """

    def __init__(self, size, blocks_ids, blocks_data):
        """

        :param blocks_ids: blocks to be build
        :param blocks_data: data for the blocks
        :param size: size.x, size.y and size.z for the cuboid
        """

        self.blocks_ids = blocks_ids
        self.blocks_data = blocks_data
        self.size = size

    @classmethod
    def chunk_equal(cls, chunk):
        """ Check if all the blocks for a chunk are equal """
        equal = True
        block = None
        data = None

        for i in range(0, len(chunk.blocks_ids)):
            current_block = chunk.blocks_ids[i]
            current_data = chunk.blocks_data[i]
            if block is None:
                block = current_block
                data = current_data
                continue
            if current_block != block or current_data != data:
                equal = False
                break

        return equal
