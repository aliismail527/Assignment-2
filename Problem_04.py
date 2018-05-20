import psutil
import sys
from datetime import datetime

# 'sys.argv' is list which recieve Command Line Args Passed ...
if len(sys.argv) > 1:
    process_id = int(sys.argv[1])
    p = psutil.Process(process_id)
else:
	print("You didn't Pass any Argument as PID")
	sys.exit(0)
		

# Getting information all about Process
with p.oneshot():
    process_name = p.name()  # execute internal routine once collecting multiple info
    process_status = p.status()  # return cached value
    process_parent_id = p.ppid()
    process_creation_time = p.create_time()
    process_files_opened = p.open_files()
    process_memory_info = p.memory_info().rss

# Getting the name of Parent Process from Parent ID
parent = psutil.Process(p.ppid())
with parent.oneshot():
    process_parent_name = parent.name()

# Getting Process Creation time of Seconds into fully Required Format
process_creation_time = datetime.fromtimestamp(process_creation_time).strftime("%A, %B %d, %Y %I:%M:%S")

print('Process ID : %d' %(process_id))
print('Process Name : %s' %(process_name))
print('Process Status : %s' %(process_status))
print('Process Parent ID : %s' %(process_parent_id))
print('Process Parent Name : %s' %(process_parent_name))
print('Process Creation Time : %s' %(process_creation_time))
print('Files Opened By the Process Info : %s' %(process_files_opened))
print('Memory Info : %s' %(process_memory_info/784))
