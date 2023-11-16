from tkinter import *


def callback(k,l):
    global player
    if player == 'X':
        b[k][l].configure(text='X')
        player = 'O'
    elif player == 'O':
        b[k][l].configure(text='O')
        player = 'X'



# celzius to farenhait
def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_label.configure(text=
        'Converted: {:.1f}'.format(temp))
    entry.delete(0, END)
message_label = Label(text='Enter a temperature',font=('Verdana', 16))
output_label = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=4)
calc_button = Button(text='Ok', font=('Verdana', 16),
            command=calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)


root = Tk()
b = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana',36), width=3, command= lambda k=i , l=j: callback(k,l))
        b[i][j].grid(row=i, column=j)
player = 'X'
mainloop()