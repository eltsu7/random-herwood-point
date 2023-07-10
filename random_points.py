from shapely.geometry import Point, Polygon
import numpy as np

from map_properties import map_points, list_of_holes


def generate_random_points(number_of_points: int, week_offset: int, seed: int = 0) -> list[Point]:
    map_polygon = Polygon(map_points, holes=list_of_holes)
    boundaries = map_polygon.bounds
    random_generator = np.random.default_rng(seed)

    points = []

    while len(points) < number_of_points:
        x = round(random_generator.uniform(boundaries[0], boundaries[2]), 4)
        y = round(random_generator.uniform(boundaries[1], boundaries[3]), 4)
        z = len(points) + 1 + (number_of_points * week_offset)
        point = Point(x, y, z)
        if map_polygon.contains(point):
            points.append(point)

    return points
