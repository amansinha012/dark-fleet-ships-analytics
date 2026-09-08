import pandas as pd
df=pd.read_csv(r"C:\Users\amant\OneDrive\Desktop\dark_fleet_\Shipping_raw_data.csv")
df['timestamps']=pd.to_datetime(df['timestamps'])
speed_limit=70
df['Is iregular']=df['Speed']>speed_limit
iregular_df=df[df['Is iregular']==True]
suspicious_ships=iregular_df.groupby(['Ships_IDs']).size().reset_index(name='Total_iregular_ships')
suspicious_ships['Risk_score']=(suspicious_ships['Total_iregular_ships']/30*100).clip(upper=100)
suspicious_ships=suspicious_ships.sort_values(by='Risk_score',ascending=False)
suspicious_ships.to_csv("high_risk_ships.csv",index=False)
print("\n Analysis Completetd")
print(f"Total Number of iregular ships are :{iregular_df}")
print("top 5 most suspicious ships are:\n")
print(suspicious_ships.head())
print("\n📁 A new file 'high_risk_vessels.csv' has been generated with your suspect list!")
