This is a simple python script that takes a time based log file and minimizes it. <br>
It checks to see if the next entry in the log has the same value and if it does, it removes it. <br>
You are left with a log file that only contains the timestamps of when the value changed.<br>
There's also a python script to decompress the log file by interpolating based on whatever your polling rate was.
