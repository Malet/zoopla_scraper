CREATE DATABASE zooplatest;

\c zooplatest;

CREATE USER externalAPI PASSWORD 'test';

CREATE TABLE zoopladump ( listing_id varchar(10), price varchar(10), beds varchar(10), latitude varchar(10), longitude varchar(10));

CREATE TABLE zooplaclean ( listing_id varchar(10), price float, beds int, latitude float, longitude float);

GRANT ALL ON zoopladump TO externalAPI;

GRANT ALL ON zooplaclean TO externalAPI;
