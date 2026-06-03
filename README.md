# Rubrica Web

Applicazione web per la gestione di una rubrica telefonica, sviluppata in Python con Flask.

## Requisiti
- Python 3.x
- MySQL
- Pip

## Installazione
```bash
git clone https://github.com/andrea-scala/rubrica-web.git
cd rubrica-web
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Creazione file .env
Crea il file .env nella dir di progetto in questo modo
```bash
HOST=localhost
PORT=3306
DB=rubrica
USERNAME=rubrica
PASSWORD=rubrica
SECRET_KEY=una-stringa-segreta-qualsiasi
```
## Avvio
```bash
sudo service mysql start
sudo mysql < schema_database.sql
python3 crea_utente.py #le credenziali sono admin admin
flask run
```

## Apertura del browser
Apri il browser su http://localhost:5000.
