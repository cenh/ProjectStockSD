# ProjectStockSD

Velkommen til vores Project Stock repository!

## Indholdsfortegnelse
* [TODO](https://github.com/cenh/ProjectStockSD#todo)
* [Kør Serveren Lokalt](https://github.com/cenh/ProjectStockSD#kør-serveren-lokalt)
* [Migrations på serveren](https://github.com/cenh/ProjectStockSD#migrations-på-serveren)
* [Git tips](https://github.com/cenh/ProjectStockSD#git-tips)
* [Diverse materiale](https://github.com/cenh/ProjectStockSD#materiale)
* [HTML Tags](https://github.com/cenh/ProjectStockSD#html-tags---ansatte)
* [DIKU Test Server Links](https://github.com/cenh/ProjectStockSD#diku-test-server-links)

## Kør serveren lokalt
### Installer afhængigheder
`[sudo] apt-get install libmysqlclient-dev python-dev # eller den tilsvarende kommando for din distribution`

`[sudo] pip install mysqlclient`

### Skift til debug mode
I filen `project_stock/project_stock/settings.py` erstat `Debug = False` med `Debug = True` (husk at den ikke skal pushes medmindre I laver andre relevante ændringer; Debug SKAL være False på webserveren).

### Login-fil
Filen `project_stock/project_stock/config.cnf` skal have følgende format:

`[client]`

`database = "database"`

`user = "username"`

`password = "password"`

`host = "128.199.39.136"`

`default-character-set = "utf8"`

Indstillingerne skal udfyldes manuelt (spørg efter dem), og husk, at denne fil heller ikke skal pushes til Github, da passwords kun skal være på webserveren og testmaskinerne.

### Kør serveren
Skift mappe til project_stock Django projektet og kør:

`python manage.py runserver`

## Migrations på serveren
### Log ind som root
`sudo -i`

### Lav migrations project_stock
`python manage.py makemigrations`

`python manage.py migrate`

### Fortryd migrations
`python manage.py squashmigrations 'app-navn' 'migration-nr'`
#### Eksempel 
`python manage.py squashmigrations projects 0004`

### Genstart serveren
`systemctl restart httpd mariadb` eller CTRL-C + `python manage.py runserver`

## Git Tips
### Se forskellen på HEAD (nyeste commit) og de *n* seneste commits:

`git diff HEAD~n HEAD [fil]`

## Materiale

Liste over forskellige materiale og evt. relevant information.

### Liste over ansatte på diku

[DIKU Ansatte](http://diku.dk/Ansatte/)

### Liste over projekter for studerende

[Erhvervsportal](http://diku.dk/diku_business_club/erhvervsportal/studerende/)

### HTML Scraping via Python evt. diverse

[xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)

[Python Guide](http://docs.python-guide.org/en/latest/scenarios/scrape/)

[Web Scraping with Beautiful Soup](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html)

[Thenewboston - Web Crawler Tutorial Python](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q)

[Thenewboston - Django for Beginners](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK) (Episode 34-36 handler om User Registration, Creating Accounts og User Authentification)

## HTML Tags - Ansatte

### Tabel

Table id og class:

`<table id="medarbejdertable" cellspacing="0" class="list" summary="Medarbejderoversigt">`

Format for rows:

`<tr><td valign='top'><a href="LINK">NAVN</a></td><td valign='top'>titel</td><td valign='top'>ARBEJDSOMRÅDE</td><td valign='top'>TELEFON</td><td valign='top'>EMAIL</td></tr>`

De ansatte har (måske alle) følgende html tags, som er brugbare for scraping:

### "pure" links

#### Foto

`<div class="person_photo"><img src="LINK" alt="NAVN"></div>`

#### Navn og titel

`<span class="person">NAVN</span></h2><p class="type">titel</p>`

#### Adresse, telefon og e-mail

`<div class="address"><p>ADRESSE</p><p>ADRESSE FORTSAT</p>`

`<ul class="relations email"><li><a href="mailto:EMAIL" class="link"><span>EMAIL</span></a></li></ul>`

`<span class="numbers"><span class="property person_contact_phone"><strong>Telefon: </strong>TELEFON NUMMER</span></span>`

#### Arbejdsgruppe

`<ul class="relations organisations"><li><h2 class="title"><span>ARBEJDS GRUPPE</span></h2></ul>`

#### Hjemmeside

`<ul class="relations"><li><a onclick="window.open(this.href); return false;" href="HJEMMESIDE" class="link"><span>HJEMMESIDE</span></a></li></ul>`

#### Præsentation


#### Publikationer


#### Aktiviteter

### "id" links

#### Foto
`<div id="forskerprofil_kontaktoplysninger"><img src="LINK" alt="NAVN"></img></div>`

#### Navn og titel
`<div xmlns="http://www.w3.org/1999/xhtml" id="forskerprofil_kontaktoplysninger"><h1>NAVN</h1></div>`

`<p class="forskerprofil_titel">titel</p>`

#### Adresse, telefon og e-mail
`<p class="forskerprofil_adresse"><strong>INSTITUT</strong><br>GADE+GADENUMMER<br>POSTNR+BY</p>`

`<p class="forskerprofil_kontakt">Telefon: NUMMER<br/>Telefon (Sekretariat): SEKRETARIATNUMMER<br/>Mobil: MOBILNUMMER<br/>E-mail: <a href="mailto:EMAIL">EMAIL</a><br/></p>`

## HTML Tags - Projekter

Projekter har følgende interessante HTML tags:

## DIKU test server links

[Bachelor Projekter](http://dikutestserver.dk/resultat.php?emne=&type=Bachelorprojekt&firma=&submit=S%C3%B8g)

[Kandidat Projekter](http://dikutestserver.dk/resultat.php?emne=&type=Kandidatprojekt&firma=&submit=S%C3%B8g)

[Kandidat Speciale](http://dikutestserver.dk/resultat.php?emne=&type=Speciale&firma=&submit=S%C3%B8g)

[Virksomhedsprojekter](http://dikutestserver.dk/resultat.php?emne=&type=Virksomhedsprojekt&firma=&submit=S%C3%B8g)

[Andre projekter](http://dikutestserver.dk/result.php?search=true&searcher=Student)
