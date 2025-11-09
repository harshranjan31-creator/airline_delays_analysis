#  Airline Delays and Wind Impact Analysis (Pacific Northwest)

###  Overview
This project analyzes flight delays and cancellations for airlines operating in the Pacific Northwest (SEA and PDX airports) using 2022 flight and weather data.  
The goal is to identify **which airlines and routes experience the most disruptions** and assess the **impact of wind gusts** on departure delays.

---

###  Objectives
1. Find which **routes** had the highest number of cancellations and longest delays.
2. Determine which **airlines** faced the greatest average departure delays.
3. Analyze whether **10 mph+ wind gusts** cause longer delays at SEA and PDX.

---

###  Key Steps
- Loaded and cleaned two datasets:
  - `flights2022.csv` – flight info and cancellations  
  - `flights_weather2022.csv` – flights merged with weather metrics
- Created new features:
  - `route` (e.g., "PDX-SFO")
  - `canceled` (flag for NA departure time)
- Calculated:
  - `mean_dep_delay` – average departure delay per route/airline  
  - `total_cancellations` – number of canceled flights
- Generated two visualizations:
  - Top 9 routes with the most cancellations  
  - Top 9 airlines with the highest average delay
- Evaluated wind impact using `wind_response` boolean (True if wind ≥10 mph increases average delays for both airports).
