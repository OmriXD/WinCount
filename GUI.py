import tkinter as tk

root = tk.Tk()
win_num = 0
lay = []


#Create new window
def create():
    top = tk.Toplevel()
    lay.append(top)

    top.title("Main Panel")
    top.geometry('500x500+100+450')

    btn = tk.Button(top,text='EXIT',command=exit_btn)
    btn.pack()

    global win_num
    win_num = win_num + 1
    display_win_num.config(text = str(win_num))

#Exit window + add 1 to win_num
def exit_btn():
    top = lay[-1]
    top.destroy()
    global win_num
    win_num = win_num - 1
    display_win_num.config(text = str(win_num))
    lay.pop(-1)

#New window button
button = tk.Button(root, text = "New Window", command = create)
button.pack()

#Display number of windows open
display_win_num = tk.Label(root, text = str(win_num))
display_win_num.pack()
display_win_num.config(text = str(win_num))


#Size and loading root
root.geometry("300x400")
root.mainloop()

