from tkinter import *
import time


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def input_dev():
    frame_input = Frame(base_frame)
    frame_input.pack(side=TOP)
    lable_input = Label(frame_input, text="input Frame")
    lable_input.pack()


def remove_dev():
    base_frame.destroy()


root = Tk()
root.title('*에그드랍 메뉴판*')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Add Device", command=input_dev)
filemenu.add_command(label="Remove Device", command=remove_dev)
filemenu.add_command(label="View all device", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Device", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Check Ping", command=donothing)
editmenu.add_command(label="Check Cpu/Mem", command=donothing)

menubar.add_cascade(label="Monitor", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

menubar.add_cascade(label="Help", menu=helpmenu)

base_frame = Frame(root, width=500, height=500)
base_frame.pack(fill='both', expand='yes')
base_lable_ip = Label(base_frame, text='IP').grid(row=0, column=0)
base_lable_os = Label(base_frame, text='OS').grid(row=0, column=1)
base_lable_memory = Label(base_frame, text='Memory').grid(row=0, column=2)
ip = Entry(base_frame, text='11.4.14.71')
os = Entry(base_frame)
memory = Entry(base_frame)
ip.grid(row=1, column=0)
os.grid(row=1, column=1)
memory.grid(row=1, column=2)
root.config(menu=menubar)
root.mainloop()
