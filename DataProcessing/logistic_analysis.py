import os
os.chdir("../")
import sys
sys.path.insert(0, ".")
from utils import *
from utils.paths import *
from utils.logistic_curve import *
import utils.paths as p

argv1 = sys.argv[1]
if(argv1 == 'world'):
	p.DATE = 'DateWorld'
	p.ITEM = 'country'
elif (argv1 == 'us'):
	p.DATE = "DateUS"
	p.ITEM = 'state'
else:
	print("Argument Error")
	exit(1)

create_paths(p.DATE)

argv2 = sys.argv[2]
if(argv2 == "confirmed"):
	Y_FIELD = "confirmed"
elif (arv2 == "deaths"):
	Y_FIELD = "deaths"
else:
	print("Argument Error")
	exit(1)




def main():

	X_FIELD = "tagged_day"
	

	df = pd.read_csv(f"{p.RAW_DATA}/data.csv")
	items = list(set(df[p.ITEM].array))
	items.sort()

	index_item = {}
	item_index = {}
	for i, item in enumerate(items):
		index_item[i] = item
		item_index[p.ITEM] = i

	data_file = f"{p.LR}/analyzed_data.csv"
	headers = [p.ITEM,'tagged_day_zero','train_error','test_error','suggested_test_size','a','b','c']
	with open(data_file, "w") as f:
		f_csv = csv.writer(f)
		f_csv.writerow(headers)
		for i, item in enumerate(items):
			region_index = i
			DATA = f"{p.DRP}/{index_item[region_index]}.csv"

			print(item)
			try:
				
				#test_size, diff, sol, train_error, test_error = find_best_test_size(DATA, X_FIELD, Y_FIELD)
				test_size, diff, sol, train_error, test_error,a,b,c = plot_logistic(item, p.LR, X_FIELD, Y_FIELD)
				print(f"{item},{sol},{train_error},{test_error}, {test_size}, {a},{b},{c}")
				row = [(item, sol, train_error, test_error, test_size,a,b,c)]

			except:
				print(f"{item},-1,-1,-1,-1,-1,-1,-1")
				row = [(item, -1, -1, -1, -1,-1,-1,-1)]
			f_csv.writerows(row)


if __name__ == "__main__":
	create_paths(p.DATE)
	main()

