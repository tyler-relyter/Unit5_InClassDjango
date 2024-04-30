from django.shortcuts import render, redirect
import os

def display_data(request):
    # Get the current directory
    data_path = os.path.join(os.path.dirname(__file__), 'data/data.txt')
    data = []
    # Read the data from the file
    with open(data_path, 'r') as input_file:
        for line in input_file:
            processed_line = line.strip().split(',')
            data.append(processed_line)

    return render(request, 'display_data.html', {'data': data})

def add_data(request):
    if request.method == "POST":
        course = request.POST.get('course')
        title = request.POST.get('title')
        instructor = request.POST.get('instructor')
        new_data = f"{course},{title},{instructor}\n"
        data_path = os.path.join(os.path.dirname(__file__), 'data/data.txt')
        with open(data_path, 'a') as output_file:
            output_file.write(new_data)
        return redirect('display_data')
    else:
        return render(request, 'add_data.html')