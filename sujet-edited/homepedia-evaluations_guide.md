---
subtitle:   Evaluations guide
author:     
version:    0.1.0
---

## Actions pour évaluer

- Demander au groupe de lancer l'application et de naviguer jusqu'à une visualisation cartographique, sans préparation préalable.

- Demander la liste des sources collectées et compter les sources distinctes : vérifier qu'elles sont au moins douze et au plus cinquante.

- Demander à voir au moins une source textuelle et la façon dont elle a été traitée, pas seulement stockée.

- Demander le schéma des bases de données et le faire commenter table par table, puis collection par collection.

- Se connecter à la base relationnelle, lancer une requête sur une table volumineuse, observer le temps de réponse et demander quels index sont en place.

- Se connecter à la base non relationnelle et demander pourquoi cette donnée n'est pas stockée dans la base relationnelle.

- Demander de lancer un traitement Spark ou Hadoop en direct, puis d'ouvrir l'interface de suivi du cluster pour constater la répartition sur plusieurs nœuds.

- Demander à voir le code de nettoyage des données et faire dérouler le traitement d'une valeur aberrante ou manquante identifiée.

- Dans l'application, changer le niveau de granularité (ville, département, région) et vérifier que les chiffres restent cohérents d'un niveau à l'autre.

- Trier puis filtrer un tableau d'indicateurs, et demander si un export des données affichées est possible.

- Choisir une carte affichée et demander pourquoi ce type de représentation a été retenu plutôt qu'un autre.

- Sélectionner une zone sans données ou appliquer un filtre vide, et observer comment l'application réagit.

- Demander à voir la trace complète d'un indicateur affiché, depuis la source brute jusqu'à l'écran.

---

## Questions & réponses pour tester la compréhension

### Collecte et sources de données

- Quels critères ont guidé le choix de vos sources ?

  Attendre des critères explicites : couverture territoriale, fraîcheur, granularité disponible, licence d'utilisation, stabilité du format. Une réponse qui se limite à la facilité d'accès est insuffisante.

- Quelle est la différence entre une donnée ouverte et une donnée simplement accessible en ligne ?

  Une donnée ouverte est publiée sous une licence qui en autorise explicitement la réutilisation. Une donnée accessible peut rester protégée par des conditions d'utilisation qui interdisent la collecte automatisée ou la rediffusion.

- Comment avez-vous identifié qu'une même commune est décrite par deux sources différentes ?

  Par une clé de rapprochement stable, typiquement le code INSEE, plutôt que par le nom de la commune. Les noms sont ambigus, orthographiés différemment et parfois partagés entre plusieurs communes.

- Que faites-vous lorsque deux sources se contredisent sur un même indicateur ?

  Attendre une règle d'arbitrage documentée : priorité à la source de référence, à la plus récente, ou conservation des deux valeurs avec leur provenance. Choisir silencieusement l'une des deux est un défaut de traçabilité.

- Comment avez-vous géré les sources dont la mise à jour est irrégulière ?

  Attendre un horodatage de la collecte, la conservation de la date de validité de la donnée, et une distinction claire entre la date de la mesure et la date de récupération.

- Quelles précautions avez-vous prises lors de la collecte automatisée sur un site tiers ?

  Lecture des conditions d'utilisation, limitation du rythme des requêtes, identification de l'agent, et préférence donnée aux jeux de données publics quand ils existent. Le contexte académique ne dispense pas de la vigilance.

- Comment relanceriez-vous votre collecte complète dans six mois ?

  Attendre un processus reproductible : scripts versionnés, paramètres externalisés, journalisation des erreurs. Une collecte réalisée à la main une seule fois ne se rejoue pas.

### Organisation des bases de données

- Pourquoi avoir retenu une base relationnelle pour certaines données et une base non relationnelle pour d'autres ?

  Le relationnel convient aux données tabulaires régulières, fortement liées, interrogées par jointures. Le non relationnel convient aux données hétérogènes, imbriquées ou de schéma variable, comme les avis textuels.

