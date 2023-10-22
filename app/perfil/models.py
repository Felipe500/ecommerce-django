import re

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from app.common.choices import ORDER_STATUS, STATES_BR
from app.common.utils import valida_cpf


class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=8)
    number = models.CharField(max_length=5)
    district = models.CharField(max_length=32)
    city = models.CharField(max_length=50)
    states = models.CharField(max_length=2, default=STATES_BR.PI, choices=STATES_BR)

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis de usuários'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def clean(self):
        error_ = {}

        if not valida_cpf(self.cpf):
            error_['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_['zip_code'] = 'CEP inválido, digite os 8 digitos do CEP'

        if error_:
            raise ValidationError(error_)
