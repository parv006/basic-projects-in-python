from vpython import *
import numpy as np

# Scene setup
scene.background = color.white
scene.title = "3D Atherosclerosis Progression"

# Vessel (transparent cylinder)
vessel = cylinder(pos=vector(0,0,0), axis=vector(0,0,20), radius=2, color=color.red, opacity=0.2)

# Red blood cells (RBCs) flowing through
rbcs = []
for i in range(20):
    angle = np.random.uniform(0, 2*np.pi)
    r = np.random.uniform(0.3, 1.6)
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    z = np.random.uniform(0, 20)
    rbcs.append(sphere(pos=vector(x, y, z), radius=0.2, color=color.red, make_trail=False))

# LDL particles (yellow spheres entering vessel wall)
ldl_particles = []

# Foam cells (orange spheres)
foam_cells = []

# Plaque layer (invisible yellow wall initially)
plaque = ring(pos=vector(0,0,15), axis=vector(0,0,1), radius=1.8, thickness=0.4, color=color.yellow, opacity=0)

# Animation loop
t = 0
while t < 400:
    rate(30)
    t += 1

    # Animate RBC flow
    for rbc in rbcs:
        rbc.pos.z -= 0.2
        if rbc.pos.z < 0:
            rbc.pos.z += 20  # loop back to start

    # LDL entry phase
    if 50 < t < 100:
        if t % 5 == 0:
            x = np.random.uniform(-0.5, 0.5)
            y = np.random.uniform(-0.5, 0.5)
            z = np.random.uniform(14.5, 15.5)
            ldl = sphere(pos=vector(x, y, z), radius=0.15, color=color.yellow)
            ldl_particles.append(ldl)

    # Macrophage converts LDL → foam cell
    if 100 < t < 150:
        if ldl_particles:
            ldl = ldl_particles.pop(0)
            foam = sphere(pos=ldl.pos, radius=0.25, color=color.orange)
            foam_cells.append(foam)
            ldl.visible = False

    # Plaque builds up
    if t > 150:
        plaque.opacity = min(1.0, plaque.opacity + 0.01)

