# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import random
import json

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🛠️  Forge-Entête v{VERSION}                                  ║
║                                                              ║
║  Générateur d'en-têtes HTTP réalistes.                      ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

# Dictionnaire de templates d'en-têtes
HEADER_TEMPLATES = {
    'chrome_windows': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="{version}", "Chromium";v="{version}"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"'
    },
    'firefox_linux': {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    },
    'safari_macos': {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-fr',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
}

def generate_headers(template_name):
    """Génère un dictionnaire d'en-têtes basé sur un template et randomise la version."""
    if template_name not in HEADER_TEMPLATES:
        return None
    
    template = HEADER_TEMPLATES[template_name].copy()
    headers = {}

    # Randomisation des versions pour plus de réalisme
    chrome_version = random.randint(105, 115)
    firefox_version = random.randint(100, 110)

    for key, value in template.items():
        if '{version}' in value:
            if 'chrome' in template_name:
                headers[key] = value.format(version=chrome_version)
            elif 'firefox' in template_name:
                 headers[key] = value.format(version=firefox_version)
        else:
            headers[key] = value
            
    return headers

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Génère des en-têtes HTTP réalistes à partir de templates.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("-l", "--list", action="store_true", help="Lister tous les templates disponibles.")
    parser.add_argument("-t", "--template", help="Le nom du template à utiliser (ex: chrome_windows).", choices=HEADER_TEMPLATES.keys())
    parser.add_argument("-o", "--output", help="Format de sortie.", choices=['raw', 'json'], default='raw')

    args = parser.parse_args()

    if args.list:
        print("[*] Templates disponibles:")
        for name in HEADER_TEMPLATES:
            print(f"  - {name}")
        return

    if not args.template:
        parser.print_help()
        return

    headers = generate_headers(args.template)
    if not headers:
        print(f"[!] Erreur: Le template '{args.template}' est introuvable.")
        return

    print(f"\n[*] En-têtes générés avec le template '{args.template}':\n")
    if args.output == 'json':
        print(json.dumps(headers, indent=2))
    else:
        for key, value in headers.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
