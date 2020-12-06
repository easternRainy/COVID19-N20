MIT License

Copyright (c) [2020] [Sicheng Zhou]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# COVID19-N20

## Description
I process the COVID-19 data provided by [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series). For World Data, first I split original data by countries. Then I tag the day as day 1 when there are at least 20 confirmed cases in that country. Finally I drop previous days before day 1. For US data, I split original data by states and do the same with threshold 10.

For example: 
- [2020-04-18 US.csv](https://github.com/secregister01/COVID19-N20/blob/master/DateWorld/2020-04-18/DroppedDay/US.csv)
	- country: US
	- date: from 3/2/20 to 4/17/20
	- confirmed: cumulative confirmed cases in US
	- deaths: cumulative death cases in US
	- new_confirmed: new confirmed cases in some day
	- new_deaths: new death cases in some day
	- tagged_day: how many days since "day 1", when there are at least 20 confirmed cases in US


- [2020-04-18 California.csv](https://github.com/secregister01/COVID19-N20/blob/master/DateUS/2020-04-18/DroppedDay/California.csv)
	- state: California
	- date: from 3/2/20 to 4/17/20
	- confirmed: cumulative confirmed cases in California
	- deaths: cumulative death cases in California
	- new_confirmed: new confirmed cases in some day
	- new_deaths: new death cases in some day
	- tagged_day: how many days since "day 1", when there are at least 10 confirmed cases in California

## Why N20?
This idea comes from the [blog](https://statisticsbyjim.com/basics/coronavirus). The author points out that setting the first day when there exist at least 20 confirmed cases can help people compare the situations in different regions by almost the same initial condition.

## Update
I will update the repository each day after Johns Hopkins CSSE updates their data until the end of COVID-19. So the dataset in today's folder may contain data upto today or yesterday. Feel free to use the data to do further analysis.

## Build the Dataset Using my Script

```
git clone https://github.com/secregister01/2020-04-13_COVID19-N20.git
cd DataProcessing
./core.sh
```
You can modify the code in core.sh to disable "github_share.py", that is, delete the last two lines of core.sh. This script is to update this repo for myself.

## Use Different Threshold Value

If you want to tag the day as day 1 when there are at least N confirmed cases in some country, say 50, you can modify DataProcessing/core.sh, changing COUNTRY_THRESHOLD's value

```
COUNTRY_THRESHOLD=50
```

For us state, change STATE_THRESHOLD to M, for example
```
STATE_THRESHOLD=30
```

After modifying the script,

```
cd DataProcessing
./core.sh
```

## Examples
- [Data Visualization](Notebooks/DataVisualization.ipynb)
- [Logistic Analysis](Notebook/LogisticModel.ipynb)

## References:
- https://github.com/CSSEGISandData/COVID-19
- https://statisticsbyjim.com/basics/coronavirus