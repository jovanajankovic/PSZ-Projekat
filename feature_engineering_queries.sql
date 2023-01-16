-- these queries where executed over cars_initial.sql

-- deleted rows with no price
delete from cars 
where cena is NULL or cena='';

-- deleted rows which do not contain exact price value
delete from cars 
where cena='Po dogovoru';

delete from cars 
where cena = 'Na upit';

-- removing substring cm^3 from column kubikaza
update cars
set kubikaza = SUBSTRING(kubikaza,1,length(kubikaza)-3);

-- removing substring km from column kilometraza
update cars 
set kilometraza = SUBSTRING(kilometraza,1,length(kilometraza)-3);

-- removing . char from column godiste
update cars 
set godiste = SUBSTRING(godiste,1,length(godiste)-1);

-- removing euro sign from column cena
update cars 
set cena = SUBSTRING(cena,1,length(cena)-4);

-- removing . from cena and kilometraza column
update cars 
set cena = REPLACE(cena,'.','');

update cars 
set kilometraza = REPLACE(kilometraza,'.','');

-- changed type from varhcar to int for columns godiste, kilometrazu, kubikazu i cenu
ALTER TABLE `cars` CHANGE `godiste` `godiste` INT NULL DEFAULT NULL;
ALTER TABLE `cars` CHANGE `kilometraza` `kilometraza` INT NULL DEFAULT NULL;
ALTER TABLE `cars` CHANGE `kubikaza` `kubikaza` INT NULL DEFAULT NULL;
ALTER TABLE `cars` CHANGE `cena` `cena` INT NULL DEFAULT NULL;

-- deleted car with id = 7073 => no data was provided
DELETE from cars where id = 7073
-- this was the only car which had 'Poluautomatski' menjac, so changed to 'Automatski/poluautomatski'
UPDATE `cars` SET `menjac` = 'Automatski / poluautomatski' WHERE `cars`.`id` = 19308

-- set to "Automatska klima" since this model mostly had this value attribute for column klima
UPDATE `cars` SET `klima` = 'Automatska klima' WHERE `cars`.`id` = 190;

-- updated cena column based on avg cena for that car model 
UPDATE `cars` SET `cena` = '4850' WHERE `cars`.`id` = 334;
UPDATE `cars` SET `cena` = '6950' WHERE `cars`.`id` = 335;
UPDATE `cars` SET `cena` = '5450' WHERE `cars`.`id` = 336;
UPDATE `cars` SET `cena` = '4650' WHERE `cars`.`id` = 337;
UPDATE `cars` SET `cena` = '3280' WHERE `cars`.`id` = 338;
UPDATE `cars` SET `cena` = '4270' WHERE `cars`.`id` = 339;
UPDATE `cars` SET `cena` = '1940' WHERE `cars`.`id` = 340;
UPDATE `cars` SET `cena` = '3170' WHERE `cars`.`id` = 341;
UPDATE `cars` SET `cena` = '5065' WHERE `cars`.`id` = 342;
UPDATE `cars` SET `cena` = '4870' WHERE `cars`.`id` = 343;
UPDATE `cars` SET `cena` = '6675' WHERE `cars`.`id` = 344;
UPDATE `cars` SET `cena` = '5700' WHERE `cars`.`id` = 345;
UPDATE `cars` SET `cena` = '5100' WHERE `cars`.`id` = 346;
UPDATE `cars` SET `cena` = '2635' WHERE `cars`.`id` = 347;
UPDATE `cars` SET `cena` = '3030' WHERE `cars`.`id` = 348;
UPDATE `cars` SET `cena` = '4030' WHERE `cars`.`id` = 349;
UPDATE `cars` SET `cena` = '5460' WHERE `cars`.`id` = 350;
UPDATE `cars` SET `cena` = '3230' WHERE `cars`.`id` = 351;
UPDATE `cars` SET `cena` = '4215' WHERE `cars`.`id` = 352;
UPDATE `cars` SET `cena` = '4940' WHERE `cars`.`id` = 353;
UPDATE `cars` SET `cena` = '3035' WHERE `cars`.`id` = 354;
UPDATE `cars` SET `cena` = '5630' WHERE `cars`.`id` = 355;
UPDATE `cars` SET `cena` = '5230' WHERE `cars`.`id` = 356;
UPDATE `cars` SET `cena` = '4685' WHERE `cars`.`id` = 357;
UPDATE `cars` SET `cena` = '4410' WHERE `cars`.`id` = 359;
UPDATE `cars` SET `cena` = '7655' WHERE `cars`.`id` = 361;
UPDATE `cars` SET `cena` = '7360' WHERE `cars`.`id` = 362;
UPDATE `cars` SET `cena` = '5590' WHERE `cars`.`id` = 363;
UPDATE `cars` SET `cena` = '5630' WHERE `cars`.`id` = 364;
UPDATE `cars` SET `cena` = '4095' WHERE `cars`.`id` = 365;
UPDATE `cars` SET `cena` = '2980' WHERE `cars`.`id` = 381;
UPDATE `cars` SET `cena` = '3640' WHERE `cars`.`id` = 2169;
UPDATE `cars` SET `cena` = '4930' WHERE `cars`.`id` = 3187;
UPDATE `cars` SET `cena` = '2960' WHERE `cars`.`id` = 4911;
UPDATE `cars` SET `cena` = '7110' WHERE `cars`.`id` = 4912;
UPDATE `cars` SET `cena` = '5345' WHERE `cars`.`id` = 4914;
UPDATE `cars` SET `cena` = '4625' WHERE `cars`.`id` = 4915;
UPDATE `cars` SET `cena` = '7670' WHERE `cars`.`id` = 4946;
UPDATE `cars` SET `cena` = '3130' WHERE `cars`.`id` = 5145;
UPDATE `cars` SET `cena` = '4120' WHERE `cars`.`id` = 5147;
UPDATE `cars` SET `cena` = '5070' WHERE `cars`.`id` = 7131;
UPDATE `cars` SET `cena` = '575' WHERE `cars`.`id` = 8499;
UPDATE `cars` SET `cena` = '1515' WHERE `cars`.`id` = 9321;
UPDATE `cars` SET `cena` = '1085' WHERE `cars`.`id` = 9583;
UPDATE `cars` SET `cena` = '1710' WHERE `cars`.`id` = 10188;
UPDATE `cars` SET `cena` = '1870' WHERE `cars`.`id` = 11136;
UPDATE `cars` SET `cena` = '4500' WHERE `cars`.`id` = 12247;
UPDATE `cars` SET `cena` = '1370' WHERE `cars`.`id` = 12294;
UPDATE `cars` SET `cena` = '7860' WHERE `cars`.`id` = 13716;
UPDATE `cars` SET `cena` = '7275' WHERE `cars`.`id` = 15969;
UPDATE `cars` SET `cena` = '1010' WHERE `cars`.`id` = 16347;
UPDATE `cars` SET `cena` = '4220' WHERE `cars`.`id` = 19076;
UPDATE `cars` SET `cena` = '2700' WHERE `cars`.`id` = 358;
UPDATE `cars` SET `cena` = '9000' WHERE `cars`.`id` = 379;
UPDATE `cars` SET `cena` = '15000' WHERE `cars`.`id` = 3805;
UPDATE `cars` SET `cena` = '200' WHERE `cars`.`id` = 8841;
UPDATE `cars` SET `cena` = '11150' WHERE `cars`.`id` = 4913;
UPDATE `cars` SET `marka` = 'Dacia', `model` = 'Logan' WHERE `cars`.`id` = 17310;

