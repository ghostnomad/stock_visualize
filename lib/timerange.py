import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_chart_range():
    while True:
        choice = input("\nHow much history? (1W, 1M, 1Y) [Q to Quit]: ").strip().lower()
        
        # We calculate the 'start_date' by looking back from right now
        now = datetime.now()

        match choice:
            #not currently supporting realtime data
            #case "1d" | "day" | "d":
            #    return now - relativedelta(days=1)
            case "1w" | "week" | "w":
                return now - relativedelta(weeks=1)
            case "1m" | "month" | "m":
                return now - relativedelta(months=1)
            case "1y" | "year" | "y":
                return now - relativedelta(years=1)
            case "q" | "quit":
                sys.exit(0)
            case _:
                print(f"⚠️  '{choice}' is not a valid range.")

#usage
#user_timeframe = get_chart_range()