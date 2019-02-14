This is python code that does the following:

Python and Bash script that will tail a NGINX, IIS or Apache log file and cumulatively aggregate 2XX, 3XX, 4XX & 5XX errors by minute. Uses a sqlite3 database.



To use, you must have python on ubuntu with initial sqlite3 db and pandas libraries installed.
I'll eventually include a script to create a small sqlite3 db for testing.
I've bundled up this script with 2 bash scripts that help set it up and run it.

To run copy all these files to your system and type:

./run-aggregate.sh 


This will start the script and run it every 60 seconds.

Repository is at:

https://github.com/bitburd

Jason
