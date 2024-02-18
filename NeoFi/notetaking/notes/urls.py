# notes/urls.py
from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDeleteView, NoteShareView, NoteHistoryView, UserSignUpView, UserLoginView

urlpatterns = [
    path('notes/create/', NoteListCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDeleteView.as_view(), name='note-retrieve-update-delete'),
    path('notes/share/', NoteShareView.as_view(), name='note-share'),
    path('notes/version-history/<int:pk>/', NoteHistoryView.as_view(), name='note-version-history'),
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
