import numpy as np
import os
import bpy
import glob

os.chdir(rf'C:\Users\')
list = glob.glob('*.txt')
N = len(list)

for i in range(0,N):
    text = list[i]
    verts = np.loadtxt(text)
    mesh = bpy.data.meshes.new('Planet')
    ob = bpy.data.objects.new('earth_'+str(i), mesh)
    bpy.context.scene.collection.objects.link(ob)
    faces = []
    mesh.from_pydata(verts, [], faces)
    mesh.update()
