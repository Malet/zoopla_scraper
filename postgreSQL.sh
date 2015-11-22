# install database
sudo apt-get install postreSQL  postgresql-server-dev-9.3
# Version and name
sudo pg_createcluster 9.3 zoopla
#default login is postgres
sudo -su postgres
#sql code begins here
psql -f postgreSQLsetup.sql
# \dt shows tables and \l shows databases
# \c connects to database
sudo service postgresql restart 
