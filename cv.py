import urllib.request, urllib.error
import json
import sys
import db

names = ["btop","java", "nginx", "varnish", "terraform"]
github_url = "https://api.github.com/repos/{}/releases/latest"
github_url_tags = 'https://api.github.com/repos/{}/tags'
endoflife_url = "https://endoflife.date/api/{}.json"
 
def check_eoflife(name):
    try:
        with urllib.request.urlopen(endoflife_url.format(name)) as url:
            json_data = json.loads(url.read().decode())
            version = json_data[0]['latest']
            date  = json_data[0]['releaseDate']
            
            return(name, version, date) 
            
    except urllib.error.HTTPError as e:
        print('HTTPError: {} endoflife.date record for {} not found!'.format(e.code, name))
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
    
def print_version(name, version, date):
    if table:
        print("|{:<10}|{:<10}|{:<10}|".format(name, version, date))
    else:
        print("{:<10} {:<10} {:<10}".format(name, version, date))   
        
def check_github_tags(name):
    try:
        print(github_url_tags.format(name))
        with urllib.request.urlopen(github_url_tags.format(name)) as url:
            json_data = json.loads(url.read().decode())
            date = 'na'
            repo_name = name.split('/')[1]
            version = json_data[0]['name']
            # version = json_data['name'].replace('_','.')
            # print(json_data['name'].replace('_','.'))
            if 'v' in version:
                version = json_data['name'].split('v')[1]
            if ')' in version:
                version = version.split(')')[0]
            if 'Version' in version:
                version = version.split(' ')[2]
            if '-' in version:
                version = version.split('-')[1]

            return(repo_name, version, date)
            
    except urllib.error.HTTPError as e:
        print('HTTPError: {} Github tags for {} not found!'.format(e.code, name))
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
                         
def check_github(name):
    try:
        with urllib.request.urlopen(github_url.format(name)) as url:
            json_data = json.loads(url.read().decode())
            date = json_data['created_at'].split('T')[0]
            repo_name = name.split('/')[1]
            version = json_data['tag_name'].replace('_','.')
            if 'v' in version:
                version = json_data['name'].split('v')[1]
            if ')' in version:
                version = version.split(')')[0]
            if 'Version' in version:
                version = version.split(' ')[2]
            if '-' in version:
                version = version.split('-')[1]

            return(repo_name, version, date) 
    
    except urllib.error.HTTPError as e:
        print('HTTPError: {} Github repository {} not found!'.format(e.code, name))
        return(name, "", "")
        
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        
def check_versions(names):
    for name in names:
        if name in db.supported:
            name = db.supported[name]
            
        if "/" in name:
            # print(check_github(name))
            name, version, date = check_github(name)
            print_version(name, version, date)
        else:
            name, version, date = check_eoflife(name)
            print_version(name, version, date)
            
def main():  
    global table   
    global names    
       
    if len(sys.argv) >1 and sys.argv[1].startswith('-'):    
        table = True
    else:
        table = False

    if len(sys.argv) >1 and  not sys.argv[1].startswith('-'):
        names = []
        names.append(sys.argv[1])

    if table :
        print("||{:<10}||{:<10}||{:<10}||".format("Name", "Version", "Release Date"))
    else:   
        print("{:<10} {:<10} {:<10}\n".format("Name", "Version", "Release Date"))
    
    check_versions(names)

if __name__ == '__main__':
    main()