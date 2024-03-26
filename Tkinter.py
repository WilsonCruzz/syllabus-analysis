import tkinter as tk
from tkinter import filedialog
import pdf
from tkPDFViewer import tkPDFViewer as pdfViewer

# creat screen obj
root = tk.Tk()
# name title
root.title("Syllabus-Analysis")
# size
# resizable
root.minsize(600, 600)
root.resizable(True, True)


def show():
    filePath = filedialog.askopenfilename()
    pdf.processPdfFile(filePath)


btn = tk.Button(root,
                text="Open",
                command=show)

btn.pack()
# keep executing
root.mainloop()
