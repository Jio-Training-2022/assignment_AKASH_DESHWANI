# A dict contains events and corresponding dates, given a date, find out what events have occurred and what are still pending. 


if __name__ == "__main__":
    events = {"2020-01-01": "New Year", "2020-01-26": "Republic Day", "2020-08-15": "Independence Day", "2020-10-02": "Gandhi Jayanti", "2020-12-25": "Christmas"}
    date = input("Enter the date to be searched: (in format YYYY-MM-DD) ")
    for key, value in events.items():
        if key < date:
            print(value, "has already occurred")
        elif key > date:
            print(value, "is yet to occur")
        else:
            print(value, "is on the date entered")