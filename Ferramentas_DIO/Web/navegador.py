import webbrowser
import tkinter

root = tkinter.Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = tkinter.Button(root, text='Abrir Google', command=google).pack(pady=20)
root.mainloop()