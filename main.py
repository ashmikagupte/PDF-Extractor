import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root=tk.Tk()
root.title("PDF Extracter")


canvas=tk.Canvas(root, width=600, height=350)
canvas.grid(columnspan=3, rowspan=6)

#logo = Image.open("logo.png")
#logo = ImageTk.PhotoImage(logo)
#label = tk.Label(root, image=logo)
#label.image=logo
#label.grid(column=1, row=0)*

label1 = tk.Label(root, text="PDF Extract", font=("Arial", 40), fg="indianred").place(x=155, y=20)
#label2 = tk.Label(root, text="Extract", font=("Chloe", 40), fg="turquoise").place(x=270, y=55)
#Font_tuple = ("Chloe", 20, "bold")
#label2.configure(font=Font_tuple)

instructions = tk.Label(root, text="Select PDF to extract its text", font="Raleway").place(x=170, y=130)
#instructions.grid(columnspan=3, column=0, row=2)

def clicked():
    txt.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        readpdf = PyPDF2.PdfFileReader(file)
        page = readpdf.getPage(0)
        content = page.extractText()

        textbox = tk.Text(root, height=10, width=50, padx=15, pady=15)
        textbox.insert(1.0, content)
        textbox.grid(column=1, row=6)

        txt.set("BROWSE")


txt = tk.StringVar()
bt = tk.Button(root, textvariable=txt, command=lambda:clicked(), font="Arial", bg="lightpink1", fg="white", height=2, width=15)
txt.set("BROWSE")
bt.grid(column=1, row=4)

canvas=tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

root.mainloop()
