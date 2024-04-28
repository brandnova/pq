from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse

from django.db.models import Count

from docs.models import *

from .models import *

from .forms import CustomUserCreationForm, MessagesForm, ReviewForm

from django.contrib import messages

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    pdf = Item.objects.all().order_by('?')

    return render(request, 'index.html', {
        'pdf_list': pdf,
    })

def about(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_instance = form.save(commit=False)
            review_instance.save()
            return redirect('home:about')  
        else:
            pass
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('?')  

    paginate = Paginator(reviews, 5)
    page= request.GET.get('page')
    rev = paginate.get_page(page)

    return render(request, 'about.html', {
        'rev': rev, 
        'form': form,
    })

def contact(request):

    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if User.is_authenticated:
                message.user = request.user
            else:
                  message.user = "Unregistered User."
            message.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect(request.path)
        else:
            messages.error(request, 'Sending failed. Please correct the errors below.')

    else:
        form = MessagesForm()

    return render(request, 'contact.html', {
    'form': form,
    'title': 'Contact',
})



def departments(request):

    department_id = request.GET.get('department', None)
    departments = Department.objects.annotate(item_count=Count('items'))  
    

    if department_id:
        filtered_items = Item.objects.filter(department_id=department_id)
    else:
        filtered_items = Item.objects.all()

    return render(request, 'departments.html', {
        'departments': departments,
        'items': filtered_items,
        'department_id': int(department_id) if department_id else None,

    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Registration successful!')
            return redirect('home:signin')  # Redirect to signin page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            return redirect('home:signup')  # Redirect to signup page with errors
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {
        'form': form
        })

def signin(request):

    return render(request, 'signin.html')

def services(request):

    return render(request, 'services.html')

def sample(request):

    return render(request, 'sample.html')



def calculate_gpa_grade_points(units, grade):
    # Assign grade points based on the grade earned
    grade_points = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'F': 0
    }

    # Calculate grade points for the course
    if grade in grade_points:
        return units * grade_points[grade]
    else:
        return 0

def calculate_gpa_tcp_tnu(course_data):
    # Initialize total credit points (TCP) and total number of units (TNU)
    total_credit_points = 0
    total_units = 0

    # Calculate total credit points and total units for the semester
    for course in course_data:
        total_credit_points += course['grade_points']
        total_units += course['units']

    return total_credit_points, total_units

def calculate_cgpa(cumulative_tcp, cumulative_tnu, current_cgpa):
    # Calculate CGPA
    total_tcp = cumulative_tcp + current_cgpa * cumulative_tnu
    total_tnu = cumulative_tnu + cumulative_tnu
    cgpa = total_tcp / total_tnu
    return round(cgpa, 2)

def gpa_cgpa_calculator(request):
    if request.method == 'POST':
        # Retrieve course data from POST parameters
        course_data = []
        for i in range(1, 11):  # Assuming up to 10 courses are allowed
            course_name = request.POST.get(f'course_name_{i}')
            if not course_name:
                break
            units = float(request.POST.get(f'units_{i}'))
            grade = request.POST.get(f'grade_{i}')

            # Calculate grade points for the course
            grade_points = calculate_gpa_grade_points(units, grade)

            # Store course data
            course_data.append({
                'course_name': course_name,
                'units': units,
                'grade': grade,
                'grade_points': grade_points
            })

        
        # Check if any course data is entered
        if not course_data:
            return HttpResponse("No course data entered. Exiting.")

        # Input cumulative data
        current_cgpa = float(request.POST.get('current_cgpa', 0))
        cumulative_tcp = float(request.POST.get('cumulative_tcp'))
        cumulative_tnu = float(request.POST.get('cumulative_tnu'))

        # Calculate total TCP and TNU for the semester
        total_credit_points, total_units = calculate_gpa_tcp_tnu(course_data)

        # Calculate GPA for the semester
        semester_gpa = total_credit_points / total_units

        # Calculate CGPA
        cgpa = calculate_cgpa(cumulative_tcp, cumulative_tnu, current_cgpa)

        # Prepare context data to pass to template
        context = {
            'course_data': course_data,
            # Other context data...
        }
        return render(request, 'gpa_cgpa_result.html', context)
    else:
        return render(request, 'gpa_cgpa_calculator.html', {
            'title': 'GPA/CGPA Calculator.',
        })




def gpa_cgpa_result(request):
    # Retrieve context data passed from the calculator view
    course_data = request.POST.getlist('course_data')
    semester_gpa = request.POST.get('semester_gpa')
    cgpa = request.POST.get('cgpa')

    # Prepare context data to pass to template
    context = {
        'course_data': course_data,
        'semester_gpa': semester_gpa,
        'cgpa': cgpa,
    }

    # Render the result template with the context data
    return render(request, 'gpa_cgpa_result.html', context)
