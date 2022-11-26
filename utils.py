import requests

def send_line(notify_url: str, token: str, message: str):      
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }          
    r = requests.post(notify_url, headers = headers, data = data)    
    if r.status_code != 200:
        print(r.status_code)
