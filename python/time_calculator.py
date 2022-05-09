from audioop import add


def add_time(start, duration):
    
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
        end_minutes =end_minutes % 60
    end_hours = start_hours + duration_hours % 12
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours






    

if __name__ == "__main__":
    print(add_time("11:06 PM", "2:02"))