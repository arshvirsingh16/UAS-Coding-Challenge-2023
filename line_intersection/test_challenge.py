from line_intersection.challenge import points_to_standard, does_line_intersect

# Tests

def test1():
    assert does_line_intersect(points_to_standard((0,10),(30,10)),(12,0),10) == 'One Intersection'
def test2():
    assert does_line_intersect(points_to_standard((0,-10),(15,15)),(9,3),5) == 'Two Intersections'
def test3():
    assert does_line_intersect(points_to_standard((0,-10),(15,15)),(10,-5),4) == 'No Intersection'
