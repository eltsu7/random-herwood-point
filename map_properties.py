import dataclasses
import json
import os.path


@dataclasses.dataclass
class MapLimits:
    lat_min = 61.4262
    lat_max = 61.4658
    lon_min = 23.7940
    lon_max = 23.9183


map_image_name = os.path.join("maps", "hervanta.png")
map_data_name = os.path.join("maps", "hervanta.umap")

map_points: list
list_of_holes: list
with open(map_data_name, "r") as file:
    umap_dict = json.loads(file.read())
    all_coordinates: dict = umap_dict["layers"][0]["features"][0]["geometry"][
        "coordinates"
    ]
    map_points = all_coordinates[0]
    list_of_holes = all_coordinates[1:]
