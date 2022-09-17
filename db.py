help = '''Usage:  cv [OPTION] [SOFTWARE]...
    or:  cv [SOFTWARE]...
    or:  cv
    
Checks SOFTWARE(S) latest version and release date using different APIs

Options:
    -a, --all    - list all supported github repositories
    --html       - generates and saves html file with versions
    -p , --print - prints the result as html on screen
    -t           - prints the result as markdown/jira table
    -s, --silent - display only the version
    -S, --simple - hide header and description
    -h, --help   - shows this message

Examples:
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
    'astro':'withastro/astro',
    'bat':'sharkdp/bat',
    'bootkube':'kubernetes-retired/bootkube',
    'bootstrap':'twbs/bootstrap',
    'bpytop':'aristocratos/bpytop',
    'btop':'aristocratos/btop', 
    'calibre':'kovidgoyal/calibre',
    'charts':'danielgindi/Charts',
    'curl':'curl/curl',
    'cv':'hjelev/cv',
    'd3':'d3/d3',
    'drawio':'jgraph/drawio',
    'duf':'muesli/duf',
    'elixir':'elixir-lang/elixir',
    'ember.js':'emberjs/ember.js',
    'exa':'ogham/exa',
    'fd':'sharkdp/fd',
    'fff':'dylanaraps/fff',
    'ffmpeg':'FFmpeg/FFmpeg',
    'flagger':'fluxcd/flagger',
    'flameshot':'flameshot-org/flameshot',
    'gardener':'gardener/gardener',
    'glog':'google/glog',
    'greenshot':'greenshot/greenshot',
    'headscale':'juanfont/headscale',
    'helix':'helix-editor/helix',
    'helm':'helm/helm',
    'home-assistant':'home-assistant/core',
    'httpie':'httpie/httpie',
    'imagemagick':'ImageMagick/ImageMagick',
    'imagemagick6':'ImageMagick/ImageMagick6',
    'immich':'immich-app/immich',
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
    'metalk8s':'scality/metalk8s',
    'nextcloud-desktop':'nextcloud/desktop',
    'nextcloud-server':'nextcloud/server',
    'node':'nodejs/node',
    'nodejs':'nodejs/node',
    'notes':'nuttyartist/notes',
    'octant':'vmware-tanzu/octant',
    'openvr':'ValveSoftware/openvr',
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
    'rpi-mqtt-monitor':'hjelev/rpi-mqtt-monitor',
    'rust':'rust-lang/rust',
    'sliver':'BishopFox/sliver',
    'steam-audio':'ValveSoftware/steam-audio',
    'tarantool':'tarantool/tarantool',
    'terraform-provider-myrasec':'Myra-Security-GmbH/terraform-provider-myrasec',
    'terraform':'hashicorp/terraform',
    'thanos':'thanos-io/thanos',
    'typescript':'microsoft/TypeScript',
    'vscode':'microsoft/vscode',
    'vue':'VUE/VUE',
    'zinc':'zinclabs/zinc',
}