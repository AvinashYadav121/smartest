from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('predict/', views.predict_price, name='predict'),
    path('predict_price/', views.predict_price, name='predict_price'),
    path('property-grid/', views.propertygrid, name='property_grid'),
    path('property-single/', views.propertysingle, name='property_single'),
    path('blog-grid/', views.bloggrid, name='blog_grid'),
    path('blog-single/', views.blogsingle, name='blog_single'),
    path('agent-single/', views.agentsingle, name='agent_single'),
    path('agents-grid/', views.agents_grid, name='agents_grid'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

    

    