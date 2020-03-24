from django.conf import settings
from .utils import import_callable, default_create_token
from rest_framework import serializers
from .ser import (PasswordResetSerializer as DefaultPasswordResetSerializer,PasswordResetConfirmSerializer as DefaultPasswordResetConfirmSerializer,PasswordChangeSerializer as DefaultPasswordChangeSerializer)
serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
PasswordResetSerializer = import_callable(serializers.get('PASSWORD_RESET_SERIALIZER',DefaultPasswordResetSerializer))

PasswordResetConfirmSerializer = import_callable(serializers.get( 'PASSWORD_RESET_CONFIRM_SERIALIZER',DefaultPasswordResetConfirmSerializer))

PasswordChangeSerializer = import_callable(serializers.get('PASSWORD_CHANGE_SERIALIZER',DefaultPasswordChangeSerializer))