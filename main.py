from mastodon import Mastodon
import html2text
import getpass

mastodon = Mastodon(client_id = 'UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8', client_secret="QF73HqmXfJfKQVQYL6Ze_C-6qC67TKgpYlXX-HslOTI", api_base_url="https://mstdn.social")
url = mastodon.auth_request_url(client_id="UOinO8Y9pqA4JmlF_WMz4kwB8QYWKqapLCV3gNB16h8", redirect_uris='urn:ietf:wg:oauth:2.0:oob', scopes=['read', 'write', 'follow', 'push'])
code = getpass.getpass(prompt="Type in your code (" +url+ "): ")
h = html2text.HTML2Text()
at = mastodon.log_in(code=code)
mastodon = Mastodon(access_token=at, api_base_url="https://mstdn.social")
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

def reply():
    rid = input("what is the the reply id of the post? ")
    con = input("> ")
    mastodon.status_post(con, in_reply_to_id=rid)

def post():
    con = input("> ")
    mastodon.toot(con)

def view(post):
    print("----------------------------------")
    print(post.account.acct)
    print("----------------------------------")
    print("Created " + str(post.created_at))
    print("----------------------------------")
    print(h.handle(post.content))
    print("----------------------------------")
    print(str(post.reblogs_count) + " Reblogs")
    print(str(post.favourites_count) + " Likes")
    print("reply id: " + str(post.id))
    print("use command reply or r to reply to this post")


while (True):
    user = mastodon.me()
    cmd = input(user.acct+" ~> ")
    
    if (cmd == "list") or (cmd == "l"):
        listposts()
    elif (cmd == "reply") or (cmd == "r"):
        reply()
    elif (cmd == "toot") or (cmd == "t"):
        post()
    elif (cmd == "exit") or (cmd == "e"):
        exit()
    else:
        post = posts[int(cmd)]
        view(post)

        


