from pyclbr import Class
from rich import print
from rich.markdown import Markdown
import html2text
h = html2text.HTML2Text()

class List:
    def __init__(self, posts):
        self.p = posts
    def run(self, prams = []):
        posts = self.p
        print("id | user")
        for i in range(len(posts)):
            post = posts[i]
            print(str(i)+" | "+post.account.acct)
        print("type the id # to view a post")

class Refresh:
    def __init__(self, mastodon, posts):
        self.p = posts
        self.m = mastodon
    def run(self, prams = []):
        posts = self.p
        mastodon = self.m
        timeline = mastodon.timeline_home(limit=100)
        posts = []
        for post in timeline:
            posts.append(post)
    

class Reply:
    def __init__(self, mastodon):
        self.m = mastodon
        
    def run(self, prams = []):
        mastodon = self.m
        try:
            rid = prams[1]
        except:
            print("[red]Did not provide id[/]")
            print("Type help to view all of the commands")
        else:
            if rid.isnumeric():
                con = input("> ")
                try:
                    mastodon.status_post(con, in_reply_to_id=rid)
                except:
                    print("[red]Post not found[/]")
            else:
                print("[red]that's not a number![/red]")

class Like:
    def __init__(self, mastodon):
        self.m = mastodon

    def run(self, prams = []):
        mastodon = self.m
        try:
            rid = prams[1]
        except:
            print("[red]Did not provide id[/]")
            print("Type help to view all of the commands")
        else:
            if rid.isnumeric():
                conf = input("Are you sure? (y/n) ")
                if conf[0] == "y":
                    try:
                        mastodon.status_favourite(int(rid))
                    except:
                        print("[red]Post not found[/]")
                else:
                    print("ok")
            else:
                print("[red]that's not a number![/red]")

class Reblog:
    def __init__(self, mastodon):
        self.m = mastodon

    def run(self, prams = []):
        mastodon = self.m
        try:
            rid = prams[1]
        except:
            print("[red]Did not provide id[/]")
            print("Type help to view all of the commands")
        else:
            if rid.isnumeric():
                conf = input("Are you sure? (y/n) ")
                if conf[0] == "y":
                    try:
                        mastodon.status_reblog(int(rid))
                    except:
                        print("[red]Post not found[/]")
                else:
                    print("ok")
            else:
                print("[red]that's not a number![/red]")    
        

class Toot:
    def __init__(self, mastodon):
        self.m = mastodon
    def run(self, prams = []):
        mastodon = self.m

        con = input("> ")
        mastodon.toot(con)

class User:
    def __init__(self, mastodon):
        self.m = mastodon
    def run(self, prams = []):
        mastodon = self.m
        
        def display(name, url, id, following, followers, posts, bio, bot):
            md = Markdown(h.handle(bio))
            if bot:
                emj = ":robot:"
            else:
                emj = ":smile:"
            print("\n----------------------------------")
            print("[bold cyan]" + name + "[/] " + emj)
            print("----------------------------------")
            print(url)
            print("----------------------------------")
            #console.print(md)
            print(md)
            print("----------------------------------")
            print(str(following) + " Following")
            print(str(followers) + " Followers")
            print("user id: " + str(id))
            print("use command follow (username) to follow to this user")

        try:
            con = prams[1]
        except: 
            print("[red]No user specified[/]")
            print("Type help to view all of the commands")
        else:
            if con.lower() == "me":
                user = mastodon.me()
                display(user.acct, user.url, user.id, user.following_count, user.followers_count, user.statuses_count, user.note, user.bot)

            else:      
                try:
                    userid = mastodon.account_lookup(con).id
                    user = mastodon.account(userid)
                    display(user.acct, user.url, user.id, user.following_count, user.followers_count, user.statuses_count, user.note, user.bot)

                except:
                    print("[red]User not found[/] 😑")

class Follow:
    def __init__(self,mastodon):
        self.m = mastodon
    def run(self, prams=[]):
        mastodon = self.m
        try:
            userid = mastodon.account_lookup(prams[1]).id
            mastodon.account_follow(userid)
            user = mastodon.account(userid)
            print("[bold green]Followed " + user.acct + "[/]")

        except:
            print("[red]User not found[/] 😑")


class View:
    def __init__(self, posts):
        self.p = posts
        
    def run(self, pt, prams = []):
        post = self.p[pt]
        #console = Console()
        md = Markdown(h.handle(post.content))
        print("\n----------------------------------")
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
        print("use command reply to reply to this post")

class Quit:
    def __init__(self, prompt):
        self.p = prompt + " (y/n) "
    def run(self, prams = []):
        ans = input(self.p)
        if ans[0] == "y":
            exit()
        else:
            print("ok")

class Help:
    def __init__(self):
        pass

    def run(self, prams = []):
        print("NOTE: none of these commands have arguments")
        print("[bold cyan]#[/] - view post of id")
        print("[bold cyan]list[/] - lists the user's timeline with it's id next to it")
        print("[bold cyan]refresh[/] - refreshes the timeline")
        print("[bold cyan]reply (id)[/] - replies to a post from reply id")
        print("[bold cyan]like (id)[/] - likes a post from reply id")
        print("[bold cyan]reblog (id)[/] - reblogs a status from it's reply id")
        print("[bold cyan]toot[/] - posts a status on mastodon")
        print("[bold cyan]user (username)[/] - view a user on mastodon")
        print("[bold cyan]follow (username)[/] - follow a user on mastodon")
        print("[bold cyan]quit[/] - exit out of MastoLine")
        print("[bold cyan]about[/] - find info about Mastoline")

class About:
    def __init__(self, codename, ver, art):
        self.c = codename
        self.v = ver
        self.a = art
    def run(self, prams=[]):
        print(self.a)
        print("[bold pink]Ver "+self.v+"[/] "+self.c)
