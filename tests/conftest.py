import sys
from os.path import abspath
from os.path import dirname as d

parent_dir = f"{d(d(abspath(__file__)))}"
sys.path.append(f"{parent_dir}/src")
