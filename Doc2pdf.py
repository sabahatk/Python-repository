from docx2pdf import convert
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

#convert(r"C:\Users\sabah\Documents\Sabahat\Job\Resumes and Cover Letters to Upload\Sabahat Khan Resume 2.docx", r"C:\Users\sabah\Documents\Sabahat\Job\Resumes and Cover Letters to Upload\Sabahat Khan Resume.pdf")
def convert_docx_to_pdf(docx_filepath, pdf_filepath):
    #lbl.configure(text = "I just got clicked")
    convert(docx_filepath, pdf_filepath)

def clicked():
    lbl.configure(text = "I just got clicked")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Docx Files",
                                                        "*.docx*"),
                                                       ("All files",
                                                        "*.*")))
    lbl2 = Label(root, text= "File selected: " + filename)
    lbl2 = lbl2.grid(row = 0, column=2)

def save_file():
   f = asksaveasfile(initialfile = 'Untitled.pdf',
defaultextension=".txt",filetypes=[("All Files","*.*"),("PDF Documents","*.pdf")])

root = Tk()

root.title("Convert Docx to PDF")

root.geometry('350x200')

lbl = Label(root, text = "Select docx file")
lbl.grid(column = 0, row = 0)

# adding Entry Field
#txt = Entry(root, width=10)
#txt.grid(column =1, row =0)

btn = Button(root, text = "Open" ,
             fg = "black", command=browseFiles)

btn.grid(column=1, row=0)

lbl = Label(root, text = "Select where to save the PDF file")
lbl.grid(column = 0, row = 1)

btn = Button(root, text = "Save" ,
             fg = "black", command=save_file)

btn.grid(column=1, row=1)

root.mainloop()
