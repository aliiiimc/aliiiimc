# Midnight Jazz — installation du profil @aliiimc

## 1. Créer le dépôt spécial

Sur https://github.com/new crée un dépôt **public** intitulé exactement `aliiimc`, sous le compte `aliiimc`.

Si le dépôt existe déjà, utilise-le à la place (préserve d'abord son contenu).

## 2. Copier les fichiers

Transfère `README.md`, `assets/midnight-jazz.gif` et `.github/workflows/snake.yml` dans le dépôt. Tu peux également transférer `assets/midnight-jazz-preview.png` (aperçu) et `INSTALLATION.md` (documentation).

Attention : `.github/workflows/` est un dossier caché. Conserve son nom exact.

En local via Git :

```bash
git clone https://github.com/aliiimc/aliiimc.git
cd aliiimc
# Copie les fichiers du kit ici en conservant les dossiers.
git add README.md assets .github/workflows/snake.yml INSTALLATION.md
git commit -m "Create midnight jazz pixel art profile"
git push
```

## 3. Activer GitHub Actions

Dans le dépôt, vérifie que `Settings > Actions > General` autorise les actions. Sous `Workflow permissions`, autorise `Read and write permissions` si nécessaire. Ensuite, dans l'onglet `Actions`, ouvre `Midnight Jazz Contribution Snake` > `Run workflow`.

Le workflow pousse des SVG sur une branche `output`. La section serpent du README ne fonctionnera qu'après sa première exécution réussie. Le workflow se déclenche ensuite chaque jour (le cron UTC peut être retardé par GitHub).

Si une politique de sécurité de l'organisation empêche `crazy-max/ghaction-github-pages`, remplace l'étape de publication par une action autorisée.

## 4. Personnaliser

- Remplace les descriptions des projets et compétences par tes compétences réelles.
- Modifie les icônes `skillicons.dev` selon tes langages.
- Remplace les badges statistiques externes si un prestataire refuse de servir l'image ou atteint ses limites.
- Le fichier `assets/midnight-jazz.gif` est une vraie animation autonome, sans script côté GitHub.
- Les cartes de statistiques externes ne sont pas garanties disponibles 24/7 : elles dépendent de services tiers.

## 5. Modifier l'animation

Le script source `build_jazz.py` (fourni dans le kit) génère les images. Il utilise Python 3 et Pillow (`pip install pillow`). Exécute-le depuis n'importe quel dossier : `python build_jazz.py`. Il remplace les images de `assets/` dans le dossier du kit en utilisant le chemin configuré dans le script. Tu peux adapter couleurs, formes, texte et trajectoires des notes de musique.

## Notes

Le fichier GIF comporte 32 images à 110 ms/image (~3,5 secondes en boucle). Les animations du GIF sont indépendantes de GitHub Actions. La Snake GitHub est la seule animation du kit qui dépend d'une exécution sur GitHub.
