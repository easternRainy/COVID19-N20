import os
os.chdir("../")
import sys
sys.path.insert(0, ".")
from utils import *
from utils.paths import *
import utils.paths as p
from pathlib import Path
import shutil

def add_paths():
	
	os.system(f"git add {p.DRP}/*")
	os.system(f"git add {p.LR}/*")

# remove all the paths that is yesterday and before
def remove_local_paths():
	for day in os.listdir(p.DATE):
		day = (str)(day)
		if day != p.today:
			try:
				os.system(f"rm -rf {os.path.join(p.DATE,day)}")
			except:
				continue

def remove_remote_paths():
	remote_files = os.popen("git ls-files").read().split("\n")
	to_delete = []
	for file in remote_files:
		try:
			tmp = file.split("/")
			if tmp[0] == p.DATE and tmp[1] != p.today:
				to_delete.append(file)
				#print(f"git rm -r {tmp[0]}/{tmp[1]}")
					
		except:
			continue

	for file in to_delete:
		try:
			print(f"git rm \"{file}\"")
			os.system(f"git rm \"{file}\"")
		except:
			continue

	
		

def workflow(ROOT):
	p.DATE = ROOT
	create_paths(p.DATE)
	add_paths()
	remove_local_paths()
	remove_remote_paths()


def main():
	workflow("DateWorld")
	workflow("DateUS")	

	os.system(f"git commit -m {p.today}")
	os.system("git push")

if __name__ == "__main__":
	main()
