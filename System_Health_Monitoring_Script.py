import psutil
import datetime

# Define thresholds
CPU_THRESHOLD = 80  # Percent
MEMORY_THRESHOLD = 80  # Percent
DISK_THRESHOLD = 80  # Percent

# Get current time
now = datetime.datetime.now()

# Check CPU usage
cpu_percent = psutil.cpu_percent(interval=1)
if cpu_percent > CPU_THRESHOLD:
    print(f"{now}: WARNING: CPU usage is {cpu_percent}%, which exceeds the threshold of {CPU_THRESHOLD}%.")

# Check memory usage
memory = psutil.virtual_memory()
memory_percent = memory.percent
if memory_percent > MEMORY_THRESHOLD:
    print(f"{now}: WARNING: Memory usage is {memory_percent}%, which exceeds the threshold of {MEMORY_THRESHOLD}%.")

# Check disk usage
disk = psutil.disk_usage('/')
disk_percent = disk.percent
if disk_percent > DISK_THRESHOLD:
    print(f"{now}: WARNING: Disk usage is {disk_percent}%, which exceeds the threshold of {DISK_THRESHOLD}%.")

# Check running processes
processes = psutil.pids()
if len(processes) > 500:  # Adjust this threshold as needed
    print(f"{now}: WARNING: There are {len(processes)} running processes, which exceeds the threshold.")