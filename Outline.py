import numpy as np
from PIL import Image, ImageFilter
import os





currDir = os.getcwd()
os.chdir("Data")
dataDir = os.getcwd()

raw = dataDir + "/raw"
processed = dataDir + "/processed"

for root, dirs, files in os.walk(raw):
    folder = root[root.rfind("/"):]
    os.mkdir("processed" + folder)
    for file in files:
        im = Image.open(raw + folder + "/" + file)
        #im = im.convert("L")
        filtered = im.convert("L").filter(ImageFilter.FIND_EDGES)
        addThis = np.array(filtered)
        org = np.array(im)
        saveThis = np.concatenate((org, addThis[..., None]), axis = 2)
        saveThis = saveThis.astype(np.uint8)
        im = Image.fromarray(saveThis)
        im.save(processed + folder + "/" + file[:-4] + "_processed.png")
        
        












