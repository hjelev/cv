class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


help = f'''{color.BOLD}Usage:{color.END}  cv [OPTION] [SOFTWARE]...
    or:  cv [SOFTWARE]...
    or:  cv
    
Checks SOFTWARE(S) latest version and release date using different APIs

{color.BOLD}Options:{color.END}
    -a, --all    - list all supported github repositories
    --html       - generates and saves html file with versions
    -p , --print - prints the result as html on screen
    -t           - prints the result as markdown/jira table
    -s, --silent - display only the version
    -S, --simple - hide header and description
    -c, --clear  - clear cache for specified [SOFTWARE]...
    -f, --find   - search supported software list
    -g, --github - search for github repositories
    -h, --help   - shows this message

{color.BOLD}Examples:{color.END}
    cv
    cv nginx
    cv -s nginx
    cv apache nginx vue
    cv -all'''
    
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
    
supported = {
    'adguardhome':'AdguardTeam/AdGuardHome',
    'angular':'angular/angular',
    'ansible':'ansible/ansible',
    'apache-airflow':'apache/airflow',
    'apache-hbase':'apache/hbase',
    'apache-log4j':'apache/logging-log4j2',
    'apache-tomcat':'apache/tomcat',
    'astro':'withastro/astro',
    'bat':'sharkdp/bat',
    'bcal':'jarun/bcal',
    'bootkube':'kubernetes-retired/bootkube',
    'bootstrap':'twbs/bootstrap',
    'bpytop':'aristocratos/bpytop',
    'btop':'aristocratos/btop', 
    'buku':'jarun/buku',
    'calibre':'kovidgoyal/calibre',
    'chartjs':'chartjs/Chart.js',
    'consul':'hashicorp/consul',
    'curl':'curl/curl',
    'cv':'hjelev/cv',
    'd3':'d3/d3',
    'ddgr':'jarun/ddgr',
    'drawio':'jgraph/drawio',
    'duf':'muesli/duf',
    'electron':'electron/electron',
    'elixir':'elixir-lang/elixir',
    'ember.js':'emberjs/ember.js',
    'exa':'ogham/exa',
    'fd':'sharkdp/fd',
    'fff':'dylanaraps/fff',
    'ffmpeg':'FFmpeg/FFmpeg',
    'flagger':'fluxcd/flagger',
    'flameshot':'flameshot-org/flameshot',
    'gardener':'gardener/gardener',
    'gitlab':'gitlabhq/gitlabhq',
    'glog':'google/glog',
    'godot':'godotengine/godot',
    'greenshot':'greenshot/greenshot',
    'haproxy':'haproxy/haproxy',
    'headscale':'juanfont/headscale',
    'helix':'helix-editor/helix',
    'helm':'helm/helm',
    'home-assistant':'home-assistant/core',
    'httpie':'httpie/httpie',
    'hyper':'vercel/hyper',
    'imagemagick':'ImageMagick/ImageMagick',
    'imagemagick6':'ImageMagick/ImageMagick6',
    'immich':'immich-app/immich',
    'jenkins':'jenkinsci/jenkins',
    'jinja':'pallets/jinja',
    'joomla':'joomla/joomla-cms',
    'jq':'stedolan/jq',
    'jquery':'jquery/jquery',
    'k9s':'derailed/k9s',
    'keda':'kedacore/keda',
    'kind':'kubernetes-sigs/kind',
    'kops':'kubernetes/kops',
    'kube-shell':'cloudnativelabs/kube-shell',
    'kubernetes':'kubernetes/kubernetes',
    'lapce':'lapce/lapce',
    'lazydocker':'jesseduffield/lazydocker',
    'lazygit':'jesseduffield/lazygit',
    'lua':'lua/lua',
    'metalk8s':'scality/metalk8s',
    'next.js':'vercel/next.js',
    'nextcloud-desktop':'nextcloud/desktop',
    'nextcloud-server':'nextcloud/server',
    'nginx':'nginx/nginx',
    'nix':'NixOS/nix',
    'nnn':'jarun/nnn',
    'node':'nodejs/node',
    'nodejs':'nodejs/node',
    'nomad':'hashicorp/nomad',
    'notes':'nuttyartist/notes',
    'octant':'vmware-tanzu/octant',
    'opensearch':'opensearch-project/OpenSearch',
    'openssl':'openssl/openssl',
    'openvr':'ValveSoftware/openvr',
    'pdd':'jarun/pdd',
    'pelican':'getpelican/pelican',
    'penpot':'penpot/penpot',
    'pi-hole':'pi-hole/pi-hole',
    'playnite':'JosefNemec/Playnite',
    'playwright':'microsoft/playwright',
    'pocketbase':'pocketbase/pocketbase',
    'popeye':'derailed/popeye',
    'portainer':'portainer/portainer',
    'powertoys':'microsoft/PowerToys',
    'proton':'ValveSoftware/Proton',
    'rails':'rails/rails',
    'rancher':'rancher/rancher',
    'react':'facebook/react',
    'redis':'redis/redis',
    'revanced':'revanced/revanced-manager',
    'rocketchat':'RocketChat/Rocket.Chat',
    'rook':'rook/rook',
    'rpi-mqtt-monitor':'hjelev/rpi-mqtt-monitor',
    'rust':'rust-lang/rust',
    'sliver':'BishopFox/sliver',
    'steam-audio':'ValveSoftware/steam-audio',
    'tarantool':'tarantool/tarantool',
    'terraform-provider-myrasec':'Myra-Security-GmbH/terraform-provider-myrasec',
    'terraform':'hashicorp/terraform',
    'thanos':'thanos-io/thanos',
    'typescript':'microsoft/TypeScript',
    'typo3':'TYPO3/typo3',
    'varnish':'varnishcache/varnish-cache',
    'vault':'hashicorp/vault',
    'vscode':'microsoft/vscode',
    'vue':'vuejs/core',
    'wordpress':'WordPress/WordPress',
    'zabbix/zabbix':'zabbix/zabbix',
    'zinc':'zinclabs/zinc',
    'rabbitmq':'rabbitmq/rabbitmq-server',
    'coroot':'coroot/coroot',
    'flask':'pallets/flask',
    'terraform-provider-aws':'hashicorp/terraform-provider-aws',
}