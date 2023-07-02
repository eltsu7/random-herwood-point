from shapely.geometry import Point, Polygon
import numpy as np

from map_properties import map_points


def generate_random_points(number_of_points: int) -> list[Point]:
    map_polygon = Polygon(map_points)
    boundaries = map_polygon.bounds

    points = []

    while len(points) < number_of_points:
        x = np.random.uniform(boundaries[0], boundaries[2])
        y = np.random.uniform(boundaries[1], boundaries[3])
        point = Point(x, y, len(points) + 1)
        if map_polygon.contains(point):
            points.append(point)

    return points
