# Window Processes Killer 

I used the psutil library to kill processes on my Windows system as I am tired of killing them manually one by one. It categorizes processes into two groups: used processes (vital Windows processes + Processes in Taskbar) and other background processes. 

Usage

1. Ensure that Python and the required libraries (psutil, pygetwindow) are installed on your system.
2. If there are background processes you don't wanna kill, add them to the `active_processes` in the `get_used_processes()` function
3. Run the script using a Python interpreter (python hitman.py).
4. You don't have enough permission to kill some processes as Windows needs them to work properly, and thus you'll get this kind of output:
```
Process Widgets.exe was killed
Process WhatsApp.exe was killed
Permission denied to kill process PresentationFontCache.exe (PID: 9024)
Permission denied to kill process vmmemWSL (PID: 15800)
Process mcafee-security.exe was killed
```

### Important Note
Carefully review and understand the list of used processes before running the script, as terminating critical system processes can cause system instability.

