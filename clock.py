from calendar import month
from apscheduler.schedulers.blocking import BlockingScheduler
from constants import LINE_GROUP_LINK

from main import aachen_an, aachen_permit

sched = BlockingScheduler(timezone="Europe/Berlin")

# @sched.scheduled_job('interval', seconds=30)
# def timed_job():        
#     aachen_an('2023', '01')
#     # aachen_permit()

# def timed_job(year, month):
#     aachen_an(year, month)

def welcome():
    print('Welcome to use Aachen Anmeldung Termin Alert!')   
    print('Note: The script only notifys appointments from Bahnhofplatz Katschhof. \nLink: https://qtermin.de/BahnhofplatzKatschhof')
    print('=======================================================================')
    print('- Steps:')
    print('1. Join the line group in order to receive alerting messages')
    print('https://imgur.com/a8huKXY.jpg')    
    print(LINE_GROUP_LINK)                
    print('2. Enter the year and the month(two digits) in which you wish to have an appointment. For example, year:2023, month:01')

def get_input_year():
    year=None
    while True:        
        year=input("Year:")
        if year.isdigit() and len(str(year)) == 4:            
            return year
        else:
            print("Enter a valid year")    

def get_input_month():
    month=None
    while True:        
        month=input("Month:")
        if month in {"01","02","03","04","05","06","07","08","09","10","11","12"}:            
            return month
        else:
            print("Enter 01, 02, 03, ... , 12")


if __name__ == "__main__":
    welcome()
    year,month=get_input_year(),get_input_month()
    sched.add_job(aachen_an, "cron", args=[year, month], second="*/30")
    sched.start()