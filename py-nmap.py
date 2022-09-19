# /usr/bin/python3

# Возможно мой код == говно_код 

# if moy_cod == govno_kod:
    #print('ne yuzay moy script!')

import nmap
import socket
import time
import os
import sys 

# Фрагменты цвета

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

error  = f"{blue}[{white}!{blue}] {red}"

success = f"{yellow}[{white}√{yellow}] {green}"

ask  =     f"{green}[{white}?{green}] {yellow}"

info  =   f"{yellow}[{white}+{yellow}] {cyan}"

info2  =   f"{green}[{white}•{green}] {purple}"


if not os.geteuid() == 0:
    sys.exit("\nТолько root может запустить этот скрипт\n")


nm = nmap.PortScanner()
clear = lambda: os.system('clear')
clear()

main_menu = f"""{blue}
{nc}________________________________________________________________________{nc}

                 ____        _   _                      ® 
                |  _ \ _   _| \ | |_ __ ___   __ _ _ __  
                | |_) | | | |  \| | '_ ` _ \ / _` | '_ \ 
                |  __/| |_| | |\  | | | | | | (_| | |_) |
                |_|    \__, |_| \_|_| |_| |_|\__,_| .__/ 
                       |___/                      |_|

                        {info}VERSION-TOOL: 1.0{cyan}
                     {info}By MYTHON-DEV or MYTH-DEV{red}
            {info}Instagram: @mython_dev and @hackingworld_d
{nc}________________________________________________________________________{nc}

        !Введите тип сканирования, которое вы хотите запустить!

{white}1){white} {yellow}Сканирование всех портов tcp!{yellow}
{white}2){white} {yellow}Обноружение ОС.{yellow}
{white}3){white} {yellow}Сканирование UDP.{yellow}
{white}4){white} {yellow}Сканирование всех известных уязвимостей.{yellow}
{white}5){white} {yellow}Сканирование всех известный портов.{yellow}
{white}6){white} {yellow}Посмотреть IP сайта(хост)\n{yellow}
{white}0){white} {red}Выйти!{red}
"""

print(main_menu)


try:

    choose = input(f'{info2}{nc}Py-Nmap:~# {nc}')

except KeyboardInterrupt:
    print(f'\n{error}Что-то не так!')
    time.sleep(0.5)
    exit(f'{success}Выход!')

def main():
    if  choose == '1':
        try:
            host_tcp_partov_all = input(f'{info}Введите ip или domen хоста: {nc}')
            print()
            print(f'{error}Cканируется 65000 портов! вы должны ждать примерно 5-15 минуты. Зависит от вашего интернета!')

            nm.scan(host_tcp_partov_all,'1-65000')
            for host in nm.all_hosts(): 
                print('Хост : %s (%s)' % (host,nm[host].hostname()))
                print('Статус : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Протокол : %s' % proto )
                    lport = nm[host][proto].keys()
                for port in lport:                                                            
                    print('Порт : %s\tstate : %s' %(port,nm[host][proto][port]['state'])) 


        except KeyboardInterrupt:
            time.sleep(0.5)
            print(f'{success}Выход!')
            exit()

    elif choose == '2':
        print()
        try:
            host_find_os = input(f'{info}Введите ip хоста: {nc}')
            print(nm.scan(host_find_os, arguments="-O")['scan'][host_find_os]['osmatch'][1])
            
        except KeyError:
            print(f'\n{error}Нет такго хоста или не удалось сканировать попробуйте дать верный ip хоста.')
        except KeyboardInterrupt:
            print(f'{success}Выход!')
        except nmap.nmap.PortScannerError:
            print('Запустите через sudo')

    elif choose == '3':
        try:
            host_udp_portov = input(f'{info}Введите ip хоста: {nc}')
            print(f'{ask}Вы должны ждать примерно 3-5 минуты. Зависит от вашего интернета!')
            print()
            nm.scan(host_udp_portov, '1-1024', '-v -sU')
            print(nm.scaninfo())
            print(f"{info}Статус хоста: ", nm[host_udp_portov].state())
            print(f"{info}protocols:",nm[host_udp_portov].all_protocols())
            print(f"{info}Open Ports: ", nm[host_udp_portov]['udp'].keys())

        except KeyboardInterrupt:
            print(f'{success}Выход!')
    elif choose == '4':
        time.sleep(0.5)
        print(f'{error}Это функция пока не доступно!')

    elif choose == '5':
        try:
            print()
            host_tcp_popular = input(f'{info}Введите ip или domen хоста: {nc}')
            print()
            print(f'{error}Вы должны ждать примерно 1-3 минуты. Зависит от вашего интернета!')

            nm.scan(host_tcp_popular,'21-1024')
            for host in nm.all_hosts(): 
                print(f'{success}Хост : %s (%s)' % (host,nm[host].hostname()))
                print(f'{success}Статус : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Протокол : %s' % proto )
                    lport = nm[host][proto].keys()
                for port in lport:                                                            
                    print(f'{info}{white}Порт : %s Статус : %s' % (port,nm[host][proto][port]['state']))

        except KeyboardInterrupt:
            time.sleep(0.5)
            print(f'{success}Выход!') 

    elif choose == '6':
        print()
        hostname = input(f'{info}Введите домен сайта(example.com): {nc}')
        print()
        try:
            print(f'{success}: {hostname}\n {success}IP адрес: {socket.gethostbyname(hostname)}')
        except socket.gaierror:
            print(f'{error}Не существует DOMEN: {hostname}')

    elif choose == '0':
        exit(f'{success}Выход!')

    else:
        print(f'{error}Не существует такая функция.')
            
main()