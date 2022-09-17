from re import I
import urllib.request, urllib.error
import json
import sys
import db
import datetime
import os
import collections

# list of sofware names to check by default
default_names = ["php", "apache"]
github_api = 'https://api.github.com/repos/{}'
github_url = 'https://api.github.com/repos/{}/releases/latest'
github_url_tags = 'https://api.github.com/repos/{}/tags'
endoflife_url = 'https://endoflife.date/api/{}.json'
html_file = os.path.join(sys.path[0], "html/index.html")


def check_eoflife(name):
    try:
        with urllib.request.urlopen(endoflife_url.format(name)) as url:
            json_data = json.loads(url.read().decode())
            try:
                version = json_data[0]['latest']
            except:  
                version = json_data[0]['cycle']
            date  = json_data[0]['releaseDate']
            try:
                link = json_data[0]['link']
            except:
                link = 'https://endoflife.date/{}'.format(name)
                
            return(name, version, date, link) 
            
    except urllib.error.HTTPError as e:
        search_supported(name)
        # print('HTTPError: {} endoflife.date record for {} not found!'.format(e.code, name))
        # exit()
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        exit()

   
def print_version(versions, options):
    if 'table' in options :
        print("||{:<28}||{:<8}||{:<15}||{}||".format("Name", "Version", "Release Date","Link"))
    elif 'silent' in options or 'simple' in options:
        pass
    else:   
        print("{:<30} {:<10} {:<15} {}\n".format("Name", "Version", "Release Date", "Link"))
        
    for version in versions:       
        original_name, name, version, date, link, *_ = version
        if 'table' in options:
            print("|{:<29}|{:<9}|{:<17}|{:<60}|".format(name, version, date, link))
        elif 'silent' in options:
            print("{:<9}".format( version))
        else:
            print("{:<30} {:<10} {:<15} {}".format(name, version, date, link))   

    if len(versions) == 1 and original_name in db.supported and \
                                    not 'silent' in options and \
                                    not 'simple' in options and \
                                    not 'table' in options:
        print('\nDescription: ' + get_github_description(db.supported[original_name]))        


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

      
def check_github_tags(name):
    try:
        with urllib.request.urlopen(github_url_tags.format(name)) as url:
            json_data = json.loads(url.read().decode())
            for tag_data in reversed(json_data):
                if has_numbers(tag_data['name']) and 'dev' not in tag_data['name']\
                                                 and 'alpha' not in tag_data['name']\
                                                 and 'dev' not in tag_data['name']:
                    json_data = tag_data
                    
            date = json_data['commit']['url']

            with urllib.request.urlopen(date) as url:
                json_data_tag = json.loads(url.read().decode())
                date = json_data_tag['commit']['author']['date'].split('T')[0]

            repo_name = name.split('/')[1]
            version = json_data['name']

            if 'v' in version:
                version = json_data['name'].split('v')[1]
            if ')' in version:
                version = version.split(')')[0]
            if 'version' in version.lower():
                version = version.split(' ')[2]
            if '-' in version:
                for v in version.split('-'):                
                    if not any(c.isalpha() for c in v):
                        version = v
            if '/' in version:
                 for v in version.split('/'):                
                    if not any(c.isalpha() for c in v):
                        version = v  
            link = f'https://github.com/{name}'
            if repo_name == 'nginx': link = 'https://nginx.org/en/CHANGES'
            
            return(repo_name, version, date, link)
            
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print('Github API rate limit exceeded')
            exit()
        print('HTTPError: {} Github tags for {} not found!'.format(e.code, name))
        exit()
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))


def get_github_description(repo):          
    try:
        with urllib.request.urlopen(github_api.format(repo)) as url:
            json_data = json.loads(url.read().decode())
            description = json_data['description']
            return(description)
            
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print('Github API rate limit exceeded')
            exit()
        print('HTTPError: {} Github repository {} not found!'.format(e.code, repo))
       
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        
                                                     
