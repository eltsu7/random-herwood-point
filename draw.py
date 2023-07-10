import datetime
import json

import matplotlib.pyplot as plt
from shapely.geometry import Point

from map_properties import map_points, MapLimits, map_image_name, list_of_holes


def draw_on_map(
    points: list[Point],
    show_image: bool = True,
    save_files: bool = False,
    plot_title: str = "",
    file_names: list[str] = [],
    annotate: bool = True,
):
    map_image = plt.imread(map_image_name)
    aspect_ratio = (
        (map_image.shape[0] / map_image.shape[1])
        * (MapLimits.lon_max - MapLimits.lon_min)
        / (MapLimits.lat_max - MapLimits.lat_min)
    )

    ax: plt.Axes
    fig: plt.Figure
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(
        [point[0] for point in map_points],
        [point[1] for point in map_points],
        zorder=1,
        alpha=0.5,
        c="b",
    )

    for hole in list_of_holes:
        ax.plot(
            [point[0] for point in hole],
            [point[1] for point in hole],
            zorder=1,
            alpha=0.3,
            c="b",
        )

    for point in points:
        ax.scatter(point.x, point.y, zorder=1, alpha=1, c="r", s=20)

    ax.set_title(plot_title, loc="left", fontsize=20)
    ax.set_title(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), loc="right", fontsize=10
    )
    ax.set_xlim(MapLimits.lon_min, MapLimits.lon_max)
    ax.set_ylim(MapLimits.lat_min, MapLimits.lat_max)
    ax.imshow(
        map_image,
        zorder=0,
        extent=(
            MapLimits.lon_min,
            MapLimits.lon_max,
            MapLimits.lat_min,
            MapLimits.lat_max,
        ),
        aspect=aspect_ratio,
    )

    if annotate:
        for point in points:
            ax.annotate(int(point.z), (point.x + 0.0003, point.y + 0.0003), fontsize=14)

        points_in_text = ""

        for point in points:
            if points_in_text != "":
                points_in_text += "\n"
            points_in_text += (
                f"{str(int(point.z)).rjust(2)}: "
                f"{format(point.y, '.4f')}, {format(point.x, '.4f')}"
            )

        offset_in_pixels = 50
        offset_x = (
            (MapLimits.lon_max - MapLimits.lon_min) / map_image.shape[1]
        ) * offset_in_pixels
        offset_y = (
            (MapLimits.lat_max - MapLimits.lat_min) / map_image.shape[0]
        ) * offset_in_pixels

        text_position_x = MapLimits.lon_min + offset_x
        text_position_y = MapLimits.lat_min + offset_y

        plt.text(
            text_position_x,
            text_position_y,
            points_in_text,
            fontsize=10,
            family="monospace",
            bbox={"boxstyle": "square", "facecolor": "white", "edgecolor": "gray"},
        )
    plt.axis("off")

    output_text_dict: dict = {
        "title": plot_title,
        "links": {},
    }

    for point in points:
        link = f"https://www.google.com/maps/search/{point.y},{point.x}"
        output_text_dict["links"][str(int(point.z))] = link

    output_json: str = json.dumps(output_text_dict, indent=4)
    print(output_json)

    if save_files:
        if not file_names:
            raise NameError("Filename is empty")
        for filename in file_names:
            with open(filename + ".txt", "w") as text_file:
                text_file.write(output_json)
            fig.savefig(filename, bbox_inches="tight", pad_inches=0.2, dpi=200)

    if show_image:
        plt.show()
