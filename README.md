# Kirjastotyökalu

## Dokumentaatio

[vaatimusmaarittely.md](/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](/dokumentaatio/changelog.md)

[arkkitehtuuri.md](/dokumentaatio/arkkitehtuuri.md)

## Releaset

[release 1 (viikko5)](/releases/tag/viikko5)

[release loppupalautus](/releases/tag/loppupalautus)
## Asennus

Asenna riippuvuudet käyttäen poetryä

```bash
poetry install
```
Ennen ohjelman käynnistystä tulee alustaa sql tietokanta ajalamma komento tiedosto "src/initializer.py" 
jos kyseisen ohjelman suoritus kaatuu "no such column: sqlite_schema tai sqlite_master" tulee vaihtaa sqlite muuttujan arvo src/services/tables.py tiedostosta. Tämä on joku eri versioiden välinen ongelma joka tuli esille kokeillessa koulun koneella. Koulun koneilla toimi aijempi sqlite_master.

Ohjelman voi käynnistää komennolla 
```bash
poetry run invoke start
``` 
Testit voi suorittaa komennolla

```bash
poetry run invoke test
``` 

Kattavuusraportin voi generoida komennolla 

```bash
poetry run invoke coverage-report
``` 

Ohjelman voi ajaa pylint testin läpi komennolla

```bash
poetry run invoke lint
``` 
