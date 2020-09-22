JHK="../COVID-19"
JHK_COVID_URL="https://github.com/CSSEGISandData/COVID-19.git"

COUNTRY_THRESHOLD=20
STATE_THRESHOLD=10

if [ ! -d $JHK ];then
	CURR_DIR="$PWD"
	cd ..
	git clone $JHK_COVID_URL
	cd "$CURR_DIR"
fi

cd $JHK
git pull
cd ../DataProcessing
echo "Process Global Data"
python3 01_01_process_world.py $COUNTRY_THRESHOLD

echo "Process US Data"
python3 01_02_process_us.py $STATE_THRESHOLD

echo "Logistic Analysis World Confirmed"
python3 logistic_analysis.py world confirmed

echo "Logistic Analysis US Confirmed"
python3 logistic_analysis.py us confirmed

echo "Update Notebooks"
jupyter nbconvert --to notebook --inplace --execute ../Notebooks/Covid19-N20.ipynb
jupyter nbconvert --to notebook --inplace --execute ../Notebooks/LogisticModel.ipynb

echo "Update Github"
python3 github_share.py
