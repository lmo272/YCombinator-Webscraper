import pandas as pd
import matplotlib.pyplot as plt

yc = pd.read_csv("ycombinator_full.csv")

location = yc.groupby("location").count()
print(location)
