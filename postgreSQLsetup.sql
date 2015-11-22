CREATE DATABASE zooplatest;

CREATE USER externalAPI PASSWORD 'test';

GRANT ALL ON SCHEMA zooplalive TO externalAPI;

CREATE TABLE zoopladump ( listing_id varchar(10), price varchar(10), beds varchar(10), latitude varchar(10), longitude varchar(10));

CREATE TABLE zooplaclean ( listing_id varchar(10), price float, beds int, latitude float, longitude float);
