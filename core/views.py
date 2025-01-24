from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import User, Project, Category, Priority, Task
from .serializers import UserSerializer, ProjectSerializer, CategorySerializer, PrioritySerializer, TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
import logging

logger = logging.getLogger(__name__)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['project', 'priority', 'category']
    search_fields = ['title', 'description']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        logger.info("Creating a new task")
        serializer.save()

