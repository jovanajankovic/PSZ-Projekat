-- a) 10 najzastupljenijih lokacija koje imaju najveci broj automobila u ponudi
select lokacija, count(*) as broj_automobila 
from cars
group by lokacija
order by count(*) 
desc limit 10;

-- b) broj automobila prema kilometrazi
select cars_kilometraza.opseg_kilometraze as opseg_kilometraze, count(*) as broj_automobila 
from (select case 
     	 when kilometraza <= 49999 then '1. ispod 50.000 km' 
     	 when kilometraza between 50000 and 99999 then '2. 50.000 - 99.999 km' 
     	 when kilometraza between 100000 and 149999 then '3. 100.000 - 149.999 km' 
     	 when kilometraza between 150000 and 199999 then '4. 150.000 - 199.999 km' 
     	 when kilometraza between 200000 and 249999 then '5. 200.000 - 249.999 km' 
     	 when kilometraza between 250000 and 299999 then '6. 250.000 - 299.999 km' 
         when kilometraza>=300000 then '7. 300.000 km ili vise'
      end as opseg_kilometraze from cars) as cars_kilometraza
group by cars_kilometraza.opseg_kilometraze;

-- c) broj automobila po godini proizvodnje
select cars_godiste.opseg_godista as opseg_godista, count(*) as broj_automobila 
from (select case 
     	 when godiste <= 1960 then '1960. godiste i stariji modeli' 
     	 when godiste between 1961 and 1970 then '1961 - 1970' 
     	 when godiste between 1971 and 1980 then '1971 - 1980' 
     	 when godiste between 1981 and 1990 then '1981 - 1990' 
     	 when godiste between 1991 and 2000 then '1991 - 2000' 
     	 when godiste between 2001 and 2005 then '2001 - 2005' 
         when godiste between 2006 and 2010 then '2006 - 2010' 
         when godiste between 2011 and 2015 then '2011 - 2015' 
         when godiste between 2016 and 2020 then '2016 - 2020' 
         else '2021 - 2022' 
      end as opseg_godista from cars) as cars_godiste
group by cars_godiste.opseg_godista;

-- d) broj (i procentualni odnos) automobila sa manuelnim ili automatskim menjacem
select menjac, count(menjac) as broj_automobila, (count(menjac) / (select count(*) from cars)) * 100 as procenat_automobila
from cars
group by menjac;

-- e) broj (i procentualni odnos) automobila za prodaju, koje pripadaju jednom od sl. opsega
select cars_cene.opseg_cena as opseg_cena, count(*) as broj_automobila, (count(opseg_cena) / (select count(*) from cars)) * 100 as procenat_automobila 
from (select case 
      	when cena < 2000 then '1. 0 - 1.999 eura' 
      	when cena between 2000 and 4999 then '2. 2.000 - 4.999 eura' 
      	when cena between 5000 and 9999 then '3. 5.000 - 9.999 eura' 
      	when cena between 10000 and 14999 then '4. 10.000 - 14.999 eura' 
      	when cena between 15000 and 19999 then '5. 15.000 - 19.999 eura' 
      	when cena between 20000 and 24999 then '6. 20.000 - 24.999 eura' 
      	when cena between 25000 and 29999 then '7. 25.000 - 29.999 eura' 
      	else '8. 30.000 eura ili vise' end as opseg_cena from cars) as cars_cene 
group by cars_cene.opseg_cena;