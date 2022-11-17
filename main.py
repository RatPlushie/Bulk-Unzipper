import os
from zipfile import ZipFile, BadZipFile

if __name__ == '__main__':
	# Getting working directory paths
	dir_path = os.getcwd()
	input_folder_path = "{}/Input".format(dir_path)
	output_folder_path = "{}/Output".format(dir_path)

	# Getting list of all files in the Input folder
	input_folder_list = os.listdir(input_folder_path)

	print("Bulk extraction beginning...\n")

	# Opening each zip file in the Input folder and extracting it to the output folder
	for file in input_folder_list:
		try:
			file_path = input_folder_path + "/" + file
			with ZipFile(file_path, 'r') as zip:
				print("Extracting {}".format(file))
				zip.extractall(output_folder_path)

		except BadZipFile:
			print ("{} is not in .zip format".format(file))

	print("\nBulk extraction complete. See Output folder for results")