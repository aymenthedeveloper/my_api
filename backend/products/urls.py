from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('', views.ProductListView.as_view(), name="prs"),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('create/', views.ProductCreateView.as_view()),
    path('update/<int:pk>', views.ProductUpdateView.as_view()),
    path('delete/<int:pk>', views.ProductDeleteView.as_view()),
    path('list-or-create/', views.ProductListCreateView.as_view()),
    path('get-token/', obtain_auth_token),
]