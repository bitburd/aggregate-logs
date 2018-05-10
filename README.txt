This is a python code to do the following for a job interview of skills:

Write a Python or Bash  script that will tail a NGINX, IIS or Apache log file and cumulatively aggregate 2XX, 3XX, 4XX & 5XX errors by minute. You can use a database. Push the code to Github and share



To use, you must have python on ubuntu with the sqlite3 db and pandas libraries installed.

I've bundled up this script with 2 bash scripts that help set it up and run it.

To run copy all these files to your system and type:

./run-aggregate.sh 


This will start the script and run it every 60 seconds.

I will upload the source to git when I get the chance at:

https://github.com/bitburd

Jason