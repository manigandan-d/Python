def BMI(weight, height):
    bmi = weight / (height ** 2)

    return bmi


weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = BMI(weight, height)

print("BMI is {} and You are considered".format(bmi), end=" ")

if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi < 25:
    print("Healthy")

elif 25 <= bmi < 30:
    print("Overweight")

else:
    print("Obese")
