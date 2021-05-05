# clockify_test
###Test task application 

This application connects to Clockify API using personal token and 
receives records of the user.

Pandas module needs to be installed.

The application checks whether it can connect to the Clockify
API and in case of success returns list of tasks and time 
spent on each task grouped by date.

If something went wrong the application tells about the error. 

The application takes no options, simply insert your API key
into config.ini without quotes and run main.py.
