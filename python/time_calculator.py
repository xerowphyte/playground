from audioop import add


def add_time(start, duration):
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    
    duration_tuple = duration.partition(":")
    print(duration_tuple)
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]
    am_and_pm_flip = {"AM" : "PM", "PM" : "AM"}

    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        start_hours += 1
        print(start_hours)
        end_minutes = end_minutes % 60

    
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12) 
    end_hours = int((start_hours + duration_hours) % 12)
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    #if(am_or_pm == "PM" and start_hours + duration_hours % 12) >= 12 :
        amount_of_days += 1
    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm
    retunTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm






    

if __name__ == "__main__":
    print(add_time("11:06 PM", "2:02"))