from random_points import generate_random_points
from draw import draw_on_map
from text_output import json_output, gpx_output
from datetime import datetime
import argparse
import pathlib


parser = argparse.ArgumentParser()
parser.add_argument("--out", type=pathlib.Path, help="Output folder")
parser.add_argument(
    "--show",
    type=bool,
    help="Show plot",
    default=False,
    action=argparse.BooleanOptionalAction,
)
parser.add_argument("--seed", type=int, help="RNG seed (integer)")
args: argparse.Namespace = parser.parse_args()

now = datetime.now()
point_week_number: int = (now - datetime(year=2023, month=7, day=3)).days // 7
calendar_week_number: int = now.isocalendar()[1]

file_names = []
if args.out:
    output_base_path: pathlib.Path = args.out
    archive_path = output_base_path.joinpath("archive")
    archive_path.mkdir(parents=True, exist_ok=True)

    base_file_name = f"week_{calendar_week_number}"

    file_names = [
        str(
            archive_path.joinpath(
                base_file_name + "_" + str(int(now.timestamp()))
            ).absolute()
        ),
        str(output_base_path.joinpath(base_file_name).absolute()),
        str(output_base_path.joinpath("latest").absolute()),
    ]

seed = args.seed
if not seed:
    seed = int(now.timestamp() * 1000000)

title = f"Viikon {calendar_week_number} kuvausrastit"
points = generate_random_points(
    number_of_points=5, week_offset=point_week_number, seed=seed
)
gpx_output(points=points, file_names=file_names, title=title)
json_output(points=points, file_names=file_names, title=title, seed=seed)
draw_on_map(
    points,
    show_image=args.show,
    file_names=file_names,
    plot_title=title,
    annotate=True,
)
