import urllib.request, urllib.error
import json
import sys
import db

# list of sofware names to check by default
names = ["java", "nginx", "varnish", "terraform"]
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
        with urllib.request.urlopen(github_url_tags.format(name)) as url:
            json_data = json.loads(url.read().decode())
            date = ' '
            repo_name = name.split('/')[1]
            version = json_data[0]['name']
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
        github_url_tags(name)
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
        # print('HTTPError: {} Github repository {} not found!'.format(e.code, name))
        return(check_github_tags(name))
        
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        
def check_versions(names):
    versions = []
    for name in names:
        if name in db.supported:
            name = db.supported[name]
            
        if "/" in name:
            name, version, date = check_github(name)
            print_version(name, version, date)
            versions.append([name, version, date])
        else:
            name, version, date = check_eoflife(name)
            print_version(name, version, date)
            versions.append([name, version, date])
    return(versions)
    
def save_html(versions):
    html_header = """<html><head><title>Versions</title></head>
    <body>
    <table class="tg">
    <thead>
    <tr>
        <th>Name</th>
        <th>Version</th>
        <th>Release Date</th>
    </tr>
    """
    html_footer = """
    </tbody>
    </table>
    </body>
    </html>
    """
    with open("html/index.html", "w") as txt_file:
        txt_file.write(html_header)
        for line in versions:
            txt_file.write('<tr>\n')
            for value in line:
                txt_file.write("<td>{}</td>".format(value) + "\n")
            txt_file.write('</tr>\n')
        txt_file.write(html_footer)
                
def main():  
    global table   
    global names    
    global html

    table = False
    html = False       
    if len(sys.argv) >1 and sys.argv[1] == '-t':    
        table = True
    elif len(sys.argv) >1 and sys.argv[1] == '-html':
        html = True

    if len(sys.argv) >1 and  not sys.argv[1].startswith('-'):
        names = []
        names.append(sys.argv[1])

    if table :
        print("||{:<10}||{:<10}||{:<10}||".format("Name", "Version", "Release Date"))
    else:   
        print("{:<10} {:<10} {:<10}\n".format("Name", "Version", "Release Date"))
    
    versions = check_versions(names)
    if html: save_html(versions)
    
if __name__ == '__main__':
    main()