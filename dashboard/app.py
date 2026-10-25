"""Local Flask dashboard for the tourism route optimiser."""

import json
import sys
from pathlib import Path

from flask import Flask, render_template, request

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from Preprocess import PLACES, prepare_workbook
from User_Interface import calculate_exact_route


WORKBOOK_FILENAME = PROJECT_ROOT / "KL_Attraction_Place.xlsx"
CONFIG_PATH = Path(__file__).with_name("data.json")

with CONFIG_PATH.open(encoding="utf-8") as config_file:
    CONFIG = json.load(config_file)

app = Flask(__name__)
workbook, all_places_sheet, _ = prepare_workbook(WORKBOOK_FILENAME)


def selected_distance_matrix(selected_places):
    """Read the selected attractions' distances from the saved matrix."""
    matrix_positions = {place: index for index, place in enumerate(PLACES, start=2)}
    return [
        [
            all_places_sheet.cell(
                row=matrix_positions[origin], column=matrix_positions[destination]
            ).value
            for destination in selected_places
        ]
        for origin in selected_places
    ]


@app.route("/", methods=["GET", "POST"])
def dashboard():
    selected_places = request.form.getlist("places")
    selected_car = request.form.get("car", "Myvi")
    error = None
    result = None

    if request.method == "POST":
        if not 3 <= len(selected_places) <= 5:
            error = "Select between 3 and 5 destinations."
        elif len(selected_places) != len(set(selected_places)):
            error = "Select each destination only once."
        elif any(place not in PLACES for place in selected_places):
            error = "An invalid destination was selected."
        else:
            try:
                if selected_car == "others":
                    consumption = float(request.form.get("custom_consumption", ""))
                    if consumption <= 0:
                        raise ValueError
                else:
                    consumption = CONFIG["cars"][selected_car]
            except (KeyError, ValueError):
                error = "Enter a positive fuel-consumption value."
            else:
                route, distance = calculate_exact_route(
                    selected_places, selected_distance_matrix(selected_places)
                )
                litres = distance / consumption
                result = {
                    "route": route,
                    "distance": distance,
                    "fuel_cost": litres * CONFIG["fuel_price_per_litre"],
                    "carbon_emission": litres * CONFIG["carbon_kg_per_litre"],
                }

    return render_template(
        "index.html",
        places=CONFIG["places"],
        cars=CONFIG["cars"],
        selected_places=selected_places,
        selected_car=selected_car,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
