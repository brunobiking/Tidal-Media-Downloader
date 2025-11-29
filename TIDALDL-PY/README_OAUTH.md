\# Authentification OAuth personnalisée pour Tidal-Media-Downloader



\## ⚠️ Avertissement important



Ce fork utilise une authentification OAuth personnalisée nécessitant \*\*vos propres credentials Tidal\*\*.



\*\*Limitation critique\*\* : L'API publique de Tidal ne permet PAS le téléchargement direct de fichiers audio haute qualité.  Cette implémentation OAuth est destinée à des fins éducatives et d'expérimentation.



---



\## 📋 Prérequis



1\. \*\*Compte développeur Tidal\*\*

  - Créez un compte sur https://developer.tidal.com/

  - Créez une nouvelle application

  - Notez votre `client_id` et `client_secret`



2. **Configuration de l'application Tidal**

  - Redirect URI : `http://localhost:8080/callback`

  - Scopes nécessaires : `r_usr w_usr w_sub`



---



\## 🚀 Installation



\### 1. Cloner le repository



```bash

git clone https://github.com/brunobiking/Tidal-Media-Downloader-devicelocksmith.git

cd Tidal-Media-Downloader-devicelocksmith/TIDALDL-PY

```



\### 2. Créer l'environnement virtuel



```bash

python -m venv venv

venv\\Scripts\\activate  # Windows

\# ou

source venv/bin/activate  # Linux/Mac

```



\### 3. Installer les dépendances



```bash

pip install -r requirements.txt

pip install -e .

```



\### 4.  Configurer les credentials



Créez un fichier `. env` dans le dossier `TIDALDL-PY` :



```env

TIDAL_CLIENT_ID=votre_client_id

TIDAL_CLIENT_SECRET=votre_client_secret

TIDAL_REDIRECT_URI=http://localhost:8080/callback

TIDAL_COUNTRY_CODE=CA

```



\*\*⚠️ NE COMMITEZ JAMAIS LE FICHIER .env SUR GITHUB\*\*



---



\## 🔑 Authentification



\### Utilisation du système OAuth



```python

from tidal\_dl.oauth\_auth import TidalOAuth



\# Initialiser l'authentification

oauth = TidalOAuth()



\# Première connexion

if not oauth.is\_authenticated():

&nbsp;   oauth.authenticate()



\# Récupérer le token

access\_token = oauth.get\_access\_token()

```



---



\## 🔒 Sécurité



\- Vos credentials sont stockés dans `. env` (non-versionné)

\- Les tokens sont dans `~/.tidal-dl-oauth.token.json`

\- Ne partagez JAMAIS ces fichiers



---



\## ⚠️ Limitations connues



1\. \*\*Pas de téléchargement haute qualité\*\* : L'API publique Tidal ne fournit pas les URLs de téléchargement direct des fichiers audio. 

2\. \*\*Fonctionnalité limitée\*\* : Seules les métadonnées et informations sont accessibles via OAuth public.

3\. \*\*Pour usage personnel uniquement\*\* : Ne distribuez pas vos credentials. 



---



\## 🐛 Dépannage



\### Erreur "TIDAL\_CLIENT\_ID must be set"

\- Vérifiez que votre fichier `.env` existe et contient les bonnes valeurs

\- Assurez-vous d'être dans le bon dossier (TIDALDL-PY)



\### Le navigateur ne s'ouvre pas

\- Copiez manuellement l'URL affichée dans le terminal

\- Vérifiez que le port 8080 n'est pas déjà utilisé



\### Token expiré

\- Le refresh devrait être automatique

\- Si problème, relancez l'authentification



---



\## 📄 Licence



Même licence que le projet original (Apache 2.0)

