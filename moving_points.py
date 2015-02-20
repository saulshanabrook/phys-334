from visual import *

original_points = []

v = vector(1, 1, 4)
dt = 0.01


for i in range(10):
    x = i
    y = i**2
    z = 0
    original_points.append(vector(x, y, z))


pts = points(pos=original_points)

for _ in range(10):
    pts.pos += v*dt
    rate(500)
