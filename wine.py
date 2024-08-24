import requests
import time
import random
import os
from colorama import init, Fore
import os
import requests
import time
from colorama import Fore

init(autoreset=True)
Z = '\x1b[0;90m'
M = '\x1b[38;5;196m'
H = '\x1b[38;5;46m'
K = '\x1b[38;5;226m'
B = '\x1b[38;5;44m'
U = '\x1b[0;95m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
A = '\x1b[38;5;248m'
xx = '\x1b[0;93m'
kk = '\x1b[93m'
hh = '\x1b[1;92m'
hi = '\x1b[32m'
uu = '\x1b[95m'
kk = '\x1b[33m'
bb = '\x1b[1;96m'
pp = '\x1b[0;34m'
Z2 = '[#000000]'
M2 = '[#FF0000]'
H2 = '[#00FF00]'
K2 = '[#FFFF00]'
B2 = '[#00C8FF]'
U2 = '[#AF00FF]'
N2 = '[#FF00FF]'
O2 = '[#00FFFF]'
P2 = '[#FFFFFF]'
J2 = '[#FF8F00]'
A2 = '[#AAAAAA]'


logo = """              
  def logo():
    clear = "\x1b[0m"
    colors = [31, 32, 36, 37, 35]

 
               ⢀⣠⣤⣤⣤⣄⡀                                                              [AADI XD]  ⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀                       
             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧                                                                       ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿                       
             ⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠃                                                                         ⠉⠻⠿⠿⠿⠟⠋                         
            ⢀⣴⣶⣿⣿⣶⣄                                                                          ⢰⣿⣿⣿⣿⣿⣿⣿⣷                           
          ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇                                                                       ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                          
         ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇                                                                     ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀                        
        ⣸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣧             ⢀⣤⣶⣾⣿⣶⣶⣤⡀                                            ⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿ ⠘⢿⣿⣿⣿⣷⡀          ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄ 
       ⣼⣿⣿⣿⣿⣿⣿⣿⣿⠇  ⠈⠻⣿⣿⣿⣿⣆        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                           ⣿⣿⣿⣿⣿⣿⣿⣿⡟ ⣀⣤⣶⣶⣌⠻⣿⣿⣿⣷⡀      ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟ 
       ⠹⣿⣿⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⠄    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟  
        ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣛⣋⣼⣿⣿⣶⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠁    
        ⢸⣻⣿⡿⣿⣿⣿⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       
        ⠈⣿⣿⣿⣿⣿⣿⡆ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       
         ⣿⣿⣿⣿⣿⣿⡇ ⢻⣿⣿⣿⣿⣿⡇  ⠈⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁       
 ⣠⣴⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡇ ⠸⣿⣿⣿⣿⣿⡇      ⠹⢿⣿⣿⢿⣿⣿⣿⡿        
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣿⣿⣿⣿⣿⡇          ⢸⣿⣿⣿⣧⣄⣀⣀⣀⣀⣀⣀⡀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇          ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠛⠛⠛⠛⠛⠛⠛⠁          ⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁
\033[1;32m ----------------------------------------------------------------------------
\033[1;32m.██╗    ██╗  ██╗██████╗ 
\033[1;32m.╚██╗██╔╝██╔══██╗
\033[1;32m.╚███╔╝ ██║  ██║
\033[1;32m.██╔██╗ ██║  ██║
\033[1;32m.█╔╝ ██╗██████╔╝
\033[1;32m. 
                                                             
\033[1;32m ----------------------------------------------------------------------------
\033[1;97m╔═════════════════════════════════════════════════════════════╗                        
       \033[1;96mWelcome To Multi Token Tool By Aadi xD ; \033[1;97m                          

\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
\x1b[1;36m{•} \x1b[1;93mAUTHOR     \033[1;31m➟    \x1b[1;92m: AADI
\x1b[1;36m{•} \x1b[1;93mTOOL       \033[1;31m➟    \x1b[1;92m: COMPILE FILE
\x1b[1;36m{•} \x1b[1;93mFROM       \033[1;31m➟    \x1b[1;92m: PAKISTAN
\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═
"""

      
def line():
        print('\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═')        


def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    print(Fore.CYAN + logo)
    
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.100092686141588.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(Fore.YELLOW + f"[+] Message {message_index + 1} sent to Convo {target_id} with Token {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] Failed to send Message {message_index + 1} to Convo {target_id} with Token {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    print(Fore.CYAN + logo)    
    
    print(Fore.MAGENTA + "[•] MULTI CONVO TOOL BY AADI LEGEND")
    print(Fore.CYAN + "--------------WE ARE HERE----------------------")
    # Remake by Asmit
    tokens_file = input(Fore.YELLOW +  "\033[1;36m[+]  Enter the path to the tokens file :: \033[1;32;1m").strip();line()
    target_id = input(Fore.YELLOW +  "\033[1;36m[+]  Enter the target ID: ").strip();line()
    messages_file = input(Fore.YELLOW +  "\033[1;36m[+] Enter the path to the messages file :: \033[1;32;1m").strip();line()
    haters_name = input(Fore.YELLOW +  "\033[1;36m[+] Enter the hater's name: ").strip();line()
    speed = float(input(Fore.YELLOW +  "\033[1;36m[+] Enter the speed (in seconds) between messages:: \033[1;32;1m").strip())
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()