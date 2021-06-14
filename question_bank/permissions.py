from django.utils.translation import ugettext_lazy as _
from rest_framework import permissions
from account import models


class QuestionAccess(permissions.BasePermission):

    message = _('اجازه دسترسي ندارید')

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        user = request.user
        if user.type == models.User.Types.QUESTION_MAKER:
            return True
        elif user.type == models.User.Types.ADMIN:
            return True
        else:
            return False