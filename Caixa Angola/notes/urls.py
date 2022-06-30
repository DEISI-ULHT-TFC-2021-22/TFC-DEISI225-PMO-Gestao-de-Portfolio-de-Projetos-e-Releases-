from django.urls.resolvers import URLPattern
from notes import views
from django.urls import path

urlpatterns = [
    path('NoteList', views.notelist, name='notelist'),
    path('AddNote/', views.addnote,  name='addnote'),
    path('Edit/<int:note_id>', views.edit_note),
    path('Delete/<int:note_id>', views.delete_note)
]