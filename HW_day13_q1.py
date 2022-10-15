# Days to go for a particular date in future. 

from datetime import datetime

if __name__ == "__main__":
    ipdate = input("enter the date in the format of yyyy-mm-dd e.g.(2017-10-10) : ")
    fdate = datetime.strptime(ipdate,"%Y-%m-%d").date()
    todaydate = datetime.today().date()
    ndaysleft = fdate - todaydate
    print("Days to go for a particular date in future: ", ndaysleft)