from django.urls import path
from . import views

urlpatterns = [

    # author's url

    path('book/', views.BookApiView.as_view(), name='book'),
    path('book/<int:pk>/', views.BookApiView.as_view(), name='book_pk'),

    # author's url
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="author_detail"),
    path('author/', views.AuthorView.as_view(), name="author"),

    # file url
    path('book/<int:pk>/upload_files', views.FileUploadView.as_view(), name='book_file')
]
