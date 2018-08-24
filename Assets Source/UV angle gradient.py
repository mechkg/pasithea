import bpy 
import math

from mathutils import Vector
from math import asin

pi_2 = math.pi / 2

def get_angle_to_horizon(pos):
    return asin(pos.z)

def get_uv(pos):
    return Vector((get_angle_to_horizon(pos)/pi_2, 0))

ob = bpy.context.active_object

ob.data.uv_textures.new("SkyGradient")

for face in ob.data.polygons:
    for vert_idx, loop_idx in zip(face.vertices, face.loop_indices):
        ob.data.uv_layers.active.data[loop_idx].uv = get_uv(ob.data.vertices[vert_idx].co)
