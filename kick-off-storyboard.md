# Homepedia — Storyboard du Kick-off (proposition v1)

> Document de travail. On itère ici sur **le contenu et l'ordre** ; on ne fabrique les
> slides qu'une fois ce plan validé.
>
> **Légende des sources fusionnées :** `[PPTX]` = deck actuel · `[PDF]` = sujet détaillé ·
> `[NOTES]` = ta note `programme kick-off.txt` · `[NEW]` = ajout proposé.
>
> **Cible :** MSc2, kick-off de 3h30 (14:00–17:30). Le deck n'occupe pas les 3h30 :
> ~40–50 min de présentation, le reste = discussion, choix de thématique, démarrage.
> Objectif du deck : qu'à la sortie, chaque groupe **sache quoi construire, pour qui,
> avec quelles données, et comment il sera évalué** — et ait déjà une piste de thématique.

---

## Fil narratif (6 actes)

| Acte | Question à laquelle on répond | Slides |
|------|-------------------------------|--------|
| 0. Ouverture | Où va-t-on cet après-midi ? | 1–2 |
| 1. Le sens (POURQUOI) | À quoi sert l'app qu'on va construire ? | 3–6 |
| 2. Choisir sa thématique | Quel problème vais-je résoudre ? | 7–9 |
| 3. La donnée | Où je trouve la donnée et comment je la collecte proprement ? | 10–13 |
| 4. La technique | Qu'est-ce qu'on attend techniquement ? | 14–16 |
| 5. Le cadre | Comment je serai évalué, en combien de temps ? | 17–19 |
| 6. Démarrer | Par quoi je commence maintenant ? | 20–22 |

---

## ACTE 0 — Ouverture

### Slide 1 — Couverture
- **Titre :** Homepedia — Big Data Immobilier
- **Sous-titre :** Explorer et expliquer le marché immobilier en France
- *Note :* on parle d'**immobilier** (résidentiel *et* commercial/tertiaire), pas seulement
  de « logement » — ça couvre aussi les problématiques type implantation d'une salle de sport,
  d'un commerce, de bureaux.
- Visuel : celui du PPTX actuel (maquettes maisons + datacenter). `[PPTX]`

### Slide 2 — Au programme cet après-midi `[NEW]`
- **Objectif :** poser le déroulé, rassurer sur le fait qu'ils repartiront avec un plan.
- Le sens du projet → Choisir sa thématique → La donnée → La technique → L'évaluation → On démarre
- 1 ligne : « À la fin, chaque groupe repart avec une thématique et 3 sources identifiées. »

---

## ACTE 1 — Le sens (POURQUOI)

### Slide 3 — Big Data 101 (condensé) `[PPTX]`
- **Objectif :** contexte rapide, ne pas s'attarder.
- Les V : **Volume · Variety · Velocity** (+ Veracity, Value).
- 2,5 trillions d'octets créés / jour.
- ⚠️ *Décision à prendre :* on garde « Velocity » ? Le projet Homepedia est surtout **batch**
  (le temps réel est un **bonus**). Je propose de mettre l'accent sur **Volume + Variety**
  et de dire explicitement « temps réel = bonus » pour éviter la confusion. `[NEW]`

### Slide 4 — ⭐ LE BUT DE L'APP (slide-clé demandée) `[NEW]` + `[PDF]`
- **Objectif :** LA slide qui répond à « c'est quoi le point, qu'est-ce qu'on cherche à expliquer ».
- Formulation proposée (à affiner ensemble) :
  > **Vous ne construisez pas un site d'annonces immobilières.**
  > Vous construisez un **outil d'aide à la décision** sur le **marché immobilier** qui
  > *explique* le territoire : pourquoi les prix, les inégalités, les risques varient
  > d'un endroit à l'autre — et ce qu'on peut en anticiper.
- 3 verbes : **Collecter → Croiser → Expliquer** (pas seulement « afficher »).
- Phrase d'ancrage `[PDF]` : *« Make data easy to capture, parse, analyse… serve quality
  visualizations from which insights will be extracted. »*

### Slide 5 — Pour qui ? (utilisateurs = décideurs) `[PDF]`
- **Objectif :** corriger définitivement l'ambiguïté particulier/pro.
- **Utilisateurs = professionnels & décideurs** : agences, collectivités, analystes de
  grandes entreprises. **Pas** le particulier qui cherche un logement.
- Ce que ça change : on optimise pour **comprendre et décider**, pas pour « visiter des biens ».

