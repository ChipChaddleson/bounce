import tkinter as tk


root = tk.Tk()
root.title("exam")

greeting = tk.Label(
    text="Wellcome to math practice",

)

greeting.grid(
    row = 0,
    column = 0,
    columnspan=2

)

# password label
tk.Label(
    text="usrname"
).grid(
    row = 1,
    column = 0
)

usrVar =  tk.StringVar()
usr = tk.Entry(
    textvariable = usrVar,

).grid(
    row = 1,
    column = 1,
)


# passworld label

tk.Label(
    text="password"
).grid(
    row = 2,
    column = 0
)

passVar =  tk.StringVar()
passw = tk.Entry(
    textvariable = passVar,

).grid(
    row = 2,
    column = 1,
)

# submition button

tk.Button(
    text="log in",
    command=lambda: print(f"username: {usrVar.get()}\n password: {passVar.get()}")

).grid(
    row = 3,
    column=1,
    sticky="nsw"
)


root.mainloop()