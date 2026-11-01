import mujoco , mujoco.viewer
import numpy as np
m = mujoco.MjModel.from_xml_path("world.xml")
mujoco.viewer.launch(m)
d = mujoco.MjData(m)
mujoco.mj_forward(m, d)

for name in ["chassis_visual", "BRW"]:
    gid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_GEOM, name)
    mid = m.geom_dataid[gid]
    print(name, "| world pos:", d.geom_xpos[gid],
          "| bounding half-size:", m.geom_aabb[gid, 3:],
          "| rgba:", m.geom_rgba[gid],
          "| group:", m.geom_group[gid],
          "| mesh verts:", m.mesh_vertnum[mid])
