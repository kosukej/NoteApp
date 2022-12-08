from . import views
from django.urls import path

app_name = "myapp"
urlpatterns = [
    path("", views.redirect_to_index, name="index"),
    path("index/", views.NoteIndexView.as_view(), name="index"),
    path("myapp/create/", views.NoteCreateView.as_view(), name="note_input"),
    path("myapp/detail/<uuid:pk>/",
         views.NoteDetailView.as_view(), name="note_detail"),
    path("myapp/update/<uuid:pk>/",
         views.NoteUpdateView.as_view(), name="note_update"),
    path("myapp/delete/<uuid:pk>/",
         views.NoteDeleteView.as_view(), name="note_delete"),
]
