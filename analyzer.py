import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt


BASE_RESULTS_DIR = "DSE_Results"

def get_config_label(folder_name):
    """ Transforma 'run_L1_32_L2_256' -> 'L1=32KB, L2=256KB' """
    match = re.search(r"L1_(\d+)_L2_(\d+)", folder_name)
    if match:
        return f"L1={match.group(1)}KB, L2={match.group(2)}KB"
    return folder_name

def parse_run(run_folder_path):
    sim_out = os.path.join(run_folder_path, "sim.out")
    power_out = os.path.join(run_folder_path, "powerstack.txt")
    
    data = {
        "Config": get_config_label(os.path.basename(run_folder_path)),
        "IPC": 0.0,
        "Cycles": 0,
        "L1_Miss": 0.0,
        "L2_Miss": 0.0,
        "Energy": 0.0
    }

    #sim.out
    if os.path.exists(sim_out):
        with open(sim_out, "r") as f:
            content = f.read()
            m_ipc = re.search(r"IPC\s*=\s*([\d\.]+)", content)
            if m_ipc: data["IPC"] = float(m_ipc.group(1))
            
            m_l1 = re.search(r"L1-D.*?miss rate\s*=\s*([\d\.]+)", content, re.DOTALL)
            if m_l1: data["L1_Miss"] = float(m_l1.group(1))

            m_l2 = re.search(r"L2.*?miss rate\s*=\s*([\d\.]+)", content, re.DOTALL)
            if m_l2: data["L2_Miss"] = float(m_l2.group(1))

    #powerstack.txt
    if os.path.exists(power_out):
        with open(power_out, "r") as f:
            content = f.read()
            m_eng = re.search(r"total\s+([\d\.]+)", content)
            if m_eng: data["Energy"] = float(m_eng.group(1))

    return data

def analyze():
    if not os.path.exists(BASE_RESULTS_DIR):
        print(f"EROARE: Nu gasesc folderul {BASE_RESULTS_DIR}!")
        return

    results = []
    print(f"Analizez folderul: {BASE_RESULTS_DIR}")

    for item in sorted(os.listdir(BASE_RESULTS_DIR)):
        path = os.path.join(BASE_RESULTS_DIR, item)
        if os.path.isdir(path) and "run_" in item:
            print(f"Procesez: {item}")
            results.append(parse_run(path))

    if not results:
        print("Nu am gasit date!")
        return

    df = pd.DataFrame(results)
    df = df.sort_values(by="Config")
    
    print("\n--- REZULTATE ---")
    print(df[["Config", "IPC", "Energy", "L1_Miss"]])
    df.to_csv(os.path.join(BASE_RESULTS_DIR, "final_results.csv"), index=False)

    #IPC
    plt.figure(figsize=(10,6))
    plt.bar(df["Config"], df["IPC"], color="skyblue", edgecolor="black")
    plt.title("IPC Analysis")
    plt.ylabel("IPC")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_RESULTS_DIR, "graph_IPC.png"))
    
    #Energy
    plt.figure(figsize=(10,6))
    plt.plot(df["Config"], df["Energy"], marker="o", color="red")
    plt.title("Energy Analysis")
    plt.ylabel("Energy (J)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_RESULTS_DIR, "graph_Energy.png"))
    
    print("\nGrafice salvate in DSE_Results!")

if __name__ == "__main__":
    analyze()
