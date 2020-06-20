# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo


class Renderer:
    """ Base class for all McThings Renderers """

    """
    Base class for all McThings Renderers
    
    A renderer reads the blocks data from mcthings.core.BlocksMemory and render it
    with a specific engine. For example, Raspberry PI uses the Python API to do it.
    """

    def render(self, memory_chunk):
        """
        Render the blocks included in the memory_chunk at position in the world

        :param memory_chunk: chunk of blocks to be rendered
        :return:
        """
        pass
