import os.path
import sys

import shapely

from random_points import generate_random_points
from draw import draw_on_map
from datetime import datetime

point_week_number: int = (
    datetime.now() - datetime(year=2023, month=7, day=3)
).days // 7
calendar_week_number: int = datetime.now().isocalendar()[1]

file_names = [
    os.path.join(
        "images", f"week_{calendar_week_number}_{int(datetime.now().timestamp())}"
    ),
    os.path.join("images", f"week_{calendar_week_number}"),
    os.path.join("images", f"latest"),
]

try:
    seed = int(sys.argv[1])
except (ValueError, IndexError):
    seed = int(datetime.now().timestamp() * 1000000)

title = f"Viikon {calendar_week_number} kuvausrastit"
points = generate_random_points(number_of_points=5, week_offset=point_week_number, seed=seed)

draw_on_map(
    points,
    show_image=False,
    save_files=False,
    file_names=file_names,
    plot_title=title,
    annotate=True,
    seed=seed,
)
