# usage: python3 split_and_drop.py [world/us] [threhold]
# example: python3 split_and_drop.py us 20

import os
os.chdir("../")
import sys
sys.path.insert(0, ".")
from utils import *

# global variables
argv1 = sys.argv[1]
argv2 = sys.argv[2]
print(argv1)
print(argv2)
if argv1 == 'world':
	p.DATE = 'DateWorld'
elif argv1 == 'us':
	p.DATE = 'DateUS'
else:
	print("Argument Error")
	exit(1)



threshold = (int)(argv2)
if threshold < 0:
	print("Argument Error")
	exit(1)



def new_per_day(df, col, index):
	'''
	example:
	df = df_china
	col = 'confirmed'
	index = 2
	return: 920-643
	'''
	if index == 0:
		return 0
	else:
		return (df.at[index, col] - df.at[index-1, col])

def tag_day(df, threshold):
	start = False
	col = 'confirmed'
	new_col = 'tagged_day'
	index = 1
	for i in range(0, len(df)):
		if df.at[i, col] >= threshold:
			start = True
		if start == True:
			df.at[i, new_col] = index
			index = index + 1
		else:
			df.at[i, new_col] = 0
	df[new_col] = df[new_col].astype(int)  


def main():

	df = pd.read_csv(f"{p.RAW_DATA}/data.csv")
	ITEMs = list(set(df[p.ITEM].array))
	ITEMs.sort()

	index_item = {}
	item_index = {}
	for i, item in enumerate(ITEMs):
		index_item[i] = item
		item_index[item] = i

	for item in ITEMs:
		df_item = df.loc[df[p.ITEM]==item]
		df_item.to_csv(f"{p.SPLIT}/{item}.csv", index=False)


	c = 'confirmed'
	d = 'deaths'
	nc = 'new_confirmed'
	nd = 'new_deaths'
	for item in ITEMs:
		df_item = pd.read_csv(f"{p.SPLIT}/{item}.csv")
		df_item[nc] = [new_per_day(df_item, c ,i) for i in range(len(df_item))]
		df_item[nd] = [new_per_day(df_item, d ,i) for i in range(len(df_item))]
		df_item.to_csv(f"{p.N_CASE}/{item}.csv", index=False)


	for item in ITEMs:
		df_item = pd.read_csv(f"{p.N_CASE}/{item}.csv")
		tag_day(df_item, threshold)
		df_item.to_csv(f"{p.TAG_DAY}/{item}.csv", index=False)

	for item in ITEMs:
		df_item = pd.read_csv(f"{p.TAG_DAY}/{item}.csv")
		df_item = df_item.drop(df_item[df_item['tagged_day']==0].index)
		df_item.to_csv(f"{p.DRP}/{item}.csv", index=False)

	# start to draw pictures


if __name__ == '__main__':
	create_paths(p.DATE)
	main()

