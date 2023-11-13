import tkinter as tk
from PIL import Image, ImageTk
#handling the input data
def is_numeric(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False
def on_submit():
    label_cat.place_forget()
    if is_numeric(entry1.get()) and is_numeric(entry2.get()):
        #bmi logic
        weight = float(entry1.get())
        height = float(entry2.get())/100
        bmi = weight/height**2
        label_op.place(x=175,y=300)
        label_op.config(text=f"Your Body Mass Index BMI is {bmi:.2f}")

        #setting the category label
        label_cat.place(x=185,y=350)
        if(bmi<18.5):
            label_cat.config(text="BMI Category: Underweight")
            label_cat.config(fg="red")
        elif(bmi>=18.5 and bmi<=24.9):
            label_cat.config(text="BMI Category: Healthy Weight")
            label_cat.config(fg="green")
        elif(bmi>=25.0 and bmi<=29.9):
            label_cat.config(text="BMI Category: Overweight")
            label_cat.config(fg="orange")
        elif(bmi>=30):
            label_cat.config(text="BMI Category: Obesity")
            label_cat.config(fg="red")

        
    #handling error events
    else:
        label_op.place_forget()
        label_cat.place(x=270,y=350)
        label_cat.config(text="     Invalid Data!    ")
        label_cat.config(fg="red")
def onbtnclick1(event):
    if entry1.get() == "Enter Your Weight(Kg)":
        entry1.delete(0,tk.END)
        entry1.config(fg='black')
def onbtnclick2(event):
    if entry2.get() == "Enter Your Height(cm)":
        entry2.delete(0,tk.END)
        entry2.config(fg='black')

root = tk.Tk()
#we are initlializing the Tk class in tkinter module and root is now the object
#its basically the main window of the program
root.title("BMI Calculator")
root.geometry("700x500")
#The above sets width and height
root.resizable(False,False)
#setting the background image
image_path = "images/bmiback.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

canvas.pack()
#creating an input box with the entry widget
entry1 = tk.Entry(root,fg='grey',font=("Helvetica", 14))
entry1.insert(0,'Enter Your Weight(Kg)')
entry1.bind('<FocusIn>',onbtnclick1)
entry1.place(x=260,y=100)
entry2 = tk.Entry(root,fg='grey',font=("Helvetica", 14))
entry2.insert(0,'Enter Your Height(cm)')
entry2.bind('<FocusIn>',onbtnclick2)
entry2.place(x=260,y=150)
# output labels
label_op = tk.Label(root,text="",font=("Helvetica", 17))
label_cat = tk.Label(root,text="",font=("Helvetica", 17,'bold'))
#creating a button
check_weight_btn = tk.Button(root,text="Check BMI",font=("Helvetica", 12),command=on_submit)
check_weight_btn.place(x=325,y=200)
root.mainloop()