from mastodon import Mastodon
import html2text
import getpass
import os.path
import configparser
from rich import print
from rich.markdown import Markdown
from .commandline import *
from .commands import *

ver = "0.0.1"
codename = "Rat :rat:"
art = r'''[bold magenta] __  __           _        _     _            
|  \/  | __ _ ___| |_ ___ | |   (_)_ __   ___ 
| |\/| |/ _` / __| __/ _ \| |   | | '_ \ / _ \
| |  | | (_| \__ \ || (_) | |___| | | | |  __/
|_|  |_|\__,_|___/\__\___/|_____|_|_| |_|\___|[/]'''


if os.path.isfile("../settings.ini") == False:
    print("setting up program files")
    f = open("../settings.ini", "x")
    f.close()
    config = configparser.ConfigParser()
    config.read("../settings.ini")
    config["DEFAULT"]["instance"] = "mstdn.social"
    f = open("settings.ini", "w")
    config.write(f)
    f.close()
mastodon = Mastodon(client_id = 'UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8', client_secret="QF73HqmXfJfKQVQYL6Ze_C-6qC67TKgpYlXX-HslOTI", api_base_url="https://mstdn.social")

#first time use
if os.path.isfile("../user.secret") == False:
    url = mastodon.auth_request_url(client_id="UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8", redirect_uris='urn:ietf:wg:oauth:2.0:oob', scopes=['read', 'write', 'follow', 'push'])
    code = getpass.getpass(prompt="Type in your code (" +url+ "): ")
    at = mastodon.log_in(code=code, to_file="../user.secret")
    
h = html2text.HTML2Text()

print("[bold blue]Logging On[/bold blue]")

mastodon = Mastodon(access_token="../user.secret", api_base_url="https://mstdn.social")
timeline = mastodon.timeline_home(limit=100)
posts = []
for post in timeline:
    posts.append(post)

list = List(posts)
refresh = Refresh(mastodon, posts)
reply = Reply(mastodon)
toot = Toot(mastodon)
view = View(posts)
close = Quit("Are you sure?")
hlp = Help()
about = About(codename, ver, art)

cmdline = CommandLine(mastodon.me().acct, "~>", [list, refresh, reply, toot, close, hlp, about], view)

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
