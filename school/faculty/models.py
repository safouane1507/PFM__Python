from django.db import models
from django.conf import settings

class Teacher(models.Model):
   
    
    teacher_id = models.CharField(max_length=20, unique=True, verbose_name="ID Enseignant")
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    gender = models.CharField(max_length=10, choices=[('Male', 'Masculin'), ('Female', 'Féminin')], verbose_name="Genre")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    joining_date = models.DateField(verbose_name="Date d'embauche")
    mobile_number = models.CharField(max_length=15, verbose_name="Numéro de téléphone")
    address = models.TextField(blank=True, null=True, verbose_name="Adresse")
    experience = models.CharField(max_length=50, blank=True, null=True, verbose_name="Expérience")
    image = models.ImageField(upload_to='teachers/', blank=True, null=True, verbose_name="Photo de profil")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#classeDepartement    
    
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du département")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    head_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments',
        verbose_name="Responsable (Enseignant)"
    )
    teachers = models.ManyToManyField(
        Teacher,
        blank=True,
        related_name='departments',
        verbose_name="Enseignants"
    )

    def __str__(self):
        return self.name


# Ligne 44 et suivantes — après class Department
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la matière")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    
    # Lien avec Department (une matière appartient à un département)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subjects',
        verbose_name="Département"
    )
    
    # Lien avec Teacher (un enseignant enseigne cette matière)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subjects',
        verbose_name="Enseignant"
    )

    def __str__(self):
        return self.name
    
#jour feries (holidays)
class Holiday(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du jour férié")
    date = models.DateField(verbose_name="Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.name} ({self.date})"
    
