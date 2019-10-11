
def tuple_points_to_list(points):
    return [list(point) for point in points]

def float_points_to_int(points):
    return [[int(float(point[0])), int(float(point[1]))] for point in points]

