from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('predict/', views.predict_price, name='predict'),
    path('predict_price/', views.predict_price, name='predict_price'),
    
   
   
    path('signup/', views.register_views, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('property-grid/', views.propertygrid, name='property_grid'),
    path('property-single/', views.propertysingle, name='property_single'),
    path('blog-grid/', views.bloggrid, name='blog_grid'),
    path('blog-single/', views.blogsingle, name='blog_single'),
    # path('agent/', views.agent, name='agent'),
    path('agent-single/', views.agentsingle, name='agent_single'),
    path('agents-grid/', views.agents_grid, name='agents_grid'),
    
]
    