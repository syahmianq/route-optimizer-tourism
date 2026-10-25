# How to Run the Tourism Route Optimiser

Follow these steps in PowerShell on Windows. Run all commands from the project folder.

## 1. Set up the environment

Open PowerShell and move into the project folder:

```powershell
cd "C:\Users\Arfan's\Documents\Syahmi Aniq Stuff\GITHUB\route-optimizer-tourism"
```

Create a Python virtual environment:

```powershell
py -m venv .venv
```

Install all required packages:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

You only need to create the environment and install the packages once.

If PowerShell blocks activation, run this command for the current PowerShell window, then activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 2. Activate  the environment

Each time you open a new PowerShell window to use the project, return to the project folder and activate the environment:

```powershell
cd "C:\Users\Arfan's\Documents\Syahmi Aniq Stuff\GITHUB\route-optimizer-tourism"
.\.venv\Scripts\Activate.ps1
```

When active, PowerShell displays `(.venv)` at the beginning of the command prompt.

## 3. Run the optimiser in the terminal

With the environment active, run:

```powershell
python Main.py
```

The terminal lists the attractions. Enter three to five destination numbers, names, or a combination of both. For example:

```text
4, 7, KLCC
```

Then choose a car type. The terminal displays the exact optimal route, total distance, estimated fuel cost, and estimated carbon emissions.

## 4. Run the optimiser in the dashboard

With the environment active, run:

```powershell
python dashboard\app.py
```

PowerShell displays a local address, normally:

```text
http://127.0.0.1:5000
```

Open that address in a web browser. Select three to five destinations, choose a car type, and select **Optimise route** to view the result.

To stop the dashboard server, return to PowerShell and press `Ctrl+C`.

## First run note

The first run requires an internet connection. The program downloads Kuala Lumpur road-network data from OpenStreetMap and creates `KL_Attraction_Place.xlsx`. Later runs reuse this saved file and are faster.
