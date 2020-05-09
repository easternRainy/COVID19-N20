from utils import *
from utils.paths import *
import utils.paths as p

countries, index_country, country_index = get_countries()
states, index_state, state_index = get_us_states()

#---------------------------Countries--------------------------------------

# plot cumulative cases multicountry
def plot_cumulative_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("Cumulative Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Confirmed Cases")
	for country in countries:
		df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
		plt.plot(df_country["tagged_day"], df_country["confirmed"], label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_normalized_cumulative_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("Normalized Cumulative Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Normalized Confirmed Cases")
	for country in countries:
		population = country_population[country]
		area = country_area[country]
		density = population / area
		#display(f"{country},{population},{area},{density}")
		if density > 0:
			df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
			plt.plot(df_country["tagged_day"], df_country["confirmed"]/density, label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

# plot new comfirmed cases multicountry
def plot_new_confirmed_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("New Daily Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("New Confirmed Cases")
	for country in countries:
		df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
		plt.plot(df_country["tagged_day"], df_country["new_confirmed"], label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

# plot deaths cases multicountry
def plot_deaths_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("Cumulative Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Death Cases")
	for country in countries:
		df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
		plt.plot(df_country["tagged_day"], df_country["deaths"], label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_normalized_deaths_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("Normalized Cumulative Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Normalized Death Cases")
	for country in countries:
		population = country_population[country]
		area = country_area[country]
		density = population / area
		if density > 0:
			df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
			plt.plot(df_country["tagged_day"], df_country["deaths"]/density, label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_new_deaths_multi_country(selected_countries):
	assert p.DATE == "DateWorld"
	
	plt.clf()
	countries = [index_country[c] for c in selected_countries]
	plt.title("Daily Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Daily Death Cases")
	for country in countries:
		df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
		plt.plot(df_country["tagged_day"], df_country["new_deaths"], label=country)
	plt.legend(countries, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_cumulative_country_save(country_index):
	assert p.DATE == "DateWorld"
	country = index_country[country_index]
	df = pd.read_csv(f"{p.DRP}/{country}.csv")
	plt.clf()
	plt.title(f"{country} Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Confirmed Cases")
	plt.bar(df["tagged_day"], df["confirmed"])
	plt.savefig(f"{p.CUM}/{country}.jpg")
	plt.clf()

def plot_deaths_country_save(country_index):
	assert p.DATE == "DateWorld"
	country = index_country[country_index]
	df = pd.read_csv(f"{p.DRP}/{country}.csv")
	plt.title(f"{country} Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Death Cases")
	plt.bar(df["tagged_day"], df["deaths"])
	plt.savefig(f"{p.DEA}/{country}.jpg")
	plt.clf()

def plot_new_confirmed_new_deaths_country(country_index):
	assert p.DATE == "DateWorld"
	country = index_country[country_index]
	df_country = pd.read_csv(f"{p.DRP}/{country}.csv")
	plt.clf()

	# plt.ylabel("Cases")
	plt.title("Title")
	plt.subplot(211)
	# plt.title(f"{country} Daily New Confirmed Cases")
	plt.bar(df_country['tagged_day'], df_country['new_confirmed'])
	plt.ylabel("New Confirmed Cases")
	plt.subplot(212)
	#plt.title(f"{country} Daily Death Cases")
	plt.bar(df_country['tagged_day'], df_country['new_deaths'])
	plt.xlabel(f"Day in {country} since N=20")
	plt.ylabel("New Death Cases")
	# plt.legend(['Daily New Confirmed Cases', 'Daily Death Cases'], bbox_to_anchor=(1, 0.5))



#---------------------------US States--------------------------------------


# plot cumulative cases multistate
def plot_cumulative_multi_state(selected_states):
	assert p.DATE == "DateUS"
	plt.clf()
	states = [index_state[c] for c in selected_states]
	plt.title("Cumulative Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Confirmed Cases")
	for state in states:
		df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
		plt.plot(df_state["tagged_day"], df_state["confirmed"], label=state)
	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

# def plot_normalized_cumulative_multi_state(selected_states):
# 	assert p.DATE == "DateUS"
# 	plt.clf()
# 	states = [index_state[c] for c in selected_states]
# 	plt.title("Normalized Cumulative Confirmed Cases Since N=20")
# 	plt.xlabel("Day")
# 	plt.ylabel("Normalized Confirmed Cases")
# 	for state in states:
# 		population = state_population[state]
# 		area = state_area[state]
# 		density = population / area
# 		#display(f"{state},{population},{area},{density}")
# 		if density > 0:
# 			df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
# 			plt.plot(df_state["tagged_day"], df_state["confirmed"]/density, label=state)
# 	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

# plot new comfirmed cases multistate
def plot_new_confirmed_multi_state(selected_states):
	assert p.DATE == "DateUS"
	plt.clf()
	states = [index_state[c] for c in selected_states]
	plt.title("New Daily Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("New Confirmed Cases")
	for state in states:
		df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
		plt.plot(df_state["tagged_day"], df_state["new_confirmed"], label=state)
	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

# plot deaths cases multistate
def plot_deaths_multi_state(selected_states):
	assert p.DATE == "DateUS"
	plt.clf()
	states = [index_state[c] for c in selected_states]
	plt.title("Cumulative Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Death Cases")
	for state in states:
		df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
		plt.plot(df_state["tagged_day"], df_state["deaths"], label=state)
	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

# def plot_normalized_deaths_multi_state(selected_states):
# 	assert p.DATE == "DateUS"
# 	plt.clf()
# 	states = [index_state[c] for c in selected_states]
# 	plt.title("Normalized Cumulative Death Cases Since N=20")
# 	plt.xlabel("Day")
# 	plt.ylabel("Normalized Death Cases")
# 	for state in states:
# 		population = state_population[state]
# 		area = state_area[state]
# 		density = population / area
# 		if density > 0:
# 			df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
# 			plt.plot(df_state["tagged_day"], df_state["deaths"]/density, label=state)
# 	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_new_deaths_multi_state(selected_states):
	assert p.DATE == "DateUS"
	
	plt.clf()
	states = [index_state[c] for c in selected_states]
	plt.title("Daily Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Daily Death Cases")
	for state in states:
		df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
		plt.plot(df_state["tagged_day"], df_state["new_deaths"], label=state)
	plt.legend(states, loc='center left', bbox_to_anchor=(1, 0.5))

def plot_cumulative_state_save(state_index):
	assert p.DATE == "DateUS"
	state = index_state[state_index]
	df = pd.read_csv(f"{p.DRP}/{state}.csv")
	plt.clf()
	plt.title(f"{state} Confirmed Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Confirmed Cases")
	plt.bar(df["tagged_day"], df["confirmed"])
	plt.savefig(f"{p.CUM}/{state}.jpg")
	plt.clf()

def plot_deaths_state_save(state_index):
	assert p.DATE == "DateUS"
	state = index_state[state_index]
	df = pd.read_csv(f"{p.DRP}/{state}.csv")
	plt.title(f"{state} Death Cases Since N=20")
	plt.xlabel("Day")
	plt.ylabel("Death Cases")
	plt.bar(df["tagged_day"], df["deaths"])
	plt.savefig(f"{p.DEA}/{state}.jpg")
	plt.clf()

def plot_new_confirmed_new_deaths_state(state_index):
	assert p.DATE == "DateUS"
	state = index_state[state_index]
	df_state = pd.read_csv(f"{p.DRP}/{state}.csv")
	plt.clf()

	# plt.ylabel("Cases")
	plt.title("Title")
	plt.subplot(211)
	# plt.title(f"{state} Daily New Confirmed Cases")
	plt.bar(df_state['tagged_day'], df_state['new_confirmed'])
	plt.ylabel("New Confirmed Cases")
	plt.subplot(212)
	#plt.title(f"{state} Daily Death Cases")
	plt.bar(df_state['tagged_day'], df_state['new_deaths'])
	plt.xlabel(f"Day in {state} since N=20")
	plt.ylabel("New Death Cases")
	# plt.legend(['Daily New Confirmed Cases', 'Daily Death Cases'], bbox_to_anchor=(1, 0.5))
	