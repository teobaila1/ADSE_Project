# ADSE_Project
For this laboratory project, we chose Option B - performing ADSE with the Sniper simulator. 
The project was split into two parts, so each student has its own: Explorer and Analyzer.

!In order to run the scripts, first you need tp change the 'home user' name in the explorer.py!

For the Explorer part, a Python script was created (explorer.py) to automate the simulation process. 
For the Analyzing part, a Python script was created (analyzer.py) to analyze the configurations created by the explorer. 
For the architectural parameters we chose L1 D-Cache (32 and 64 Kb) and L2 Cache (256 and 512 Kb) from the config/base.cfg.

To start the simulations, the following command was used: python3 explorer.py. This script will start Sniper and simulate the configurations. The results will be saved in the folder DSE_Results.
To start the analyzing, the following command was used: python3 analyzer.py. This script will start analyzing the configurations made by the explorer. The graphics and csv file will be in the DSE_Results folder.

