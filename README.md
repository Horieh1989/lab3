
# Lab 3: Linear Classification of 2D Data Points

## Overview
This project investigates **linear classification** of 2D points. The goal is to classify points as above or below a line (`y = kx + m`) and visualize the classification. The classification depends on the slope and intercept of the line.

## Files
- `main.py` – Python script for classification, plotting, and CSV writing.  
- `labelled_data.csv` – Output file with points and their class (0 = below, 1 = above).  
- `report.ipynb` – Optional VG notebook comparing multiple lines.

## How It Works
1. **Data Loading** – Downloads `unlabelled_data.csv` and loads `x_data` and `y_data`.  
2. **Lines** –  
   - Main line (`y_line`) with flexible slope and intercept (default slope -1).  
   - VG lines for comparison:  
     - `f(x) = -0.489x`  
     - `g(x) = -2x + 0.16`  
     - `h(x) = 800x - 120`  
3. **Classification** – Points above the line → 1, below → 0.  
4. **CSV Output** – Writes `labelled_data.csv` with x, y, class columns.  
5. **Visualization** – Plots points and all lines for comparison.

## Example Output
```

Above: [[2.09 2.56] ...]
Below: [[-1.88 -1.99] ...]
y_line: 300 points above, 300 under
f_line: 301 points above, 299 under
g_line: 301 points above, 299 under
h_line: 302 points above, 298 under

````

## VG Notes
- VG lines show how classification changes with different slopes and intercepts.  
- Line choice depends on classification goals (e.g., splitting evenly vs. specific horizontal/vertical separation).  
- Infinitely many lines are possible; the “best” line maximizes distance between point groups.

## Classification Logic
- `yi` above `y_line(xi)` → group 1  
- `yi` below `y_line(xi)` → group 0  
- Main line slope (`k`) and intercept (`m`) are flexible; if no intercept is given, it is calculated automatically as the median of `(x_data + y_data)`.

## How to Run
1. Ensure Python 3.x with `numpy` and `matplotlib`.  
2. Run:
```bash
python main.py
````

3. The program will classify points, save `labelled_data.csv`, and display a plot showing:

   * Points above the line (blue)
   * Points below the line (yellow)
   * Main line and VG comparison lines

## Notes

* Main line: slope = -1, gives a 45° downward line.
* f(x) line: slope = -0.489, intercept auto-calculated.
* g(x) line: slope = -2, intercept = 0.16.
* h(x) line: slope = 800, intercept = -120 (steep upward line).
* Classification is sensitive to slope and intercept; choose based on your goal.



