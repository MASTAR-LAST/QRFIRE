import os
from sys import stdout
from time import sleep
from typing import Union
from types import NoneType
from subprocess import check_output
from qrcode import make
from colorama import Fore, Style

# Tool made by Muhammed Alkohawaldeh
# Github: https://github.com/MASTAR-LAST

def sprint(text, second=0.03):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)


print(f"""{Fore.LIGHTCYAN_EX}{Style.BRIGHT}
  _______ _______ _______ ___ _______ _______ 
 |   _   |   _   |   _   |   |   _   |   _   |
 |.  |   |.  l   |.  1___|.  |.  l   |.  1___|
 |.  |   |.  _   |.  __) |.  |.  _   |.  __)_ 
 |:  1   |:  |   |:  |   |:  |:  |   |:  1   |
 |::..   |::.|:. |::.|   |::.|::.|:. |::.. . |
 `----|:.`--- ---`---'   `---`--- ---`-------'
      `--'                                    
{Fore.BLUE}QR code generator Made by {Fore.GREEN}Muhammed Alkohawaldeh
{Fore.RESET}{Style.RESET_ALL}""")
class QRG:
    def __init__(self, *, contant, imagename, savepath, extension):
        self.contant = contant
        self.imagename = imagename
        self.savepath = savepath
        self.extension = extension
        self.info_shower()
        self.create_qrcode_image()

    def create_qrcode_image(self):

        try:
            img = make(self.contant)

            img.save(f"{self.savepath}/{self.imagename}.{self.extension}", f"{str(self.extension).upper()}")
        except KeyError:
            sprint(f"{Fore.RED}This extension is not availble{Fore.RESET}")
            exit(1)

    def info_shower(self):
        sprint(f"{Style.BRIGHT}Image name: {Fore.CYAN}{self.imagename}{Fore.RESET}{Style.RESET_ALL}")
        sprint(f"{Style.BRIGHT}Image path: {Fore.CYAN}{self.savepath}{Fore.RESET}{Style.RESET_ALL}")
        sprint(f"{Style.BRIGHT}Image extension: {Fore.CYAN}{self.extension}{Fore.RESET}{Style.RESET_ALL}\n")


if __name__ == '__main__':
    import argparse as par

    parser = par.ArgumentParser(prog='qrfire', description='QR code generator')
    parser.add_argument('contant', help='the contant that will be coded')
    parser.add_argument('-p', '--path', help='Specify a path to save the image')
    parser.add_argument('-n', '--name', help='Specify the name of the image to save')
    parser.add_argument('-e', '--extension', help='Determine the extension of the image')
    args = parser.parse_args()

    curront_path: str = check_output('pwd').decode('utf-8').strip().replace("\\", " ")
    default_ext: str = 'png'

    contant: str = args.contant
    imagename: str = args.name
    path: str = args.path
    extension: str = args.extension
    cases_list: list[Union[str, None]] = [contant, imagename, path, extension]

    match cases_list:
        case [str(), NoneType(), str(), str()]:
            QRG(contant=contant, imagename=contant+'_qrcode', savepath=path, extension=extension)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{path}{Fore.RESET}')

        case [str(), str(), NoneType(), str()]:
            QRG(contant=contant, imagename=imagename, savepath=curront_path, extension=extension)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{curront_path}{Fore.RESET}')

        case [str(), str(), str(), NoneType()]:
            QRG(contant=contant, imagename=imagename, savepath=path, extension=default_ext)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{path}{Fore.RESET}')

        case [str(), str(), NoneType(), NoneType()]:
            QRG(contant=contant, imagename=imagename, savepath=curront_path, extension=default_ext)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{curront_path}{Fore.RESET}')

        case [str(), NoneType(), NoneType(), str()]:
            QRG(contant=contant, imagename=contant+'_qrcode', savepath=curront_path, extension=extension)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{curront_path}{Fore.RESET}')

        case [str(), NoneType(), str(), NoneType()]:
            QRG(contant=contant, imagename=contant+'_qrcode', savepath=path, extension=default_ext)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{path}{Fore.RESET}')

        case [str(), NoneType(), NoneType(), NoneType()]:
            QRG(contant=contant, imagename=contant+'_qrcode', savepath=curront_path, extension=default_ext)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{curront_path}{Fore.RESET}')
        
        case _:
            QRG(contant=contant, imagename=imagename, savepath=path, extension=extension)
            sprint(f'{Fore.GREEN}Done! in {Fore.LIGHTMAGENTA_EX}{path}{Fore.RESET}')