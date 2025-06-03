# Northeastern University - PARCS Lab - 2025 Summer Coding Challenge

This is a research problem based on one of our AI-CARING systems that tests both your critical thinking and programming skills.

## Problem Statement:
We are developing a reminder system that provides just-in-time reminders. These reminders are delivered through a display in the kitchen. You can think of them as digital sticky notes. Our reminders are only shown to the user when they are relevant. For example, if a user leaves their food in the microwave, the system detects and creates a reminder (note) on the display. The note is accompanied by sound and lights to attract the user's attention. This is what we call just-in-time reminders and is better than simply sticking a post-it-note on the microwave door.

To provide these just-in-time reminders, the system constantly evaluates and checks the status of the house. We accomplish this by periodically running an evaluation function for each reminder. If the function returns `True`, that means the reminder should be triggered. For example, a reminder that checks if the fridge door is left open will check the door sensor reading every minute.

Our research tells us there are different types of reminders -- there are some reminders that should happen all the time, whereas others might just be for one time. For example, "remind me to close the fridge door" should happen every time whereas "remind me to call my son at 8pm" should only happen once. There are more than the two types that I described here.

Your challenge is two-fold -- first, you will modify our reminder data structure to include information about whether the reminder should be repeated; second, you will then implement the system.

## Part 1
*You will only need to modify `home.json` for this part.*

`home.json` describes the reminders and their associated evaluation functions of this home. For the purpose of this exercise, we are using simplified evaluation functions, they are more complicated in our actual system. The JSON file consists of a list of reminders. Each reminder has the following properties: 

```json
    "reminder": "close the fridge",
    "eval_func": "def machine1(home_data):\n  if home_data[\"one\"]:\n    print(\"machine 1 true\")\n    return True\n  else:\n    return False"
```

- `reminder` is what the reminder is about
- `eval_func` is the function the house runs to check if the reminder should be triggered.

`eval_func` takes in the current time and home data and will return `True` if the reminder should be triggered. We already implemented the eval_func for each reminder. *Do not change the eval_func*.

### TODO:
> Look at each type of reminder and think about what additional properties you should add to each reminder to tell the system how often the reminders should be triggered and whether it should be repeated. What are the different types of reminder you can think of?

## Part 2
*you will only need to modify `home.json` and `main.py` for this part*

Now that you have categorized the reminders and given them additional information, it is time to implement the system. We have written some code that simulates a day at 1-hour increments. In `main.py`, there is a loop where each cycle is an hour. For example, the first cycle will be 8pm, followed by 9pm. You need to evaluate the correct eval functions in the loop.

### TODO:
> Implement code that reads `home.json`, have the `eval_func` run in each loop, and run the function `publish(name)` with the reminder name if it succeed (return True). After it runs true, figure out whether it should be checked or ran in the future. For example, the reminder `Remind me to call my son at 9pm today` should only be ran once but other reminders might need to be repeated.
