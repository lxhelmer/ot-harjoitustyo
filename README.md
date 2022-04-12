# Kirjastotyökalu

## Dokumentaatio

[vaatimusmaarittely.md](/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](/dokumentaatio/tyoaikakirjanpito.md)

[Changelog.md](/dokumentaatio/Changelog.md)

## Asennus

Asenna riippuvuudet käyttäen poetryä

```bash
poetry install
```

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
