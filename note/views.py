from django.shortcuts import render
from rest_framework import generics
from note.serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,logout, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from note.models import Note
from note.serializers import NoteSerializer
# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    




class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data)

        return Response({"error":"wrong Creditentials"}, status = status.HTTP_400_BAD_REQUEST)




class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
         

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
 