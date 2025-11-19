
# Get process
ps -ef | grep process_name

# Kill process
pkill process_name -9 # force
killall process_name -9 # force
kill -9 PID # force
kill PID
kill -15 PID # graceful

# find out what process locking a file
lsof /path/to/file
# find out what process locking a port
lsof -i :port_number
# find out what process locking a directory
lsof +D /path/to/directory
# find out what process locking a mount point
lsof /mount/point
# find out what process locking a user and its children and grandchildren
lsof -u username -R -R

# unmount and remount where a directory has no inodes left
umount /path/to/mountpoint
mount /path/to/mountpoint
# or
fuser -km /path/to/mountpoint
umount /path/to/mountpoint
mount /path/to/mountpoint

# what is fuser -km /path/to/mountpoint?
# fuser -k sends the SIGKILL signal to all processes accessing the specified file or directory.
# The -m option tells fuser to treat the specified path as a mount point, meaning
# it will identify and target all processes using files or directories within that mount point.
# The -k option is used to kill those processes.
# This command is useful when you need to unmount a filesystem but there are active processes using it,
# preventing the unmount operation. By using fuser -km, you can forcefully terminate those processes,
# allowing you to proceed with the unmounting.  

# Find large files
find /path -type f -size +100M

# Find empty directories
find /path -type d -empty

# Find files by name
find /path -name "filename"

# Find files by extension
find /path -name "*.ext"

# Find files by modification time (e.g., modified in the last 7 days)
find /path -type f -mtime -7

