# from tools import *
from tkinter import *


# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Cut N Paste GUI")
#         master.geometry('350x200')
#
#         self.label = Label(master, text="Cut N Paste GUI")
#         self.txt = Entry(window, width=10)
#         self.label.pack()
#
#         self.button = Button(master, text="Greet", command=self.greet)
#         self.button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#
#     def greet(self):
#         print("Greetings!")
#
#     # def num_styles(self):
#         # PARAMETERS['NUM_STYLES'] =



# window = Tk()
# my_gui = MyFirstGUI(window)
# window.mainloop()


from tkinter import *

window = Tk()

window.title("Cut N Paste GUI")

window.geometry('500x500')

lbl = Label(window, text="Number of styles")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


def style_clicked():
    lbl.configure(text="Done")
    style_num = int(txt.get())
    if type(style_num) is int and style_num > 0:
        if style_num > len(os.listdir("./Style_Transfer/styles")):
            print("Not enough styles available")
        else:
            PARAMETERS['STYLE_STEPS'] = style_num


btn = Button(window, text="set", command=style_clicked)

btn.grid(column=2, row=0)

window.mainloop()