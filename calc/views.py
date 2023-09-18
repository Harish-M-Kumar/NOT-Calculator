from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from sympy import *

# Create your views here.

def home(req):
    if req.method == 'POST':
        return render(req, 'index.html')
    else:
        return render(req, 'index.html')

def math(req):
    return render(req, 'math.html')

def conversion(req):
    return render(req, 'conversion.html')

def health(req):
    return render(req, 'health.html')

def currency(req):
    return render(req, 'currency.html')

# for math
def add(req):
    if req.method == 'POST':
        num1 = float(req.POST['add1'])
        num2 = float(req.POST['add2'])
        return render(req, 'add.html', {'output': f"The sum is : {num1 +num2}"})
    else:
        return render(req, 'add.html')
    
def subtract(req):
    if req.method == 'POST':
        num1 = float(req.POST['subt1'])
        num2 = float(req.POST['subt2'])
        return render(req, 'subt.html', {'output': f"The difference is : {num1 - num2}"})
    else:
        return render(req, 'subt.html')
    
def multiplicaion(req):
    if req.method == 'POST':
        num1 = float(req.POST['mult1'])
        num2 = float(req.POST['mult2'])
        return render(req, 'mult.html', {'output': f"The product is : {num1 * num2}"})
    else:
        return render(req, 'mult.html')
    
def division(req):
    if req.method == 'POST':
        num1 = float(req.POST['divi1'])
        num2 = float(req.POST['divi2'])
        if num2 == 0:
            return render(req, 'divi.html', {'output': "Enter valid numbers"})
        return render(req, 'divi.html', {'output': f"The quotient is : {num1 / num2}"})
    else:
        return render(req, 'divi.html')
    
def integration(req):
    if req.method == 'POST':
        x = symbols('x')
        y = req.POST['inetgrate']
        ans = integrate(y, x)
        return render(req, 'integ.html', {'output':f"The integration is : {ans}"})
    else:
        return render(req, 'integ.html')
    
def differentiation(req):
    if req.method == 'POST':
        x = symbols('x')
        y = req.POST['differentiate']
        ans = diff(y, x)
        return render(req, 'diff.html', {'output':f"The derivative is : {ans}"})
    else:
        return render(req, 'diff.html')
    


# for health

def bmi(req):
    if req.method == 'POST':
        height = float(req.POST['height'])
        weight = float(req.POST['weight'])
        bmi = round(weight/(height/100)**2, 2)
        if bmi<18.5:
            return render(req, 'bmi.html', {'output1':f"BMI : {bmi}", 'output2':"Please Eat, you are thin!!!"})
        elif bmi>=18.5 and bmi<=24.9:
            return render(req, 'bmi.html', {'output1':f"BMI : {bmi}", 'output2':"you are fit!!!"})
        elif bmi<=29.9:
            return render(req, 'bmi.html', {'output1':f"BMI : {bmi}", 'output2':"you are fat!!!"})
        else:
            return render(req, 'bmi.html', {'output1':f"BMI : {bmi}", 'output2':"you are a 10, size of 10 planets!!!"})
    else:
        return render(req, 'bmi.html')
    
def calorie(req):
    if req.method == 'POST':
        height = float(req.POST['height'])
        weight = float(req.POST['weight'])
        age = int(req.POST['age'])
        gender = req.POST['gender']
        if gender == "male":
            bmr = 10*weight + 6.25*height - 5*age + 5
            return render(req, "calorie.html", {'output':f'Your basic calorie requirment is : {bmr}'})
        else:
            bmr = 10*weight + 6.25*height - 5*age -161
            return render(req, "calorie.html", {'output':f'Your basic calorie requirment is : {bmr}'})
    else:
        return render(req, "calorie.html")
    

# for converstion

