# Lab 3 – Linear Classification

This lab focuses on **linear classification** of 2D points. The goal is to classify points relative to a straight line and visualize the results.

# Repository Contents
- `main.py` – Python script to classify points based on a line.
- `unlabelled_data.csv` – Input data file with points to classify.# rainbowcsv extension
- `labelled_data.csv` – Output file with an added column: 0 if a point is to the left/below the line, 1 otherwise.
- `report.ipynb` *(optional, for VG)* – Short report analyzing multiple lines and comparing their classification performance.
- `README.md` – This file.

## Usage
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```
2. Make sure you have Python installed. Install dependencies if needed:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the classification script:
    ```bash
    python main.py
    ```
   This will:
   - Load `unlabelled_data.csv`.
   - Classify each point as above/below or left/right of your line.
   - Save the results to `labelled_data.csv`.
   - Display a plot showing the points, their class, and the line.

## VG Tasks (Optional)
- Compare your line with additional lines:
  - `f(x) = -0.489x`
  - `g(x) = -2x + 0.16`
  - `h(x) = 800x - 120`
- Classify points using these lines and discuss differences in `report.ipynb`.

## Notes
- The project demonstrates basic linear classification and visualization using Python.
- Reuse code wherever possible to keep the scripts concise and organized.

