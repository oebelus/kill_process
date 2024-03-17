import psutil
import json
import pygetwindow as gw

processes = psutil.process_iter()

processes_dictionary = {}

processes_to_add = []

for process in processes:
    name = process.name()
    rss_mb = process.memory_info().rss / (1024 ** 2)
    if name not in processes_to_add:
        processes_dictionary[name] = rss_mb
        processes_to_add.append(name)
    else:
        processes_dictionary[name] += rss_mb

#print(json.dumps(processes_dictionary, indent=2))
active_processes = []

def get_used_processes() -> list:
    active_processes = [
        "System Idle Process",
        "System",
        "smss.exe",
        "csrss.exe",
        "wininit.exe",
        "services.exe",
        "lsass.exe",
        "winlogon.exe",
        "spoolsv.exe",
        "explorer.exe",
        "svchost.exe",
        "dwm.exe",
        "ctfmon.exe",
        "taskhostw.exe"
    ]
    for i in processes_dictionary.keys():
        process_without_exe = i[:len(i)-4].lower()
        if gw.getWindowsWithTitle(process_without_exe):
            active_processes.append(i)
            for process in psutil.process_iter(['name']):
                if process.name() == i:
                    children = process.children()
                    for child in children:
                        active_processes.append(child.name())
    return set(active_processes)

def get_background_processes(active_processes: list) -> list:
    all = [process.name() for process in psutil.process_iter()]
    return list(set(all) - set(active_processes))

def kill_background_processes(background_processes):
    for process in psutil.process_iter(['name']):
        if process.name() in background_processes:
            try:
                process.kill()
                print(f'Process {process.name()} was killed')
            except:
                print(f"Permission denied to kill process {process.name()} (PID: {process.pid})")

active_processes = get_used_processes()
background_processes = get_background_processes(active_processes)
kill_background_processes(background_processes)

