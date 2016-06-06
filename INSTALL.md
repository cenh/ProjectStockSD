## Kør Project Stock webapplikationen lokalt
### Installer afhængigheder
`sudo apt-get install libmysqlclient-dev python-dev python-pip # (Ubuntu/Debian)`

`sudo yum install mariadb-devel python-devel python-pip # (RedHat/CentOS)`

Installer Django og mysqlclient med pip

`sudo pip install django mysqlclient`

### Kør serveren
Skift mappe til project_stock (mappen der indeholder manage.py)

`cd project_stock`

Kør følgende kommando i en terminal:

`python manage.py runserver`

### Åben siden
Navigér til http://127.0.0.1:8000/ i en browser på samme maskine

### Kør unit tests (valgfrit)
Kør følgende kommando i en terminal:

`python manage.py test --settings=project_stock.test_settings`