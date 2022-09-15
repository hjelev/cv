# cv

Check a list of software for its latest version and release date using different APIs.

    Usage:  cv [OPTION] [SOFTWARE]...
        or:  cv [SOFTWARE]...
        or:  cv
        
    Options:
        -a, --all    - list all supported github repositories
        --html       - generates html file with versions
        -t           - prints the result as markdown/jira table
        -s, --silent - display only the version
        -h, --help   - shows this message

    Examples:
        cv
        cv nginx
        cv -s nginx
        cv apache nginx vue
        cv -all

# Example script output:

    > cv
    Name                           Version    Release Date    Link

    apache                         2.4.54     2012-02-21      https://downloads.apache.org/httpd/Announcement2.4.html
    nginx                          1.23.1     2022-06-21      https://nginx.org/en/CHANGES
    php                            8.1.10     2021-11-23      https://endoflife.date/php
    terraform                      1.2.9      2022-09-07      https://github.com/hashicorp/terraform/releases/tag/v1.2.9
    vue                            3.3.0      2015-10-08      https://github.com/VUE/VUE/releases/tag/3.3.0

    > cv fff                                                  
    Name                           Version    Release Date    Link

    fff                            2.2        2020-09-17      https://github.com/dylanaraps/fff/releases/tag/2.2

    Description:
    📁 A simple file manager written in bash.

    > cv apache php nginx 
    Name                           Version    Release Date    Link

    apache                         2.4.54     2012-02-21      https://downloads.apache.org/httpd/Announcement2.4.html
    php                            8.1.10     2021-11-23      https://endoflife.date/php
    nginx                          1.23.1     2022-06-21      https://nginx.org/en/CHANGES


# Supported software

## Github

- adguardhome - <https://github.com/AdguardTeam/AdGuardHome>
- angular - <https://github.com/angular/angular>
- bat - <https://github.com/sharkdp/bat>
- bootstrap - <https://github.com/twbs/bootstrap>
- bootstrap - <https://github.com/twbs/bootstrap>
- bpytop - <https://github.com/aristocratos/bpytop>
- btop - <https://github.com/aristocratos/btop>
- calibre - <https://github.com/kovidgoyal/calibre>
- curl - <https://github.com/curl/curl>
- cv - <https://github.com/hjelev/cv>
- drawio - <https://github.com/jgraph/drawio>
- duf - <https://github.com/muesli/duf>
- elixir - <https://github.com/elixir-lang/elixir>
- ember.js - <https://github.com/emberjs/ember.js>
- exa - <https://github.com/ogham/exa>
- fd - <https://github.com/sharkdp/fd>
- fff - <https://github.com/dylanaraps/fff>
- ffmpeg - <https://github.com/FFmpeg/FFmpeg>
- flameshot - <https://github.com/flameshot-org/flameshot>
- greenshot - <https://github.com/greenshot/greenshot>
- helm - <https://github.com/helm/helm>
- home-assistant - <https://github.com/home-assistant/core>
- httpie - <https://github.com/httpie/httpie>
- imagemagick - <https://github.com/ImageMagick/ImageMagick>
- imagemagick6 - <https://github.com/ImageMagick/ImageMagick6>
- jinja - <https://github.com/pallets/jinja>
- joomla - <https://github.com/joomla/joomla-cms>
- jq - <https://github.com/stedolan/jq>
- jquery - <https://github.com/jquery/jquery>
- k9s - <https://github.com/derailed/k9s>
- kubernetes - <https://github.com/kubernetes/kubernetes>
- nextcloud-desktop - <https://github.com/nextcloud/desktop>
- nextcloud-server - <https://github.com/nextcloud/server>
- node - <https://github.com/nodejs/node>
- nodejs - <https://github.com/nodejs/node>
- pelican - <https://github.com/getpelican/pelican>
- pi-hole - <https://github.com/pi-hole/pi-hole>
- popeye - <https://github.com/derailed/popeye>
- rails - <https://github.com/rails/rails>
- react - <https://github.com/facebook/react>
- redis - <https://github.com/redis/redis>
- rpi-mqtt-monitor - <https://github.com/hjelev/rpi-mqtt-monitor>
- tarantool - <https://github.com/tarantool/tarantool>
- terraform-provider-myrasec - <https://github.com/Myra-Security-GmbH/terraform-provider-myrasec>
- terraform - <https://github.com/hashicorp/terraform>
- vscode - <https://github.com/microsoft/vscode>
- vue - <https://github.com/VUE/VUE>

## Everything listed on <https://endoflife.date>

