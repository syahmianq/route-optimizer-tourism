"""Run the Kuala Lumpur tourism route optimiser."""

from Preprocess import PLACES, prepare_workbook
from User_Interface import run_application


WORKBOOK_FILENAME = "KL_Attraction_Place.xlsx"


def main():
    """Prepare route data and start the optimiser."""
    workbook, all_places_sheet, selected_sheet = prepare_workbook(WORKBOOK_FILENAME)
    run_application(
        workbook,
        all_places_sheet,
        selected_sheet,
        PLACES,
        WORKBOOK_FILENAME,
    )


if __name__ == "__main__":
    main()
