# Generated by Django 4.2.6 on 2023-10-22 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Perfil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                ("date_of_birth", models.DateField()),
                ("cpf", models.CharField(max_length=11)),
                ("address", models.CharField(max_length=60)),
                ("number", models.CharField(max_length=5)),
                ("district", models.CharField(max_length=32)),
                ("city", models.CharField(max_length=50)),
                (
                    "states",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        default="PI",
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil do usuário",
                "verbose_name_plural": "Perfis de usuários",
            },
        ),
    ]
