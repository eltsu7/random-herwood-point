from random_points import generate_random_points
from draw import draw_on_map
from datetime import datetime


week_number = datetime.now().isocalendar()[1]
filename = f"images\\week_{week_number}"

points = generate_random_points(5)
draw_on_map(points, save_image=True, image_name=filename)
