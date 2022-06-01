from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def generate_password(request):
    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    uppercase = False
    special = False
    numbers = False

    special_list = list('!&')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
        uppercase = True

    if request.GET.get('special'):
        characters.extend(special_list)
        special = True

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        numbers = True

    lenght = int(request.GET.get('lenght', 12))

    def make_password(lenght=12):
        thepassword = ''
        for x in range(lenght):
            thepassword += random.choice(characters)
        return thepassword

    output_password = make_password(lenght)

    def chek_output_password_on_conditions(password: str):
        if uppercase:
            if not any(s.isupper() for s in password):
                return chek_output_password_on_conditions(make_password(lenght))

        if numbers:
            if not any(s.isdigit() for s in password):
                return chek_output_password_on_conditions(make_password(lenght))

        if special:
            if not any(s in password for s in special_list):
                return chek_output_password_on_conditions(make_password(lenght))

        return password

    return render(request, 'generator/generate.html', {'password': chek_output_password_on_conditions(output_password)})
