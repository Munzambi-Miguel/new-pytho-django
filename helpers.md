## Munzambi Miguel 

hoje vamos aprender como iniciar um projecto django no entanto para criação de um primeiro projeto temos 
o seguinte comando:

````python

    py -m django startproject demopython

    py manage.py help
    py manage.py help
    py manage.py help

    # Permite correr as migrates na base de dados
    py manage.py migrate

    # Permite iniciar o project
    python manage.py runserver

    # instalando o python
    py -m pip install django


    pip freeze > requirements.txt


````

````
Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
````