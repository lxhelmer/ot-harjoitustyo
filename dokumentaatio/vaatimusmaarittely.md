# Vaatimusmäärittely

## Sovelluksen tarkoitus

Ohjelmisto on yleispätevä kirjastosovellus. Tarkoituksena on antaa käyttäjälle helppokäyttöinen tapa käyttää SQL-tauluja tiedon tallentamiseen ja tarkasteluun
Ohjelmiston pääpointteja on monimutkaisten sql-toimintojen käytön helpottaminen käyttäjälle graafisen käyttöliittymän ja valmiiksi luotujen toimintojen kautta.
Käyttäjä voi esimerkiksi luoda uusia tauluja tai yhdistää olemassaolevia kirjoittamatta itse komentoja. Tavoitteena on saavuttaa hyvä kompromissi 
helppokäyttöisyyden ja toimintojen monimutkaisuuden välillä. Myös tiedon esittäminen selkeässä muodossa ja esitysmuodon hallinnoiminen on käyttäjäkokemuksen
kannalta keskiössä. 

## Käyttäjät
Sovelluksella ei lähtökohtaisesti tarvitse olla eri tasoisia käyttäjiä koska normaalilla käyttäjätasolla on oikeus hallinnoida kaikkia tauluja. 
Myöhemmässä kehityksessä voidaan luoda matalamman käyttöoikeustason käyttäjä jolla on mahdollisuus ainoastaan taulujen katsomiseen. Tätä jatkokehittämällä
voidaan luoda eri taulujen välille luokituksia jolloin käyttäjä voi tarkkailla vain niitä tauluja joihin hänellä on oikeus.

## Toiminnallisuus
Käyttäjä voi ohjelmiston avattuaan valita seuraavista toiminnoista: 

1. Siirtyä selaamaan olemassaolevia kirjastoja(sql-tauluja).
2. Luoda uuden kirjaston ja siirtyä sen määrittelyyn.
3. Hallinnoida kirjastoja (poistaminen ja jatkokehityksessä tasoja)

Nämä vaihtoehdot vastaavat omia näkymiään joissa käyttäjä voi suorittaa haluamiaan näkymää vastaavia toimintoja. 

# Jatkokehitysideoita 
Kirjastojen luomiseen voi kehittää laajempia ja monimutkaisempia rakenteita. Esimerkiksi esimerkiksi tauluun voidaan tallentaa muiden solujen mukaan
määrittyviä arvoja tms automaattista laskentaa hyödyntäviä arvoja. Ohjelmaan voidaan myös lisätä taulujen välillä tapahtuvaa vertailua tai niiden yhdistelyä 
pysyvästi tai väliaikaisesti tiedon esitysnäkymässä. Lisäksi voidaan kehittää käyttäjä osiossa kaavailtu lupahierarkia.


# Toteutettu
- Toteutettu käyttöliittymän perusnäkymä sekä taulukon katsomiseen johtava näkymä
- Toteutettu testejä suhteellisen hyvällä kattavuudella
- Toteutettu loput käyttöliittymän näkymät(taulukon luonti, sekä taulukon katsomis näkymä)
