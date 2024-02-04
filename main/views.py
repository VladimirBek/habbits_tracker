from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from main.models import Habit
from main.pagination import CustomPaginationClass
from main.permissions import IsHabitCreator
from main.serializers import HabitsCreateSerializers, HabitsListSerializers


class HabitsCreateView(generics.CreateAPIView):
    """.
    Controller for creating an instance of the model 'Habbit'.
    """

    serializer_class = HabitsCreateSerializers

    def perform_create(self, serializer):
        """
        Method for automatically adding 'user' field to the model 'Habbit'
        """

        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListView(generics.ListAPIView):
    """
    Controller for displaying a list of instances of the model 'Habbit'.
    """

    serializer_class = HabitsListSerializers
    pagination_class = CustomPaginationClass

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Habit.objects.all()

        return Habit.objects.filter(user=self.request.user)


class PublicHabitsListView(generics.ListAPIView):
    """
Controller for displaying a list of public instances of the model 'Habbit'.
    """

    serializer_class = HabitsListSerializers
    pagination_class = CustomPaginationClass
    queryset = Habit.objects.filter(is_public=True)


class HabitsUpdateView(generics.UpdateAPIView):
    """
Controller for updating an instance of the model 'Habbit'.
    """

    serializer_class = HabitsCreateSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator | IsAdminUser]


class HabitsDeleteView(generics.DestroyAPIView):
    """
Controller for deleting an instance of the model 'Habbit'.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator | IsAdminUser]
