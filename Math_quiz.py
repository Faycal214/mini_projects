from tkinter import *
import random

window = Tk()
window.title("Quiz game")
window.geometry("500x500")
window.minsize(600,500)
window.config(bg="#F0F0F0")


question = StringVar()
answer = StringVar()
GivenAsnwer = StringVar()
score = StringVar()
questionNumber = IntVar()

score.set(0)
GivenAsnwer.set(0)

def generate_questions():
    global question , answer, GivenAsnwer
    
    operations = ['+','-','*','/']
    
    number_1 = random.randint(1,10)
    number_2 = random.randint(1,10)
    
    GivenAsnwer.set("")
    answer_entry = Entry(window,textvariable=GivenAsnwer,bg='white',font=('courrier',25))
    answer_entry.grid(row=3,column=0)
    
    operation = random.choice(operations)
    
    question.set(str(number_1)  + "" + operation + "" + str(number_2))
    answer.set(eval(question.get()))
    
    
    label_question = Label(window,text=f"Question: {question.get()}",font=('courrier',40),bg='white')
    label_question.grid(row=2,column=0)

generate_questions()


def check_answer():
    global score
    global label_affiche
    
    questionNumber.set(questionNumber.get() + 1)
    
    if label_affiche :
        label_affiche.destroy()
    
    if answer.get() == GivenAsnwer.get():
        score.set(int(score.get()) + 1)
         
        label_affiche = Label(window,text='correct',fg='green',font=('courrier',25))
        label_affiche.grid(row=4,column=0)
        
        score_label = Label(window,text=f"score : {score.get()}",font=('courrier',25),fg='black')
        score_label.grid(row=5,column=0)
        
    elif answer.get() != GivenAsnwer.get() :
        label_affiche = Label(window,text='incorrect',fg='red',font=('courrier',25))
        label_affiche.grid(row=4,column=0)
    
    generate_questions()


def restart():
    global score, label_affiche, GivenAsnwer, questionNumber
    
    
    questionNumber.set(0)
    questionScale = Scale(window, from_=0,to=10,orient= HORIZONTAL, length=400, variable=questionNumber)
    questionScale.grid(row=1,column=0)
    
    
    GivenAsnwer.set("")
    answer_entry = Entry(window,textvariable=GivenAsnwer,bg='white',font=('courrier',25))
    answer_entry.grid(row=3,column=0)
    
    score.set(0)
    score_label = Label(window,text=f"score : {score.get()}",font=('courrier',25),fg='black')
    score_label.grid(row=5,column=0)
    
    if label_affiche :
        label_affiche.destroy()
    
    label_affiche = Label(window,text='Result',fg='blue',font=('courrier',25))
    label_affiche.grid(row=4,column=0)
    
    generate_questions()


label = Label(window,text="welcome to the Quiz game",fg="black",font=('courrier',25))
label.grid(row=0,column=0)

questionScale = Scale(window, from_=0,to=10,orient= HORIZONTAL, length=400, variable=questionNumber)
questionScale.grid(row=1,column=0)

Complet_question_label = Label(window,text='10 question',font=('courrier',25))
Complet_question_label.grid(row=1,column=1)

label_question = Label(window,text=f"Question: {question.get()}",font=('courrier',40),bg='white')
label_question.grid(row=2,column=0)


answer_entry = Entry(window,textvariable=GivenAsnwer,bg='white',font=('courrier',25))
answer_entry.grid(row=3,column=0)

submit_button = Button(window,text='submit',font=('courrier',25),bg='green',command= check_answer)
submit_button.grid(row=3,column=1)

label_affiche = Label(window,text='Result',fg='blue',font=('courrier',25))
label_affiche.grid(row=4,column=0)

restart_button = Button(window,text="Restart",font=("courrier",25),bg="red",command=restart)
restart_button.grid(row=4,column=1)

score_label = Label(window,text=f"score : {score.get()}",font=('courrier',25),fg='black')
score_label.grid(row=5,column=0)



window.mainloop()