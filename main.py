import os
from zipfile import ZipFile

# Getting working directory paths
dir_path = os.getcwd()
input_folder_path = "{}/Input".format(dir_path)
output_folder_path = "{}/Output".format(dir_path)

# Getting list of all files in the Input folder
input_folder_list = os.listdir(input_folder_path)

print("Bulk extraction beginning...")
print()

# Opening each zip file in the Input folder and extracting it to the output folder
for file in input_folder_list:
	print("Extracting {}".format(file))

	file_path = input_folder_path + "/" + file
	with ZipFile(file_path, 'r') as zip:
		zip.extractall(output_folder_path)

print()
print("Bulk extraction complete")