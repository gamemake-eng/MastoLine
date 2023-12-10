from mastodon import Mastodon
import html2text
import getpass
import os.path
import configparser
from rich import print
#from rich.console import Console
from rich.markdown import Markdown

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
print("logging on")
mastodon = Mastodon(access_token="user.secret", api_base_url="https://mstdn.social")
timeline = mastodon.timeline_home(limit=100)
posts = []
for post in timeline:
    posts.append(post)


def listposts():
    timeline = mastodon.timeline_home(limit=100)
    for i in range(len(posts)):
        post = posts[i]
        print(str(i)+" | "+post.account.acct)
    print("type id# to view a post")

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
        print("that's not a number!")

def post():
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
print("Welcome to mastoline! Mastodon on your terminal!")
print("------------------------------------")
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
        post()
    elif (cmd == "help") or (cmd == "h"):
        print("NOTE: none of these commands have arguments")
        print("# - view post of id")
        print("list/l - lists the user's timeline with it's id next to it")
        print("refresh/f - refreshes the timeline")
        print("reply/r - replies to a post from reply id")
        print("toot/t - posts a status on mastodon")
    elif (cmd == "exit") or (cmd == "e"):
        exit()
    else:
        if cmd.isnumeric() and int(cmd) < 40:
            post = posts[int(cmd)]
            view(post)
        else:
            print("It's not existing :star:")

        


