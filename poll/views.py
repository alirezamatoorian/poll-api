from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *


# Create your views here.


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated, DeleteAndUpdateOnlyByOwner]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
