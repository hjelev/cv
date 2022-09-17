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
        -S, --simple - hide header and description
        -h, --help   - shows this message

    Examples:
        cv
        cv nginx
        cv -s nginx
        cv apache nginx vue
        cv -all

# Example script outputs:

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

# Usage

To use the script clone the repositoy and add a function to your .bashrc or .zshrc file like this (update the path to the script):

```
cv() {
    python3 /home/username/git/cv/cv.py "$@"
}
```

# Supported software

## 82 Github repos
| Software name  | Repository link |
| -------------- | ----------------|
| adguardhome | https://github.com/AdguardTeam/AdGuardHome|
| angular | https://github.com/angular/angular|
| astro | https://github.com/withastro/astro|
| bat | https://github.com/sharkdp/bat|
| bootkube | https://github.com/kubernetes-retired/bootkube|
| bootstrap | https://github.com/twbs/bootstrap|
| bpytop | https://github.com/aristocratos/bpytop|
| btop | https://github.com/aristocratos/btop| 
| calibre | https://github.com/kovidgoyal/calibre|
| charts | https://github.com/danielgindi/Charts|
| curl | https://github.com/curl/curl|
| cv | https://github.com/hjelev/cv|
| d3 | https://github.com/d3/d3|
| drawio | https://github.com/jgraph/drawio|
| duf | https://github.com/muesli/duf|
| elixir | https://github.com/elixir-lang/elixir|
| ember.js | https://github.com/emberjs/ember.js|
| exa | https://github.com/ogham/exa|
| fd | https://github.com/sharkdp/fd|
| fff | https://github.com/dylanaraps/fff|
| ffmpeg | https://github.com/FFmpeg/FFmpeg|
| flagger | https://github.com/fluxcd/flagger|
| flameshot | https://github.com/flameshot-org/flameshot|
| gardener | https://github.com/gardener/gardener|
| glog | https://github.com/google/glog|
| greenshot | https://github.com/greenshot/greenshot|
| headscale | https://github.com/juanfont/headscale|
| helix | https://github.com/helix-editor/helix|
| helm | https://github.com/helm/helm|
| home-assistant | https://github.com/home-assistant/core|
| httpie | https://github.com/httpie/httpie|
| imagemagick | https://github.com/ImageMagick/ImageMagick|
| imagemagick6 | https://github.com/ImageMagick/ImageMagick6|
| immich | https://github.com/immich-app/immich|
| jinja | https://github.com/pallets/jinja|
| joomla | https://github.com/joomla/joomla-cms|
| jq | https://github.com/stedolan/jq|
| jquery | https://github.com/jquery/jquery|
| k9s | https://github.com/derailed/k9s|
| keda | https://github.com/kedacore/keda|
| kind | https://github.com/kubernetes-sigs/kind|
| kops | https://github.com/kubernetes/kops|
| kube-shell | https://github.com/cloudnativelabs/kube-shell|
| kubernetes | https://github.com/kubernetes/kubernetes|
| lapce | https://github.com/lapce/lapce|
| lazydocker | https://github.com/jesseduffield/lazydocker|
| lazygit | https://github.com/jesseduffield/lazygit|
| metalk8s | https://github.com/scality/metalk8s|
| nextcloud-desktop | https://github.com/nextcloud/desktop|
| nextcloud-server | https://github.com/nextcloud/server|
| node | https://github.com/nodejs/node|
| nodejs | https://github.com/nodejs/node|
| notes | https://github.com/nuttyartist/notes|
| octant | https://github.com/vmware-tanzu/octant|
| openvr | https://github.com/ValveSoftware/openvr|
| pelican | https://github.com/getpelican/pelican|
| penpot | https://github.com/penpot/penpot|
| pi-hole | https://github.com/pi-hole/pi-hole|
| playnite | https://github.com/JosefNemec/Playnite|
| playwright | https://github.com/microsoft/playwright|
| pocketbase | https://github.com/pocketbase/pocketbase|
| popeye | https://github.com/derailed/popeye|
| portainer | https://github.com/portainer/portainer|
| powertoys | https://github.com/microsoft/PowerToys|
| proton | https://github.com/ValveSoftware/Proton|
| rails | https://github.com/rails/rails|
| rancher | https://github.com/rancher/rancher|
| react | https://github.com/facebook/react|
| redis | https://github.com/redis/redis|
| revanced | https://github.com/revanced/revanced-manager|
| rocketchat | https://github.com/RocketChat/Rocket.Chat|
| rpi-mqtt-monitor | https://github.com/hjelev/rpi-mqtt-monitor|
| rust | https://github.com/rust-lang/rust|
| sliver | https://github.com/BishopFox/sliver|
| steam-audio | https://github.com/ValveSoftware/steam-audio|
| tarantool | https://github.com/tarantool/tarantool|
| terraform-provider-myrasec | https://github.com/Myra-Security-GmbH/terraform-provider-myrasec|
| terraform | https://github.com/hashicorp/terraform|
| thanos | https://github.com/thanos-io/thanos|
| typescript | https://github.com/microsoft/TypeScript|
| vscode | https://github.com/microsoft/vscode|
| vue | https://github.com/VUE/VUE|
| zinc | https://github.com/zinclabs/zinc|

## Everything listed on <https://endoflife.date>

