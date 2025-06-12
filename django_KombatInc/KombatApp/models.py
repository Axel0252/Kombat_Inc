from django.db import models

class Incontro(models.Model):
    RISULTATI = [
        ('B', 'Blu'),
        ('R', 'Rosso'),
    ]
    id_incontro = models.IntegerField(primary_key=True)
    angoloB = models.CharField(max_length=150, null=True)
    angoloR = models.CharField(max_length=150, null=True)
    esito = models.CharField(choices=RISULTATI, null=True) # Blu o Rosso
    ora = models.TimeField(null=False)
    data = models.DateField(null=False)
    categoria = models.CharField(max_length=150, null=False)
    coachAngoloB = models.CharField(max_length=150, null=True)
    coachAngoloR = models.CharField(max_length=150, null=True)

class Atleta(models.Model):
    CINTURE = [
        ('W', 'Bianca'),
        ('G', 'Gialla'),
        ('B', 'Blu'),
        ('M', 'Marrone'),
        ('N', 'Nera'),
    ]
    numTessera = models.CharField(max_length=150, primary_key=True)
    nome = models.CharField(max_length=150, null=False)
    cognome = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=150, null=False, unique=True)
    palestra = models.CharField(max_length=150, null=False)
    cintura = models.CharField(max_length=150, null=False, choices=CINTURE)
    categoria = models.CharField(max_length=150, null=False)
    storico = models.ForeignKey(Incontro, on_delete=models.CASCADE, related_name='atleti', null=True)

class Torneo(models.Model):
    GRADI = [
        ('AM', 'Amatore'),
        ('SP', 'Semi-Pro'),
        ('PR', 'Professionista'),
    ]
    DISCIPLINE = [
        ('MMA', 'Mixed Martial Arts'),
        ('K1', 'KickBoxing'),
        ('BJJ', 'Brasilian Jiu-Jitsu'),
    ]
    ID_torneo = models.IntegerField(primary_key=True)
    gradoMin = models.CharField(null=False, choices=GRADI)
    luogo = models.CharField(max_length=150, null=False)
    data = models.DateField(null=False)
    podio = models.JSONField(null=False)
    disciplina = models.CharField(null=False, choices=DISCIPLINE)
    a_pagamento = models.BooleanField(null=False, default=False)
    id_incontro = models.ForeignKey(Incontro, on_delete=models.CASCADE, related_name='tornei')

class Organizzatore(models.Model):
    numTessera = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, null=False)
    cognome = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=32, null=False)
    federazione = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)

class Ticket(models.Model):
    id_ticket = models.IntegerField(primary_key=True)
    costo = models.FloatField(null=False)
    data_prenotazione = models.DateField(null=False)
    scadenza = models.DateTimeField(null=False)

class Arbitro(models.Model):
    numTessera = models.IntegerField(primary_key=True)
    nome = models.CharField(null=False, max_length=150)
    cognome = models.CharField(null=False, max_length=150)
    password = models.CharField(null=False, max_length=32)
    email = models.EmailField(null=False)
    età = models.IntegerField(null=False)
    id_incontro = models.ForeignKey(Incontro, on_delete=models.CASCADE, related_name='arbitri')

class Coach(models.Model):
    GRADI = [
        ('1', '1 dan'),
        ('2', '2 dan'),
        ('3', '3 dan'),
        ('4', '4 dan'),
        ('5', '5 dan'),
    ]
    numTessera = models.IntegerField(primary_key=True)
    nome = models.CharField(null=False, max_length=150)
    cognome = models.CharField(null=False, max_length=150)
    password = models.CharField(null=False, max_length=32)
    email = models.CharField(null=False, max_length=150)
    palestra = models.CharField(null=False, max_length=150)
    grado = models.CharField(null=False, max_length=150, choices=GRADI)
    numTessera_atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, related_name='coach', null=True)

class Organizzazione(models.Model):
    numTessera = models.ForeignKey(Organizzatore, on_delete=models.CASCADE, related_name='organizzazione')
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='organizzazione')
