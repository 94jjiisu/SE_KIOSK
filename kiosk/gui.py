from tkinter import *
#tk 객체 인스턴스 생성
root = Tk()

#창 제목
root.title('초기화면')

#창 크기
root.geometry("600x600+100+100")

#창 크기 조절 가능여부
root.resizable(True, True)

#x 누를때 까지 메인 화면에 표시, 유지
root.mainloop()