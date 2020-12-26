import tkinter
class User:
    def __init__(self, name=" ", gender=" ", dob=" ", weight=0.0, height=0.0):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.weight = weight
        self.height = height
    def calculate_bmi(self):
        return float(self.weight / (self.height * self.height))
    def bmi_analysis(self):
        bmi = self.calculate_bmi()
        if bmi < 18.50:
            analysis = "underweight:("
        elif bmi < 25:
            analysis = "healthy:)"
        elif bmi < 30:
            analysis = "overweight!!!"
        else:
            analysis = "obesity!!!"
        return analysis

def calculate():
    user = User(weight=float(weight_entry.get()), height=float(height_entry.get()))
    bmi_label.configure(text="Your BMI is " + str(round(user.calculate_bmi(), 2))+ " you are "+ user.bmi_analysis() + ".")
interface = tkinter.Tk()
interface.title("BMI Calculator")
interface.minsize(200, 200)
height_label = tkinter.Label(text="Height (m)")
weight_label = tkinter.Label(text="Weight (Kg)")
bmi_label = tkinter.Label()
height_entry = tkinter.Entry(justify="right")
weight_entry = tkinter.Entry(justify="right")
calculate_button = tkinter.Button(text="Calculate", command=calculate)
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry.grid(row=0, column=1, padx=10, pady=10)
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry.grid(row=1, column=1, padx=10, pady=10)
bmi_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
calculate_button.grid(row=4, column=1, padx=10, pady=10)
tkinter.mainloop()