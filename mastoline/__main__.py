from mastodon import Mastodon
from .mastodon_plugin.mastodon_plugin import Plugin
import html2text
import getpass
import os.path
import configparser
from rich import print
from rich.markdown import Markdown
from .commandline import *
import os
import sys

file_path = os.path.dirname(__file__)+"/"
print(file_path)





ver = "0.0.1"
codename = "Rat :rat:"
art = r'''[bold magenta] __  __           _        _     _            
|  \/  | __ _ ___| |_ ___ | |   (_)_ __   ___ 
| |\/| |/ _` / __| __/ _ \| |   | | '_ \ / _ \
| |  | | (_| \__ \ || (_) | |___| | | | |  __/
|_|  |_|\__,_|___/\__\___/|_____|_|_| |_|\___|[/]'''


if os.path.isfile(file_path+"../settings.ini") == False:
    print("setting up program files")
    f = open(file_path+"../settings.ini", "x")
    f.close()
    config = configparser.ConfigParser()
    config.read(file_path+"../settings.ini")
    config["DEFAULT"]["instance"] = "mstdn.social"
    f = open(file_path+"../settings.ini", "w")
    config.write(f)
    f.close()

plugin = Plugin()

cmdline = CommandLine("you", "~>", [list, refresh, reply, like, reblog, toot, close, hlp, about], view)

print("------------------------------------")
print(art)
print("[bold pink]Ver "+ver+"[/] "+codename)
print("Welcome to [bold cyan]MastoLine![/] Mastodon in your terminal!")
print("------------------------------------")

def main():
    while (True):
        cmdline.run()

if __name__ == "__main__":
    main()
