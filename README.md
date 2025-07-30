# 🛠️ Forge-Entête - Générateur d'En-têtes HTTP Réalistes

**Créé par ozGod-sh**

## Description

Forge-Entête est un générateur d'en-têtes HTTP réalistes qui simule différents navigateurs et systèmes d'exploitation. Il est conçu pour les tests de sécurité, l'évasion de détection et la simulation de trafic légitime lors d'audits de sécurité.

## Fonctionnalités

### 🌐 Templates de navigateurs
- **Chrome Windows** : Simulation complète de Chrome sur Windows
- **Firefox Linux** : Headers Firefox sur Ubuntu/Linux
- **Safari macOS** : En-têtes Safari sur macOS
- **Versions randomisées** : Numéros de version aléatoires réalistes

### 🔧 Formats de sortie
- **Format brut** : Affichage standard clé: valeur
- **Format JSON** : Export structuré pour intégration
- **Headers complets** : Tous les en-têtes nécessaires inclus

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Forge-Entete
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python forge_entete.py [OPTIONS]
```

### Options disponibles
- `-l, --list` : Lister tous les templates disponibles
- `-t, --template TEMPLATE` : Template à utiliser (chrome_windows, firefox_linux, safari_macos)
- `-o, --output FORMAT` : Format de sortie (raw, json)
- `-h, --help` : Affiche l'aide

### Exemples d'utilisation

#### 1. Lister les templates
```bash
python forge_entete.py --list
```

#### 2. Générer des headers Chrome Windows
```bash
python forge_entete.py -t chrome_windows
```

#### 3. Export JSON
```bash
python forge_entete.py -t firefox_linux -o json
```

## Structure des fichiers

```
Forge-Entete/
├── forge_entete.py     # Script principal
└── README.md          # Cette documentation
```

## Templates disponibles

### Chrome Windows
```python
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36'
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
'Accept-Encoding': 'gzip, deflate, br'
'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="{version}", "Chromium";v="{version}"'
```

### Firefox Linux
```python
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0'
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3'
'Accept-Encoding': 'gzip, deflate, br'
```

### Safari macOS
```python
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
'Accept-Language': 'fr-fr'
'Accept-Encoding': 'gzip, deflate, br'
```

## Cas d'usage

### Tests de sécurité
- **Évasion de détection** : Contourner les systèmes de détection basés sur User-Agent
- **Tests de WAF** : Vérifier les règles de filtrage
- **Simulation de trafic** : Générer du trafic réaliste
- **Bypass de restrictions** : Contourner les blocages par navigateur

### Développement web
- **Tests cross-browser** : Simuler différents navigateurs
- **Validation de compatibilité** : Tester les réponses par navigateur
- **Analytics** : Tester les systèmes de tracking
- **A/B Testing** : Simuler différents profils utilisateur

## Exemple de sortie

### Format brut (défaut)
```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🛠️  Forge-Entête v1.0.0                                  ║
║                                                              ║
║  Générateur d'en-têtes HTTP réalistes.                      ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] En-têtes générés avec le template 'chrome_windows':

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Sec-Ch-Ua: "Not_A Brand";v="99", "Google Chrome";v="112", "Chromium";v="112"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
```

### Format JSON
```json
{
  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-User": "?1"
}
```

## Intégration avec d'autres outils

### Avec curl
```bash
# Générer les headers et les utiliser avec curl
python forge_entete.py -t chrome_windows -o json > headers.json
curl -H "User-Agent: $(cat headers.json | jq -r '.["User-Agent"]')" http://example.com
```

### Avec Python requests
```python
import subprocess
import json

def get_realistic_headers(template='chrome_windows'):
    result = subprocess.run(['python', 'forge_entete.py', '-t', template, '-o', 'json'], 
                          capture_output=True, text=True)
    return json.loads(result.stdout.split('\n')[-2])  # Dernière ligne JSON

import requests
headers = get_realistic_headers('firefox_linux')
response = requests.get('http://example.com', headers=headers)
```

### Scripts d'automatisation
```bash
#!/bin/bash
# Tester avec différents navigateurs
templates=("chrome_windows" "firefox_linux" "safari_macos")
for template in "${templates[@]}"; do
    echo "=== Test avec $template ==="
    python forge_entete.py -t "$template" > headers_$template.txt
    # Utiliser les headers générés...
