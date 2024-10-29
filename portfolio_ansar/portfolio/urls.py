from django.urls import path, include
from .views import index, skills, portfolio, books, posts

urlpatterns = [
    # path('', index, name='about_me'),
    # path('skills', skills, name='skills'),
    # path('portfolio', portfolio, name='portfolio'),
    # path('', books, name='books')
    path('', posts, name='posts')
]