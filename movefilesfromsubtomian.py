import shutil
import os
source = "Desktop/content/waste/"
destination = "Desktop/content/"
files = os.listdir(source)
for file in files:
	file_name = os.path.join(source, file)
	shutil.move(file_name, destination)
print("Files Moved")