done
```

## Randomisation des versions

### Chrome (105-115)
```python
chrome_version = random.randint(105, 115)
# Génère: Chrome/112.0.0.0, Chrome/108.0.0.0, etc.
```

### Firefox (100-110)
```python
firefox_version = random.randint(100, 110)
# Génère: Firefox/105.0, Firefox/103.0, etc.
```

### Réalisme
- **Versions récentes** : Utilise des versions plausibles
- **Cohérence** : Maintient la cohérence entre les headers
- **Mise à jour** : Versions adaptées à la période actuelle

## Analyse des en-têtes

### En-têtes de sécurité modernes
```python
# Chrome/Chromium headers
'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="112"'
'Sec-Ch-Ua-Mobile': '?0'
'Sec-Ch-Ua-Platform': '"Windows"'
'Sec-Fetch-Dest': 'document'
'Sec-Fetch-Mode': 'navigate'
'Sec-Fetch-Site': 'none'
'Sec-Fetch-User': '?1'
```

### Différences par navigateur
- **Chrome** : Headers Sec-Ch-Ua complets
- **Firefox** : Pas de headers Sec-Ch-Ua
- **Safari** : Headers simplifiés, Accept-Language différent

## Limitations

### Templates statiques
- **Nombre limité** : Seulement 3 templates de base
- **Pas de mobile** : Pas de simulation mobile
- **Versions fixes** : Plage de versions limitée
- **Pas de personnalisation** : Templates non modifiables

### Détection possible
- **Patterns reconnaissables** : Peut être détecté par des systèmes avancés
- **Pas de comportement** : Seulement les headers, pas le comportement
- **Fingerprinting** : Vulnérable au fingerprinting avancé
- **Cohérence** : Peut manquer de cohérence avec le comportement réel

## Améliorations futures

### Nouveaux templates
- Navigateurs mobiles (Chrome Mobile, Safari Mobile)
- Navigateurs alternatifs (Edge, Opera, Brave)
- Versions historiques pour tests de compatibilité
- Templates personnalisables

### Fonctionnalités avancées
- Génération basée sur des statistiques réelles
- Simulation de comportement de navigation
- Headers contextuels (referer, cookies)
- Rotation automatique des templates

### Interface
- Interface graphique
- API REST pour intégration
- Configuration par fichier
- Base de données de templates

## Contre-mesures (détection)

### Techniques de détection
```python
# Détection d'incohérences
def detect_fake_headers(headers):
    user_agent = headers.get('User-Agent', '')
    sec_ch_ua = headers.get('Sec-Ch-Ua', '')
    
    # Vérifier la cohérence Chrome
    if 'Chrome' in user_agent and not sec_ch_ua:
        return True  # Chrome moderne devrait avoir Sec-Ch-Ua
    
    # Vérifier les versions
    if 'Firefox/200.0' in user_agent:
        return True  # Version irréaliste
    
    return False
```

### Fingerprinting avancé
- **TLS fingerprinting** : Analyse de la négociation TLS
- **HTTP/2 fingerprinting** : Ordre des headers HTTP/2
- **JavaScript fingerprinting** : Propriétés du navigateur
- **Timing analysis** : Analyse des temps de réponse

## Bonnes pratiques

### Utilisation éthique
- **Tests autorisés** : Uniquement sur vos propres systèmes
- **Documentation** : Documenter l'utilisation dans les tests
- **Rotation** : Varier les templates pour plus de réalisme
- **Contexte** : Adapter les headers au contexte d'utilisation

### Efficacité
- **Combinaison** : Utiliser avec d'autres techniques d'évasion
- **Mise à jour** : Maintenir les versions à jour
- **Validation** : Tester l'efficacité des headers générés
- **Monitoring** : Surveiller la détection

## Outils complémentaires

### Génération de trafic
- **Selenium** : Automatisation de navigateur réel
- **Playwright** : Contrôle de navigateurs modernes
- **Puppeteer** : Automatisation Chrome/Chromium
- **requests-html** : Requests avec support JavaScript

### Analyse de headers
- **Burp Suite** : Analyse et modification de headers
- **OWASP ZAP** : Proxy de sécurité
- **Wireshark** : Analyse de trafic réseau
- **curl** : Client HTTP en ligne de commande

## Sécurité et éthique

⚠️ **Utilisation responsable uniquement**
- Utilisez uniquement pour des tests autorisés
- Ne pas utiliser pour contourner des restrictions légitimes
- Respecter les termes d'utilisation des sites web
- Utiliser pour améliorer la sécurité, pas pour nuire

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Forge-Entête v1.0.0** | Créé par ozGod-sh