import pickle
import numpy as np
import os
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegistrationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CustomUserCreationForm
# from .forms import CustomUserCreationForm



# Load the model and columns
model_path = os.path.join("estimator", "ml", "model.pkl")
columns_path = os.path.join("estimator", "ml", "columns.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "rb") as f:
    model_columns = pickle.load(f)

# Public view (no login required)
def home(request):
    return render(request, "home.html")

# Authenticated views
@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, "about.html")

@login_required(login_url='/accounts/login/')
def contact(request):
    return render(request, "contact.html")

@login_required(login_url='/accounts/login/')
def propertygrid(request):
    return render(request, "property-grid.html")

@login_required(login_url='/accounts/login/')
def propertysingle(request):
    return render(request, "property-single.html")

@login_required(login_url='/accounts/login/')
def bloggrid(request):
    return render(request, "blog-grid.html")

@login_required(login_url='/accounts/login/')
def blogsingle(request):
    return render(request, "blog-single.html")

@login_required(login_url='/accounts/login/')
def agentsingle(request):
    return render(request, 'agent-single.html')

@login_required(login_url='/accounts/login/')
def agents_grid(request):
    return render(request, 'agents-grid.html')

@login_required(login_url='/accounts/login/')
def predict_price(request):
    if request.method == "POST":
        try:
            total_sqft = float(request.POST.get("total_sqft"))
            bath = int(request.POST.get("bath"))
            bhk = int(request.POST.get("bhk"))
            location = request.POST.get("location").strip().lower()

            x = np.zeros(len(model_columns))
            x[0] = total_sqft
            x[1] = bath
            x[2] = bhk

            if location in model_columns:
                loc_index = model_columns.index(location)
                x[loc_index] = 1

            predicted_price = round(model.predict([x])[0], 2)
            return JsonResponse({"prediction": f"₹ {predicted_price} Lakhs"})

        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"})

    # If GET request, return page with locations
    return render(request, "predict.html", {
        "locations": model_columns[3:]  # Skip numeric columns
    })




def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

    



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

