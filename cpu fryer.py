import os
import multiprocessing
import psutil
import time
import torch

# Function to MAX out CPU instantly
def burn_cpu():
    while True:
        x = 99999999 ** 99999999  # Extreme calculations for heat

# Function to overload GPU with massive calculations
def burn_gpu():
    print("🔥 Overloading GPU...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tensor_size = (75000, 75000)  # Even bigger matrix ops for instant heat

    while True:
        _ = torch.rand(tensor_size, device=device) @ torch.rand(tensor_size, device=device)

# Force-disable power-saving features
def disable_power_limits():
    print("⚡ Disabling power limits...")
    os.system("powercfg /setactive SCHEME_MIN")  # Windows: Forces High Performance mode
    os.system("powercfg /change monitor-timeout-ac 0")  
    os.system("powercfg /change standby-timeout-ac 0")  

# Overclock GPU (Linux/NVIDIA users only)
def overclock_gpu():
    print("💥 MAX GPU POWER MODE...")
    os.system("nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'")  # Forces GPU to highest performance

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"🔥 EXECUTING MAXIMUM OVERLOAD ON {num_cores} CPU CORES + GPU!")

    # Start CPU burners
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)

    # Start GPU burner
    gpu_process = multiprocessing.Process(target=burn_gpu)
    gpu_process.start()

    # Disable power saving and overclock
    if os.name == "nt":
        disable_power_limits()  
    else:
        overclock_gpu()  

    # Run FOREVER until the laptop completely dies
    while True:
        time.sleep(1)
