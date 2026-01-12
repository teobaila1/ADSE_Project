# ADSE_Project
For this laboratory project, we chose Option B - performing ADSE with the Sniper simulator. 
The project was split into two parts, so each student has its own: Explorer and Analyzer. 

For the Explorer part, a Python script was created (explorer.py) to automate the simulation process. 
For the architectural parameters we chose L1 D-Cache (32 and 64 Kb) and L2 Cache (256 and 512 Kb) from the config/base.cfg.

To start the simulations, the following command was used: python3 explorer.py. This script will start Sniper and simulate the configurations. The results will be saved in the folder DSE_Results.

For each configuration, there is a subfolder that contains the sim.out (performance statistics) and powerstack.txt (the energy consumption report).
