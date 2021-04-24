import csv
import pandas as pd
import plotly.express as px

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total = 0
totalAttepmts = len(file_data)

for x in file_data:
    total += float(x[2])

mean = total / totalAttepmts

df = pd.read_csv("data.csv")
fig = px.scatter(df, x = "student_id", y = "level", color = "attempt")
fig.show()