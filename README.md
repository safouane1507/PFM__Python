# Rapport de Projet de Fin de Module : Application Web de Gestion Scolaire "PreSkool"
> - **Encadré par : 	Pr. AHSAIN Sara**
> - **Préparé par :**
> - **Mohamed Reda Benmoussa**
> - **Safouane Bousakhra**

 ═══════════════════════════════════════════════════════════════════


     
 🎬  DEMO VIDEO 
 


https://github.com/user-attachments/assets/197bc350-60a8-4de2-9248-1f8807168249




═══════════════════════════════════════════════════════════════════════

<div align="center">

# 🏫 School Management System

**Système de Gestion Scolaire — Projet de Fin de Module**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> Une application web complète pour gérer les étudiants, les enseignants,  
> les cours, les examens et les emplois du temps d'un établissement scolaire.

</div>

---

## 📋 Table des Matières

- [✨ Fonctionnalités](#-fonctionnalités)
- [🗂️ Architecture & Modules](#️-architecture--modules)
- [📐 Diagramme de Classes](#-diagramme-de-classes)
- [🚀 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [▶️ Lancement](#️-lancement)
- [👥 Comptes de Test](#-comptes-de-test)
- [📸 Captures d'écran](#-captures-décran)
- [🛠️ Technologies Utilisées](#️-technologies-utilisées)
- [📁 Structure du Projet](#-structure-du-projet)
- [🤝 Contribution](#-contribution)

---

## ✨ Fonctionnalités

| Fonctionnalité | Admin | Enseignant | Étudiant |
|---|:---:|:---:|:---:|
| Gestion des étudiants (CRUD) | ✅ | ❌ | ❌ |
| Gestion des enseignants (CRUD) | ✅ | ❌ | ❌ |
| Gestion des départements | ✅ | ❌ | ❌ |
| Gestion des matières | ✅ | ✅ | 👁️ |
| Emploi du temps | ✅ | ✅ | 👁️ |
| Examens & Résultats | ✅ | ✅ | 👁️ |
| Jours fériés | ✅ | 👁️ | 👁️ |
| Authentification & Rôles | ✅ | — | — |
| Réinitialisation de mot de passe | ✅ | ✅ | ✅ |

> ✅ Accès complet &nbsp;|&nbsp; 👁️ Lecture seule &nbsp;|&nbsp; ❌ Pas d'accès

---

## 🗂️ Architecture & Modules

Le projet est organisé en **3 applications Django** indépendantes :

```
school/
├── home_auth/      # Authentification, rôles utilisateurs, reset password
├── faculty/        # Enseignants, Départements, Matières, Examens, Emploi du temps
└── student/        # Étudiants & Parents
```

---

## 📐 Diagramme de Classes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           home_auth                                     │
│                                                                         │
│  AbstractUser ◁──── CustomUser ────────────────────────────────────┐   │
│                      ├── is_student                                 │   │
│                      ├── is_teacher                                 │   │
│                      └── is_admin                                   │   │
│                                                                     │   │
│  PasswordResetRequest ──────FK──────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                             faculty                                     │
│                                                                         │
│   Teacher ◄──FK(head)── Department ──M2M──► Teacher                    │
│      ▲                       ▲                                          │
│      │ FK                    │ FK                                       │
│   Subject ──FK──────────────►┘                                          │
│      ▲                                                                  │
│      │ FK                                                               │
│   Exam ◄──FK── ExamResult ──FK──► Student (student app)                │
│                                                                         │
│   Timetable ──FK──► Subject                                             │
│            └──FK──► Teacher                                             │
│                                                                         │
│   Holiday   (indépendant)                                               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                             student                                     │
│                                                                         │
│   Parent ◄──1:1── Student                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

### Relations Clés

| Source | Type | Cible | Cardinalité |
|--------|------|-------|-------------|
| `PasswordResetRequest` | ForeignKey | `CustomUser` | N → 1 |
| `Department` | ForeignKey | `Teacher` (responsable) | N → 1 |
| `Department` | ManyToManyField | `Teacher` | M ↔ N |
| `Subject` | ForeignKey | `Department` | N → 1 |
| `Subject` | ForeignKey | `Teacher` | N → 1 |
| `Exam` | ForeignKey | `Subject` | N → 1 |
| `ExamResult` | ForeignKey | `Exam` | N → 1 |
| `ExamResult` | ForeignKey | `Student` | N → 1 |
| `Timetable` | ForeignKey | `Subject` | N → 1 |
| `Timetable` | ForeignKey | `Teacher` | N → 1 |
| `Student` | OneToOneField | `Parent` | 1 ↔ 1 |

---

## 🚀 Installation

### Prérequis

- Python **3.10+**
- pip
- Git

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/safouane1507/PFM__Python.git
cd PFM__Python

# 2. Créer un environnement virtuel
python -m venv monenv

# 3. Activer l'environnement
# Windows :
monenv\Scripts\activate
# Linux / macOS :
source monenv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

---

## ⚙️ Configuration

```bash
# Se placer dans le dossier Django
cd school

# Appliquer les migrations
python manage.py migrate

# (Optionnel) Créer un superutilisateur
python manage.py createsuperuser
```

> **Note :** Le projet utilise **SQLite** par défaut, aucune configuration de base de données supplémentaire n'est requise.

---

## ▶️ Lancement

```bash
cd school
python manage.py runserver
```

Ouvrez votre navigateur à l'adresse : **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 👥 Comptes de Test

| Rôle | Nom d'utilisateur | Mot de passe |
|------|-------------------|--------------|
| Admin | `admin` | `admin123` |
| Enseignant | `teacher1` | `teacher123` |
| Étudiant | `student1` | `student123` |

---

## 📸 Captures d'écran

<!-- Ajoutez vos captures d'écran ici :
![Dashboard Admin](assets/screenshots/dashboard.png)
![Liste des étudiants](assets/screenshots/students.png)
![Emploi du temps](assets/screenshots/timetable.png)
-->

> 🖼️ *Les captures d'écran seront ajoutées prochainement.*

---

## 🛠️ Technologies Utilisées

| Technologie | Rôle |
|-------------|------|
| **Python 3.11** | Langage principal |
| **Django 4.x** | Framework web back-end |
| **SQLite** | Base de données (développement) |
| **Bootstrap 5** | Interface utilisateur responsive |
| **HTML5 / CSS3 / JS** | Front-end |
| **Pillow** | Gestion des images de profil |

---

## 📁 Structure du Projet

```
PFM__Python/
│
├── school/                     # Répertoire principal Django
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── school/                 # Configuration du projet
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── home_auth/              # App : Authentification & Rôles
│   │   ├── models.py           #   CustomUser, PasswordResetRequest
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── faculty/                # App : Enseignants, Cours, Examens
│   │   ├── models.py           #   Teacher, Department, Subject,
│   │   │                       #   Holiday, Exam, ExamResult, Timetable
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── student/                # App : Étudiants & Parents
│   │   ├── models.py           #   Student, Parent
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── static/                 # CSS, JS, images statiques
│   └── templates/              # Templates HTML
│
├── rapport/                    # Documents & rapports du projet
├── requirements.txt
└── README.md
```

---

## 🤝 Contribution

Les contributions sont les bienvenues !

```bash
# 1. Forker le projet
# 2. Créer une branche feature
git checkout -b feature/ma-fonctionnalite

# 3. Committer les changements
git commit -m "feat: ajout de ma fonctionnalité"

# 4. Pousser la branche
git push origin feature/ma-fonctionnalite

# 5. Ouvrir une Pull Request
```

---

<div align="center">

Fait avec ❤️ — Projet de Fin de Module · LST IDAI

</div>
