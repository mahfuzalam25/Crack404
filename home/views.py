from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Project, Website, Home, Review, Team, About
from django.contrib import messages

# Create your views here.

def get_website_data():
    return Website.objects.all().order_by('-created_at')

def get_about_data():
    return About.objects.all()

def get_project_data():
    return Project.objects.all().order_by('-created_at')

def get_review_data():
    return Review.objects.all().order_by('-created_at')
def get_team_data():
    return Team.objects.all()

def home(request):
    if request.method == 'POST':
        customername = request.POST.get('customername')
        customerdesignation = request.POST.get('customerdesignation')
        customerimage = request.FILES.get('customerimage')  # Handle image upload
        customerreview = request.POST.get('customerreview')
        # Create a new review instance and save it
        review = Review(
            customername=customername,
            customerdesignation=customerdesignation,
            customerimage=customerimage,
            customerreview=customerreview,
        )
        review.save()
        # Optionally, you can add a success message
        messages.success(request, 'Thank you for your review!')
        # Redirect to the home page after saving
        return redirect('home')  # Assuming 'home' is the name of your home URL

    banners = Home.objects.all().order_by('-created_at')
    projects = get_project_data()
    websites = get_website_data()
    abouts = get_about_data()
    review = get_review_data()
    teams = get_team_data()
    context = {
        'projects':projects,
        'websites':websites,
        'abouts':abouts,
        'banners':banners,
        'review':review,
        'teams':teams,
        }
    return render(request,'home/index.html', context)

def websites(request):
    websites = get_website_data()
    context = {'websites': websites}
    return render(request, 'home/website.html', context)

def about(request):
    abouts = get_about_data()
    context = {'abouts':abouts}
    return render(request, 'home/about.html', context)

def projects(request):
    projects = get_project_data()
    context = {'projects':projects}
    return render(request, 'home/projects.html',context)

def team(request):
    teams = get_team_data()
    context = {'teams':teams}
    return render(request,'home/team.html', context)

def career(request):
    return render(request,'home/career.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        #print(f"{last_name} {email} {content}")
        if len(first_name)<2 or len(last_name)<2 or len(email)<10 or len(content)<4:
            messages.error(request,'Please fill the form again.')
        else:
            contact = Contact(first_name=first_name, last_name=last_name, email=email,content=content)
            contact.save()
            messages.success(request,'Your messages is been sent')
    return render(request, 'home/contact.html')

