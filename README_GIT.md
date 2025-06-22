### 🧑‍💻 Mitentwickeln – Branches & Git Flow

So arbeitest du am Projekt mit, ohne den Hauptcode (main/master) direkt zu verändern:

---

#### 🔻 Repository klonen

```bash
git clone https://github.com/DEIN_USERNAME/catering.git
cd catering
```

> 💡 Ersetze den Link durch deinen eigenen Repo-Link (z. B. von GitHub).

---

#### 🌱 Neuen Branch erstellen

```bash
git checkout -b feature/mein-feature
```

Beispiel:

```bash
git checkout -b feature/bestell-logik
```

---

#### 💾 Änderungen machen und committen

Dateien bearbeiten, speichern und dann:

```bash
git add .
git commit -m "✨ Neue Bestelllogik hinzugefügt"
```

---

#### 🔼 Branch hochladen

```bash
git push -u origin feature/bestell-logik
```

---

#### 🔁 Merge oder Pull Request

- Entweder lokal zusammenführen:

```bash
git checkout main
git merge feature/bestell-logik
git push
```

- Oder über GitHub: Öffne einen **Pull Request**, lasse Änderungen überprüfen und mergen.

---

#### 🧽 Branch löschen (optional)

```bash
git branch -d feature/bestell-logik
git push origin --delete feature/bestell-logik
```