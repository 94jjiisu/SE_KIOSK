import tkinter

root = tkinter.Tk()  # TKinter가 좌지우지할 processor를 만듦
root.config(width=800, height=600, bg="gray")

# label / entry pair
l1 = tkinter.Label(root, text="First Name:")
e1 = tkinter.Entry(root)

# put in first row
l1.grid(row=0, column=0)  # grid는 입력창의 크기를 알아서 조정해준다.
e1.grid(row=0, column=1)

# label / entry pair
l2 = tkinter.Label(root, text="Last Name:")
e2 = tkinter.Entry(root)

# put in second row
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

# label / entry /button tripple
l3 = tkinter.Label(root, text="Age:", bg="light gray")
e3 = tkinter.Entry(root, bg="dark slate gray")
b3 = tkinter.Button(root, text="submit", bg="slate gray")  # button 만들기.
# text와 background color 지정

# put in third row
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
b3.grid(row=3, column=1)

root.mainloop()  # 프로그램의 다른 동작이 진행될 때 까지 기다린다.
