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

    current_house_data = fake_home_data.get()
    while current_house_data is not None:
        print("current time is", curr_time.strftime("%H:%M:%S"))
        
        # eval function should look like:
        # eval_func(curr_time, current_house_data)
        
        current_house_data = fake_home_data.get()
        curr_time += timedelta(hours=1)


if __name__ == "__main__":
    main()