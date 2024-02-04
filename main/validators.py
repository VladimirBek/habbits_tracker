from datetime import timedelta
from rest_framework import status
from rest_framework.serializers import ValidationError


class DurationValidator:
    """
    Class for validating the duration of the habit.
    The duration of the habit cannot exceed 120 seconds.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        related_habit = value.get('related_habit')

        main_habit_duration = value.get(self.field, timedelta())
        main_habit_duration_in_sec = main_habit_duration.total_seconds()

        if main_habit_duration_in_sec > 120:
            raise ValidationError(
                {
                    'message': "Время выполнения привычки не может превышать 120 секунд.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )

        if related_habit:

            related_habit_duration = related_habit.get(self.field, timedelta())
            related_habit_duration_in_sec = related_habit_duration.total_seconds()

            if main_habit_duration_in_sec > 120 or related_habit_duration_in_sec > 120:
                raise ValidationError(
                    {
                        'message': "Время выполнения привычки не может превышать 120 секунд.",
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )


class InitialInstanceFieldsValidator:
    """
    Class for validating the fields of the instance of the model 'Habit'.

    Cases, when an error is raised 'ValidationError':
        - In case if making a flag 'is_pleasure' in True within the instance of general habit
        - In cade if habbit not public and its fields 'related_habit' and 'reward' are empty
        - In case, if both fields 'related_habit' and 'reward' are filled
    """

    def __call__(self, value):
        is_pleasure_habit = value.get('is_pleasure')
        related_habit = value.get('related_habit')
        reward = value.get('reward')

        if is_pleasure_habit:

            raise ValidationError(
                {
                    'message': "Недопустимо указывать признак приятной привычки у основной привычки",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )

        if not value.get('is_public'):
            if not (related_habit or reward):

                raise ValidationError(
                    {
                        'message': "Вы должны добавить связанную приятную привычку ('related_habit') "
                                   "или указать награду ('reward')",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )

        if related_habit and reward:
            raise ValidationError(
                {
                    'message': "Не допускается одновременное указание награды и связанной привычки.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )