import os

def rename_files(directory, prefix, endfix):
    i = 0
    for filename in os.listdir(directory):
        if filename != 'rename.py' and os.path.isfile(os.path.join(directory, filename)):
            new_name = prefix + str(i) + endfix
            if not filename.startswith(prefix) or not filename.endswith(endfix):
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                i += 1


directory_path = r'C:\path'  # Replace with your directory path
new_prefix = 'img_'  
end_fix = '.png'
rename_files(directory_path, new_prefix, end_fix)
