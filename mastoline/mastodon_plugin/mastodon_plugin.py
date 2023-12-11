from mastodon import Mastodon
import html2text
import getpass
import os.path
import configparser
from rich import print
from rich.markdown import Markdown
from .commands import *
import os

file_path = os.path.dirname(__file__)+"/../"
print(file_path)

class Plugin:
    def __init__(self, codename, ver, art):

        if os.path.isfile(file_path+"../mastodon.ini") == False:
            print("setting up program files")
            f = open(file_path+"../mastodon.ini", "x")
            f.close()
            config = configparser.ConfigParser()
            config.read(file_path+"../mastodon.ini", encoding="utf-8")
            config["DEFAULT"]["instance"] = "mstdn.social"
            f = open(file_path+"../mastodon.ini", "w", encoding="utf-8")
            config.write(f)
            f.close()


        mastodon = Mastodon(client_id = 'UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8', client_secret="QF73HqmXfJfKQVQYL6Ze_C-6qC67TKgpYlXX-HslOTI", api_base_url="https://mstdn.social")

        #first time use
        if os.path.isfile(file_path+"../user.secret") is False:
            url = mastodon.auth_request_url(client_id="UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8", redirect_uris='urn:ietf:wg:oauth:2.0:oob', scopes=['read', 'write', 'follow', 'push'])
            code = getpass.getpass(prompt="Type in your code (" +url+ "): ")
            at = mastodon.log_in(code=code, to_file=file_path+"../user.secret")
            
        h = html2text.HTML2Text()

        print("[bold blue]Logging On[/bold blue]")

        mastodon = Mastodon(access_token=file_path+"../user.secret", api_base_url="https://mstdn.social")
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
        like = Like(mastodon)
        reblog = Reblog(mastodon)

        self.commands = [list, refresh, reply, like, reblog, toot, close, hlp, about]
        self.view = view

