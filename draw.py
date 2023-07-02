import datetime

import matplotlib.pyplot as plt
from shapely.geometry import Point

from map_properties import map_points, MapLimits, map_name


def draw_on_map(
    points: list[Point],
    show_image: bool = True,
    save_image: bool = False,
    plot_title: str = "",
    image_name: str = "",
):
    map_image = plt.imread(map_name)
    aspect_ratio = (
        (map_image.shape[0] / map_image.shape[1])
        * (MapLimits.lon_max - MapLimits.lon_min)
        / (MapLimits.lat_max - MapLimits.lat_min)
    )

    ax: plt.Axes
    fig: plt.Figure
    fig, ax = plt.subplots(figsize=(12, 8))

    x = [point[0] for point in map_points]
    y = [point[1] for point in map_points]
    ax.plot(x, y, zorder=1, alpha=0.5, c="b")

    for i, point in enumerate(points):
        ax.scatter(point.x, point.y, zorder=1, alpha=1, c="r", s=20)
        ax.annotate(int(point.z), (point.x + 0.0003, point.y + 0.0003), fontsize=14)

    ax.set_title(plot_title, loc="left", fontsize=20)
    ax.set_title(datetime.datetime.now(), loc="right", fontsize=10)
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

    points_in_text = ""

    for point in points:
        if points_in_text != "":
            points_in_text += "\n"
        points_in_text += f"{int(point.z)}: {format(point.y, '.6f')}, {format(point.x, '.6f')}"

    offset = (MapLimits.lon_max - MapLimits.lon_min) * 0.02
    text_position_x = MapLimits.lon_min + offset
    text_position_y = MapLimits.lat_min + (offset * (map_image.shape[0] / map_image.shape[1]))

    plt.text(
        text_position_x,
        text_position_y,
        points_in_text,
        fontsize=10,
        # family="monospace",
        bbox={
            "boxstyle": "square",
            "facecolor": "white",
            "edgecolor": "gray"
        }
    )

    plt.axis("off")
    if save_image:
        if image_name == "":
            raise NameError("Filename is empty")
        fig.savefig(image_name, bbox_inches="tight", pad_inches=0.2, dpi=200)
    if show_image:
        plt.show()
