import shutil
import os

# Paths to the directories you want to copy from (relative to the current directory, one level above)
source_class_sz = '../class_sz/class-sz'

# Destination path (relative to the current directory, which is class_sz_data)
destination_class_sz = './class-sz'

# Directories to include within class-sz
subdirs_to_copy = ['bbn', 'class_sz_auxiliary_files/includes']

# Copy the required subdirectories while preserving the structure
for subdir in subdirs_to_copy:
    src = os.path.join(source_class_sz, subdir)
    dest = os.path.join(destination_class_sz, subdir)
    shutil.copytree(src, dest, dirs_exist_ok=True)

print("Selected directories from class-sz/ have been copied to class_sz_data repository.")
