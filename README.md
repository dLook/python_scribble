python_scribble
===============

Aplikaciju napraviti kao novi Django projekt. Za spremanje podataka koristite SQLite bazu zbog 
jednostavnosti. U requirements.txt datoteci navedite dodatne pakete koje ste koristili prilikom 
izrade zadatka kao i inačicu Djanga koja je korištena.  
 
Zadatak spremite u neki repozitorij (predlažemo GitHub ili Bitbucket) i pošaljite nam link. Ako 
vam zbog nekog razloga to nije moguće možete postali zapakiran zadatak i navedite razlog zbog 
kojeg niste koristili repozitorij. 
 
Prvenstveno nas zanima kod u Djangu, za html dizajn vašeg zadatka možete upotrijebiti default 
stil bilo kojeg CSS frameworka (npr. http://getbootstrap.com/ ili http://purecss.io/ ). Ako koristite 
CSS framework sve što je potrebno za prikaz spremite u repozitorij ili arhivu. 
 
U definiciji zadatka nije definirana struktura potrebnih tablica (modela), na vama je da ih definirate 
prema zahtjevima. 
 
Opis zadatka
 
1. Napraviti stranicu s prikazom liste i forme za unos adrese RSS feeda. Svaki feed na sebi 
mora imati oznaku aktivnosti koju je moguće mijenjati (ovu točku ne smatramo rješenjem ako se 
to napravi uz pomoć Django admina). 
 
2. Napraviti Django manage komandu koja dohvaća aktivne feedove i sprema njihove unose 
(entries) u bazu. 
  a. iz sadržaja pojedinog unosa posebno izdvojiti sve riječi 
  b. svaku riječ spremiti u tablicu riječi tako da je svaka riječ navedena samo jednom 
  (jedinstveni ključ po riječi) 
  c. u dodatnu tablicu spremiti koliko puta se svaka pojedina riječ ponavlja u 
  pojedinom unosu te koliko se pojedina riječ ponavlja u pojedinom feedu, a uz 
  svaku riječ možete zapisati i ukupan broj pojavljivanja 
 
3. Napraviti JSON API kojemu se kao parametar predaje riječ i kao odgovor dobije broj 
ponavljanja te riječi. Kao parametar može se predati url feeda ili url unosa i u tom slučaju se 
dobije broj ponavljanja te riječi u feedu ili u unosu. 
 
4. Napraviti stranicu s top listom riječi prema broju pojavljivanja. Omogućiti filtriranje po 
feedovima. Definirati optimalan broj riječi po stranici i u slučaju da ih ima previše napraviti 
straničenje (paging). 
