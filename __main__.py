from mastodon import Mastodon
import html2text
import getpass
import os.path
import configparser
from rich import print
from rich.markdown import Markdown

ver = "0.0.1"
codename = "Rat :mouse:"
art = r'''[bold magenta] __  __           _        _     _            
|  \/  | __ _ ___| |_ ___ | |   (_)_ __   ___ 
| |\/| |/ _` / __| __/ _ \| |   | | '_ \ / _ \
| |  | | (_| \__ \ || (_) | |___| | | | |  __/
|_|  |_|\__,_|___/\__\___/|_____|_|_| |_|\___|[/]'''


if os.path.isfile("settings.ini") == False:
    print("setting up program files")
    f = open("settings.ini", "x")
    f.close()
    config = configparser.ConfigParser()
    config.read("settings.ini")
    config["DEFAULT"]["instance"] = "mstdn.social"
    f = open("settings.ini", "w")
    config.write(f)
    f.close()
mastodon = Mastodon(client_id = 'UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8', client_secret="QF73HqmXfJfKQVQYL6Ze_C-6qC67TKgpYlXX-HslOTI", api_base_url="https://mstdn.social")

#first time use
if os.path.isfile("./user.secret") == False:
    url = mastodon.auth_request_url(client_id="UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8", redirect_uris='urn:ietf:wg:oauth:2.0:oob', scopes=['read', 'write', 'follow', 'push'])
    code = getpass.getpass(prompt="Type in your code (" +url+ "): ")
    at = mastodon.log_in(code=code, to_file="user.secret")
    
h = html2text.HTML2Text()

print("[bold blue]Logging On[/bold blue]")

mastodon = Mastodon(access_token="user.secret", api_base_url="https://mstdn.social")
timeline = mastodon.timeline_home(limit=100)
posts = []
for post in timeline:
    posts.append(post)


def listposts():
    timeline = mastodon.timeline_home(limit=100)
    print("id | user")
    for i in range(len(posts)):
        post = posts[i]
        print(str(i)+" | "+post.account.acct)
    print("type the id # to view a post")

def refresh():
    timeline = mastodon.timeline_home(limit=100)
    posts = []
    for post in timeline:
        posts.append(post)


def reply():
    rid = input("what is the the reply id of the post? ")
    if rid.isnumeric():
        con = input("> ")
        mastodon.status_post(con, in_reply_to_id=rid)
    else:
        print("[red]that's not a number![/red]")

def poststatus():
    con = input("> ")
    mastodon.toot(con)

def view(post):
    #console = Console()
    md = Markdown(h.handle(post.content))
    print("----------------------------------")
    print(post.account.acct)
    print("----------------------------------")
    print("Created " + str(post.created_at))
    print("----------------------------------")
    #console.print(md)
    print(md)
    print("----------------------------------")
    print(str(post.reblogs_count) + " Reblogs")
    print(str(post.favourites_count) + " Likes")
    print("reply id: " + str(post.id))
    print("use command reply or r to reply to this post")

print("------------------------------------")
print(art)
print("[bold pink]Ver "+ver+"[/] "+codename)
print("Welcome to [bold cyan]MastoLine![/] Mastodon in your terminal!")
print("------------------------------------")

def main():
    while (True):
        user = mastodon.me()
        cmd = input(user.acct+" ~> ")
    
        if (cmd == "list") or (cmd == "l"):
            listposts()
        elif (cmd == "refresh") or (cmd == "f"):
            refresh()
        elif (cmd == "reply") or (cmd == "r"):
            reply()
        elif (cmd == "toot") or (cmd == "t"):
            poststatus()
        elif (cmd == "help") or (cmd == "h"):
            print("NOTE: none of these commands have arguments")
            print("[bold cyan]#[/] - view post of id")
            print("[bold cyan]list/l[/] - lists the user's timeline with it's id next to it")
            print("[bold cyan]refresh/f[/] - refreshes the timeline")
            print("[bold cyan]reply/r[/] - replies to a post from reply id")
            print("[bold cyan]toot/t[/] - posts a status on mastodon")
            print("[bold cyan]exit/e[/] - exit out of MastoLine")
            print("[bold cyan]about/a[/] - find into about Mastoline")
        elif (cmd == "exit") or (cmd == "e"):
            exit()
        elif (cmd == "about") or (cmd == "a"):
            print(art)
            print("[bold pink]Ver "+ver+"[/] "+codename)
        else:
            if cmd.isnumeric() and int(cmd) < 40:
                post = posts[int(cmd)]
                view(post)
            else:
                print("It's not existing :star:")

if __name__ == "__main__":
    main()
