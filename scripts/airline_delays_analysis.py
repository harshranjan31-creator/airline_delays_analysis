# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Start your code here!
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# ROUTES summary (REQUIRED)
# =========================
# Ensure inputs exist/typed:
flights["canceled"] = flights["dep_time"].isna()
flights["route"] = flights["origin"].str.upper() + "-" + flights["dest"].str.upper()
flights["dep_delay"] = pd.to_numeric(flights["dep_delay"], errors="coerce")

routes_delays_cancels = (
    flights
    .groupby("route", dropna=True)
    .agg(
        mean_dep_delay=("dep_delay", "mean"),      # exact name expected
        total_cancellations=("canceled", "sum")    # exact name expected
    )
    .reset_index()
)

# Object required by checker: top routes by cancellations (top 9)
top_routes_by_cancellations = (
    routes_delays_cancels
    .sort_values("total_cancellations", ascending=False)
    .head(9)
    .reset_index(drop=True)
)

# Bar plot (1): Top 9 highest number of cancellations by route
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(top_routes_by_cancellations["route"], top_routes_by_cancellations["total_cancellations"])
ax1.set_title("Top 9 Routes by Number of Cancellations")
ax1.set_xlabel("Route")
ax1.set_ylabel("Total Cancellations")
ax1.set_xticklabels(top_routes_by_cancellations["route"], rotation=45, ha="right")
plt.tight_layout()
top9_route_cancels_bar = fig1

# ==========================
# AIRLINES summary (REQUIRED)
# ==========================
airlines_delays_cancels = (
    flights
    .groupby("airline", dropna=True)
    .agg(
        mean_dep_delay=("dep_delay", "mean"),      # exact name expected
        total_cancellations=("canceled", "sum")    # exact name expected
    )
    .reset_index()
)

# Object required by checker: top airlines by average departure delay (top 9)
top_airlines_by_delay = (
    airlines_delays_cancels
    .sort_values("mean_dep_delay", ascending=False)
    .head(9)
    .reset_index(drop=True)
)

# Bar plot (2): Top 9 highest average departure delays by airline
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(top_airlines_by_delay["airline"], top_airlines_by_delay["mean_dep_delay"])
ax2.set_title("Top 9 Airlines by Average Departure Delay (minutes)")
ax2.set_xlabel("Airline")
ax2.set_ylabel("Average Departure Delay (min)")
ax2.set_xticklabels(top_airlines_by_delay["airline"], rotation=45, ha="right")
plt.tight_layout()
top9_airline_delays_bar = fig2

