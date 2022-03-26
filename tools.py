from tkinter import Image
from PIL import Image
import os

def convertImageToPdf (path,outDir='', fileList=[]) :
    imageList = []
    files = []

    if path == '' :
        files= fileList
    else :
        files =os.listdir(path)

    mainPage = 'NULL'

    for file in files :
        currentPath = file if path == '' else path+'/'+file
        print(currentPath)
        currentImage = Image.open(f'{currentPath}')
        currentTransformer = currentImage.convert('RGB')
        if mainPage == 'NULL' :
            mainPage = currentTransformer
        else :
            imageList.append(currentTransformer)
    
    outDirectory = f'{outDir}' if outDir != '' else  'doc.pdf';
    mainPage.save(outDirectory, save_all=True, append_images= imageList)