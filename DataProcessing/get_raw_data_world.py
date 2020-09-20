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

def main():
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


	data_file = f"{p.RAW_DATA}/data.csv"

	col_num = len(global_death.columns)

	
	headers = ['country', 'date', 'confirmed', 'deaths']
	with open(data_file, 'w') as f:
		f_csv = csv.writer(f)
		f_csv.writerow(headers)
		for country in countries:
			df_confirmed = global_confirmed.loc[global_confirmed[CR]==country]
			df_death = global_death.loc[global_death[CR]==country]
			for date in dates:
				num_confirmed = df_confirmed[date].sum()
				num_death = df_death[date].sum()
				
				line = f"{country},{date},{num_confirmed},{num_death}"
				
				if len(line)>MIN_LINE_LEN:
					print(line)
					row = [(country.replace('*',""), date, num_confirmed, num_death)]
					f_csv.writerows(row)
				else:
					print("line lengh Error")
		
if __name__ == "__main__":
	create_paths(p.DATE)
	main()
