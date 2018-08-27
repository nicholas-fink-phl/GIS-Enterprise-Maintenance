import glob
import os

# compares folders where both should have the same files present

done_list = []

done = glob.iglob(r'file path\*.tif')
for x in done:
    done_file = os.path.basename(x)
    done_list.append(done_file)
orig = glob.iglob(r'file path\*.tif')
for y in orig:
    orig_file = os.path.basename(y)
    if orig_file not in done_list:
        print(orig_file)
