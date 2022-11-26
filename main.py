import requests
import datetime
from utils import send_line
from constants import *

def aachen_an(year: str, month: str):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    url = f'https://qtermin.de/api/timeslots?date={year}-{month}-01&serviceid=94948&rangesearch=1&caching=false&capacity=1&duration=10&cluster=false&slottype=0&fillcalendarstrategy=0&showavcap=false&appfuture=70&appdeadline=0&appdeadlinewm=0&oneoff=null&msdcm=0&calendarid=57095,57096,57097,74724,74725,133598'
    headers = {"User-Agent": user_agent, "webid": 'bahnhofplatzkatschhof'}    
    res = requests.get(url, headers=headers).json()

    message = ''
    for t in res:        
        if t['start'][5:7] == month:
            message += '\n'
            message += t['start'][:10]
    ft = "%H:%M:%S%z"        
    t = datetime.datetime.now().strftime(ft)
    if message:
        send_line(NOTIFY_URL, TOKEN, message)     
        print(f'{message} at {t}')
    else:        
        print(f'No available appointment in month {month} at {t}')

def aachen_permit():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"    
    headers = {"User-Agent": user_agent}
    
    url_1 = 'https://termine.staedteregion-aachen.de/auslaenderamt/'
    url_2 = 'https://termine.staedteregion-aachen.de/auslaenderamt/select2?md=1'
    url_3 = "https://termine.staedteregion-aachen.de/auslaenderamt/suggest?mdt=52&select_cnc=1&cnc-204=0&cnc-205=0&cnc-198=0&cnc-201=0&cnc-202=0&cnc-189=0&cnc-203=0&cnc-196=0&cnc-200=0&cnc-199=0&cnc-188=0&cnc-186=0&cnc-193=0&cnc-183=0&cnc-184=0&cnc-185=0&cnc-187=0&cnc-190=0&cnc-195=0&cnc-191=1&cnc-194=0&cnc-197=0&cnc-192=0"
    url_4 = 'https://termine.staedteregion-aachen.de/auslaenderamt/suggest?cnc-191=1&loc=28'

    res_1 = requests.get(url_1, headers=headers)
    res_2 = requests.get(url_2, headers=headers,cookies=res_1.cookies)
    res_3 = requests.get(url_3, headers=headers,cookies=res_2.cookies)
    res_4 = requests.get(url_4, headers=headers,cookies=res_3.cookies)
    ft = "%H:%M:%S%z"        
    t = datetime.datetime.now().strftime(ft)
    if "Kein freier Termin verfügbar" not in res_4.text:
        send_line(NOTIFY_URL, TOKEN, "延簽有預約名額")     
        print(f'{"延簽有預約名額"} at {t}')
    else:
        print(f'{"延簽沒有預約名額"} at {t}')
    