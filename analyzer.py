import os
import sys
import re
import pandas as pd
import matplotlib.pypplot as plt


BASE_RESULTS_DIR = "results"


def parse_run(run_folder_path):
	sim_out = os.path.join(run_folder_path, "sim.out") 
	power_out = os.path.join(run_folder_path, "powerstack.txt")
	config_file = 
