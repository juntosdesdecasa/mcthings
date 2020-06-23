# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo


class Renderer:
    """ Base class for all McThings Renderers """

    """
    Base class for all McThings Renderers
    
    A renderer reads the blocks data from mcthings.core.BlocksMemory and render it
    with a specific engine. For example, Raspberry PI uses the Python API to do it.
    """

    def render(self, blocks_memory):
        """
        Render the blocks included in the memory_chunk at position in the world

        :param blocks_memory: memory with the blocks to be rendered
        :return:
        """

    def post_to_chat(self, message):
        """
        Send a message to the chat in the renderer it it exists
        :param message:
        :return:
        """

    def get_block(self, position):
        """
        Get the rendered block at the given position
        :param position:
        :return:
        """

    def get_blocks(self, init_pos, end_pos):
        """
        Get the rendered cuboid at init_pos and end_pos
        :param init_pos:
        :param end_pos:
        :return:
        """