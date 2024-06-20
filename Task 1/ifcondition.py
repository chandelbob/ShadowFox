'''
1. Write a program to determine the BMI Category based on user input. Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

def bmi():
    height= float(input("enter height in meters:"))
    weight=float(input("enter your weight in kilogram:"))
BMI = (weight / (height * 2))                 # Calculating BMI 

    # Start of If Else ladder
    #  
if BMI >= 30 :                                 
        print("Obesity")
elif BMI > 25 and BMI <= 29 :       
        print("Overweight")
elif BMI > 18.5 and BMI <= 25 :     
        print("Normal")
elif BMI < 18.5 :                   
        print("Underweight")
else :
        print ("Wrong Input")           # Wrong Input 

bmi()                   # Calling Funtion 


