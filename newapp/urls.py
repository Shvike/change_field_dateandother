from django.urls import re_path, path
from newapp import views


urlpatterns = [
    # re_path("", views.main_page)
    path("entry/<int:id>/", views.UpdateEntry.as_view(), name="update_entry"),
    re_path("", views.main_view.as_view(), name="main"),
]