# notes/views.py
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from .models import Note, NoteHistory
from .serializers import NoteSerializer, NoteHistorySerializer, UserSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Perform login logic here using the provided username and password
        username = request.data.get('username')
        password = request.data.get('password')

        # Print or log information for debugging
        print(f"Attempting login with username: {username}, password: {password}")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=200)
        else:
            print("Authentication failed. User not found or invalid credentials.")
            return Response({'message': 'Invalid credentials'}, status=401)



class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteShareView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_ids = request.data.get('shared_with', [])
        instance.shared_with.set(user_ids)
        instance.save()
        return Response({'message': 'Note shared successfully'}, status=status.HTTP_200_OK)

class NoteHistoryView(generics.ListAPIView):
    queryset = NoteHistory.objects.all()
    serializer_class = NoteHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        note_id = self.kwargs.get('pk')
        return NoteHistory.objects.filter(note__id=note_id)
    
class NoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def default_view(self, request):
        return render(request, 'default.html')