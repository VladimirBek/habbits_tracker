from rest_framework.permissions import BasePermission


class IsHabitCreator(BasePermission):
    """
   Class for checking that the current user is the creator of the habbit.
    """

    def has_object_permission(self, request, view, obj):
        """
        Method for checking that the current user is the creator of the habbit.
        return: True if the current user is the creator of the habbit, False otherwise
        """

        if request.user == obj.user:
            return True

        return False