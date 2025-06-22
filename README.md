# 🍽️ Catering Bestellsystem (Flutter + FastAPI)

Ein digitales Bestellsystem für die Gastronomie, das Kellnern, Bar und Küche hilft, Bestellungen effizient zu verwalten – **vollständig offlinefähig**.

---

## 🧩 Funktionen

- Flutter-App zur Auswahl von Tischen
- Jeder Tisch führt zu einer Bestellseite
- Testweise Kommunikation mit lokalem Server (FastAPI)
- Unterstützung für Emulator oder Handy im selben WLAN
- Ideal für Raspberry Pi oder lokale Offline-Server

---

## 🚀 Projektstruktur

```
.
├── lib/
│   └── main.dart             # Flutter UI & HTTP-Anfragen
├── catering_server/
│   └── server.py             # FastAPI Server
└── README.md
```

---

## ⚙️ Voraussetzungen

### 📱 Flutter App

- [Flutter SDK](https://docs.flutter.dev/get-started/install)
- Android Studio **oder** VS Code + Android Emulator
- `http`-Paket in `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^0.13.6
```

Dann im Projektverzeichnis ausführen:

```bash
flutter pub get
```

---

### 🖥️ Backend Server (FastAPI)

#### Installation (einmalig):

```bash
pip install fastapi uvicorn
```

#### Server starten:

```bash
cd catering_server
uvicorn server:app --host 0.0.0.0 --port 8000
```

🔁 **Achte darauf, dass deine IP im Flutter-Code korrekt ist!**  
Ersetze z. B. `http://10.0.1.3:8000/message` durch die IP deines lokalen Servers.  
Diese findest du mit:

```bash
ipconfig   # auf Windows
```

---

## 📲 Flutter App starten

1. Projekt in VS Code oder Android Studio öffnen
2. Emulator starten oder Handy anschließen
3. App starten mit:

```bash
flutter run
```

Du solltest die Tischauswahl sehen. Jeder Button führt zur Bestellseite mit einem Test-Button.

---

## 🧪 Testkommunikation

Drücke auf:

- **„Testnachricht an Server“** (in Übersicht)
- **„Test-Nachricht an Server“** (auf Bestellseite)

Der Server gibt im Terminal z. B. folgendes aus:

```
Nachricht erhalten: Test von Tisch 3
```

---

## 🛠️ Weiterentwicklung

**Geplant:**

- Bestellungen mit Artikeln und Mengen
- Rollensystem (Bar, Küche, Kellner)
- Lokale Datenbank zur Speicherung
- Konfigurierbare Speisekarte und Tische

**Später:**

- Export-Funktion (PDF/CSV)
- Statistikseite
- Nutzerverwaltung (für Admins)

---

## 🛜 Netzwerkmodell (offlinefähig)

- App verbindet sich direkt mit lokalem Server (z. B. Raspberry Pi)
- Keine Internetverbindung nötig
- Gäste **sind nicht im gleichen Netzwerk** wie das System

## 👤 Entwickler

> Dieses Projekt wurde von Paul Forthuber begonnen und soll langfristig ausbaufähig sein.  
> Ziel: vollständige digitale Lösung für Servicepersonal, Küche & Bar in der Gastronomie – offline & sicher.

## 🧰 Anforderungen & Installation

### 🔧 Systemvoraussetzungen

| Komponente           | Beschreibung                                      |
|----------------------|---------------------------------------------------|
| Flutter SDK          | Für die mobile App-Entwicklung                    |
| Android Studio       | Zum Starten eines Emulators (oder echtes Gerät)  |
| Python 3.x           | Für den lokalen Server (FastAPI)                 |
| Pip                  | Python-Paketmanager (meist vorinstalliert)       |
| Git                  | Für Versionierung und Teamarbeit                 |

---

### 📥 Installation – Schritt für Schritt

#### 1. Flutter installieren

👉 Anleitung: [https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install)

Danach im Terminal prüfen:

```bash
flutter doctor
```

---

#### 2. Android Studio installieren

👉 Download: [https://developer.android.com/studio](https://developer.android.com/studio)

- Erstelle ein virtuelles Gerät im AVD Manager
- Aktiviere USB-Debugging auf deinem echten Gerät (optional)

---

#### 3. Python & Pip installieren

- Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Nach der Installation im Terminal prüfen:

```bash
python --version
pip --version
```

---

#### 4. FastAPI & Uvicorn installieren

```bash
pip install fastapi uvicorn
```

Optional: Anforderungen speichern

```bash
pip freeze > requirements.txt
```

---

#### 5. Git installieren

👉 Download: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Terminal-Test:

```bash
git --version
```

---

#### 6. Projekt clonen und starten

```bash
git clone https://github.com/DEIN_USERNAME/catering.git
cd catering
flutter pub get
flutter run
```

Server starten:

```bash
cd catering_server
uvicorn server:app --host 0.0.0.0 --port 8000
```