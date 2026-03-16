import pandas as pd
import numpy as np

rows = 1000

data = {
    "Temperature": np.random.randint(20,40,rows),
    "Humidity": np.random.randint(30,90,rows),
    "Hour": np.random.randint(0,24,rows),
    "Day": np.random.randint(1,31,rows),
    "Month": np.random.randint(1,13,rows)
}

df = pd.DataFrame(data)

df["Energy"] = (
    df["Temperature"]*2 +
    df["Humidity"]*0.5 +
    df["Hour"]*3 +
    np.random.randint(10,50,rows)
)

df.to_csv("dataset/energy_consumption_data.csv",index=False)

print("Dataset generated successfully")