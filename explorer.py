import os
import subprocess

l1_sizes = ["32", "64"]
l2_sizes = ["256", "512"]

SNIPER_DIR = "/home/teutu/snipersim"
SNIPER_EXE = os.path.join(SNIPER_DIR, "run-sniper")
CONFIG_FILE= os.path.join(SNIPER_DIR, "config/gainestown.cfg")
BENCHMARK = os.path.join(SNIPER_DIR, "test/fft/fft")

def run_explorer():
	experiment_title = os.path.abspath("DSE_Results")
	os.makedirs(experiment_title, exist_ok=True)

	for l1 in l1_sizes:
		for l2 in l2_sizes:
			run_dir = os.path.join(experiment_title, f"run_L1_{l1}_L2_{l2}")
			os.makedirs(run_dir, exist_ok=True)

			cmd = [SNIPER_EXE, "-c", CONFIG_FILE,  "-c", f"perf_model/l1_dcache/cache_size={l1}", "-c", f"perf_model/l2_cache/cache_size={l2}", "--power",  "-d", run_dir, "--", BENCHMARK, "-p1"]
			print(f"\n>>> Rulam L1={l1} KB, L2={l2} KB")
			try:
				subprocess.run(cmd, check=True)
			except subprocess.CalledProcessError as e:
				print(f"Eroare la executia Sniper: {e}")
if __name__== "__main__":
	run_explorer()

