import requests
import threading


lock = threading.Lock()
def main():
  url = "https://anywebsite.com"                       #Any website you want to make a POST request to

  
  # Defining Headers
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  }

  #The Params which are needed for the POST request for your site
  login_Data = {
   'email': 'xyz@gmail.com',
    'password': 'blahblahblah',
    'otherparam': '1'
  }
  
  lock.acquire()
  r = requests.post(url, data = login_Data, headers = headers)                             # Making a POST Request with Headers and Data we defined just above
  
  
  #Checking if the request was successfull, in our case, checking the login is successfull or not
  if (r.status_code == 200):
    print("POST Request Successfull" )

  lock.release()

threads = int(input(f'Threads: '))

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = main).start()
        except:
            pass


