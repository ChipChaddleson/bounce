import random
import tkinter as tk

root = tk.Tk()
root.title("grade thing or smt")




gradeVar = tk.StringVar()
gradeVar.set("1")
tk.Label(
    text= "enter your grade"
).grid(
    row=0, column=0, 
    sticky="e"

)
tk.Entry(
    textvariable=gradeVar,
).grid(
    row=0, column=1,
)


nameVar = tk.StringVar()
tk.Label(
    text= "enter your Name"
).grid(
    row=1, column=0,
    sticky="e"

)
tk.Entry(
    textvariable=nameVar,
).grid(
    row=1, column=1,
    sticky="e"
)

questionVar = tk.StringVar()
questionVar.set("2")
tk.Label(
    text= "how many questions"
).grid(
    row=2, column=0,
    sticky="e"

)
tk.Entry(
    textvariable=questionVar,
).grid(
    row=2, column=1,
)


arg1 = tk.StringVar()
arg1.set(str(random.randint(1*(int(gradeVar.get())), 10*(int(gradeVar.get())))))

tk.Label(
    textvariable=arg1,
).grid(
    row=3, column=0,
    sticky="e"

)




tk.Label(
    text = "+"
).grid(
    row=3, column=0,

)




arg2 = tk.StringVar()
# arg2.set(str(random.randint(1*(int(gradeVar.get())), 10*(int(gradeVar.get())))))
arg2.set("10")

tk.Label(
    textvariable=arg2,
).grid(
    row=3, column=0,
    sticky="w"

)

tk.Label(
    text = "="

).grid(
    row=3, column=1,

)

awnserVar = tk.StringVar()

tk.Entry(
    textvariable=awnserVar,
).grid(
    row = 3, column = 2,
    sticky="e",
)

resultVar = tk.StringVar()
finalGrade = []
awnseredQuestions = 0
progressVar =  tk.StringVar()
progressVar.set("0%")
nameYourAwnserIs = tk.StringVar()


# final function when user is ready to see final grades
def evaluate(a, b, awnser): 
    global resultVar, awnseredQuestions
    print(str(eval(f"{a} + {b} == {str(awnser)}")))
    if ((eval(f"{a} + {b} == {str(awnser)}")) == True):
        finalGrade.append(1)
        resultVar.set("correct")
    else: 
        resultVar.set("incorrect")
        finalGrade.append(0)
    # 
    awnseredQuestions += 1
    progressVar.set(f"your progress is: {(awnseredQuestions/int(questionVar.get()))*100:.1f}%") # get prograss
    nameYourAwnserIs.set(f"{nameVar.get().capitalize()}, your awnser is")
    print(resultVar.get())
    newArgs()



tk.Button(
    text="submit",
    command= lambda: evaluate(arg1.get(), arg2.get(), awnserVar.get()),
).grid(
    row= 4, column = 2
)


tk.Label(
    textvariable = nameYourAwnserIs
).grid(
    row=5, column=0,
    columnspan=2
)

tk.Label(
    textvariable = resultVar
).grid(
    row = 5, column = 2,
    sticky="w",
)

tk.Label(
    textvariable = progressVar
).grid(
    row = 6, column = 1,
)

tk.Label(
    text = "do you want your results"
).grid(
    row = 7, column = 0
)

# create new args for the math
def newArgs():
    arg1.set(str(random.randint(1*(int(gradeVar.get())), 10*(int(gradeVar.get())))))
    arg2.set(str(random.randint(1*(int(gradeVar.get())), 10*(int(gradeVar.get())))))


finalGradeResults = tk.StringVar()
def finalResults():
    finalGradeResults.set(f"your final grade is: {((sum(finalGrade)/int(questionVar.get()))):.1%}")

# view results
tk.Button(
    text="yes",
    command= lambda: finalResults()
).grid(
    row= 7, column = 2, sticky = "w"
)
# exit program
tk.Button(
    text = "exit",
    command=lambda: root.destroy()
).grid(
    row= 7, column = 2, sticky="e"

)


tk.Label(
    textvariable= finalGradeResults,
).grid(
    row= 8, column = 2
)









root.mainloop()
