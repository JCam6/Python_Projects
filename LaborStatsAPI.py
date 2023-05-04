#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import requests
import json
import prettytable
import csv
import matplotlib
import matplotlib.pyplot as plt


# In[28]:


headers = {"Content-type": "application/json"}

data = json.dumps(
    {
        "seriesid": ["CUUR0000SA0"],
        "startyear": "2018",
        "endyear": "2018",
    }
)

p = requests.post(
    "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
)

json_data = json.loads(p.text)

for series in json_data["Results"]["series"]:
    x = prettytable.PrettyTable(["series id", "year", "period", "value", "footnotes"])
    seriesId = series["seriesID"]
    for item in series["data"]:
        year = item["year"]
        period = item["period"]
        value = item["value"]
        footnotes = ""
        for footnote in item["footnotes"]:
            if footnote:
                footnotes = footnotes + footnote["text"] + ","
        if "M01" <= period <= "M12":
            x.add_row([seriesId, year, period, value, footnotes[0:-1]])

output = open(seriesId + ".csv", "w")
output.write(x.get_string())
output.close()


# In[20]:


data_pull = pd.read_csv("CUUR0000SA0.csv", delimiter="|", header=[1], skiprows=[2, 15])
data_pull.sort_values(by=" period ", ascending=[True], inplace=True)
data_pull


# In[21]:


data_pull.keys()


# In[27]:


get_ipython().run_line_magic("matplotlib", "inline")
data_pull.plot(
    figsize=(12, 8),
    kind="bar",
    x=" period ",
    y="  value  ",
    legend=False,
)

plt.ylabel("Value")
plt.xlabel("Period")

plt.axis([-1, 12, 246, 255])
plt.grid(True)


# In[ ]:


# In[ ]:
