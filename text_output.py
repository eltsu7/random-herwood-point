import json

from shapely import Point
from gpxpy import gpx


def json_output(
    points: list[Point],
    title: str,
    file_names: list[str] = [],
    save_output: bool = False,
    seed: int = 0,
):
    output_text_dict: dict = {"title": title, "links": {}, "seed": seed}

    for point in points:
        link = f"https://www.google.com/maps/search/{point.y},{point.x}"
        output_text_dict["links"][str(int(point.z))] = link

    output_json: str = json.dumps(output_text_dict, indent=4)
    print(output_json)

    if save_output:
        for filename in file_names:
            with open(filename + ".txt", "w") as text_file:
                text_file.write(output_json)


def gpx_output(
    points: list[Point],
    title: str,
    file_names: list[str] = [],
    save_output: bool = True,
    seed: int = 0,
):
    map = gpx.GPX()
    map.name = title

    for point in points:
        map.waypoints.append(
            gpx.GPXWaypoint(
                latitude=point.y, longitude=point.x, name=str(int(point.z))
            )
        )

    if save_output:
        for filename in file_names:
            with open(filename + ".gpx", "w") as text_file:
                text_file.write(map.to_xml())

    print(map.to_xml())
