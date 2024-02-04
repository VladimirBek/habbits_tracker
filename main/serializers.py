from rest_framework import serializers
from main.models import Habit
from main.validators import DurationValidator, InitialInstanceFieldsValidator


class RelatedHabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения информации связанных привычек.
    """

    class Meta:
        model = Habit
        fields = ['place', 'time', 'action', 'duration']


class HabitsCreateSerializers(serializers.ModelSerializer):
    """
    Сериализатор модели Habit.
    Используется при вызове POST запросов в контроллерах HabitsCreateView и HabitsUpdateView.
    :user: автоматическое заполнение поля при создании экземпляра Привычки.
    :related_habit: отображение информации о связанной привычке в случае, если она указана.
    """

    user = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)
    related_habit = RelatedHabitSerializer(required=False)

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            InitialInstanceFieldsValidator(),
            DurationValidator(field='duration'),
        ]

    def create(self, validated_data):
        """
        Метод переопределен для возможности создания связанной привычки
        При вызове POST запроса метод получает от пользователя переданные данные. В случае, если был передан словарь
        'related_habit', то создается привычка и связанная приятная привычка

        :param validated_data: Данные указанные пользователем при вызове POST запроса
        :return: Привычка или Привычка и связанная привычка, если информация о второй была указана.
        """

        related_habit_data = validated_data.pop('related_habit', None)
        related_habit_user = validated_data.get('user')

        if related_habit_data:

            related_habit = Habit.objects.create(
                user=related_habit_user,
                **related_habit_data,
                is_pleasure=True,
                related_habit=None
            )

            validated_data['related_habit'] = related_habit

        habit = Habit.objects.create(**validated_data)
        return habit


class HabitsListSerializers(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове GET запросов в контроллере HabitsListView
    user: автоматическое заполнение поля при создании экземпляра Привычки
    periodicity: отображение текстового описания выбранной периодичности
    related_habit: отображение информации о связанной привычки в случае, если она указана.
    """

    user = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)

    periodicity = serializers.ChoiceField(
        choices=Habit.PERIODICITY_CHOICES,
        source='get_periodicity_display',
        read_only=True
    )

    related_habit = RelatedHabitSerializer(required=False, read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'