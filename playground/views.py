from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")

# Create view that returns http response with a random string
def say_random_stuff(request):
    random_string = generate_random_string()
    context = {'random_string': random_string}
    return render(request, 'say_random_stuff.html', context)

def generate_random_string():
    # Generate a random string using any desired method
    # For example, you can use the random.choice() function to select random characters from a predefined set of characters
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_string = ''.join(random.choice(characters) for _ in range(10))
    return random_string
