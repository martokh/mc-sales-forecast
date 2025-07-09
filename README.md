# Monte Carlo Sales Forecast

**Author:** Martin Hristov    
**Language:** Python 3  
**Dependencies:** matplotlib

## Overview

This script performs a Monte Carlo simulation to forecast weekly and annual sales and profit for a climbing gear retail shop. It accounts for seasonal demand and optional winter marketing costs.

## Features

- 52-week simulation broken into four 13-week seasons (Winter, Spring, Summer, Autumn)  
- Season-specific customer and spending factors  
- Fixed weekly costs and variable cost per customer  
- Optional winter advertising cost adjustment  
- 5 000 Monte Carlo runs to estimate average revenue and profit  
- Plots average weekly revenue vs. profit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/martokh/mc-sales-forecast.git
   cd mc-sales-forecast
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
   pip install matplotlib

## Usage

Run the simulation:
   ```bash
   python mc-sales-forecast.py
   ```

## Example Output
   ```bash
   Simulation complete (5000 runs)
   Annual revenue: 235123.45 lv
   Annual profit: 17432.10 lv
   ```

(Your numbers may vary per run.)

## License
MIT License © Martin Hristov
