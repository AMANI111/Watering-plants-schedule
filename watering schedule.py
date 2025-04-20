#a scenario where if the user chooses "snooze," the reminder is sent to another user.
#If that user accepts, the task ends; otherwise, the process continues until the task is completed.
#I would like to add time to this, so the reminder is sent at 12pm, 
#and if no one completed the task to resent the reminder at 4pm
#add real notifications using SMS

import calendar #days of the week
import datetime #accessing standard libraries for time-related data
def print_today():
    today = datetime.datetime.today().weekday() #creating today using datetime
    today_name = calendar.day_name[today] #today is day of the week from calendar
    print(f"Day of the week: {today_name}") #print day of the week
    return today_name #return a value I intend to use later

def create_day_dict(): #create a empty dictionary to bring days of the calendar
    return {i: calendar.day_name[i] for i in range(7)} #simplified for brevity. uses calendar function
#to map through days of the week (7 not 6 makes it loop). For each number i in this range, the dictionary comprehension 
#assigns the key i (the day number) to the value calendar.day_name[i] (the name of the day).

def my_date(day): #create a function to print name of given weekday number
    day_dict = create_day_dict()
    if 0 <= day <= 6: #comparison that checks if the value of day is within a specific range includive of 0 & 6
        print(day_dict[day])
    else:
        print("Invalid number. Between 0 - 6")

def create_watering_schedule(): #create dictionary of watering tasks
#define the watering task for day of the week
    watering_schedule = {}  # initialize empty dictionary
    for i in range(7): #This loops over the integers from 0 to 6, which represent the days of the week.
        watering_schedule[calendar.day_name[i]] = "water plants."  #For each i, it assigns the task "water plants."
        #to the corresponding day in the calendar.day_name list.
    return watering_schedule #This returns the dictionary watering_schedule, which holds the watering task for each day.
watering_schedule = create_watering_schedule() 
print("\nWatering schedule for the week") #and print watering schedule for each day
for day in calendar.day_name:
    print(f"{day}; {watering_schedule[day]}") #KVP for dictionary of watering tasks


#dynamically change the watering schedule based on user input
today = print_today()
print(f"\nWere the plants watered?\n")
prompt = 'Type "yes" or "snooze".\n'
volunteer = ['Ben', 'Andrew', 'Miriam', 'Camilla', 'Monica'] #holds names of volunteers who could potentially water the plants. 
# In a real application, I could replace these with user IDs or emails or phone numbers
#track task is done
task_done = False
accepted_by = None
while True: #while true if, elif statements
    answer = input(prompt).lower()
    if answer == 'yes':
        print("Thank you \n")
        task_done = True
        accepted_by = "You"
        break
    elif answer == 'snooze':
        watering_schedule[today] += "   (snoozed)"
        print("Task has been snoozed")
        print("Reminder to water plants sent to another member.")
        for person in volunteer:
            print(f"\nHello {person}! The plants need watering this {today}.")
            volunteer_answer = input("Type 'yes' if you will do it or 'no' to skip.\n").lower()
            if volunteer_answer == 'yes':
                print(f"Thank you! The plants have now been watered. \n")
                task_done = True
                accepted_by = person
                break
            else:
                print("You have skipped.\n")
        break   
    else:                                                                                                                                                         
        print("Please type a valid response: yes or snooze.")

if task_done:
    print(f"Task completed by {accepted_by}.")
else:
   print("\nThe plants did not get watered today. Please check later. \n")