def check_github(name):
    try:
        with urllib.request.urlopen(github_url.format(name)) as url:
            json_data = json.loads(url.read().decode())
            date = json_data['created_at'].split('T')[0]
            repo_name = name.split('/')[1]
            version = json_data['tag_name'].replace('_','.')
            link = json_data['html_url']
            
            if 'v' in version:
                version = json_data['tag_name'].split('v')[1]
            elif ')' in version:
                version = version.split(')')[0]
            elif 'Version' in version:
                version = version.split(' ')[2]
            elif '-' in version:
                for v in version.split('-'):                
                    if not any(c.isalpha() for c in v):
                        version = v
            elif '/' in version:
                 for v in version.split('/'):                
                    if not any(c.isalpha() for c in v):
                        version = v                    
            elif 'n' in version:
                version = version.split('n')[1]
            elif '@' in version:
                version = version.split('@')[1]
                
            if '_' in version:
                version = version.split('_')[0]
                
            return(repo_name, version, date, link) 
    
    except urllib.error.HTTPError as e:
        # print('HTTPError: {} Github repository {} not found!'.format(e.code, name))
        if e.code == 403:
            print('Github API rate limit exceeded')
            exit()
        elif e.code == 404:
            return(check_github_tags(name))
        else: exit()
        
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        exit()
   
        
def check_versions(names):    
    versions = []
    for name in names:
        original_name = name
        if name in db.supported:
            name = db.supported[name]
            
        if "/" in name:
            name, version, date, link = check_github(name)
            versions.append([original_name, name, version, date, link])
        else:
            name, version, date, link = check_eoflife(name)
            versions.append([original_name, name, version, date, link])
            
    return(versions)
    
    
def save_html(versions, html_file, options):
    e = datetime.datetime.now()
    timestamp = f"<p><small>Versions checked on {e.day}/{e.month}/{e.year} at {e.hour}:{e.minute}:{e.second}.</small></p>"
    html_content = db.html_header
    link = False
    for line in versions:
        if len(line) > 3:
            link = line[-1]
            line.pop()
            line.pop(0)
        
        html_content = (html_content + '    <tr>\n')
        for x, value in enumerate(line):
            if x == 1 and link:
                html_content = (html_content +\
                     "            <td><a href='{}' target='_blank'>{}</a></td>".format(link, value) + "\n")
            else:
                html_content = (html_content +\
                     "            <td>{}</td>".format(value) + "\n")
        html_content = (html_content + '    </tr>\n')
        
    html_content = (html_content + db.html_footer.format(timestamp))
    
    if 'print html' in options:
        print(html_content)
    else:
        with open( html_file, "w") as txt_file:
            try:
                txt_file.write(html_content)
                print(f'HTML result is saved as: {html_file}')
            except:
                print(f'Unable to save html file in {html_file}')


def check_arguments(arguments):
    arguments.pop(0)
    args = []
    names = []  
    for arg in arguments:
        if arg.startswith('-'): args.append(arg)
        else: names.append(arg)
    if len(names) < 1 : names = default_names
    
    return(args, names)


def search_supported(name):
        found = False
        for n, value in db.supported.items():
            if name in value:
                print('{:<30} - https://github.com/{}'.format(n, value))
                found = True
        if not found : print(f'Found no software like {name}!')
        exit()    

def process_args(args, names):
    valid_args = ['-p', '--print', '-a', '--all', '-h', \
                  '--help', '--html', '-s', '--silent', \
                  '-t', '--table', '-l', '-S', '--simple',\
                  '-f', '--find'] 
    options = []    
    if '-h' in args or '--help' in args:
        print(db.help)
        exit()
    elif '-l' in args:
        print(github_url)
        print(github_url_tags)
        print(endoflife_url)
        exit()
    elif '-t' in args or '--table' in args:
        options.append('table')
    elif '-a' in args or '--all' in args:
        for software in collections.OrderedDict(sorted(db.supported.items())):
            print('{:<30} - https://github.com/{}'.format(software, db.supported[software]))     
        print('\n{} Supported github repositories'.format(len(db.supported)))          
        exit()
    elif '--html' in args:
        options.append('html')
    elif '-s' in args or '--silent' in args:
        options.append('silent')
    elif '-S' in args or '--simple' in args:
        options.append('simple')
    elif '-p' in args or '--print' in args:
        options.append('print html')
    elif '-f' in args or '--find' in args:
        search_supported(names[0])
    for arg in args:
        if arg not in valid_args: 
            print(f'Unrecognized option: {arg} \ncheck: cv --help')
            exit()      
            
    return(options)
    
    
def main():      
    args, names = check_arguments(sys.argv)
    options = process_args(args, names)            
    versions = check_versions(names)

    if 'html' in options or 'print html' in options: 
        save_html(versions, html_file, options)
    else:
        print_version(versions, options)

if __name__ == '__main__':
    main()