import glob
import os
import shutil

search_dir = "/Users/bytedance/Desktop/Aidance_QA/x-body-normal/viggle_result_raw2/"
files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
files.sort(key=lambda x: os.path.getmtime(x))
files = files[::-1]
for i in range(len(files)):
    shutil.move(files[i],search_dir+'/%d.mp4'%(i+35))
