import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# House Price per square foot
df['pxHousePerSqFt'] = df.medPrice / df.medSqFt

# Gallons of Oil per Barrel
bVol = 42.0

# Need 7.48 gallons of oil to raise 1SqFt by 1Ft
galPerCuFt = 7.48 

# Cubic feet per barrel
cuFtPerBar = bVol / galPerCuFt

# Oil Price per cubic foot
df['pxOilPerCuFt'] = df.wtisplc / cuFtPerBar

# Oily House Index = House (sqFt) over Oil (cuFt)
df['OHI'] = df.pxHousePerSqFt / df.pxOilPerCuFt

# Forcing higher house price to match XKCD
#df['OHI'] = (df.pxHousePerSqFt * 1.2) / df.pxOilPerCuFt

with plt.xkcd():
    df.plot(x='year', y='OHI')
    plt.savefig('ohi.pdf')
