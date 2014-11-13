import urllib.request
r = urllib.request.urlopen("http://sports.espn.go.com/nfl/bottomline/scores").read()
print(type(r.split('&')))
