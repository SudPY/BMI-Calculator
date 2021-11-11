weight = float(input("Enter the weight in kg : "))
height = float(input("Enter the height in cm : "))
bmi = weight / (height/100) ** 2

def calc_bmi():
    if bmi < 18.5:
        print("Your bmi is ", bmi, "You are underweight")
    elif bmi > 24.9:
        print("Your bmi is ", bmi, "You are overweight")
    elif bmi > 18.5 and bmi < 24.9:
        print("Your bmi is ", bmi, "You have normal weight")
    else: 
        print("Your bmi is ", bmi, "You are obese")

calc_bmi()
