from django.shortcuts import render
import hashlib
from KombatApp.models import *
from django.core.exceptions import ValidationError

def index(request):
    return render(request, 'index.html', {})

def get_user_info(email, password):
    user_exists = {
        "exists" : False,
        "data" : {},
        "redirect" : "",
        "type" : "",
    }
    if Atleta.objects.filter(email=email, password=password).exists():
        user_exists["exists"] = True
        user_exists['data'] = Atleta.objects.filter(email=email, password=password)
        user_exists['redirect'] = "homeAtleta.html"
        user_exists['type'] = "Atleta"
    if Coach.objects.filter(email=email, password=password).exists():
        user_exists["exists"] = True
        user_exists['data'] = Coach.objects.filter(email=email, password=password)
        user_exists['redirect'] = "homeCoach.html"
        user_exists['type'] = "Coach"
    if Arbitro.objects.filter(email=email, password=password).exists():
        user_exists["exists"] = True
        user_exists['data'] = Arbitro.objects.filter(email=email, password=password)
        user_exists['redirect'] = "homeArbitro.html"
        user_exists['type'] = "Arbitro"
    if Organizzatore.objects.filter(email=email, password=password).exists():
        user_exists["exists"] = True
        user_exists['data'] = Organizzatore.objects.filter(email=email, password=password)
        user_exists['redirect'] = "homeOrganizzatore.html"
        user_exists['type'] = "Organizzatore"
    return user_exists

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        user = get_user_info(email, hashed_password)
        if(user['exists']):
            utente = user['data'].get()
            return render(request, user['redirect'], {'email' : email, 'data': utente, 'type': user['type']})
        else:
            return render(request, 'index.html', {'error_message' : "Credenziali non valide, riprova."})
    else:
        return render(request, 'index.html', {'error_message' : "Metodo non valido"})

def registrazione(request):
    return render(request, 'registration.html')

def registrazione_coach(request):
    return render(request, 'registrazione_coach.html')

def registrazione_atleta(request):
    return render(request, 'registrazione_atleta.html')

def registra_atleta(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Se esiste già
        atleta = Atleta.objects.filter(email=email)
        if len(atleta) != 0:
            return render(request, 'registration.html', {'error_message':"Questa mail è già associata ad un altro utente."})
        
        password = request.POST.get('passw')
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        numTess = request.POST.get('numTess')
        cintura = request.POST.get('cintura')
        categoria = request.POST.get('categoria')
        atleta = Atleta.objects.create(
            email=email, 
            password=hashed_password,
            nome=nome,
            cognome = cognome,
            numTessera = numTess,
            cintura = cintura,
            categoria = categoria
        )
        try:
            atleta.full_clean() # Forza un controllo sull'aver inserito solo i valori consentiti
        except ValidationError:
            return render(request, 'index.html', {'error_message':"Dati inseriti non validi"})
        return render(request, 'index.html', {'success_message':"Registrazione avvenuta con successo"})
    else:
        return render(request, 'registration.html', {'error_message':"Problemi nella registrazione"})
    

def registra_coach(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Se esiste già
        coach = Coach.objects.filter(email=email)
        if len(coach) != 0:
            return render(request, 'registration.html', {'error_message':"Questa mail è già associata ad un altro utente."})
        
        password = request.POST.get('passw')
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        numTess = request.POST.get('numTess')
        coach = Coach.objects.create(
            email=email, 
            password=hashed_password,
            nome = nome,
            cognome = cognome,
            numTessera = numTess,
        )

        try:
            coach.full_clean()
        except ValidationError:
            return render(request, 'registration.html', {'error_message':"Dati inseriti non validi"})

        return render(request, 'index.html', {'success_message':"Registrazione avvenuta con successo"})
    else:
        return render(request, 'registration.html', {'error_message':"Problemi nella registrazione"})
    
def visualizza_incontro(request):
    if request.method == 'POST':
        id_incontro = request.POST.get('id_incontro')
        incontro = Incontro.objects.filter(id_incontro=id_incontro).get()
        arbitro = Arbitro.objects.filter(id_incontro=id_incontro).get()
    return render(request, 'visualizza_incontro.html', {'incontro':incontro, 'arbitro':arbitro})

def area_personale(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        hashedPassw = request.POST.get('passw')
        tipo = request.POST.get('type')
        user = get_user_info(email, hashedPassw)['data'].get()
    return render(request, 'area_personale.html', {'user':user, 'type':tipo})

def update_user_info(nome, cognome, passw, email, 
                     età, federazione, palestra, grado, cintura, categoria, tipo, old_email):
    if tipo == 'Atleta':
        Atleta.objects.filter(email=old_email).update(
            email=email, 
            password=passw,
            nome=nome,
            cognome = cognome,
            cintura = cintura,
            categoria = categoria
        )
        return True
    elif tipo == 'Arbitro':
        Arbitro.objects.filter(email=old_email).update(
            email=email, 
            password=passw,
            nome=nome,
            cognome = cognome,
            età = età
        )
        return True
    elif tipo == 'Coach':
        Coach.objects.filter(email=old_email).update(
            email=email, 
            password=passw,
            nome=nome,
            cognome = cognome,
            palestra = palestra,
            grado = grado
        )
        return True
    elif tipo == 'Organizzatore':
        Organizzatore.objects.filter(email=old_email).update(
            email=email, 
            password=passw,
            nome=nome,
            cognome = cognome,
            federazione = federazione
        )
        return True
    else:
        return False

def modifyData(request):
    if request.method == 'POST':
        old_email = request.POST.get('old_email')
        nome = request.POST.get('nome', '')
        cognome = request.POST.get('cognome', '')
        passw = request.POST.get('passw', '')
        email = request.POST.get('email', '')
        età = request.POST.get('età', '')
        federazione = request.POST.get('federazione', '')
        palestra = request.POST.get('palestra', '')
        grado = request.POST.get('grado', '')
        cintura = request.POST.get('cintura', '')
        categoria = request.POST.get('categoria', '')
        tipo = request.POST.get('type')
        if update_user_info(nome,
                         cognome,
                         passw,
                         email,
                         età,
                         federazione,
                         palestra,
                         grado,
                         cintura,
                         categoria,
                         tipo,
                         old_email):
            return render(request, 'index.html', {'success_message':"Utente aggiornato correttamente"})
        else:
            return render(request, 'index.html', {'error_message':"Errore nell'aggiornamento dati"})
    else:
        return render(request, 'index.html', {'error_message':"Errore nell'aggiornamento dati"})    

def visualizzaTornei(request):
    tornei = Torneo.objects.all().values('ID_torneo', 'a_pagamento', 'data', 'disciplina', 'gradoMin', 'luogo', 'organizzazione', 'podio')
    return render(request, 'visualizzaTornei.html', {'tornei':tornei})