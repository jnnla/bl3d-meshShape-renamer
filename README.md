# bl3d-meshShape-renamer
A python script for Blender that will rename child mesh shapes to match their transform-node parents. 

DISCLAIMER: I don't claim to have any deep expertise or understanding of programming or code. I'm just experimenting, learning and sharing what works so that I might help and learn from others.

![](blenderChildRenamer.gif)

This script was written and used in Blender 3.3. It was intended to ensure that the child mesh shape name matches its parent transform node. To use it:

1) Select an object or group of objects in the viewport.
2) Run the script.
3) Note that the mesh shape node underneath its parent now matches the parent name...with a 'msh_' pre-pended. 
