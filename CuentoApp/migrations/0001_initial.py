# Generated by Django 5.0 on 2024-01-27 01:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Editorial",
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
                ("nombre", models.CharField(max_length=200)),
                ("direccion", models.CharField(blank=True, max_length=200)),
                ("telefono", models.CharField(blank=True, max_length=20)),
                ("sitio_web", models.URLField(blank=True)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="editoriales_logos/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Autor",
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
                ("biografia", models.TextField(blank=True)),
                (
                    "foto",
                    models.ImageField(
                        blank=True, null=True, upload_to="autores_fotos/"
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="autor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Avatar",
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
                ("imagen", models.ImageField(upload_to="avatares/")),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="avatar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cuento",
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
                ("titulo", models.CharField(max_length=200)),
                ("sinopsis", models.TextField()),
                ("texto_completo", models.TextField()),
                (
                    "fecha_publicacion",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "imagen_portada",
                    models.ImageField(
                        blank=True, null=True, upload_to="cuentos_portadas/"
                    ),
                ),
                (
                    "autores",
                    models.ManyToManyField(
                        related_name="cuentos", to="CuentoApp.autor"
                    ),
                ),
            ],
        ),
    ]