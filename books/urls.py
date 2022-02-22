from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views
from django.urls import path, include


urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>', views.BooksDetail.as_view()),
    
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)