import pickle
from django.urls import reverse
import numpy as np
import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.http import JsonResponse


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

# @login_required(login_url='/accounts/login/')
# def predict_price(request):
#     if request.method == "POST":
#         try:
#             total_sqft = float(request.POST.get("total_sqft"))
#             bath = int(request.POST.get("bath"))
#             bhk = int(request.POST.get("bhk"))
#             location = request.POST.get("location").strip().lower()

#             x = np.zeros(len(model_columns))
#             x[0] = total_sqft
#             x[1] = bath
#             x[2] = bhk

#             if location in model_columns:
#                 loc_index = model_columns.index(location)
#                 x[loc_index] = 1

#             predicted_price = round(model.predict([x])[0], 2)

#             return render(request, "predict.html", {
#                 "prediction": f"Estimated Price: ₹ {predicted_price} Lakhs"
#             })
#         except Exception as e:
#             return render(request, "predict.html", {
#                 "error": f"Error: {str(e)}"
#             })

#     return render(request, "predict.html", {
#         "locations": model_columns[3:]  # Skip total_sqft, bath, bhk
#     })



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



def register_views(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request, user)
                return redirect('home')
        else:
            form = UserRegistrationForm()
        
        return render(request, 'registration/signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout view
@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    
    # Safe redirect fallback
    try:
        return redirect('login')
    except:
        return redirect(reverse('home'))