import math

def paint_calc(height, width, cover):
    area = height * width
    no_of_cans = area / cover
    round_up_cans = math.ceil(no_of_cans)
    print(f"You will need {round_up_cans} cans of paint")


h = int(input("Enter the height of the wall in meters: "))
w = int(input("Enter the width of the wall in meters: "))
coverage = 5

paint_calc(height=h, width=w, cover=coverage)
