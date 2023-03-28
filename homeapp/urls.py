from django.urls import path
from homeapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('single-blog/', views.singleBolg, name="singleBlog"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('portfolio-details/', views.portfolioDetails, name="portfolioDetails"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('pricing/', views.pricing, name="pricing"),
    path('services/', views.services, name="services"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('project-form/', views.projectForm, name="form"),
    path('form/', views.form, name="form"),
]