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



def main():
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


	data_file = f"{p.RAW_DATA}/data.csv"

	col_num = len(us_death.columns)

	
	headers = ['state', 'date', 'confirmed', 'deaths']
	with open(data_file, 'w') as f:
		f_csv = csv.writer(f)
		f_csv.writerow(headers)
		for state in states:
			df_confirmed = us_confirmed.loc[us_confirmed[CR]==state]
			df_death = us_death.loc[us_death[CR]==state]
			for date in dates:
				num_confirmed = df_confirmed[date].sum()
				num_death = df_death[date].sum()
				
				line = f"{state},{date},{num_confirmed},{num_death}"
				
				if len(line)>MIN_LINE_LEN:
					print(line)
					row = [(state, date, num_confirmed, num_death)]
					f_csv.writerows(row)
				else:
					print("line lengh Error")
		
if __name__ == "__main__":
	create_paths(p.DATE)
	print(p.today)
	main()
