from distutils.command.upload import upload
import speedtest
from time import sleep
speed = speedtest.Speedtest()
option = int(input('''Select your option:
1. Download speed⬇
2. Upload speed⬆
3. Download & Upload speed ↕
4. Ping᭼
'''))
if option < 1 or option > 4:
    sleep(2)
    print('🤖 Sorry, you have entered the wrong option')

    
    if option == 1:
        print(f'The download speed is ', download_speed, ' Mbps')
    elif option == 2:
        print(f'The upload speed is ', upload_speed, ' Mbps')
    elif option == 3:
        print(f'The download speed is ', download_speed,
              ' Mbps and \n the upload speed is ', upload_speed)
    elif option == 4:
        s = []  # empty list
        speed.get_servers(s)
        print('Your ping is ', speed.results.ping, ' ms')
    else:
        print('🤖uhuh, something went wrong please try again')
