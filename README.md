# ProjectStockSD

Velkommen til vores Project Stock repository!

## Kør serveren lokalt
### Installer afhængigheder
`[sudo] apt-get install libmysqlclient-dev python-dev # eller den tilsvarende kommando for din distribution`

`[sudo] pip install mysqlclient`

### Skift til debug mode
I filen `project_stock/project_stock/settings.py` erstat `Debug = False` med `Debug = True` (husk at den ikke skal commites medmindre I laver andre relevante ændringer; Debug skal være False på webserveren).

### Login-fil
Filen `project_stock/project_stock/config.cnf` skal have følgende format:

`[client]`

`database = "database"`

`user = "username"`

`password = "password"`

`host = "128.199.39.136"`

`default-character-set = "utf8"`

Denne fil skal heller ikke pushes til Github, da passwords kun skal være på webserveren og testmaskinerne.

### Kør serveren
Skift mappe til project_stock Django projektet og kør:

`python manage.py runserver`

## Migrations på serveren
### Lav migrations
`sudo python manage.py makemigrations`

`sudo python manage.py migrate`

### Genstart serveren
`sudo systemctl restart httpd mariadb` eller CTRL-C + `python manage.py runserver`

## Git Tips
### Hjælp til git kommandoer:

`git [kommando] --help`

Eksempler:

git add --help

git commit --help

git help --help

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

## HTML Tags - Ansatte

### Tabel

Table id og class:

`<table id="medarbejdertable" cellspacing="0" class="list" summary="Medarbejderoversigt">`

Format for rows:

`<tr><td valign='top'><a href="LINK">NAVN</a></td><td valign='top'>STILLING</td><td valign='top'>ARBEJDSOMRÅDE</td><td valign='top'>TELEFON</td><td valign='top'>EMAIL</td></tr>`

De ansatte har (måske alle) følgende html tags, som er brugbare for scraping:

### Foto

`<div class="person_photo"><img src="LINK" alt="NAVN"></div>`

### Navn og Stilling

`<span class="person">NAVN</span></h2><p class="type">STILLING</p>`

### Adresse, Telefon og Email

`<div class="address"><p>ADRESSE</p><p>ADRESSE FORTSAT</p>`

`<ul class="relations email"><li><a href="mailto:EMAIL" class="link"><span>EMAIL</span></a></li></ul>`

`<span class="numbers"><span class="property person_contact_phone"><strong>Telefon: </strong>TELEFON NUMMER</span></span>`

### Arbejdsgruppe

`<ul class="relations organisations"><li><h2 class="title"><span>ARBEJDS GRUPPE</span></h2></ul>`

### Hjemmeside

`<ul class="relations"><li><a onclick="window.open(this.href); return false;" href="HJEMMESIDE" class="link"><span>HJEMMESIDE</span></a></li></ul>`

### Præsentation


### Publikationer


### Aktiviteter


## HTML Tags - Projekter

Projekter har følgende interessante HTML tags:
