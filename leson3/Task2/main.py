import platform
import os
import psutil

def get_system_info():
    system_info = {}

    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Platform'] = platform.platform()
    system_info['Processor'] = platform.processor()

    try:
        system_info['RAM'] = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    except Exception as e:
        system_info['Error'] = f"An error occurred while fetching system information: {e}"

    return system_info

info = get_system_info()

print("\nSystem Information:")
for key, value in info.items():
    print(f"{key}: {value}")
