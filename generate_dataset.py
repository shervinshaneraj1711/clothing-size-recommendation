import pandas as pd
import random

# Size measurement rules (realistic ranges)
size_ranges = {
    "S": {"chest": (86, 91), "waist": (71, 76), "hip": (86, 91)},
    "M": {"chest": (92, 97), "waist": (77, 82), "hip": (92, 97)},
    "L": {"chest": (98, 103), "waist": (83, 88), "hip": (98, 103)},
    "XL": {"chest": (104, 109), "waist": (89, 94), "hip": (104, 109)}
}

data = []

# Generate 500 samples
for _ in range(500):
    size = random.choice(["S", "M", "L", "XL"])
    
    chest = random.randint(*size_ranges[size]["chest"])
    waist = random.randint(*size_ranges[size]["waist"])
    hip = random.randint(*size_ranges[size]["hip"])
    
    height = random.randint(150, 185)  # cm
    weight = random.randint(45, 95)    # kg
    
    data.append([height, weight, chest, waist, hip, size])

# Create DataFrame
columns = ["Height", "Weight", "Chest", "Waist", "Hip", "Size"]
df = pd.DataFrame(data, columns=columns)

# Save CSV
df.to_csv("body_measurements.csv", index=False)

print("Dataset created successfully!")
