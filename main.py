from sample_data_reader import SampleDataReader
import time
import json
from datetime import datetime, timedelta

def publish(reminder: str) -> None:
    print(f"publishing: {reminder}")

def main():

    fake_home_data = SampleDataReader("home_data.json")
    with open("home.json", "r") as f:
        home_config = json.load(f)
    
    curr_time = datetime.now() 
    # set the cur time to 8pm
    curr_time = curr_time.replace(hour=20, minute=0, second=0, microsecond=0)

    completed_reminders = set()
    daily_reminders_published = {}

    current_house_data = fake_home_data.get()
    while current_house_data is not None:
        print("current time is", curr_time.strftime("%H:%M:%S"))
        
        for reminder in home_config:
            name = reminder["name"]
            trigger_type = reminder["trigger_type"]
            repeats = reminder["repeats"]
            code = reminder["code"]

            if name in completed_reminders:
                continue

            if repeats == "daily":
                if daily_reminders_published.get(name) == curr_time.date():
                    continue

            funcs = {}
            exec(code, funcs)
            eval_func_name = code.split("(")[0].split(" ")[1]
            eval_func = funcs[eval_func_name]

            if eval_func(curr_time, current_house_data):
                publish(name)

                if repeats == "daily":
                    daily_reminders_published[name] = curr_time.date()
                elif trigger_type == "once" or repeats == "never":
                    completed_reminders.add(name)


        
        current_house_data = fake_home_data.get()
        curr_time += timedelta(hours=1)


if __name__ == "__main__":
    main()