def kmMi(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "KToM":
            km = float(req.POST['kilometer'])
            mi = km * 0.621371
            return render(req, 'kmMi.html', {'output':f"Miles : {mi}"})
        else:
            mi = float(req.POST['miles'])
            km = mi * 1.60934
            return render(req, 'kmMi.html', {'output':f"Kilometers : {km}"})
    else:
        return render(req, 'kmMi.html')

def kgLb(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "KgToLbs":
            kgs = float(req.POST['kilogram'])
            pound = kgs *2.20462
            return render(req, 'kgLb.html', {'output':f"Pounds : {pound}"})
        else:
            pounds = float(req.POST['Pounds'])
            kgs = pounds * 0.453592
            return render(req, 'kgLb.html', {'output':f"Kilograms : {kgs}"})
    else:
        return render(req, 'kgLb.html')
    
def meFeet(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "FtToM":
            ft = float(req.POST['ft'])
            mtr = ft * 0.3048
            return render(req, 'meFeet.html', {'output':f"Meters : {mtr}"})
        else:
            mtr = float(req.POST['mtr'])
            ft = mtr * 3.28084
            return render(req, 'meFeet.html', {'output':f"Feet : {ft}"})
    else:
        return render(req, 'meFeet.html')
    
def binary(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "BToD":
            bina = req.POST['binary']
            deci = int(bina, 2)
            return render(req, 'binary.html', {'output':f"Decimal : {deci}"})
        else:
            deci = int(req.POST['decimal'])
            bina = bin(deci)
            return render(req, 'binary.html', {'output':f"Binary : {bina}"})
    else:
        return render(req, 'binary.html')
    
def octal(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "OToD":
            octa = req.POST['octal']
            deci = int(octa, 8)
            return render(req, 'octal.html', {'output':f"Decimal : {deci}"})
        else:
            deci = int(req.POST['decimal'])
            octa = oct(deci)
            return render(req, 'octal.html', {'output':f"Octal : {octa}"})
    else:
        return render(req, 'octal.html')
    
def hexa(req):
    if req.method == 'POST':
        x = req.POST['unit']
        if x == "HToD":
            hexa = req.POST['hexa']
            deci = int(hexa, 16)
            return render(req, 'hexa.html', {'output':f"Decimal : {deci}"})
        else:
            deci = int(req.POST['decimal'])
            hexa = hex(deci)
            return render(req, 'hexa.html', {'output':f"Hexadecimal : {hexa}"})
    else:
        return render(req, 'hexa.html')
    

# for currency
def inr(req):
    if req.method == 'POST':
        rup = float(req.POST['inr'])
        aud = round(rup / 53.08, 2)
        usd = round(rup / 83.12, 2)
        pou = round(rup / 103.62, 2)
        return render(req, 'inr.html',{'ans1':f"AUD : {aud}",'ans2': f"USD : {usd}", 'ans3': f"POUND : {pou}"})
    else:
        return render(req, 'inr.html')
    
def usd(req):
    if req.method == 'POST':
        usd = float(req.POST['usd'])
        aud = round(usd * 1.57, 2)
        inr = round(usd * 83.12, 2)
        pou = round(usd * 0.8, 2)
        return render(req, 'usd.html',{'ans1':f"AUD : {aud}",'ans2': f"INR : {inr}", 'ans3': f"POUND : {pou}"})
    else:
        return render(req, 'usd.html')
    
def aud(req):
    if req.method == 'POST':
        aud = float(req.POST['aud'])
        usd = round(aud * 0.64, 2)
        inr = round(aud * 53.08, 2)
        pou = round(aud * 0.51, 2)
        return render(req, 'usd.html',{'ans1':f"USD : {usd}",'ans2': f"INR : {inr}", 'ans3': f"POUND : {pou}"})
    else:
        return render(req, 'aud.html')
    
def pound(req):
    if req.method == 'POST':
        pou = float(req.POST['pounds'])
        usd = round(pou * 1.25, 2)
        inr = round(pou * 103.62, 2)
        aud = round(pou * 1.95, 2)
        return render(req, 'usd.html',{'ans1':f"USD : {usd}",'ans2': f"INR : {inr}", 'ans3': f"AUD : {aud}"})
    else:
        return render(req, 'pound.html')