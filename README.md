# Kuala Lumpur Tourism Route Optimiser

This Python application finds an efficient driving route between multiple tourist attractions in Kuala Lumpur. Choose three to five destinations and a car type; the application returns an optimised visiting order, total distance, estimated fuel cost, and estimated carbon emissions.

It is a network-analysis project. It does not use machine learning.

## How it works

1. The preprocessing module downloads the local drivable road network from OpenStreetMap.
2. It calculates the shortest road distance between every supported attraction.
3. Those distances are saved in `KL_Attraction_Place.xlsx` as a distance matrix.
4. You choose 3–5 attractions in the terminal.
5. The program evaluates every possible visiting order (permutation) and selects the route with the lowest total distance. For 3–5 selected attractions, this produces the exact shortest route.
6. It estimates fuel usage, fuel cost, and carbon emissions using the selected car's fuel consumption.

## Requirements

- Python 3.10 or newer
- Internet connection for the first run, so OSMnx can obtain OpenStreetMap road data
- PowerShell on Windows (the commands below use PowerShell)

## Installation

Open PowerShell in this project folder. For example:

```powershell
cd "C:\Users\Arfan's\Documents\Syahmi Aniq Stuff\GITHUB\route-optimizer-tourism"
```

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, run this for the current terminal session and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Install the project packages:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the optimiser

With the virtual environment activated, run:

```powershell
python Main.py
```

On the first run, the program downloads map data and creates `KL_Attraction_Place.xlsx`. This can take a little longer than later runs. Later runs reuse the saved distance matrix, so they do not need to download it again.

## Using the application

1. The terminal displays the available attractions.
2. Enter between three and five attraction numbers, names, or a mix of both, separated by commas. Names are not case-sensitive. The displayed number beside each attraction is its selection number.

   ```text
   4, 7, 2, 3
   ```

   This is also valid:

   ```text
   KLCC, 4, Central Market
   ```

3. Choose a car from the displayed list, such as `Myvi`, or enter `others`.
4. If you select `others`, enter its fuel consumption in kilometres per litre (km/L).
5. Review the summary, which includes the visit order, total distance, estimated fuel cost, and estimated carbon emissions.

## Project files

| File | Purpose |
| --- | --- |
| `Main.py` | Main entry point. Run this file to start the application. |
| `Preprocess.py` | Downloads map data, creates/loads the Excel distance matrix, and prepares worksheets. |
| `User_Interface.py` | Handles terminal prompts, input validation, route calculation, and result display. |
| `requirements.txt` | Lists Python packages that must be installed. |
| `KL_Attraction_Place.xlsx` | Generated file containing the all-attractions and selected-attractions distance matrices. |

## Supported attractions

- National Art Gallery
- Saloma Bridge
- KLCC
- KL Tower
- National Monument
- Merdeka Square
- Central Market
- Bukit Bintang
- Perdana Botanical Garden
- National Mosque
- Chinatown
- Royal Museum
- Little India
- Thean Hou Temple

## Technical method

- **Road network:** OSMnx retrieves OpenStreetMap's driving network around Kuala Lumpur.
- **Distance calculation:** NetworkX calculates weighted shortest paths using road length.
- **Route optimisation:** an exhaustive permutation solver evaluates every possible open route and selects the exact minimum-distance route. At the maximum of five chosen attractions, it evaluates only `5! = 120` orders.
- **Fuel and emissions:** the displayed estimates use the selected car's km/L figure, a fuel price of RM1.99 per litre, and 2.3 kg of carbon emissions per litre.

The summary reports the exact solver duration in minutes. It measures only the permutation solver, excluding map loading, Excel work, and user input. The route should still be treated as a planning aid: live traffic, road closures, tolls, parking, opening hours, and real-time routing are not included.

## Troubleshooting

### `python` or `py` is not recognised

Install Python from [python.org](https://www.python.org/downloads/) and ensure the Python installer option to add Python to PATH is enabled. Then reopen PowerShell.

### `ModuleNotFoundError`

Activate the virtual environment and reinstall the dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Map download fails on the first run

Check your internet connection and run `python Main.py` again. If an incomplete `KL_Attraction_Place.xlsx` file was created, delete that generated file and rerun the program.
