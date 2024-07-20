import swisseph as swe

# Set the date for which you want to calculate the planetary positions
year = 2024
month = 7
day = 19
hour = 12.0  # UTC time

# Calculate the Julian Day Number
jd = swe.julday(year, month, day, hour)

# Define flags (use default flags for simplicity)
flags = swe.FLG_SWIEPH | swe.FLG_SPEED

# Get the position of the Sun
sun = swe.calc_ut(jd, swe.SUN, flags)

# Get the position of the Moon
moon = swe.calc_ut(jd, swe.MOON, flags)

print(f"Sun: {sun}")
print(f"Moon: {moon}")