- Quel modèle non relationnel avez-vous choisi, et pourquoi correspond-il à votre donnée ?

  Attendre une justification par la forme de la donnée : document pour des avis de structure variable, clé-valeur pour un accès direct, graphe pour des relations territoriales. Le nom du moteur ne suffit pas comme réponse.

- À quoi sert un index, et quel est son coût ?

  Un index accélère la recherche en évitant le parcours complet de la table. Il coûte de l'espace disque et ralentit les écritures, puisqu'il doit être maintenu à chaque insertion ou mise à jour.

- Comment avez-vous choisi vos clés d'indexation communes entre les sources ?

  Attendre une clé stable, unique et présente dans la majorité des sources, typiquement un code territorial officiel, complétée par une table de correspondance pour les sources qui ne la portent pas.

- Qu'est-ce que la normalisation, et dans quel cas avez-vous choisi de dénormaliser ?

  La normalisation supprime la redondance en éclatant les données en tables liées. La dénormalisation réintroduit volontairement de la redondance pour éviter des jointures coûteuses en lecture, ce qui se justifie sur les données servies à l'application.

- Comment garantissez-vous qu'une même commune porte le même identifiant dans toutes vos tables ?

  Par une table de référence des territoires alimentée en premier, à laquelle toutes les autres tables se rattachent par clé étrangère ou par contrôle applicatif au moment du chargement.

- Que faudrait-il changer si le volume de données était multiplié par cent ?

  Attendre une réflexion sur le partitionnement, l'archivage des données froides, le pré-calcul des agrégats et la séparation entre la base de traitement et la base servant l'application.

### Traitement distribué et big data

- Qu'apporte un moteur distribué comme Spark par rapport à un traitement sur une seule machine ?

  La répartition du calcul et de la mémoire sur plusieurs machines, ce qui permet de traiter des volumes qui ne tiennent pas sur un seul poste, et de réduire le temps de traitement par parallélisation.

- Quelle est la différence entre une transformation et une action ?

  Une transformation décrit un calcul sans l'exécuter, elle construit un plan. Une action déclenche l'exécution de ce plan et produit un résultat. C'est ce qui explique qu'un enchaînement de transformations semble instantané.

- Pourquoi un traitement distribué peut-il être plus lent qu'un traitement local sur un petit volume ?

  Le coût fixe de distribution, de sérialisation et d'échange réseau entre les nœuds dépasse le gain de parallélisation quand la donnée est petite.

- Qu'est-ce qu'un shuffle, et pourquoi cherche-t-on à le limiter ?

  Une redistribution des données entre les nœuds, provoquée par les opérations qui regroupent par clé. Elle implique des écritures disque et du trafic réseau, ce qui en fait le poste de coût dominant de nombreux traitements.

- Comment le travail se répartit-il entre les nœuds de votre cluster ?

  Attendre une explication du découpage en partitions et de leur affectation aux exécuteurs, ainsi que la conscience qu'une répartition déséquilibrée laisse des nœuds inactifs pendant qu'un seul termine.

- Que se passe-t-il si un nœud tombe pendant un traitement ?

  Le moteur recalcule les partitions perdues à partir du plan d'exécution, sur les nœuds restants. La tolérance aux pannes est obtenue par recalcul, pas par réplication du résultat intermédiaire.

- Quelle étape de votre pipeline est le goulot d'étranglement, et comment l'avez-vous mesuré ?

  Attendre une mesure, pas une intuition : durée par étape relevée dans l'interface de suivi, ou instrumentation du code. Une réponse sans chiffre indique que le pipeline n'a jamais été profilé.

### Analyse textuelle et intelligence artificielle

