from rich import print
from rich.markdown import Markdown
import html2text
h = html2text.HTML2Text()

class List:
    def __init__(self, posts):
        self.p = posts
    def run(self):
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
    def run(self):
        posts = self.p
        mastodon = self.m
        timeline = mastodon.timeline_home(limit=100)
        posts = []
        for post in timeline:
            posts.append(post)
    

class Reply:
    def __init__(self, mastodon):
        self.m = mastodon
        
    def run(self):
        mastodon = self.m
        rid = input("what is the the reply id of the post? ")
        if rid.isnumeric():
            con = input("> ")
            mastodon.status_post(con, in_reply_to_id=rid)
        else:
            print("[red]that's not a number![/red]")


class Toot:
    def __init__(self, mastodon):
        self.m = mastodon
    def run(self):
        mastodon = self.m

        con = input("> ")
        mastodon.toot(con)

class View:
    def __init__(self, posts):
        self.p = posts
        
    def run(self, pt):
        post = self.p[pt]
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

class Quit:
    def __init__(self, prompt):
        self.p = prompt + " (y/n) "
    def run(self):
        ans = input(self.p)
        if ans[0] == "y":
            exit()
        else:
            print("ok")

class Help:
    def __init__(self):
        pass

    def run(self):
        print("NOTE: none of these commands have arguments")
        print("[bold cyan]#[/] - view post of id")
        print("[bold cyan]list[/] - lists the user's timeline with it's id next to it")
        print("[bold cyan]refresh[/] - refreshes the timeline")
        print("[bold cyan]reply[/] - replies to a post from reply id")
        print("[bold cyan]toot[/] - posts a status on mastodon")
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