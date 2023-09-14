import math as m

def points_to_standard(p1: tuple, p2: tuple):
    # a = (y1-y2)
    # b = (x2-x1)
    # c = (x1*y2-x2*y1)

    a = p1[1]-p2[1]
    b = p2[0]-p1[0]
    c = p1[0]*p2[1]-p2[0]*p1[1]

    return (a,b,c)

def does_line_intersect(line: tuple, center: tuple,r: int):

    #general form of an equation: ax + by + c = 0
    a,b,c = line

    #formula for distance
    distance = abs(a*center[0]+b*center[1]+c)/ m.sqrt(a**2+b**2)

    if r == distance:
        return 'One Intersection'
    elif r > distance:
        return 'Two Intersections'
    else:
        return 'No Intersection'
standard_form = points_to_standard((0,-10),(15,15))
print(does_line_intersect(standard_form,(9,3),5))