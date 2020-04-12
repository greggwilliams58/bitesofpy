from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    if line[0] == "E":
        date_object = datetime.strptime(line[6:25], "%Y-%m-%dT%H:%M:%S")
    elif line[0] == "I":
        date_object = datetime.strptime(line[5:24], "%Y-%m-%dT%H:%M:%S")
    else:
        print("unrecognised format")
        pass
    return date_object


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_dates = []
    for line in loglines:
        if "Shutdown initiated" in line:
            date = datetime.strptime(line[5:24], "%Y-%m-%dT%H:%M:%S")
            shutdown_dates.append(date)

    first_date = shutdown_dates[0]
    last_date = shutdown_dates[-1]

    td_raw = last_date - first_date

    return td_raw