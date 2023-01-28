from email.mime import image
from textwrap import fill
import tkinter
from tkinter import *
import pandas as pd
import random
current_card = {}

try:
    data = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    dataframe= pd.read_csv('data/french_words.csv')
    data = dataframe.to_dict(orient='records')
else:
    data = data.to_dict(orient='records')










def next_card():
    global current_card,flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(data)
    canvas.itemconfig(title_text,text= 'French',fill='black')
    canvas.itemconfig(word,text= current_card['French'],fill='black')
    canvas.itemconfig(card_background,image=card_front_image)
    flip_time =window.after(3000,func=flip_card)

   




def flip_card():
    canvas.itemconfig(title_text,text= 'English',fill='white')
    
    canvas.itemconfig(word,text= current_card['English'],fill='white')
    canvas.itemconfig(card_background,image=card_back_image)



def is_known():
    data.remove(current_card)
    remain = pd.DataFrame(data)
    remain.to_csv('words_to_learn.csv',index=False)
    print(len(data))
    next_card()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(padx=100,pady=50,bg=BACKGROUND_COLOR)



flip_time = window.after(3000,func=flip_card)




canvas = Canvas(width=800,height=526,highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')

card_background=canvas.create_image(400,263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR)
title_text = canvas.create_text(400,150,text='',font=('Ariel',35,'italic'))
word=canvas.create_text(400,263,text='',font=('Ariel',40,'bold'))
canvas.grid(row=0,column=0,columnspan=2)



cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image= cross_image,highlightthickness=0,command = next_card)
unknown_button.grid(row=1,column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image= right_image,highlightthickness=0,command= is_known)
right_button.grid(row=1,column=1)



next_card()



















# canvas = Canvas(width=100,height=100)
# right_image = PhotoImage(file='images/right.png')
# canvas.create_image(50,50,image=right_image)
# # canvas.create_text(100,130,text='title',fill='white',font=('Ariel',40,'italic'))
# canvas.grid(row=1,column=0)

# canvas = Canvas(width=100,height=100)
# wrong_image = PhotoImage(file='images/wrong.png')
# canvas.create_image(50,50,image=wrong_image)
# # timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
# canvas.grid(row=1,column=1)


# # canvas = Canvas(width=100,height=100)
# # tomato_image = PhotoImage(file='images/right.png')
# # canvas.create_image(50,50,image=tomato_image)
# # # timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
# # canvas.grid(row=0,column=0)

window.mainloop()
