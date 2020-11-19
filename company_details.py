import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

columns = ["name", "year_founded", "team_size", "location", "batch", "short_description", "long_description"]
ycombinator = pd.DataFrame(columns=columns)

links = pd.read_csv("merged_working_links.csv")
links.columns = ["index_1","index_2", "links"]
links_list = links["links"].values.tolist()
print(links_list)


for i in np.arange(0, len(links_list)):
    url = links_list[i]
    request = requests.get(url)
    page = request.text
    soup = BeautifulSoup(page, "html.parser")

    name = (soup.find("div", {"h1", "heavy"})).get_text(strip=True)
    short_description = (soup.find("h3").get_text(strip=True))
    long_description = (soup.find("p").get_text(strip=True))

    details = (soup.find(("div"), ("highlight-box"))).get_text(strip=True)
    matchObj = re.match(r'(.*)Founded(\d*)Team Size(\d*)Location(.*)', details,re.M|re.I)

    year = matchObj.group(2)
    team_size = matchObj.group(3)
    location = matchObj.group(4)

    batch = (soup.find(("span"), ("pill pill-orange"))).get_text(strip=True)

    dict = {
        "name": name,
        "year_founded": year,
        "team_size": team_size,
        "location": location,
        "batch": batch,
        "short_description": short_description,
        "long_description": long_description,
        }

    ycombinator = ycombinator.append(pd.DataFrame.from_records([dict], columns=dict.keys()))

ycombinator.to_csv("ycombinator_full.csv")
