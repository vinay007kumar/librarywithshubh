from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views
from django.urls import path, include


urlpatterns = [
    path('', views.api_root),
    path('books/', views.BooksList.as_view(), name='books-list'),
    path('books/<int:pk>', views.BooksDetail.as_view(), name='books-detail'),
    
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)