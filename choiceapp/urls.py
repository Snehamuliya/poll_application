from django.urls import path
from .views import index, signup, login, u_logout, poll, activity, GeneratePDF, profilePDF

urlpatterns = [
    path('', index, name="home"),
    path('signup', signup),
    path('login', login, name="login"),
    path('logout', u_logout),
    path('profile', profilePDF),
    path('polls', poll),
    path('activities', activity),
    path('pdf', GeneratePDF.as_view(), name="pdf"),
]
