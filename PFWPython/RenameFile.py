import os

def print_name_machine():
   for files in get_file_name():
      print files

def rename_file():
   path = '/home/r2d2/Downloads/prankpic'
   file_list = os.listdir(path)
   print file_list

   saved_path = os.getcwd()
   #Here is where the script is saved
   print ('Current Working Directory: ') + saved_path
   
   #Bellow will change the work directory
   os.chdir('/home/r2d2/Downloads/prankpic')
   
   for files in file_list:
      os.rename(files, files.translate(None, "0123456789"))
    
    #Bellow will back to work directory
    #os.chdir(saved_path)

rename_file()
