from tkinter import *

def Library_Login():
    Window=Tk()
    Window.title("Library")
 
Label(text="Welcome to Library \n Choose to Login as a Student,teacher or librarian", bg="yellow", width="300", height="2", font=("Calibri",13)).pack()
Label(text="\n\n").pack()

Button(text="STUDENT",height="6", width="80").pack()
Label(text="\n\n").pack()

Button(text="TEACHER",height="6", width="80").pack()
Label(text="\n\n").pack()

Button(text="LIBRARIAN",height="6", width="80").pack()
Library_Login()

Window.mainloop()


