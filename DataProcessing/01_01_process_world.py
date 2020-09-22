#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir("../")
import sys
sys.path.insert(0, ".")
from utils import *
from utils.paths import *
import utils.paths as p

p.DATE = "DateWorld"
jhk_path = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
global_confirmed_path = jhk_path + 'time_series_covid19_confirmed_global.csv'
global_death_path = jhk_path + 'time_series_covid19_deaths_global.csv'
COUNTRY = 1
START = 4
MIN_LINE_LEN = 7
CR = 'Country/Region'


# In[59]:


def misplaced_subtraction(alist):
    alist = np.array(list(alist))
    A = alist[:len(alist)-1]
    B = alist[1:len(alist)]
    return np.insert(B-A, 0, 0)


# In[ ]:


def main():
    threshold = int(sys.argv[1])
    create_paths(p.DATE)
    
    global_confirmed = pd.read_csv(global_confirmed_path)
    global_death = pd.read_csv(global_death_path)

    countries = list(set(global_confirmed[CR]))
    countries.sort()

    dates = list(global_confirmed.columns)[START:]


    if len(global_death) != len(global_confirmed):
        print("Number of Country Error")

    check_country = global_death['Country/Region'] == global_confirmed['Country/Region']

    if False in list(check_country):
        print("Country not one-to-one Error")

    check_col = global_death.columns == global_confirmed.columns

    if False in check_col:
        print("Column different Error")

    df_global_confirmed_group = global_confirmed.groupby(CR).sum().drop(columns=["Lat", "Long"]).transpose()
    df_global_death_group = global_death.groupby(CR).sum().drop(columns=["Lat", "Long"]).transpose()
    date = df_global_confirmed_group.index
    
    for country in countries:
        confirmed = df_global_confirmed_group[country]
        deaths = df_global_death_group[country]
        new_confirmed = misplaced_subtraction(confirmed)
        new_deaths = misplaced_subtraction(deaths)
        d = {"country": country, "date":date, "confirmed": confirmed, "deaths": deaths,
            "new_confirmed":new_confirmed, "new_deaths":new_deaths}
        df = pd.DataFrame(data=d)

        df = df[df["confirmed"] > threshold]

        df["tagged_day"] = range(1,len(df)+1)
        df.to_csv(f"{p.DRP}/{country}.csv", index=False)


# In[ ]:


if __name__ == "__main__":
    main()

