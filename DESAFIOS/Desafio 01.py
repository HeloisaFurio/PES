import time
import os

verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
branco = "\033[37m"
reset = "\033[0m"

bandeira = f"""
{verde}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{amarelo}⠟⠋⠙⠻{verde}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿{amarelo}⡿⠟⠋⣀⣠⣤⣤⣄⣀⠉⠻⢿{verde}⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿{amarelo}⠿⠛⠉⠄⢠{azul}⣾⣿⣿⣿⣿⣿⣿⣷{amarelo}⡄⠄⠉⠛⠿{verde}⣿⣿⣿⣿⣿⣿
⣿⣿⣿{amarelo}⠿⠛⠁⠄⠄⠄⠄{azul}⣔⣷⣷⣦⣤⣬{branco}⣹{azul}⡛⠿⣿⡄{amarelo}⠄⠄⠄⠄⠙⠿{verde}⣿⣿⣿
⣿⣿⣿{amarelo}⣶⣄⡀⠄⠄⠄⠄{azul}⣿⣻⢿⣿⣿⣟{branco}⣿{azul}⣿⡾⣌⠁{amarelo}⠄⠄⠄⠄⣠⣴{verde}⣿⣿⣿
⣿⣿⣿⣿⣿⣿{amarelo}⣶⣤⡀⠄⠘{azul}⢿⣿⣿⣿⣿⣽⣏⡿⠃{amarelo}⠄⢀⣤⣶{verde}⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿{amarelo}⣷⣦⣄⠉⠙⠛⠛⠛⠉⣀⣴⣾{verde}⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{amarelo}⣷⣦⣄⣠⣴⣾{verde}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{reset}
"""

brazil = """
88                                              88
88                                           88 88
88                                              88
88,dPPYba,  8b,dPPYba,  ,adPPYYba, 888888888 88 88
88P'   "8a  88P' "Y8    ""     `Y8    a8P"   88 88
88     d8   88          ,adPPPPP88  ,d8P'    88 88
88b, ,a8"   88          88,    ,88 ,d8"      88 88
8Y"Ybbd8"'  88          `"8bbdP"Y8 888888888 88 88888888
"""

while True:
    os.system("cls")  # se não limpar, troca por "clear"
    print(bandeira)
    time.sleep(3)

    os.system("cls")
    print(brazil)
    time.sleep(3)