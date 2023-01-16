-- a) broj automobila za svaku od dostupnih marki
select marka, count(*) as broj_automobila 
from cars 
group by marka;

-- b) broj automobila koji se prodaje po gradovima
select lokacija, count(*) as broj_automobila
from cars
group by lokacija;

-- c) 1. broj automobila po bojama
select boja, count(*) as broj_automobila
from cars
group by boja;

-- c) 2. broj automobila po karoseriji
select karoserija, count(*) as broj_automobila
from cars 
group by karoserija;

-- d) 1. 30 najskupljih automobila
select id, marka, model, godiste, kilometraza, karoserija, cena 
from cars 
order by cena DESC
limit 30;

-- d) 2. 30 najskupljih u potkategoriji dzip/SUV
select id, marka, model, godiste, kilometraza, karoserija, cena 
from cars 
where karoserija = 'Džip/SUV' 
order by cena DESC
limit 30;

-- e) automobili proizvedeni 2021 ili 2022
select id, marka, model, godiste, kilometraza, karoserija, cena 
from cars
where godiste = 2021 or godiste = 2022
order by cena desc;

-- f) 1. automobil koji ima najvecu kubikazu
select id, marka, model, godiste, kubikaza, cena 
from cars 
where kubikaza = (select max(kubikaza) from cars);

-- f) 2. automobil koji ima najvecu snagu motora
select id, marka, model, godiste, motor, cena 
from cars 
where motor = (select max(motor) from cars);

-- f) 3. automobil koji ima najvecu kilometrazu
select id, marka, model, godiste, kilometraza, cena 
from cars 
where kilometraza = (select max(kilometraza) from cars);