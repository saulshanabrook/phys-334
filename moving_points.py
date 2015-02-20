from visual import *


v = vector(1, 1, 4)
dt = 0.01

# ok so first we are gonna build up a list of all the initial points in a list of vectors
original_points = []

# to make some initial points, im gonna iterate `i` through a bunch of numbers
for i in range(10):
    # here I decided to just to make some weird shape where y is i squared
    # here you would do whatever you need to to make a shape
    x = i
    y = i**2
    z = 0
    
    original_points.append(vector(x, y, z))

# so we are gonna plot the original points
points(pos=original_points)

# now we are gonna make another plot the moving points
moving_pts = points(pos=original_points, color=color.orange)

# now change the points we are moving (i.e. you would do lorentz contraction)
for pt in moving_pts.pos:
    # here we are changing x to x + y,
    pt[0] = pt[0] + pt[1]
    # pt[0] refers to x, pt[1] to y, and pt[2] to z

# we dont want the whole scene to move, if this is not set, it will try to keep it in the middle
scene.autoscale=False

# now we are going through a big range, and for each value in it, we are moving the the pts by `v*dt`
for _ in range(100000):
    moving_pts.pos += v*dt
    rate(500)


