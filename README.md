# cv - Check Version

Check a list of software for its latest version and release date using different APIs.

    Usage:  cv [OPTION] [SOFTWARE]...
        or:  cv [SOFTWARE]...
        or:  cv
        
    Options:
        -a, --all    - list all supported github repositories
        --html       - generates html file with versions
        -p , --print - prints the result as html on screen
        -t , --table - prints the result as markdown/jira table
        -s, --silent - display only the version
        -S, --simple - hide header and description
        -c, --clear  - clear cache for specified software
        -f, --find   - search supported software list
        -h, --help   - shows this message

    Examples:
        cv
        cv nginx
        cv -s nginx
        cv apache nginx vue
        cv -all

# Example script outputs:
```
> cv
Name                           Version    Release Date    Link

apache                         2.4.54     2012-02-21      https://downloads.apache.org/httpd/Announcement2.4.html
nginx                          1.23.1     2022-06-21      https://nginx.org/en/CHANGES
php                            8.1.10     2021-11-23      https://endoflife.date/php
terraform                      1.2.9      2022-09-07      https://github.com/hashicorp/terraform/releases/tag/v1.2.9
vue                            3.3.0      2015-10-08      https://github.com/VUE/VUE/releases/tag/3.3.0
```

```
> cv fff                                                  
Name                           Version    Release Date    Link

fff                            2.2        2020-09-17      https://github.com/dylanaraps/fff/releases/tag/2.2

Description:
📁 A simple file manager written in bash.
```

```
> cv apache php nginx 
Name                           Version    Release Date    Link

apache                         2.4.54     2012-02-21      https://downloads.apache.org/httpd/Announcement2.4.html
php                            8.1.10     2021-11-23      https://endoflife.date/php
nginx                          1.23.1     2022-06-21      https://nginx.org/en/CHANGES
```

# Usage

To use the script clone the repositoy and add a function to your .bashrc or .zshrc file like this (update the path to the script):

```
cv() {
    python3 /home/username/git/cv/cv.py "$@"
}
```

# Supported software

## 113 Github repos
| Software name  | Repository link |
| -------------- | ----------------|
| adguardhome | AdguardTeam/AdGuardHome |
| angular | angular/angular |
| ansible | ansible/ansible |
| apache-airflow | apache/airflow |
| apache-hbase | apache/hbase |
| apache-log4j | apache/logging-log4j2 |
| apache-tomcat | apache/tomcat |
| astro | withastro/astro |
| bat | sharkdp/bat |
| bcal | jarun/bcal |
| bootkube | kubernetes-retired/bootkube |
| bootstrap | twbs/bootstrap |
| bpytop | aristocratos/bpytop |
| btop | aristocratos/btop | 
| buku | jarun/buku |
| calibre | kovidgoyal/calibre |
| charts | danielgindi/Charts |
| consul | hashicorp/consul |
| curl | curl/curl |
| cv | hjelev/cv |
| d3 | d3/d3 |
| ddgr | jarun/ddgr |
| drawio | jgraph/drawio |
| duf | muesli/duf |
| electron | electron/electron |
| elixir | elixir-lang/elixir |
| ember.js | emberjs/ember.js |
| exa | ogham/exa |
| fd | sharkdp/fd |
| fff | dylanaraps/fff |
| ffmpeg | FFmpeg/FFmpeg |
| flagger | fluxcd/flagger |
| flameshot | flameshot-org/flameshot |
| gardener | gardener/gardener |
| gitlab | gitlabhq/gitlabhq |
| glog | google/glog |
| godot | godotengine/godot |
| greenshot | greenshot/greenshot |
| haproxy | haproxy/haproxy |
| headscale | juanfont/headscale |
| helix | helix-editor/helix |
| helm | helm/helm |
| home-assistant | home-assistant/core |
| httpie | httpie/httpie |
| hyper | vercel/hyper |
| imagemagick | ImageMagick/ImageMagick |
| imagemagick6 | ImageMagick/ImageMagick6 |
| immich | immich-app/immich |
| jenkins | jenkinsci/jenkins |
| jinja | pallets/jinja |
| joomla | joomla/joomla-cms |
| jq | stedolan/jq |
| jquery | jquery/jquery |
| k9s | derailed/k9s |
| keda | kedacore/keda |
| kind | kubernetes-sigs/kind |
| kops | kubernetes/kops |
| kube-shell | cloudnativelabs/kube-shell |
| kubernetes | kubernetes/kubernetes |
| lapce | lapce/lapce |
| lazydocker | jesseduffield/lazydocker |
| lazygit | jesseduffield/lazygit |
| lua | lua/lua |
| metalk8s | scality/metalk8s |
| next.js | vercel/next.js |
| nextcloud-desktop | nextcloud/desktop |
| nextcloud-server | nextcloud/server |
| nginx | nginx/nginx |
| nix | NixOS/nix |
| nnn | jarun/nnn |
| node | nodejs/node |
| nodejs | nodejs/node |
| nomad | hashicorp/nomad |
| notes | nuttyartist/notes |
| octant | vmware-tanzu/octant |
| opensearch | opensearch-project/OpenSearch |
| openssl | openssl/openssl |
| openvr | ValveSoftware/openvr |
| pdd | jarun/pdd |
| pelican | getpelican/pelican |
| penpot | penpot/penpot |
| pi-hole | pi-hole/pi-hole |
| playnite | JosefNemec/Playnite |
| playwright | microsoft/playwright |
| pocketbase | pocketbase/pocketbase |
| popeye | derailed/popeye |
| portainer | portainer/portainer |
| powertoys | microsoft/PowerToys |
| proton | ValveSoftware/Proton |
| rails | rails/rails |
| rancher | rancher/rancher |
| react | facebook/react |
| redis | redis/redis |
| revanced | revanced/revanced-manager |
| rocketchat | RocketChat/Rocket.Chat |
| rook | rook/rook |
| rpi-mqtt-monitor | hjelev/rpi-mqtt-monitor |
| rust | rust-lang/rust |
| sliver | BishopFox/sliver |
| steam-audio | ValveSoftware/steam-audio |
| tarantool | tarantool/tarantool |
| terraform-provider-myrasec | Myra-Security-GmbH/terraform-provider-myrasec |
| terraform | hashicorp/terraform |
| thanos | thanos-io/thanos |
| typescript | microsoft/TypeScript |
| typo3 | TYPO3/typo3 |
| varnish | varnishcache/varnish-cache |
| vault | hashicorp/vault |
| vscode | microsoft/vscode |
| vue | VUE/VUE |
| wordpress | WordPress/WordPress |
| zabbix/zabbix | zabbix/zabbix |
| zinc | zinclabs/zinc |

## Everything listed on <https://endoflife.date>

