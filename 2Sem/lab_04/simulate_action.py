import sys
import time
import random

def simulate_action(action_name):
    processing_times = {"action1": 3, "action2": 2, "action3": 1}
    cpu_loads = {"action1": 25, "action2": 15, "action3": 1}

    processing_time = processing_times.get(action_name, 0)
    cpu_load = cpu_loads.get(action_name, 0)

    print(f"Simulating {action_name}...")
    time.sleep(processing_time)
    print(f"{action_name} completed. CPU load: {cpu_load}%\n")

if __name__ == "__main__":
    action_name = sys.argv[1]
    simulate_action(action_name)
