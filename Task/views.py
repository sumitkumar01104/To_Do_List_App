from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from rest_framework.permissions import AllowAny


#templtes 
def index(request):
    return render(request,'index.html')
# ── REGISTER ──────────────────────────────────────────────
class RegisterView(APIView):
    def post(self, request):
        authentication_classes = []     
        permission_classes = [AllowAny]
        username = request.data.get('username')
        password = request.data.get('password')
        email    = request.data.get('email', '')

        if not username or not password:
            return Response(
                {"error": "Username aur password zaroori hain"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Yeh username pehle se exist karta hai"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"message": "Account ban gaya!", "token": token.key},
            status=status.HTTP_201_CREATED
        )


# ── LOGIN ──────────────────────────────────────────────────

class LoginView(APIView):
    authentication_classes = []      
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Username aur password dono bharo"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {"non_field_errors": ["Username ya password galat hai!"]},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key})


# ── LOGOUT ─────────────────────────────────────────────────
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logout ho gaye!"}, status=status.HTTP_200_OK)


# ── TASKS: LIST + CREATE ───────────────────────────────────
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class       = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        # Sirf logged-in user ki tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Task save karte waqt user automatically set ho
        serializer.save(user=self.request.user)


# ── TASK: RETRIEVE + UPDATE + DELETE ──────────────────────
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class       = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        # Sirf apni task access kar sake
        return Task.objects.filter(user=self.request.user)


# ── SUBTASKS: LIST + CREATE ────────────────────────────────
class SubtaskListCreateView(generics.ListCreateAPIView):
    serializer_class       = SubtaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        return Subtask.objects.filter(
            task__user=self.request.user,
            task__id=self.kwargs['task_pk']
        )

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_pk'], user=self.request.user)
        serializer.save(task=task)


# ── SUBTASK: RETRIEVE + UPDATE + DELETE ───────────────────
class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class       = SubtaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        return Subtask.objects.filter(
            task__user=self.request.user,
            task__id=self.kwargs['task_pk']
        )