# Import libraries
import os
import PyPDF2
import asyncio
import time
import psutil

async def pdfPrint(file_path):
	# # Insert the directory path in here
	# # path = 'C:\\Users\\DELL\\Documents\\print'
	# path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents\\print') 
	# # print(desktop)

	# # Extracting all the contents in the directory corresponding to path
	# l_files = os.listdir(path)
	
	# # Iterating over all the files
	# for file in l_files:

	# # Instantiating the path of the file
	# 	file_path = f'{path}\\{file}'

	# 	# Checking whether the given file is a directory or not
	# 	if os.path.isfile(file_path):
	try:
		# Printing the file pertaining to file_path
		os.startfile(file_path, 'print')
		#print(f'Printing {file}')
		# creating a pdf file object
		file_extention = file_path[-3:]
		if file_extention == 'pdf':
			print( "file is PDF try to print")
			
			# creating a pdf file object
			with open(file_path, 'rb') as pdfFileObj:
				print("step#1")
				
				# creating a pdf reader object
				pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
				print("step#2")
				
				# printing number of pages in pdf file
				# print(pdfReader.numPages)
				# print("step#3")
				
				# creating a page object
				pageObj = pdfReader.getPage(0)
				print("step#4")
				
				# extracting text from page
				print(pageObj.extractText())
				print("step#5")
			# print(pageObj.extractText())
			
			# # closing the pdf file object
			# task_2 = asyncio.create_task(pdfFileObj.close())
			# var = await task_2
			#pdfFileObj.close()
			return "done"

	except Exception as e:
		# Catching if any error occurs and alerting the user
		#os.remove(file_path)
		print(f'ALERT: could not be printed! Please check\
		the associated softwares, or the file type.')
		# ... PRINT THE ERROR MESSAGE ... #
		print(e)

# else:
# print(f'ALERT: {file} is not a file, so can not be printed!')
print("printing is done")

async def pdfDelete(file_path): 
	await asyncio.sleep(5)
	print('try to delete')
	if os.path.exists(file_path):
		try:
			os.remove(file_path)
			return("done")
		except Exception as e:
			print(e)
			print("not able to delete") 
	else:
		print("The file does not exist") 
  


async def pdfKill():
	print('try to kill PDF')
	await asyncio.sleep(5)
	try:
		for p in psutil.process_iter():
			# print(p.name)
			if p.name() == "AcroRd32.exe":
				print("AcroRd32.exe")
				p.terminate()
				p.kill()
				return "killed"
	except Exception as e:
		print(e)
		print("not able to kill") 


async def main():
    
	await asyncio.sleep(1)
	print("waiting for another file")
	# await asyncio.wait([pdfPrint()])
		# Insert the directory path in here
	# path = 'C:\\Users\\DELL\\Documents\\print'
	path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents\\print') 
	# print(desktop)

	# Extracting all the contents in the directory corresponding to path
	l_files = os.listdir(path)

	# Iterating over all the files
	for file in l_files:

	# Instantiating the path of the file
		file_path = f'{path}\\{file}'

		# Checking whether the given file is a directory or not
		if os.path.isfile(file_path):
			start_time = time.time()
			print("file is found")
			task_1 = asyncio.create_task(pdfPrint(file_path))
			var_1 = await task_1
			print("print was done!")
			print("--- %s seconds ---" % (time.time() - start_time))
			task_2 = asyncio.create_task(pdfKill())
			var_2 = await task_2
			print("PDF Killed!")
			task_3 = asyncio.create_task(pdfDelete(file_path))
			var_3 = await task_3
			print("delete was done!")
			print("--- %s seconds ---" % (time.time() - start_time))
		else:
			print(f'ALERT: {file} is not a file, so can not be printed!')
		
		


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	while True:
		loop.run_until_complete(main())
		loop.close
  
		


