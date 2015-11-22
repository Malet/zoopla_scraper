# install database
sudo apt-get install postreSQL
# Version and name
sudo pg_createcluster 9.3 zoopla
#default login is postgres
sudo -su postgres
#sql code begins here
psql -f postgreSQLsetup.sql
