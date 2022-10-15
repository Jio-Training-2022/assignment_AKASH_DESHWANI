# Hours to go for a particular time. 
# todaytime = datetime.today().time() ## when finding subtraction this giving error need to check why ??
# TO ASK -> why this is not working ??

from datetime import datetime 

if __name__ =="__main__":
    from datetime import datetime

    # start time and end time
    starttime = input("enter the current time in the format of hh:mm:ss e.g.(13:30:00) : ")
    endtime = input("enter the end time in the format of hh:mm:ss e.g.(13:30:00) : ")
    start_time = datetime.strptime(starttime, "%H:%M:%S")
    end_time = datetime.strptime(endtime, "%H:%M:%S")
    print(type(start_time))
    print(type(end_time))
    delta = end_time - start_time

    sec = delta.total_seconds()
    print('difference in seconds:', sec)

    min = sec / 60
    print('difference in minutes:', min)

    # get difference in hours
    hours = sec / (60 * 60)
    print('difference in hours:', hours)


    # starttime = input("enter the time in the format of hh:mm:ss e.g.(13:30:00) : ")
    # stat_time = datetime.strptime(starttime,"%H:%M:%S").time()
    # # todaytime = datetime.today().time().isoformat(iptime) ## this giving error need to check why ?
    # endtime = input("enter the time in the format of hh:mm:ss e.g.(13:30:00) : ")
    # endtime_1 = datetime.strptime(endtime,"%H:%M:%S").time()
    # timeleft = stat_time - endtime_1
    # print("Hours to go for a particular time: ", timeleft)