from alpaca.data.timeframe import TimeFrame
from enum import Enum

class UserTimeFrame(Enum):
    # This acts as our data map
    MINUTE = TimeFrame.Minute
    HOUR = TimeFrame.Hour
    DAY = TimeFrame.Day
    WEEK = TimeFrame.Week

def get_timeframe():
    while True:
        choice = input("\nEnter Interval (Min, Hour, Day, Week) [Q to Quit]: ").strip().lower()

        match choice:
            case "min" | "minute":
                return UserTimeFrame.MINUTE.value
            
            case "hour":
                return UserTimeFrame.HOUR.value
            
            case "day":
                return UserTimeFrame.DAY.value
            
            case "week":
                return UserTimeFrame.WEEK.value
            
            case "q" | "quit":
                print("Exiting program...")
                exit()
            
            case _:
                print(f"❌ '{choice}' is not recognized. Try again.")
            