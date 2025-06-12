from django.contrib import admin
from django.urls import path
from KombatApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("registration", registrazione, name='registrazione'),
    path('registra_atleta', registra_atleta, name="registra_atleta"),
    path('registra_coach', registra_coach, name="registra_coach"),
    path('registrazione_atleta', registrazione_atleta, name="registrazione_atleta"),
    path('registrazione_coach', registrazione_coach, name="registrazione_coach"),
    path('login', login, name="login"),
    path('visualizza_incontro', visualizza_incontro, name='visualizza_incontro'),
    path('area_personale', area_personale, name="area_personale"),
    path('modifyData', modifyData, name="modifyData"),
    path('tornei', visualizzaTornei, name="visualizzaTornei"),
]