-- deleted cars which were not provided with all neccessary data
DELETE FROM `cars` WHERE `cars`.`id` = 8842;
DELETE FROM `cars` WHERE `cars`.`id` = 15590;
DELETE FROM `cars` WHERE `cars`.`id` = 19820;

-- updating unreal kubikaza values based on real model
UPDATE `cars` SET `kubikaza` = '1686' WHERE `cars`.`id` = 10766;
UPDATE `cars` SET `kubikaza` = '1248' WHERE `cars`.`id` = 5273;
UPDATE `cars` SET `kubikaza` = '1248' WHERE `cars`.`kubikaza` = 13000 LIMIT 1;
UPDATE `cars` SET `kubikaza` = '1360' WHERE `cars`.`id` = 4352;
UPDATE `cars` SET `kubikaza` = '1398' WHERE `cars`.`id` = 11384;
UPDATE `cars` SET `kubikaza` = '1600' WHERE `cars`.`id` = 15186;
UPDATE `cars` SET `kubikaza` = '1598' WHERE `cars`.`id` = 836;
UPDATE `cars` SET `kubikaza` = '1900' WHERE `cars`.`id` = 18059;
UPDATE `cars` SET `kubikaza` = '2000' WHERE `cars`.`id` = 2769;
UPDATE `cars` SET `kubikaza` = '1600' WHERE `cars`.`id` = 15366;
UPDATE `cars` SET `kubikaza` = '1560' WHERE `cars`.`id` = 4156;
UPDATE `cars` SET `kubikaza` = '1900' WHERE `cars`.`id` = 8243;
UPDATE `cars` SET `kilometraza` = '192000', `kubikaza` = '1560' WHERE `cars`.`id` = 11508;
UPDATE `cars` SET `kubikaza` = '1560' WHERE `cars`.`id` = 13097;
UPDATE `cars` SET `kubikaza` = '1968' WHERE `cars`.`id` = 2641;
UPDATE `cars` SET `kubikaza` = '2000' WHERE `cars`.`id` = 10424;
UPDATE `cars` SET `kubikaza` = '650' WHERE `cars`.`id` = 8904;
UPDATE `cars` SET `kubikaza` = '1900' WHERE `cars`.`id` = 9269;

-- converting all lokacija values to uppercase values
update cars set lokacija = upper(lokacija);

-- updating automatski to automatski/poluautomatski
update cars set menjac = 'Automatski / poluautomatski' where menjac = 'Automatski';

-- updating motor to kW and removing kS value and string (kW / kS)
update cars
set motor = substring(motor,1,LOCATE("/", motor) - 1)

-- changing motor type from varchar to INT
ALTER TABLE `cars` CHANGE `motor` `motor` INT NULL DEFAULT NULL;

-- updating wrong user input for motor values in kW
UPDATE `cars` SET `motor` = '140' WHERE `cars`.`id` = 5451;