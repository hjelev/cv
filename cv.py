import urllib.request, urllib.error
import json
import sys
import db
import datetime

# list of sofware names to check by default
names = ["java", "nginx", "varnish", "terraform", "terraform-provider-myrasec"]
names.sort()
github_url = 'https://api.github.com/repos/{}/releases/latest'
github_url_tags = 'https://api.github.com/repos/{}/tags'
endoflife_url = 'https://endoflife.date/api/{}.json'


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
        print('HTTPError: {} endoflife.date record for {} not found!'.format(e.code, name))
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))

   
def print_version(versions):
    if table :
        print("||{:<28}||{:<8}||{:<15}||{}||".format("Name", "Version", "Release Date","Link"))
    else:   
        print("{:<30} {:<10} {:<15} {}\n".format("Name", "Version", "Release Date", "Link"))
    
    for version in versions:       
        original_name, name, version, date, link, *_ = version
        if table:
            print("|{:<29}|{:<9}|{:<17}|{:<60}|".format(original_name, version, date, link))
        else:
            print("{:<30} {:<10} {:<15} {}".format(original_name, version, date, link))   
        
        
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
            link = json_data['html_url']
            
            if 'v' in version:
                version = json_data['tag_name'].split('v')[1]
            if ')' in version:
                version = version.split(')')[0]
            if 'Version' in version:
                version = version.split(' ')[2]
            if '-' in version:
                version = version.split('-')[1]
            
            return(repo_name, version, date, link) 
    
    except urllib.error.HTTPError as e:
        print('HTTPError: {} Github repository {} not found!'.format(e.code, name))
        # return(check_github_tags(name))
        
    except urllib.error.URLError as e:
        print('URLError: {} '.format(e.reason))
        
        
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
    
    
def save_html(versions):

    html_header = """<html>
<head>
    <title>Versions</title>
    <style>
        html {
            font-family: 'helvetica neue', helvetica, arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #D6EEEE;
        }
    </style>
</head>
<body>
    <table class="tg">
    <thead>
        <tr>
            <th>Software Name</th>
            <th>Latest Version</th>
            <th>Release Date</th>
        </tr>
    """
    html_footer = """
    </tbody>
    </table>
    {}
</body>
</html>
    """
    e = datetime.datetime.now()
    timestamp = "<p><small>Versions checked on %s/%s/%s at %s:%s:%s.</small></p>" % (e.day, e.month, e.year, e.hour, e.minute, e.second)

    with open("html/index.html", "w") as txt_file:
        txt_file.write(html_header)
        link = False
        for line in versions:
            if len(line) > 3:
                link = line[-1]
                line.pop()
                line.pop(0)
            
            txt_file.write('    <tr>\n')
            for x, value in enumerate(line):
                if x == 1 and link:
                    txt_file.write("            <td><a href='{}' target='_blank'>{}</a></td>".format(link, value) + "\n")
                else:
                    txt_file.write("            <td>{}</td>".format(value) + "\n")
            txt_file.write('    </tr>\n')
            
        txt_file.write(html_footer.format(timestamp))

            
def main():  
    global table   
    global names    
    global html
    table = False
    html = False  
         
    if len(sys.argv) >1 and sys.argv[1] == '-t':    
        table = True
    elif len(sys.argv) >1 and sys.argv[1] == '-l':    
        print(github_url)
        print(github_url_tags)
        print(endoflife_url)
        return
        
    elif len(sys.argv) >1 and sys.argv[1] == '-all':
        print('{} Supported github repositories:\n'.format(len(db.supported)))
        for software in db.supported:
            print('{:<30} - https://github.com/{}'.format(software, db.supported[software])) 
        return
               
    elif len(sys.argv) >1 and sys.argv[1] == '-html':
        html = True

    elif len(sys.argv) >1 and not sys.argv[1].startswith('-'):
        options = list(sys.argv)
        options.pop(0)
        names = options

    versions = check_versions(names)
    print_version(versions)
    
    if html: save_html(versions)


if __name__ == '__main__':
    main()