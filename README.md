# Kombat Inc.

Tafuro Alessandro 0334000086

## Installazione
Per scaricare la repository eseguire il comando:
```
git clone https://github.com/Axel0252/Kombat_Inc.git
```
Una volta fatto ciò, entrare nella cartella `django_KombatInc` ed eseguire da terminale:
```
# Da powershell o cmd
python -m venv venv
```
E poi:
```
# Da PowerShell
venv/Scripts/activate
# Oppure
venv/Scripts/activate.ps1

# Da cmd
venv/Scripts/activate.bat
```
Ora che l'ambiente virtuale è attivo, è possibile installare le dipendenze con:
```
python -m pip install -r requirements.txt
```

## Utilizzo

Per avviare il server eseguire:
```
py manage.py runserver
```

Gli utenti già registrati sono
Arbitri:
```
email: roberto.bianchi@example.com
passw: arb123

email: sara.rossi@example.com
passw: arb456

email:antonio.verdi@example.com
passw: arb789
```
Atleti:
```
luca.bianchi@example.com
pass123

anna.verdi@example.com
pass456

marco.rossi@example.com
pass789
```
Coach:
```
federico.marroni@example.com
coach123

chiara.blu@example.com
coach456

luigi.verdi@example.com
coach789
```
Organizzatori:
```
giorgio.neri@example.com
org123

elisa.blu@example.com
org456

paolo.verde@example.com
org789
```

