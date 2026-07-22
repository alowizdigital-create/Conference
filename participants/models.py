from django.db import models
from core.models import BaseModel, Company
import uuid


class Participant(BaseModel):


    QUALITY_CHOICES = [
        ('responsable', 'Responsable'),
        ('pasteur', 'Pasteur'),
        ('etudiant_pasteur', 'Étudiant pasteur'),
        ('protocole', 'Protocole'),
        ('evangeliste', 'Évangeliste'),
    ]

    COUNTRY_CHOICES = [
        ('CM', 'Cameroun'),
        ('CF', 'République centrafricaine'),
        ('TD', 'Tchad'),
        ('GA', 'Gabon'),
        ('CG', 'Congo'),
        ('CD', 'République démocratique du Congo'),
        ('CI', "Côte d'Ivoire"),
        ('SN', 'Sénégal'),
        ('BF', 'Burkina Faso'),
        ('ML', 'Mali'),
        ('NE', 'Niger'),
        ('GN', 'Guinée'),
        ('BJ', 'Bénin'),
        ('TG', 'Togo'),
        ('FR', 'France'),
        ('US', 'États-Unis'),
    ]


    full_name = models.CharField(
        max_length=150,
        verbose_name="Nom complet"
    )

    local_church = models.CharField(
        max_length=150,
        verbose_name="Église locale"
    )

    congregation = models.CharField(
        max_length=150,
        verbose_name="Congrégation"
    )

    city = models.CharField(
        max_length=100,
        verbose_name="Ville"
    )

    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        verbose_name="Pays"
    )

    quality = models.CharField(
        max_length=30,
        choices=QUALITY_CHOICES,
        verbose_name="Qualité"
    )

    phone = models.CharField(
        max_length=30,
        verbose_name="Téléphone"
    )

    photo = models.ImageField(
        upload_to="participants/",
        blank=True,
        null=True,
        verbose_name="Photo"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.full_name
