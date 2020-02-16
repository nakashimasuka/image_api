# image_api -> cleverdoc test technique

Api de stockage d'images dans un dossier et de récupération des informations dans un fichier csv.

Pour lancer l'api, à la racine du repo entrez:        ' python main.py '

Puis rendez-vous à l'adresse: ' http://0.0.0.0:3000/ '

Vous pouvez atteindre les pages:    ' http://0.0.0.0:3000/get/ '; 
                                    ' http://0.0.0.0:3000/get/{index}/ '; 
                                    ' http://0.0.0.0:3000/get/{index}/image/ ';
                                    ' http://0.0.0.0:3000/refresh/ '

Si une erreur apparait, allez à l'adresse 'http://0.0.0.0:3000/refresh' puis réessayez.
Si le fichier file.csv est supprimé, allez à l'adresse 'http://0.0.0.0:3000/refresh' et il sera recréer.

L'adresse 'http://0.0.0.0:3000/get/{index}/image' est pas fonctionnelle à 100%, je n'arrive pas à renvoyer l'image en json.

Je tiens à préciser que créer une api en python avec flask est une première pour moi. J'ai donc travaillé 2h samedi afin de me familiariser avec cet environement.
