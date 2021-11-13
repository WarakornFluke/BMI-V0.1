
name = input('What is your name:')
height = int(input('What is your height in cm:'))
weight = int(input ('What is your weight in kg:'))
BMI = int(weight/height/height*10000)
if BMI > 35:
    print(name + ' you are ' 'Extremely Obese.')
elif 30 < BMI < 34.9 :
    print(name + ' you are ' 'Obese.')
elif 25 < BMI < 29.9 :
    print(name + ' you are ' 'Overweight.')
elif 18.5 < BMI < 24.9 :
    print(name + ' you are ' 'Normal.')
else:
    print(name + ' you are ' 'Underweight.')