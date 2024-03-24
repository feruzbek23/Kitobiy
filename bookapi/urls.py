from django.urls import path
from . import views



urlpatterns = [

    # author's url
    path("secret/", views.UserAuthentification.as_view(), name='user'),    

    path('books/', views.BookApiView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookApiView.as_view(), name='books_pk'),

    # author's url
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="author_detail"),
    path('author/', views.AuthorView.as_view(), name="author"),

    # file url
    path('books/<int:pk>/upload_files', views.FileUploadView.as_view(), name='books_file')
]
