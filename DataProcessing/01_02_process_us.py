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

p.DATE = "DateUS"
jhk_path = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
us_confirmed_path = jhk_path + 'time_series_covid19_confirmed_US.csv'
us_death_path = jhk_path + 'time_series_covid19_deaths_US.csv'
STATE = 6
START = 11
MIN_LINE_LEN = 7
CR = 'Province_State'
POP = 'Population'


# In[2]:


def misplaced_subtraction(alist):
    alist = np.array(list(alist))
    A = alist[:len(alist)-1]
    B = alist[1:len(alist)]
    return np.insert(B-A, 0, 0)


# In[78]:


def main():
    threshold = int(sys.argv[1])
    create_paths(p.DATE)
    us_confirmed = pd.read_csv(us_confirmed_path)
    us_death = pd.read_csv(us_death_path)
    us_death = us_death.drop([POP], axis=1)

    states = list(set(us_confirmed[CR]))
    states.sort()

    dates = list(us_confirmed.columns)[START:]


    if len(us_death) != len(us_confirmed):
        print("Number of State Error")

    check_state = us_death[CR] == us_confirmed[CR]

    if False in list(check_state):
        print("State not one-to-one Error")

    check_col = us_death.columns == us_confirmed.columns

    if False in check_col:
        print("Column different Error")


    columns_drop = ['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Country_Region', 'Lat', 'Long_', 'Combined_Key']
    df_us_confirmed_group = us_confirmed.drop(columns=columns_drop).groupby(CR).sum().transpose()
    df_us_death_group = us_death.drop(columns=columns_drop).groupby(CR).sum().transpose()
    date = df_us_confirmed_group.index

    for state in states:
        confirmed = df_us_confirmed_group[state]
        deaths = df_us_death_group[state]
        new_confirmed = misplaced_subtraction(confirmed)
        new_deaths = misplaced_subtraction(deaths)
        d = {"state": state, "date":date, "confirmed": confirmed, "deaths": deaths,
            "new_confirmed":new_confirmed, "new_deaths":new_deaths}
        df = pd.DataFrame(data=d)

        df = df[df["confirmed"] > threshold]

        df["tagged_day"] = range(1,len(df)+1)
        df.to_csv(f"{p.DRP}/{state}.csv", index=False)


# In[ ]:


if __name__ == "__main__":
    main()