### Slide 6 — Les grandes questions auxquelles l'app répond `[PDF]` + `[NOTES]`
- **Objectif :** rendre le but concret par des questions réelles.
- Exemples PDF :
  - « Comment réduire les inégalités dans mon département ? »
  - « Quels risques d'investir ici liés au réchauffement à 15 ans ? »
  - « Où implanter mes 10 prochaines franchises ? »
- Exemple NOTES : « Comment se situe cette localité (quartier / ville / département)
  par rapport à la **moyenne nationale** ? »

---

## ACTE 2 — Choisir sa thématique

### Slide 7 — Choisis ta thématique (1/2) : les familles de sujets `[NEW]` + `[NOTES]`
- **Objectif :** donner un menu de directions, pas une seule.
- 6 familles proposées (chacune = un angle d'app) :
  1. **Inégalités territoriales** & mixité sociale
  2. **Risque climatique & immobilier** (exposition, assurabilité à 10–15 ans)
  3. **Stratégie d'implantation** (franchises, commerces, services publics)
  4. **Attractivité & dynamique** d'un territoire (flux entrants/sortants, gentrification)
  5. **Investissement & rendement** locatif
  6. **Qualité de vie & accès aux services** (soins, éducation, transports)
- Consigne : « Choisissez-en **une** comme fil rouge. »

### Slide 8 — Choisis ta thématique (2/2) : exemples de problématiques `[NEW]`
- **Objectif :** montrer à quoi ressemble une bonne problématique (qui se répond avec de la donnée croisée).
- Quelques exemples travaillés (2–3 par famille), ex. :
  - *Inégalités :* « Quelles communes décrochent le plus vite par rapport à la moyenne nationale ? »
  - *Climat :* « Quelles zones cumulent hausse des prix ET exposition croissante aux catastrophes ? »
  - *Implantation :* « Où ouvrir une salle de sport : densité, revenu, âge médian, concurrence ? »
  - *Attractivité :* « Quels territoires deviennent attractifs avant que les prix ne montent ? »
- ⚠️ À remplir ensemble — dis-moi si tu veux 1 ou 2 exemples par famille.

### Slide 9 — Enrichir l'analyse : variables explicatives `[NOTES]`
- **Objectif :** leur donner des « ingrédients » pour croiser (répond à ta liste de la note).
- Regroupées par domaine :
  - **Économie :** PIB/hab, taux de chômage, revenu médian, taux de pauvreté
  - **Démographie :** âge moyen, densité, **solde migratoire** (entrants − sortants) + son évolution
  - **Santé / services :** accès aux soins (densité de médecins), espérance de vie
  - **Bâti / énergie :** **classe énergétique (DPE)**, ancienneté du bâti
  - **Climat / risque :** tendance des températures (20 ans), catastrophes naturelles, **coût des assurances**
  - **Société :** résultats/participation électorale (⚠️ à manier avec précaution & éthique), tourisme
- Message : « Le prix **seul** n'explique rien. La valeur du projet, c'est le **croisement**. »

---

## ACTE 3 — La donnée

### Slide 10 — Le pipeline attendu (vue d'ensemble) `[PDF]`
- **Objectif :** montrer les 4 étapes obligatoires d'un coup.
- **Collecte → Organisation (BDD) → Traitement Big Data → Visualisation interactive**
- 1 ligne chacune. C'est la colonne vertébrale du reste du deck.

### Slide 11 — Où trouver la donnée : sources & API `[NOTES]` + `[NEW]`
- **Objectif :** les faire démarrer vite (ta demande explicite de liens).
- Présenté par thème, avec le type (fichier / API / open data).
- **Liste détaillée en Annexe A** (à vérifier ensemble avant de figer).
- Règle du sujet `[PDF]` : **12 à 50 sources**, dont **au moins 1 textuelle**, couvrant
  **état / région / département / ville**.

### Slide 12 — La source textuelle (obligatoire) `[PDF]` + `[PPTX]`
- **Objectif :** insister sur l'exigence la moins comprise.
- Il faut **traiter** le texte (sentiment / thèmes), pas juste l'afficher.
- Exemple d'accroche PDF : *« Combien de fois le mot “rats” apparaît-il dans les avis
  des restaurants de cette zone ? »*
- Pistes de corpus textuel : avis de communes (villesavivre.fr), descriptions Wikipédia,
  forums, presse locale. → doit devenir un **indicateur** (ex. score de satisfaction / commune).

### Slide 13 — Collecte responsable `[NOTES]` + `[PDF]`
- **Objectif :** sensibilisation légale/éthique.
- Donnée **ouverte** ≠ donnée simplement **accessible** en ligne.
- Lire les CGU, limiter le rythme des requêtes, privilégier l'open data (INSEE, data.gouv).
- Le contexte académique **ne dispense pas** de la vigilance.

---

## ACTE 4 — La technique

### Slide 14 — Architecture des bases `[PDF]` + `[PPTX]`
- **Relationnel + NoSQL** obligatoires : tabulaire régulier vs hétérogène/textuel.
- Schéma expliqué, **clés communes** (code INSEE, pas le nom de commune !), indexation.

### Slide 15 — Traitement distribué `[PDF]` + `[PPTX]`
- **Spark / Hadoop** sur **cluster multi-nœuds** (pas une seule machine).
- Nettoyage documenté, ≥ 3 analyses tirées du pipeline.
- ⚠️ *Action pédago :* dire concrètement **comment ils accèdent au cluster**
  (Databricks free / tokens campus / VMs locales). À trancher avant le kick-off.

### Slide 16 — Restituer : tables + cartes + interactivité `[PDF]` + `[PPTX]`
- **Tables** triables/filtrables, exportables.
- **Cartes** (choroplèthe / bulles / chaleur…) aux 3 échelles (ville/dépt/région).
- **App interactive** qui lit la base (pas de fichiers statiques), l'utilisateur sélectionne
  zones & indicateurs. Éviter le **chartjunk**.

---

## ACTE 5 — Le cadre

### Slide 17 — Comment vous serez évalués (6 axes /30) `[grading_scale]`
- Reprise de la slide déjà construite : Collecte /5 · Bases /5 · Traitement /5 ·
  Textuel /4 · Visualisation /6 · Application /5 → **/30 + bonus**.

### Slide 18 — Modalités & organisation `[NEW]`
- Projet **en groupe (3–4 pers. — à confirmer)**, éval finale « point de vue client »,
  livrables (app déployée + code + config + schéma BDD + doc archi).

### Slide 19 — Calendrier `[NOTES/EDT]`
- 14 sept Kick Off · 25 sept FU 1/3 · 20 nov FU 2/3 · 8 janv FU 3/3 · 12 févr Keynote finale.

---

## ACTE 6 — Démarrer

### Slide 20 — Ils l'ont déjà fait : inspiration `[PPTX]`
- Gapminder · villesavivre.fr · data.ameli (Data pathologies) · Numbeo · meilleursagents.
- Message : « Inspirez-vous, **ne copiez pas**. »

### Slide 21 — Aller plus loin : bonus `[PDF]`
- Autres pays, déploiement en ligne, authentification, **temps réel**, admin, tour guidé.

### Slide 22 — Vos 2 premières heures `[NEW]`
- **Objectif :** anti-page-blanche, action immédiate.
- 1) Choisir une thématique · 2) Lister 3 sources (dont 1 textuelle) · 3) Croquis de l'app ·
  4) Répartir les rôles. → Puis Q&R.

