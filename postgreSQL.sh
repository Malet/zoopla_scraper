# install database
sudo apt-get install postreSQL
# Version and name
sudo pg_createcluster 9.3 zoopla
#default login is postgres
sudo -su postgres
#sql code begins here
psql

CREATE DATABASE zooplatest;
-- not sure about this command below
CREATE SCHEMA zooplalive;

CREATE USER externalAPI PASSWORD 'test';

GRANT ALL ON SCHEMA zooplalive TO externalAPI;

CREATE TABLE zoopladump ( listing_id varchar(10), price varchar(10), beds varchar(10), latitude varchar(10), longitude varchar(10));

CREATE TABLE zooplaclean ( listing_id varchar(10), price float, beds int, latitude float, longitude float);
