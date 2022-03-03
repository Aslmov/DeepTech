Ce projet est une plateforme en ligne pour le groupe Deeptech.

Les technologies utilise pour le developpement du site sont reactjs dans le cote front-end et djongo dans le cote back-end

Pour installer le projet et le run il faut:

Installer python version 3.9 ou superieur: [python](https://www.python.org/downloads/)

Installer pip:

`` python -m pip install --upgrade pip ``

Installer ensuite django 

`` pip install django ``

En cas de probleme copier cette commande

`` pip install -u django ``

Ensuite installer djangorestframework et django-cors-headers

`` pip install djangorestframework django-cors-headers ``

Installer egalement [Nodejs](https://nodejs.org/en/)

Puis installer le projet:

`` git clone https://github.com/AIDaft/DeepTech.git ``

Mais attention si vous compter travailler sur une branch en particulier faites un git clone depuis cette branch

Dans le repetoire du projet effectuer une migration

`` py manage.py migrate ``

Maintenant executer le projet:

Pour le server

`` py manage.py runserver ``

apres ouvrer un nouveau cmd, aller dans le repetoire du projet et maintenant changer de repetoire vers le dossier frontend et executer cette commande:

`` npm i ``

`` npm start ``

Taper ensuite dans votre navigateur:

`` localhost:3000 ``

Et voila vous pouvez commencer a travailler






