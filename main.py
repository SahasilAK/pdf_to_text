import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


window = tk.Tk()
window.title('PDF to TEXT')


def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=window, mode='rb', title='Choose a file', filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        text_box = tk.Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")





canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3,rowspan=3)

logo = Image.open('logo/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

dis_info = tk.Label(window, text='Select a PDF file to convert to text', font='Raleway')
dis_info.grid(columnspan=3, column=0, row=1)

browse_text = tk.StringVar()
browse_btn = tk.Button(window, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg='#20bebe', fg='white', height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(window, width=600,height=250)
canvas.grid(columnspan=3)
window.mainloop()
