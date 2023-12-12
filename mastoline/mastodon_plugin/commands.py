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
        rid = input("what is the the reply id of the post? ")
        if rid.isnumeric():
            con = input("> ")
            mastodon.status_post(con, in_reply_to_id=rid)
        else:
            print("[red]that's not a number![/red]")

class Like:
    def __init__(self, mastodon):
        self.m = mastodon

    def run(self, prams = []):
        mastodon = self.m
        rid = input("what is the the reply id of the post? ")
        if rid.isnumeric():
            conf = input("Are you sure? (y/n) ")
            if conf[0] == "y":
                mastodon.status_favourite(int(rid))
            else:
                print("ok")
        else:
            print("[red]that's not a number![/red]")

class Reblog:
    def __init__(self, mastodon):
        self.m = mastodon

    def run(self, prams = []):
        mastodon = self.m
        rid = input("what is the the reply id of the post? ")
        if rid.isnumeric():
            conf = input("Are you sure? (y/n) ")
            if conf[0] == "y":
                mastodon.status_reblog(int(rid))
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
            print("use command follow to follow to this user")

        try:
            con = prams[1]
            if con.lower() == "me":
                user = mastodon.me()
                display(user.acct, user.url, user.id, user.following_count, user.followers_count, user.statuses_count, user.note, user.bot)

            else:      
                try:
                    userid = mastodon.account_lookup(con).id
                    user = mastodon.account(userid)
                    display(user.acct, user.url, user.id, user.following_count, user.followers_count, user.statuses_count, user.note, user.bot)

                except:
                    print("User not found 😑")
        except: 
            print("No user specified")

        

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
        print("[bold cyan]reply[/] - replies to a post from reply id")
        print("[bold cyan]like[/] - likes a post from reply id")
        print("[bold cyan]reblog[/] - reblogs a status from it's reply id")
        print("[bold cyan]toot[/] - posts a status on mastodon")
        print("[bold cyan]user[/] - view a user on mastodon")
        print("[bold cyan]quit[/] - exit out of MastoLine")
        print("[bold cyan]about[/] - find into about Mastoline")

class About:
    def __init__(self, codename, ver, art):
        self.c = codename
        self.v = ver
        self.a = art
    def run(self):
        print(self.a)
        print("[bold pink]Ver "+self.v+"[/] "+self.c)
