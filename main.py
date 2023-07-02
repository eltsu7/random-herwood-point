from random_points import generate_random_points
from draw import draw_on_map
from datetime import datetime


week_number = datetime.now().isocalendar()[1]
filename = f"images\\week_{week_number}_{int(datetime.now().timestamp())}"
title = f"Viikko {week_number}"

points = generate_random_points(10)
for i, point in enumerate(points):
    print(f"{i + 1}: https://google.com/maps/search/?api=1&query={point.y},{point.x}")

draw_on_map(
    points,
    show_image=True,
    save_image=True,
    image_name=filename,
    plot_title=title,
    annotate=True,
)
