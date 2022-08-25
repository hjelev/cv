import urllib.request
import json
import sys
 
names = ["aristocratos/btop","java", "nginx", "varnish", "hashicorp/terraform"]
github_url = "https://api.github.com/repos/{}/releases/latest"
endoflife_url = "https://endoflife.date/api/{}.json"
 
def check_eoflife(name):
    with urllib.request.urlopen(endoflife_url.format(name)) as url:
        data = json.loads(url.read().decode())
        if len(sys.argv) >1:
            print("|{:<10}|{:<10}|{:<10}|".format(name, data[0]['latest'],data[0]['releaseDate']))
        else:
            print("{:<10} {:<10} {:<10}".format(name, data[0]['latest'],data[0]['releaseDate']))
 
def check_github(name):
    with urllib.request.urlopen(github_url.format(name)) as url:
        data = json.loads(url.read().decode())
        if len(sys.argv) >1:
            print("|{:<10}|{:<10}|{:<10}|".format(name.split('/')[1], data['name'].split('v')[1], data['created_at'].split('T')[0]))
        else:
            print("{:<10} {:<10} {:<10}".format(name.split('/')[1], data['name'].split('v')[1], data['created_at'].split('T')[0]))
 
def check_versions(names):
    for name in names:
        if "/" in name:
            check_github(name)
        else:
            check_eoflife(name)
 
if len(sys.argv) >1 :
    print("||{:<10}||{:<10}||{:<10}||".format("Name", "Version", "Release Date"))
else:   
    print("{:<10} {:<10} {:<10}\n".format("Name", "Version", "Release Date"))
 
check_versions(names)