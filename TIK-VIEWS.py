import os, time, requests, random
try:from user_agent import generate_user_agent
except ModuleNotFoundError:
    os.system('pip install user_agent')
    os.system('clear')
    from user_agent import generate_user_agent
from user_agent import generate_user_agent
user_agent = generate_user_agent()
g = '\x1b[1;32m'
r = '\x1b[1;31m'
b = '\x1b[1;34m'
c = '\x1b[1;36m'
w = '\x1b[1;37m'
def wait():
    for i in range(100):
        print(f'\n\n{g}[ + ] Wait 2 Menite For Next Submit : {i + 1}/120', end='\r')
        time.sleep(1)
        os.system('clear')
class TikDemoVeiw:
    def __init__(self):print("DEVLOPER: @N_C_P")
    def boost_video(self, user: str, link: str) -> dict:
        response = requests.post('https://api.likesjet.com/freeboost/3', json={'link': link, 'tiktok_username': user, 'email': f'DEMOABOHSN{random.randint(10000, 99999)}@gmail.com'}, headers={'Host': 'api.likesjet.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': user_agent}).json()
        return response
def main():
    user = input(f'{c}[?]TikTok UserName:{w} ')
    link = input(f'{b}[?]Video Link: {w}')
    booster = TikDemoVeiw()
    response = booster.boost_video(user, link)
    if response.get('status'):
        print(f'{g}[√] Successfully 1000 View send ENJOY YOU{w}')
        wait()
        main()
    else:
        print(f"{r}[\u200c#] SORRY I CAN'T SEND VIEW IN YOUR VIDEO{w}")
        wait()
        main()
main()