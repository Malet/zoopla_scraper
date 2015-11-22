CREATE DATABASE zooplatest;

\c zooplatest;

CREATE USER externalAPI PASSWORD 'test';

GRANT ALL PRIVILEGES ON DATABASE zooplatest to externalAPI;

CREATE TABLE zooplajsondump ( listing_id serial, data text);

CREATE TABLE zooplaclean ( listing_id varchar(10), price float, beds int, latitude float, longitude float);
