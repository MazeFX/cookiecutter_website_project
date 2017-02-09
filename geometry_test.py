from math import sin, cos ,tan

border = 0.25

shape = [(0, 0),
         (-1, 2),
         (3, 1),
         (3, 2),
         (5, 0),
         (3, -2),
         (3, -1),
         (-1, -2),
         (0, 0)]

shape_lines = []
for i in range(len(shape)):
    line = shape[i]
