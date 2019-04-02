from django.shortcuts import render, HttpResponse, redirect
from .fibonacci_number import calculate_fibonacci_number
import time

def index(request):
    return render(request, 'fibonacci/index.html', {
        'title': 'Enter any number'
    })

def fib_calculator(request):
    number = request.GET.get('number', '')
    if number == '':
        return redirect('/')
    start = time.time()
    result = calculate_fibonacci_number(number)
    stop = time.time()
    total_time = stop - start
    print(total_time)
    if result == -1:
        return render(request, 'fibonacci/error.html', {
            'title': 'Cannot calculate fibonacci number for a negative number'
        })
    return render(request, 'fibonacci/results.html', {
        'result': str(result),
        'time_taken': str(total_time)
    })