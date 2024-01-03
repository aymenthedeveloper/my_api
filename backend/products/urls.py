from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.ProductMixinView.as_view(), name="prs"),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('create/', views.ProductMixinView.as_view()),
    path('update/<int:pk>', views.ProductMixinView.as_view()),
    path('delete/<int:pk>', views.ProductMixinView.as_view()),
    path('list-or-create/', views.ProductListCreateView.as_view()),
]