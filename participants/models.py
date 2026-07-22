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
        ('CMR', 'Cameroun'),
        ('RCA', 'République centrafricaine'),
        ('TCHAD', 'Tchad'),
        ('GM', 'Gambie'),
        ('ET', 'Ethiopie'),
        ('CAG', 'Congo'),
        ('CI', "Côte d'Ivoire"),
        ('SN', 'Sénégal'),
        ('FR', 'France'),
        ('USA', 'États-Unis'),
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
        max_length=9,
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
