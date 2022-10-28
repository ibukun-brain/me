from django.urls import path
from app import views as app_view

app_name = "app"

urlpatterns = [
    path(
        '', 
        view=app_view.IndexView.as_view(),
        name="home"
    )
]