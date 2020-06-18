# McThings [![Documentation Status](https://readthedocs.org/projects/mcthings/badge/?version=latest)](https://mcthings.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/mcthings.svg)](https://badge.fury.io/py/mcthings) [![Twitter](docs/img/twitter.png)](https://twitter.com/McthingsP)

A Python programming framework for building a World of Scenes in Minecraft. Scenes are compositions of Things (Python objects) implemented using the
[Raspberry PI Minecraft](https://www.minecraft.net/en-us/edition/pi/)
[API](https://www.stuffaboutcode.com/p/minecraft-api-reference.html) (which also works in [Minetest](https://github.com/arpruss/raspberryjammod-minetest)). It is based
on [mcpi library](https://github.com/martinohanlon/mcpi). 
[This is the reference notebook](https://github.com/juntosdesdecasa/minecraft/blob/develop/server/data/python/scene0_10.ipynb)
with a complete sample. And there is a [intro video tutorial](https://www.youtube.com/watch?v=p6NUFdUbcYk&t=2s) and [a more complete one](https://www.youtube.com/watch?v=teGjAXomBVs&t=4s).

A Thing is a built based on blocks (voxels based on cubes): [Pyramid](mcthings/pyramid.py), [River](mcthings/river.py),
[House](mcthings/house.py), [Fence](mcthings/fence.py)
and may others. All the Things share the [Thing API](mcthings/thing.py). 
A Thing can be [decorated](https://twitter.com/acstw/status/1265510248892239873)
using existing decorators like [LightDecorator](mcthings/decorators/light_decorator.py) 
or you can create your own one. A [decorated house](https://github.com/juntosdesdecasa/mcthings_extra/blob/develop/tests/test_entity.py#L40).
Scenes can also be decorated [like this sample](https://twitter.com/acstw/status/1267591965169811456)
with a railway ([BorderDecorator](mcthings/decorators/border_decorator.py)) around a Scene.

And Things can also be rotated. For example, in this scene [the castle is rotated
180 degrees](https://github.com/juntosdesdecasa/mcthings_scenes/tree/develop/notebooks/scene0_42.ipynb) so the portal is accessible from the town ways.

There is also a repository for experimental, incubating or with extra dependencies Things
at [McThings Extra](https://github.com/juntosdesdecasa/mcthings_extra).

A [World](mcthings/world.py) is a list of Scenes placed in concrete positions. 
And a [Scene is a list](mcthings/scene.py) of Things built in a specific position and order. Scenes can be shared
loading and saving them to files. Scenes can be also saved as Schematics
and converted with [Mineways](http://www.realtimerendering.com/erich/minecraft/public/mineways/) 
to be used for [3D rendering and printing](https://twitter.com/acstw/status/1262944914234540032). 
You [can share scenes adding them
to this repository](https://github.com/juntosdesdecasa/mcthings_scenes). 
And they can be [interactive](https://www.youtube.com/watch?v=TjHqt3WO-o0) 
as [in this app](https://github.com/juntosdesdecasa/mcthings_scenes/blob/develop/apps/scene_interactive.py).

[This scene](https://github.com/juntosdesdecasa/mcthings_scenes/tree/develop/notebooks/scene_basic.ipynb) includes 
a river, a house in each side of the river and a bridge for crossing the river.

![A Scene in Minecraft](https://raw.githubusercontent.com/juntosdesdecasa/mcthings_scenes/develop/notebooks/img/scene_basic.png)

Things can be built using [MinecraftDrawing](https://minecraft-stuff.readthedocs.io/en/latest/index.html). 
[Sphere](mcthings/sphere.py) and [Circle](mcthings/circle.py) Things are used with Pyramids in the next 
[scene](https://github.com/juntosdesdecasa/mcthings_scenes/tree/develop/notebooks/scene_sphere_circle_pyramid.ipynb):

![Pyramids with Spheres](https://raw.githubusercontent.com/juntosdesdecasa/mcthings_scenes/develop/notebooks/img/scene_sphere_circle_pyramid.png)

And Things can also be built from [Schematics](https://www.minecraft-schematics.com/) (there are thousands!). 
There is a [sample notebook](https://github.com/juntosdesdecasa/mcthings_scenes/tree/develop/notebooks/Schematics.ipynb).

![Schematic inside McThings](https://raw.githubusercontent.com/juntosdesdecasa/mcthings_scenes/develop/notebooks/img/schematic.png)
