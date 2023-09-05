# to calculate a BMI of a person to ckeck they are obese or normal or underweight or overweight
def bmi_category(bmi):
    # BMI scale factor
    if bmi < 16:
        return 'category= severe thinness'
    elif bmi >= 16 and bmi < 17:
        return 'category= moderate thinness'
    elif bmi >= 17 and bmi <= 18.5:
        return 'category= mild thinness or underweight'
    elif bmi >= 18.5 and bmi < 24.9:
        return 'category= normal weight'
    elif bmi >= 25 and bmi < 29.9:
        return 'category= overweight'
    elif bmi >= 30 and bmi < 35:
        return 'category= obese class 1'
    elif bmi >= 35 and bmi < 40:
        return 'category= obese class 2'
    else:
        return 'category= obese class 3'


age = int(input('enter your age'))
# BMI cannot be calculated for children below the age of 2
if age <= 2:
    print('BMI cannot be calculated for children below the age of 2')
else:
    print('you can enter your height in meter,centi meter, and in ft')
    print('press 1 if you want to enter your height in meter\n 2 if you want to enter your height in centimeter 3 if you want to enter your height in ft')
    height_type = int(input('enter the method you want to provide your input: '))
    height = float(input('enter your height'))
    weight = float(input('enter your weight'))
    # if they want to enter their input in meter
    if height_type == 1:
        bmi = weight / (height ** 2)
        print('your BMI is ', bmi)
        bmi_cat = bmi_category(bmi)
        print('and your category is', bmi_cat)
    # if they want to enter their input in cm
    elif (height_type == 2):
        height = height / 100
        print('your height in meter is : ', height)
        bmi = weight / (height ** 2)
        print('your BMI is ', bmi)
        bmi_cat2 = bmi_category(bmi)
        print('and your category is', bmi_cat2)
    elif (height_type == 3):
        height = height / 3.281
        print('your height in meter is : ', height)
        bmi = weight / (height ** 2)
        print('your BMI is ', bmi)
        bmi_cat3 = bmi_category(bmi)
        print('and your category is', bmi_cat3)
    else:
        print('invalid input')
