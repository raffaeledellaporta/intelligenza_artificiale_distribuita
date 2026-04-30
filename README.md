# Distributed Bank Token Ring System

## Descrizione del Progetto

Questo progetto implementa un sistema distribuito che simula un ambiente bancario composto da 4 nodi (ATM), utilizzando l’algoritmo di **mutua esclusione Token Ring**.

Ogni nodo rappresenta un ATM indipendente che:

* comunica tramite socket su localhost
* non condivide memoria con gli altri nodi
* può eseguire transazioni (deposito/prelievo) solo quando possiede il token

Il sistema garantisce:

* mutua esclusione
* consistenza del saldo
* assenza di concorrenza nelle operazioni critiche

---

# Configurazione dell’Ambiente

## Requisiti

* Python 3.10 o superiore
* Sistema operativo: Windows / Linux / macOS

## Clonare il progetto

```bash
git clone https://github.com/raffaeledellaporta/intelligenza_artificiale_distribuita
cd distributed-bank-token-ring
```

# Architettura del Sistema

* 4 nodi: ATM1, ATM2, ATM3, ATM4
* Comunicazione: socket TCP su localhost
* Topologia logica: anello (ring)

```
ATM1 → ATM2 → ATM3 → ATM4 → ATM1
```

* Ogni nodo conosce solo il proprio successore
* Il token circola continuamente tra i nodi

---

# Avvio del Sistema

## Step 1: Aprire 4 terminali separati

### Terminale 1

```bash
python run/run_atm1.py
```

### Terminale 2

```bash
python run/run_atm2.py
```

### Terminale 3

```bash
python run/run_atm3.py
```

### Terminale 4

```bash
python run/run_atm4.py
```

---

## Step 3: Inviare il Token Iniziale

Aprire un quinto terminale ed eseguire lo script 
```bash
python run/start_token.py
```
Questo comando invierà il token iniziale al nodo ATM1, consentendo l’inizio del ciclo token ring.
Questo invia il token iniziale ad ATM1

---

# Comportamento del Sistema

Una volta avviato:

* Il token circola tra i nodi
* Solo il nodo con il token può:

  * entrare nella sezione critica
  * eseguire una transazione

---

# Output Atteso

Nel terminale di ogni nodo verranno mostrati:

* Ricezione del token
* Inoltro del token
* Inizio transazione
* Fine transazione
* Saldo aggiornato

### Esempio:

```
[ATM2] Ricevuto TOKEN
[ATM2] Inizio transazione withdraw 200
[ATM2] Saldo aggiornato: 800
[ATM2] Inviato TOKEN a ATM3
```

---

# Proprietà Garantite

Il sistema dimostra:

* ✔ Mutua esclusione (una sola transazione alla volta)
* ✔ Consistenza del saldo
* ✔ Ordinamento deterministico tramite token
* ✔ Assenza di race condition

---

# Associazione Nodo – Terminale

Ogni nodo è eseguito in un terminale separato:

| Terminale | Nodo |
| --------- | ---- |
| 1         | ATM1 |
| 2         | ATM2 |
| 3         | ATM3 |
| 4         | ATM4 |

Ogni log è identificato dal nome del nodo:

```
[ATM1] ...
[ATM2] ...
```

---

# Porte Utilizzate

| Nodo | Porta |
| ---- | ----- |
| ATM1 | 5001  |
| ATM2 | 5002  |
| ATM3 | 5003  |
| ATM4 | 5004  |

---

# Video Dimostrativo

Il repository include un video che mostra:

* Tutti i 4 nodi in esecuzione
* Circolazione del token
* Esecuzione delle transazioni
* Assenza di accessi concorrenti

---

# Repository GitHub

Il codice completo del progetto è disponibile qui:

```
https://github.com/raffaeledellaporta/intelligenza_artificiale_distribuita
```

Contiene:

* codice sorgente completo
* commenti esplicativi
* video dimostrativo

---

# Note Finali

* Il sistema è completamente distribuito
* Non viene utilizzata memoria condivisa
* Il coordinamento avviene esclusivamente tramite messaggi
* L’algoritmo implementato è **Token Ring**

---

# Autore

Nome: Raffaele Della Porta
Matricola: 0322500029
Laurea: LM-32 - Ingegneria Informatica e dell’Intelligenza Artificiale Applicata
Corso : Intelligenza Artificiale Distribuita