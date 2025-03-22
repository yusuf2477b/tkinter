#1. import tkinter moduke



from tkinter import *
window = Tk()
window.title('tkinter sample window')
window.geometry('300x300')
#label
greeting = Label(text="hello user", fg='black', bg='white')
#button
button = Button (text="click me", bg='black', fg='white')
#entry
entry = Entry(fg="yellow", bg="blue",width = 50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='sample frame')
label.pack()

textbox = Text(fg='green',bg='yellow')
textbox.pack()
window.mainloop()