---

## Annexe A — Sources de données & API

> **Deux niveaux :** ✅ = endpoint **testé en live le 10/09/2026, renvoie bien du JSON/CSV** ·
> ◻️ = source connue à confirmer au moment de figer les slides.
> La plupart des exemples ✅ sont **sans clé d'API** — parfaits pour démarrer vite.

### A.1 — Testées aujourd'hui (URL copiables) ✅

**🌡️ Météo / climat — Open-Meteo (JSON ou CSV, sans clé)**
Historique complet (réanalyse ERA5, depuis 1940), idéal pour « tendance des températures sur 20 ans » :
```
https://archive-api.open-meteo.com/v1/archive?latitude=48.85&longitude=2.35&start_date=2004-01-01&end_date=2024-12-31&daily=temperature_2m_mean
```
→ ajouter `&format=csv` pour du CSV. *(testé : renvoie 13.3 / 9.8 / 7.7 °C…)*
Alternative officielle FR : Météo-France via `meteo.data.gouv.fr` (fichiers CSV).

**💶 PIB / habitant — Eurostat (JSON-stat, sans clé)**
PIB par habitant au niveau **région** (NUTS2), pratique aussi pour le bonus « autres pays » :
```
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gdp?format=JSON&unit=EUR_HAB&geo=FR10&time=2021
```
→ *(testé : 59 400 €/hab pour l'Île-de-France en 2021)*. Enlever `geo=`/`time=` pour tout récupérer.
Pour du **local FR** (commune/EPCI) : INSEE **Melodi** `https://api.insee.fr/melodi/` (JSON ;
catalogue : `https://api.insee.fr/melodi/V2/catalog/dcat`).

**🗺️ Découpage géographique — API Géo (JSON/GeoJSON, sans clé)**
Communes, départements, régions + contours (pour les cartes) :
```
https://geo.api.gouv.fr/departements?fields=nom,code,codeRegion
https://geo.api.gouv.fr/communes?codeDepartement=75&fields=nom,code,population,centre
```
→ *(testé : renvoie les 96+ départements en JSON)*. Ajouter `&format=geojson&geometry=contour` pour les tracés.

**🌊 Risques naturels — Géorisques API v1 (JSON, sans token)**
Arrêtés catastrophe naturelle (inondation, sécheresse…) par code INSEE, pour la thématique « risque climatique » :
```
https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=30007&page_size=20
```
→ *(testé, sans jeton en v1)*. Beaucoup d'autres endpoints (aléas, retrait-gonflement argiles, etc.).

**⚡ Classe énergétique (DPE) — ADEME data-fair (JSON, sans clé)**
15,5 M de diagnostics ; champs `etiquette_dpe`, `nom_commune_ban`, `code_postal_ban`… :
```
https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines?size=20&q=Carcassonne
```
→ *(testé : renvoie des logements avec étiquette C/GES A…)*. Export CSV via `&format=csv`.

### A.2 — À confirmer ensemble ◻️

**🏠 Immobilier / prix (le cœur du sujet) — DVF**
- Fichiers **CSV géolocalisés** prêts à charger : `files.data.gouv.fr/geo-dvf/latest/csv/` (par année & département). ◻️
- Micro-API JSON (POC, non garantie) : `api.cquest.org/dvf?code_commune=…` ◻️
- Explorateur officiel : `app.dvf.etalab.gouv.fr` ◻️

**📮 Adresses / géocodage — BAN**
- `https://api-adresse.data.gouv.fr/search/?q=…` (JSON) · géocodage **CSV en masse** via `/search/csv/`. ◻️

**👥 Emploi / social**
- France Travail open data (`francetravail.io`, datasets CSV sur `data.gouv.fr`) · API Marché du travail. ◻️
- data.ameli (`data.ameli.fr`, « Data pathologies ») · accès aux soins DREES (indicateur APL). ◻️

**🏫 Éducation** — `data.education.gouv.fr` (établissements, résultats). ◻️
**🗳️ Élections (bord politique — ⚠️ éthique)** — résultats Min. Intérieur via `data.gouv.fr`. ◻️
**🌍 POI / commerces (concurrence, implantation)** — OpenStreetMap Overpass API + Nominatim. ◻️

**💬 Textuel (≥ 1 source obligatoire)**
- villesavivre.fr (avis de communes) · Wikipédia / Wikidata (descriptions) · presse locale / forums (⚠️ CGU) ·
  Numbeo (qualité de vie, ⚠️ CGU). ◻️

### A.3 — Les 2 patterns génériques à leur apprendre
Beaucoup de portails open data FR exposent **automatiquement** une API. Reconnaître ces 2 formes
débloque des **centaines** de jeux de données :
- **OpenDataSoft** (Explore API v2.1) : `…/api/explore/v2.1/catalog/datasets/<id>/records?…` (JSON)
  et `…/exports/csv` (CSV).
- **data-fair** (ADEME & co.) : `…/data-fair/api/v1/datasets/<id>/lines?…` (JSON) + `&format=csv`.

---

## Décisions ouvertes (à trancher avant fabrication)

1. **Format final** — options :
   - **A. Reveal.js / HTML** (Markdown → 1 fichier `.html`) : s'ouvre dans Safari sans logiciel,
     export PDF facile, 100 % Mac-friendly, je contrôle le design. *(recommandé)*
   - **B. Keynote `.key`** : natif Mac mais je ne peux pas le générer directement
     (il faudrait passer par un import pptx, perte de fidélité).
   - **C. PPTX** : je le génère bien, Keynote l'importe, mais c'est ce que tu veux éviter.
   - **D. PDF** : universel mais non éditable.
2. **Nombre d'exemples** par famille de thématique (slide 8) : 1 ou 2 ?
3. **Slide « Velocity »** : on assume que le temps réel est un bonus ? (je le recommande)
4. **Taille des groupes** : 3–4 ? autre ?
5. **Accès au cluster** (slide 15) : quelle solution annonces-tu ?
6. Faut-il **découper** la présentation en 2 (avant/après une pause) ?
