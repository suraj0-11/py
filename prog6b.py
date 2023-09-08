import shutil
dir_name = 'idklol'
arch = 'idk'
shutil.make_archive(arch,'zip',dir_name)
print(f"the file {dir_name} is archieved")
