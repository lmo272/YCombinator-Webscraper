import pandas as pd

links_1 = pd.read_csv("working_links_0-100.csv")
links_2 = pd.read_csv("working_links_100-10000.csv")
links_3 = pd.read_csv("working_links_10001-20000.csv")
links_4 = pd.read_csv("working_links_20001-30000.csv")

links_1.columns = ["index", "links"]
links_2.columns = ["index", "links"]
links_3.columns = ["index", "links"]
links_4.columns = ["index", "links"]

links = links_1.append(links_2).append(links_3).append(links_4)
links.to_csv("merged_working_links.csv")
