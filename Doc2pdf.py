from docx2pdf import convert
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import tkinter as tk

global save_filepath
global open_filepath
#convert(r"C:\Users\sabah\Documents\Sabahat\Job\Resumes and Cover Letters to Upload\Sabahat Khan Resume 2.docx", r"C:\Users\sabah\Documents\Sabahat\Job\Resumes and Cover Letters to Upload\Sabahat Khan Resume.pdf")
def convert_docx_to_pdf():
    #lbl.configure(text = "I just got clicked")
    #retrieve_text = self.
    #print 
    #convert(docx_filepath, pdf_filepath)
    global save_filepath
    global open_filepath
    validation = validate_fields()
    
    if validation:
        save_filepath = save_filepath + filename_input.get()
        convert(open_filepath, save_filepath)

def validate_fields():
    global open_filepath
    global save_filepath
    lbl2 = Label(root, text = "")
    if not filename_input.get() or filename_input.get().endswith(".pdf") == False:
        
        lbl2.grid(column = 0, row = 5)
        lbl2.configure(text = "Please fill in all fields and provide the proper format.")
        return False
    else:
        lbl2 = Label(root, text = "")
        lbl2.grid(column = 0, row = 5)
        lbl2.configure(text = "File successfully converted.")
        return True

def clicked():
    lbl.configure(text = "I just got clicked")


file_locations = []



def browseFiles(path_store: list):
    filepath = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Docx Files",
                                                        "*.docx*"),
                                                       ("All files",
                                                        "*.*")))
    lbl2 = Label(root, text= "File selected: " + filepath)
    lbl2 = lbl2.grid(row = 0, column=2)
    path_store.append(filepath)

    global open_filepath
    #return filepath
    #return_input(filepath)
    open_filepath = filepath
    print(open_filepath)


    #path_store[1] = filepath



#def save_file():
#   f = asksaveasfile(initialfile = 'Untitled.pdf',
#defaultextension=".txt",filetypes=[("All Files","*.*"),("PDF Documents","*.pdf")])

    #file = filedialog.asksaveasfile(defaultextension='.pdf')
    #file.close()

def get_save_location(path_store: list):
    filepath = askdirectory()
    print(filepath)

    lbl3 = Label(root, text= "Folder selected: " + filepath)
    lbl3 = lbl3.grid(row = 1, column=2)
    #path_store[0] = filepath
    global save_filepath
    save_filepath = filepath
    #path_store.append(filepath)
    #print(path_store)

root = tk.Tk()

root.title("Convert Docx to PDF")

root.geometry('350x200')

lbl = Label(root, text = "Select docx file")
lbl.grid(column = 0, row = 0)

# adding Entry Field
filename_input=tk.StringVar()

txt = Entry(root, textvariable=filename_input, width=30)
txt.grid(column = 0, row =2)


btn = Button(root, text = "Open" ,
             fg = "black", command=lambda: browseFiles(file_locations))

#Place in first row, second column
btn.grid(column=1, row=0)

lbl = Label(root, text = "Select where to save the PDF file")
lbl.grid(column = 0, row = 1)

btn = Button(root, text = "Select Folder" ,
             fg = "black", command=lambda: get_save_location(file_locations))



btn.grid(column=1, row=1)



btn = Button(root, text = "Convert" ,
             fg = "black", command=lambda: convert_docx_to_pdf())

btn.grid(column=0, row=3)

root.mainloop()
