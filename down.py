import urllib3
http = urllib3.PoolManager()

'''Utility script to download tagged images to put into training folders'''

urls = [
    "https://kicat.net/i/DW1FSJc8Ac.png",
    "https://kicat.net/i/nEGkgfFbsk.png",
    "https://kicat.net/i/mun38ABwSW.png",
    "https://kicat.net/i/TgI96VLQFb.png",
    "https://kicat.net/i/cg0gzN50m9.png"

]
N = 1

for url in urls:
    r = http.request('GET', url)
    Name = str(N+1)
    N += 1
    with open("1"+Name+".png", "wb") as fcont:
        fcont.write(r.data)
