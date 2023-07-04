import os.path
import sys

from random_points import generate_random_points
from draw import draw_on_map
from datetime import datetime


week_number = datetime.now().isocalendar()[1]
filenames = [
    os.path.join("images", f"week_{week_number}_{int(datetime.now().timestamp())}"),
    os.path.join("images", f"latest"),
]

title = f"Viikon {week_number} kuvausrastit"

points = generate_random_points(5)

draw_on_map(
    points,
    show_image=False,
    save_files=True,
    image_names=filenames,
    plot_title=title,
    annotate=True,
)
