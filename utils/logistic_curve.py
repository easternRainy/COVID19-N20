from utils import *
from utils.paths import *
import utils.paths as p

from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def train_test_split_by_DATA(DATA, X_FIELD, Y_FIELD, test_size=0.2):
	df_region = pd.read_csv(DATA)
	df_train, df_test = train_test_split(df_region, test_size=test_size)
	x_train, y_train = df_train[X_FIELD].values, df_train[Y_FIELD].values
	x_test, y_test = df_test[X_FIELD].values, df_test[Y_FIELD].values
	
	return x_train, y_train, x_test, y_test

def logistic_model(x, a, b, c):
	#print(x)
	return c/(1 + np.exp(-(x-b)/a))

def ratio_error(y_pred, y_test):
	tmp =  [np.power((a-b)/b, 2) for a, b in zip(y_pred, y_test)]
	return np.sqrt(sum(tmp)/len(tmp))

def logistic_learn2(x_train, y_train, x_test, y_test):
	x_train_list, y_train_list, x_test_list, y_test_list = [list(o) for o in [x_train, y_train, x_test, y_test]]
	fit = curve_fit(logistic_model, x_train_list, y_train_list, maxfev=10000000)
	params, params_covariance = fit
	a = params[0]
	b = params[1]
	c = params[2]
	#display(f"{a},{b},{c}")
	# which day to end
	sol = int(fsolve(lambda x : logistic_model(x, a, b, c) - int(c),b))
	
	y_train_pred = logistic_model(x_train_list, a,b,c)
	train_error = ratio_error(y_train_pred, y_train)
	y_test_pred = logistic_model(x_test_list, a,b,c)
	test_error = ratio_error(y_test_pred, y_test)
	
	return sol, (float)(a), (float)(b), (float)(c), train_error, test_error


def find_best_test_size(DATA, X_FIELD, Y_FIELD):
	best_test_size = 10
	best_diff = 10
	best_sol = -1
	best_train_error = -1
	best_test_error = -1
	for i in np.arange(0.15,0.7,0.01):
		x_train, y_train, x_test, y_test = train_test_split_by_DATA(DATA, X_FIELD, Y_FIELD, i)
		sol, a,b,c, train_error, test_error = logistic_learn2(x_train, y_train,x_test, y_test)
		diff = abs(train_error - test_error)
		if(diff < best_diff):
			best_diff = diff
			best_test_size = i
			best_sol, best_train_error, best_test_error = sol, train_error, test_error
	return best_test_size, best_diff, best_sol, best_train_error, best_test_error
	
def plot_logistic(region, savepath, X_FIELD, Y_FIELD):

	DATA = f"{p.DRP}/{region}.csv"
	
	df_region = pd.read_csv(DATA)
	test_size,best_diff,best_sol,best_train_error,best_test_error = find_best_test_size(DATA, X_FIELD, Y_FIELD)
	
	x_train, y_train, x_test, y_test = train_test_split_by_DATA(DATA, X_FIELD, Y_FIELD, test_size)
	sol, a, b, c, train_error, test_error = logistic_learn2(x_train, y_train,x_test, y_test)
	print(f"{sol},{a},{b},{c}")
	x = np.linspace(0,200, 1000)
	y = logistic_model(x, a, b, c)
	plt.clf()
	plt.xlabel("Day")
	plt.title(f"{Y_FIELD} Cases in {region}, sol={sol}")
	plt.plot(x, y, "red")
	plt.plot(df_region[X_FIELD], df_region[Y_FIELD], "blue")
	print(f"{savepath}/{region}.jpg")
	plt.savefig(f"{savepath}/{region}.jpg")

	return test_size,train_error-test_error,sol,train_error,test_error,a,b,c