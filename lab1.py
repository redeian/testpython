# Challenge!
# ----------------------------------
# creating a function to calculate the area of circle.
# Users will specify the number of circle, 
# the program will calculate the area of each circle with radius -1
# for example
# input : 5
# process: [the area of circle of radius 1-5 will be calcuated]. 
# output: [print all areas on the screen]

def cal_circle_area( radius ):
    return 3.141 * radius * radius

circle_number = int(input("give me number : "))

areas = []

for i in range(1, circle_number+1):
    area = cal_circle_area(i)
    areas.append(area)

    print (f"the area of {i} is {area}")

areas.pop(0)
areas.append(10)
print(sum(areas))

# Challenge 2!
# --------------------------------
# from the first challenge...store all areas in an array. :)
# take the first area of the list, 
#                    and then add 10 at the end of the array.
# Then, sum of all areas and display on screen.

grades = {'Mark': 'A', 
          'Jib': 'B'}

print(grades['Mark']) # A
print("Mark")