import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sb

print("Creating Dashboard\n")

df = pd.read_csv(r"C:\Users\amant\OneDrive\Desktop\dark_fleet_\Shipping_raw_data.csv")
high_risk_ships = pd.read_csv(r"C:\Users\amant\OneDrive\Desktop\dark_fleet_\high_risk_ships.csv")
print("Columns in Raw Data:", df.columns.tolist())
sb.set_theme(style="darkgrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('MARITIME DARK FLEET INTELLIGENCE DASHBOARD', fontsize=18, fontweight='bold', color='#1a1a1a')
iregular_coordinates = df[df['Speed'] > 70.0]
sb.kdeplot(
    data=iregular_coordinates, 
    x='longitudes', 
    y='latitudes', 
    cmap='Reds', 
    fill=True, 
    thresh=0.05, 
    levels=15,
    ax=axes[0]
)

axes[0].set_title('Geospatial Anomaly Hotspots (Dark Fleet Activity)', fontsize=14, fontweight='semibold')
axes[0].set_xlabel('Longitude Coordinate', fontsize=12)
axes[0].set_ylabel('Latitude Coordinate', fontsize=12)
axes[0].set_xlim(-180, 180)
axes[0].set_ylim(-60, 60)

# --- FIXED SYNTAX HERE ---
low_count = len(high_risk_ships[high_risk_ships['Risk_score'] <= 33])
med_count = len(high_risk_ships[(high_risk_ships['Risk_score'] > 33) & (high_risk_ships['Risk_score'] <= 66)])
high_count = len(high_risk_ships[high_risk_ships['Risk_score'] > 66])

labels = ['Low Risk (0-33)', 'Medium Risk (34-66)', 'High Risk (67-100)']
Ships_counts = [low_count, med_count, high_count]
chart_colors = ['#2ecc71', '#f39c12', '#c0392b']  # Traffic lights: Green, Orange, Red

bars = axes[1].bar(labels, Ships_counts, color=chart_colors, edgecolor='black', width=0.5) 
axes[1].set_title('Vessel Security Risk Classification Distribution', fontsize=13, fontweight='semibold')
axes[1].set_ylabel('Number of Active Cargo Ships')

for bar in bars:
    y_val = bar.get_height()
    axes[1].annotate(f'{int(y_val)}', 
                     xy=(bar.get_x() + bar.get_width() / 2, y_val),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('dark_fleet_dashboard.png', dpi=300)

print("🎯 Step 3 Complete! Visual file saved successfully as: 'dark_fleet_dashboard.png'")
plt.show()
