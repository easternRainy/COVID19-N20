import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import datetime
import os
import requests
import re
import numpy as np
from bs4 import BeautifulSoup
import csv
import sys

from utils.paths import *
import utils.paths as p

def create_path(path_name):
	split = path_name.split("/")
	to_create = split[len(split)-1]
	root = '/'.join(split[0:len(split)-1])
	if to_create not in os.listdir(root):
		os.mkdir(path_name)

def create_paths(ROOT):
	DATE = ROOT
	today = str(datetime.date.today())
	if DATE == "DateWorld":
		ITEM = 'country'
	elif DATE == "DateUS":
		ITEM = 'state'
	else:
		print("Range Error, world or US")
		exit(1)
		
	WORK = f"{DATE}/{today}"

	DRP = f"{WORK}/DroppedDay"
	
	ANA = f"{WORK}/Analysis"
	LR = f"{ANA}/LogisticRegression"
	
	# modify global variables
	p.DATE = DATE
	p.today = today
	p.ITEM = ITEM
	p.WORK = WORK
	p.DRP = DRP
	p.ANA = ANA
	p.LR = LR
	



	if DATE not in os.listdir():
		os.mkdir(DATE)

	paths = [WORK, DRP, ANA, LR]
	for path in paths:
		create_path(path)

# return list of countries, and two dictionaries
def get_countries():
	today = str(datetime.date.today())
	df = pd.read_csv(f"DateWorld/{today}/RawData/data.csv")
	countries = list(set(df['country'].array))
	countries.sort()
	index_country = {}
	country_index = {}
	for i, country in enumerate(countries):
		index_country[i] = country
		country_index[country] = i
	return countries, index_country, country_index

def get_us_states():
	today = str(datetime.date.today())
	df = pd.read_csv(f"DateUS/{today}/RawData/data.csv")
	states = list(set(df['state'].array))
	states.sort()
	index_state = {}
	state_index = {}
	for i, state in enumerate(states):
		index_state[i] = state
		state_index[state] = i
	return states, index_state, state_index

# search google to get gdp of country
def get_gdp_pc(country):
	query_country = country.lower().replace(" ", "+")
	gdp_regex = "[0-9,.]+ USD \([0-9]+\)"
	query = f"https://www.google.com/search?q={query_country}+gdp+per+capita&rlz=1C5CHFA_enUS890US890&oq={query_country}+GDP+per+capita"
	html = requests.get(query)
	html = (str)(html.content)
	return re.findall(gdp_regex, html) 

# search google to get population of country
def get_population(country):
	query_country = country.lower().replace(" ", "+")
	query = f"https://www.google.com/search?q={query_country}+population&rlz=1C5CHFA_enUS890US890&oq={query_country}+population"
	html = requests.get(query).content
	soup = BeautifulSoup(html, 'html.parser')
	population = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
	try:
		return population.get_text()
	except:
		return -1

# search google to get area of country
def get_area(country):
	query_country = country.lower().replace(" ", "+")
	query = f"https://www.google.com/search?q={query_country}+area&rlz=1C5CHFA_enUS890US890&oq={query_country}+area"
	html = requests.get(query).content
	soup = BeautifulSoup(html, 'html.parser')
	area = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
	try:
		return area.get_text()
	except:
		return -1

# create country-gdp dictionary
def create_country_gdp(file):
	result = {}
	with open(file, "r") as f:
		lines = f.read().split("\n")
		for line in lines:
			
			line = line.split(":")
			
			country = line[0]
			gdp = (float)(line[1])
			result[country] = gdp
	return result


# create country-population dictionary
def create_country_population(file):
	result = {}
	with open(file, "r") as f:
		lines = f.read().split("\n")
		for line in lines:
			line = line.split(":")
			
			country = line[0]
			population = (float)(line[1])
			result[country] = population
	return result

# get cumulative death today of region
def today_cumulative_death(region):
	df_region = pd.read_csv(f"{p.DRP}/{region}.csv")
	return df_region.iloc[len(df_region)-1]["deaths"]

# create country-cumulative_death dictionary
def create_country_cumulative_death(countries):
	result = {}
	countries,_,_ = get_countries()
	for country in countries:
		try:
			
			deaths = today_cumulative_death(country)
			
		except:
			deaths = -1
			
		result[country] = deaths
		#print(f"{country},{deaths}")
	return result

# create country-area dictionary
def create_country_area(file):
	result = {}
	with open(file, "r") as f:
		lines = f.read().split("\n")
		for line in lines:
			line = line.split(":")
			
			country = line[0]
			area = float(line[1])
			result[country] = area
	return result

# Diffenence of Tagged Day of peak new deaths and new confimed
def peak_diff(region):
	peak_new_confirmed = 0
	peak_new_confirmed_tagged_day = 0
	peak_new_deaths = 0
	peak_new_deaths_tagged_day = 0
	
	df_region = pd.read_csv(f"{p.DRP}/{region}.csv")
	for index, row in df_region.iterrows():
		if row['new_confirmed'] > peak_new_confirmed:
			peak_new_confirmed = row['new_confirmed']
			peak_new_confirmed_tagged_day = row['tagged_day']
		if row['new_deaths'] > peak_new_deaths:
			peak_new_deaths = row['new_deaths']
			peak_new_deaths_tagged_day = row['tagged_day']
	if peak_new_confirmed_tagged_day==0 and peak_new_deaths_tagged_day == 0:
		return -1
	else:
		return peak_new_deaths_tagged_day - peak_new_confirmed_tagged_day

def create_country_peak_diff():
	result = {}
	countries, _, _ = get_countries()
	for country in countries:
		diff = peak_diff(country)
		if(diff != -1):
			result[country] = diff
	return result
