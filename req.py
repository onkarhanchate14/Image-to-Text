import os

import sys, time, threading
try:
    from PIL import Image
except:
    os.system("pip3 install Pillow")
try:
    from pytesseract import pytesseract
except:
    os.system("pip3 install pytesseract")
try:
    import tkinter as tk
except:
    os.system("pip3 install tk")
from tkinter.filedialog import askopenfilename,askdirectory

try:
    import glob
except:
    os.system("pip3 install glob2")

try:
    from fpdf import FPDF
except:
    os.system("pip3 install fpdf")
try:
    import unicodedata    
except:
    os.system("pip3 install unicodedata2")

ImageFileDir = ""
def MainFun():
    
    def GetImageFileDir():
        global ImageFileDir
        def openfile():
            global filename
            filename = askdirectory(title="Open file")
            return [filename.replace("/",r"\\") , filename]

        # def printfile():
        #     # print(filename)
        #     return filename
        window = tk.Tk()
        filename = "" # global variable
        ImageFileDir = openfile()
        window.destroy()

    GetImageFileDir()
    # print(location)
    ImageList = []
    def AllImages():
        global ImageFileDir
        os.chdir(ImageFileDir[1])
        lst = []
        for file in glob.glob("*.png"):
            lst.append(str(file))
        return lst[:]
    ImageList = AllImages()
    # print(ImageList)
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # image_path = r"C:\Users\Hp\Pictures\Screenshots\\"+ImageList[1]
    pdf = FPDF()
    for i in range(10):
        image_path = ImageFileDir[0]+"\\"+ImageList[i]
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text1 = pytesseract.image_to_string(img)
        # print(str(text[:-1]))
        def strip_accents(text):
            return "".join(char for char in unicodedata.normalize('NFKD', text) if unicodedata.category(char) != 'Mn')

        text1 = text1[::-1].encode('utf-8')

        
        
        # Add a page
        pdf.add_page()
        
        # set style and size of font 
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
        
        # create a cell
        text1 = str(text1[::-1].decode('latin-1'))
        c = 0
        for i in range(0,len(text1),70):
            c+=1
            pdf.cell(10, 10, txt =text1[i:i+70] , ln = c )
        
        # add another cell
        pdf.image(image_path, w=180, h=100)
        # pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
        #          ln = 2, align = 'C')
        
        # save the pdf with name .pdf
    pdf.output("C:\\GEN_PDF\\generated_PDF.pdf")   
    pdf=FPDF(orientation='P', unit='mm', format='A3')

def animated_loading():
    frames = ['''
  ____  
 / ___|  
| |     
| |___ 
 \____|

              ''','''
  ____    _  
 / ___|  / \  
| |     / _ \ 
| |___ / ___ \ 
 \____/_/   \_\\

              ''','''
  ____    _    ____  
 / ___|  / \  / ___|
| |     / _ \ \___ \\
| |___ / ___ \ ___) |
 \____/_/   \_\____/

              ''','''
  ____    _    ____  ____  
 / ___|  / \  / ___|| __ )
| |     / _ \ \___ \|  _ \\
| |___ / ___ \ ___) | |_) |
 \____/_/   \_\____/|____/

              ''','''
  ____    _    ____  ____  _____ 
 / ___|  / \  / ___|| __ )| ____|
| |     / _ \ \___ \|  _ \|  _| 
| |___ / ___ \ ___) | |_) | |___
 \____/_/   \_\____/|____/|_____|

              ''','''
  ____    _    ____  ____  _____ ____  
 / ___|  / \  / ___|| __ )| ____|  _ \\
| |     / _ \ \___ \|  _ \|  _| | |_) |
| |___ / ___ \ ___) | |_) | |___|  _ <
 \____/_/   \_\____/|____/|_____|_| \_\\

              ''','''
  ____    _    ____  ____  _____ ____   ____ 
 / ___|  / \  / ___|| __ )| ____|  _ \ / ___|
| |     / _ \ \___ \|  _ \|  _| | |_) | |  _ 
| |___ / ___ \ ___) | |_) | |___|  _ <| |_| |
 \____/_/   \_\____/|____/|_____|_| \_\\____|

              ''']
    frames = frames+frames[::-1]
    for char in frames:
        sys.stdout.write('\r'+char)
        time.sleep(.2)
        os.system('cls' if os.name == 'nt' else 'clear')
        # sys.stdout.flush() 
        # time.sleep(.1)


def animated():
    the_process = threading.Thread( target=MainFun)
    the_process.start()

    # the_process2 = threading.Thread( target=animated_loading)
    # the_process2.start()
    # MainFun()
    while the_process.is_alive():
        animated_loading()
    print("")
flag = True
def createDir():
    directory = "GEN_PDF"
    
    # Parent Directory path
    parent_dir = "C:/"
    
    # Path
    path = os.path.join(parent_dir, directory)
    
    # Create the directory
    # 'Nikhil'
    try:
        os.makedirs(path, exist_ok = True)
        
    except OSError as error:
        flag = False
        
        # print("Directory '%s' can not be created" % directory)    
createDir()
animated()
if(flag==True):
    print("Output file will be generated at : C:/GEN_PDF with name generated_PDF.pdf")
else:
    print("Old generated_PDF.pdf file will be replaced with new PDF\n")
    print("Output file generated at : C:/GEN_PDF with name generated_PDF.pdf\n\n")
print('''Tool made by:                _                    
  ___ __ _ ___| |__   ___ _ __ __ _ 
 / __/ _` / __| '_ \ / _ \ '__/ _` |
| (_| (_| \__ \ |_) |  __/ | | (_| |
 \___\__,_|___/_.__/ \___|_|  \__, |
                              |___/ 
''')
    
    
    