- Quelle information avez-vous extraite de vos données textuelles, et en quoi est-elle exploitable ?

  Attendre un indicateur agrégeable et croisable avec le reste des données, par exemple un score de satisfaction par commune, et non une simple restitution des avis.

- Comment transforme-t-on un texte libre en une donnée utilisable par un calcul ?

  Par une chaîne de traitement : nettoyage, découpage en unités, puis représentation numérique du texte, par comptage de termes ou par vecteurs appris. Le calcul porte ensuite sur cette représentation.

- Sur quoi repose l'analyse de sentiment que vous utilisez, et quelles sont ses limites ?

  Attendre la distinction entre approche par dictionnaire et approche par modèle appris. Limites communes : ironie, négation, vocabulaire spécifique au domaine, textes courts ou multilingues.

- Comment savez-vous que le résultat de votre analyse textuelle est fiable ?

  Par une évaluation sur un échantillon annoté à la main, même petit. Sans comparaison à une vérité de référence, la fiabilité est une conviction et non une mesure.

- Quels biais peut porter un corpus d'avis rédigés par des habitants ?

  Biais de participation : les avis extrêmes sont surreprésentés. Biais géographique et générationnel selon qui utilise la plateforme. Biais temporel si les avis anciens ne sont jamais retirés.

- Pourquoi ne suffit-il pas d'afficher les commentaires bruts dans l'application ?

  Parce que le sujet demande une donnée traitée. Un commentaire brut n'est ni comparable, ni agrégeable, ni croisable avec un indicateur chiffré : il ne produit aucune analyse.

- Si vous utilisez un modèle pré-entraîné, sur quelles données a-t-il été entraîné et pourquoi cela compte ?

  Attendre la conscience que le domaine et la langue d'entraînement conditionnent la qualité des résultats. Un modèle entraîné sur des avis produits commerciaux se comporte mal sur des avis de villes.

### Visualisation et application interactive

- Qu'est-ce que le chartjunk, et pouvez-vous en montrer un exemple que vous avez retiré ?

  Tout élément graphique qui n'apporte pas d'information : effets de volume, dégradés décoratifs, grilles trop denses, axes redondants. Attendre un exemple concret issu de leurs propres itérations.

- Comment choisissez-vous entre une carte choroplèthe et une carte à symboles proportionnels ?

  La choroplèthe convient aux données relatives, rapportées à une surface ou à une population. Les symboles proportionnels conviennent aux valeurs absolues, qui seraient trompeuses si on les coloriait par territoire.

- Pourquoi une carte choroplèthe peut-elle induire en erreur sur des territoires de tailles très inégales ?

  Parce que l'œil pondère l'information par la surface. Un département vaste et peu peuplé occupe visuellement plus de place qu'une métropole dense, ce qui fausse la perception du phénomène.

- Comment avez-vous choisi vos classes de couleurs et vos bornes de discrétisation ?

  Attendre une méthode assumée : quantiles, seuils naturels, intervalles égaux, et la conscience que changer la méthode change la carte. Une palette par défaut non questionnée est un signal faible.

- Qu'est-ce qui change dans la lecture d'un indicateur selon qu'il est affiché à l'échelle de la ville ou de la région ?

  L'agrégation masque la dispersion interne. Une moyenne régionale peut cacher des écarts communaux importants, ce qui rend la conclusion dépendante du niveau choisi.

- Comment votre application reste-t-elle réactive quand la donnée affichée est volumineuse ?

  Attendre des mécanismes explicites : agrégats pré-calculés, chargement partiel, simplification des géométries, mise en cache. Recalculer l'ensemble à chaque interaction ne tient pas à l'échelle.

- Qui est l'utilisateur cible de votre application, et quelle décision doit-il pouvoir prendre après l'avoir utilisée ?

  Attendre un utilisateur professionnel identifié, agence immobilière, collectivité ou analyste, et une décision concrète. Une réponse centrée sur le particulier en recherche de logement montre que le cadrage du sujet a été manqué.
