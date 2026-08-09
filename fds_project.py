import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Job_Postings": [1200, 1450, 1800, 2300, 3100, 3900, 4700]
}

df = pd.DataFrame(data)

print(df)

plt.plot(df["Year"], df["Job_Postings"], marker="o")
plt.xlabel("Year")
plt.ylabel("Job Postings")
plt.title("Data Science Job Posting Trend")
plt.grid(True)
plt.show()
