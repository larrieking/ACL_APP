from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_details, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name="post_share")
]
