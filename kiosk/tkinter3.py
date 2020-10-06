from tkinter import *

root = Tk()
# option을 다른 파일을 read하는 것으로 지정할 수 있다.
root.option_readfile('optionDB')
root.title('세번째 예제 - radio_button')

fruit = [('bugger', 1), ('chicken', 2), ('cola', 3)]
var = IntVar()
for menu, value in fruit:
    Radiobutton(root, text=menu, value=value, variable=var).pack(anchor=W)
var.set(3)  # value가 3인 controller를 set해준다.
root.mainloop()
