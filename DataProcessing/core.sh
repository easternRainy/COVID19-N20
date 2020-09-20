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
echo "Get Raw Data World"
python3 get_raw_data_world.py

echo "Get Raw Data US"
python3 get_raw_data_us.py

echo "Split Data World"
python3 split_and_drop.py world $COUNTRY_THRESHOLD

echo "Split Data US"
python3 split_and_drop.py us $STATE_THRESHOLD

echo "Logistic Analysis World Confirmed"
python3 logistic_analysis.py world confirmed

echo "Logistic Analysis US Confirmed"
python3 logistic_analysis.py us confirmed

echo "Update Github"
python3 github_share.py
