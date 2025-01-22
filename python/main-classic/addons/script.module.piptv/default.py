# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# pipTV
#-------------------------------------------------------------------------------

from lib.utils import *

error_flag = False


def get_historial():
    historial = list()
    settings_path= os.path.join(data_path, "historial.json")
    if os.path.isfile(settings_path):
        try:
            historial = load_json_file(settings_path)
        except Exception:
            logger("Error load_file", "error")

    return historial


def add_historial(contenido):
    historial = get_historial()
    settings_path = os.path.join(data_path, "historial.json")

    trobat = False
    for i in historial:
        if i['url'] == contenido['url']:
            trobat = True
            break

    if not trobat:
        historial.insert(0, contenido)
        dump_json_file(historial[:10], settings_path)


def notification_info(*args,**kwargs):
    transmitter = kwargs['class_name']
    msg = kwargs['event_name']

    logger("%s: %s" %(transmitter, msg))
    #xbmcgui.Dialog().notification('Acestream %s' % transmitter, msg, os.path.join(runtime_path, 'resources', 'media', 'icono_aces_horus.png'))


def notification_error(*args,**kwargs):
    global error_flag
    transmitter = kwargs.get('class_name', ADDON_NAME)
    event = kwargs.get('event_name','')
    msg = args[0]
    error_flag = True

    logger("Error in %s: %s" % (transmitter, msg))

    if event != 'error::subprocess':
        xbmcgui.Dialog().notification('Error Acestream %s' % transmitter, msg,
                                      os.path.join(runtime_path, 'resources', 'media', 'error.png'))


def mainmenu():
    itemlist = list()

    itemlist.append(Item(
        label=translate(30050),
        action='agenda_deportes'
    ))

    itemlist.append(Item(
        label=translate(30051),
        action='search_deportes'
    ))

    if get_setting("show_history"):
        itemlist.append(Item(
            label = translate(30037),
            action = 'historial'
        ))

    if get_setting("show_empty_play"):
        itemlist.append(Item(
            label= 'Play',
            action='play'
        ))

    itemlist.append(Item(
        label= translate(30021),
        action='open_settings'
    ))

    return itemlist


def agenda_deportes(item):

    if not item.filtro:
        itemlist = list()
        if get_setting("show_ala"): itemlist.append(Item(label='Alavés', action='agenda_deportes', filtro='equipo/alaves'))
        if get_setting("show_atb"): itemlist.append(Item(label='Athletic de Bilbao', action='agenda_deportes', filtro='equipo/athletic-club-de-bilbao'))
        if get_setting("show_atm"): itemlist.append(Item(label='Atlético de Madrid', action='agenda_deportes', filtro='equipo/at-madrid'))
        if get_setting("show_fcb"): itemlist.append(Item(label='Barça', action='agenda_deportes', filtro='equipo/fc-barcelona'))
        if get_setting("show_betis"): itemlist.append(Item(label='Betis', action='agenda_deportes', filtro='equipo/real-betis'))
        if get_setting("show_cel"): itemlist.append(Item(label='Celta de Vigo', action='agenda_deportes', filtro='equipo/celta'))
        if get_setting("show_cadiz"): itemlist.append(Item(label='Cádiz', action='agenda_deportes', filtro='equipo/cadiz'))
        if get_setting("show_esp"): itemlist.append(Item(label='Espanyol', action='agenda_deportes', filtro='equipo/espanyol'))
        if get_setting("show_geta"): itemlist.append(Item(label='Getafe', action='agenda_deportes', filtro='equipo/getafe'))
        if get_setting("show_girona"): itemlist.append(Item(label='Girona', action='agenda_deportes', filtro='equipo/girona'))
        if get_setting("show_lp"): itemlist.append(Item(label='Las Palmas', action='agenda_deportes', filtro='equipo/las-palmas'))
        if get_setting("show_lega"): itemlist.append(Item(label='Leganés', action='agenda_deportes', filtro='equipo/leganes'))
        if get_setting("show_mall"): itemlist.append(Item(label='Mallorca', action='agenda_deportes', filtro='equipo/mallorca'))
        if get_setting("show_osa"): itemlist.append(Item(label='Osasuna', action='agenda_deportes', filtro='equipo/osasuna'))
        if get_setting("show_rayo"): itemlist.append(Item(label='Rayo Vallecano', action='agenda_deportes', filtro='equipo/rayo-vallecano'))
        if get_setting("show_rm"): itemlist.append(Item(label='Real Madrid', action='agenda_deportes', filtro='equipo/real-madrid'))
        if get_setting("show_rs"): itemlist.append(Item(label='Real Sociedad', action='agenda_deportes', filtro='equipo/real-sociedad'))
        if get_setting("show_sev"): itemlist.append(Item(label='Sevilla', action='agenda_deportes', filtro='equipo/sevilla-fc'))
        if get_setting("show_val"): itemlist.append(Item(label='Valencia', action='agenda_deportes', filtro='equipo/valencia'))
        if get_setting("show_vall"): itemlist.append(Item(label='Valladolid', action='agenda_deportes', filtro='equipo/valladolid'))
        if get_setting("show_vill"): itemlist.append(Item(label='Villareal', action='agenda_deportes', filtro='equipo/villareal'))

        if get_setting("show_liga"): itemlist.append(Item(label=translate(30054), action='agenda_deportes', filtro='competicion/la-liga'))
        if get_setting("show_segunda"): itemlist.append(Item(label=translate(30059), action='agenda_deportes', filtro='competicion/segunda-division-espana'))
        if get_setting("show_copa"): itemlist.append(Item(label=translate(30055), action='agenda_deportes', filtro='competicion/copa-del-rey'))
        if get_setting("show_champions"): itemlist.append(Item(label=translate(30056), action='agenda_deportes', filtro='competicion/liga-campeones'))
        if get_setting("show_europaleague"): itemlist.append(Item(label=translate(30062), action='agenda_deportes', filtro='competicion/europa-league'))
        if get_setting("show_conference"): itemlist.append(Item(label=translate(30068), action='agenda_deportes', filtro='competicion/uefa-europa-conference-league'))
        if get_setting("show_premier"): itemlist.append(Item(label=translate(30063), action='agenda_deportes', filtro='competicion/premier-league'))

        if get_setting("show_acb"): itemlist.append(Item(label=translate(30057), action='agenda_deportes', filtro='deporte/baloncesto/competicion/liga-endesa'))
        if get_setting("show_euroleague"): itemlist.append(Item(label=translate(30058), action='agenda_deportes', filtro='deporte/baloncesto/competicion/euroliga'))

        if get_setting("show_tenis"): itemlist.append(Item(label=translate(30064), action='agenda_deportes', filtro='deporte/tenis'))
        if get_setting("show_golf"): itemlist.append(Item(label=translate(30065), action='agenda_deportes', filtro='deporte/golf'))
        if get_setting("show_motos"): itemlist.append(Item(label=translate(30066), action='agenda_deportes', filtro='deporte/motociclismo'))
        if get_setting("show_motogp"): itemlist.append(Item(label=translate(30070), action='agenda_deportes', filtro='deporte/motociclismo/competicion/moto-gp'))
        if get_setting("show_moto2"): itemlist.append(Item(label=translate(30071), action='agenda_deportes', filtro='deporte/motociclismo/competicion/moto-2'))
        if get_setting("show_moto3"): itemlist.append(Item(label=translate(30072), action='agenda_deportes', filtro='deporte/motociclismo/competicion/moto-3'))
        if get_setting("show_coches"): itemlist.append(Item(label=translate(30067), action='agenda_deportes', filtro='deporte/automovilismo'))
        if get_setting("show_f1"): itemlist.append(Item(label=translate(30069), action='agenda_deportes', filtro='deporte/automovilismo/competicion/formula-1'))

        return itemlist
    else:
        url = 'https://www.futbolenlatv.es/' + item.filtro
        return do_agenda_deportes(url)

def do_agenda_deportes(url):
    # logger("do_agenda_deportes, url %s" % url)

    from six.moves import urllib_request

    if sys.version_info[0] >= 3:
        from html.parser import unescape
    else:
        from HTMLParser import HTMLParser
        unescape = HTMLParser().unescape

    itemlist = list()

    if 'competicion/' in url:
        mostrar_competicio = False
    else:
        mostrar_competicio = True

    # try:
    # data = six.ensure_str(urllib_request.urlopen(url).read()) # falla per 403!
    headers = dict()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    req = urllib_request.Request(url, headers=headers)
    data = six.ensure_str(urllib_request.urlopen(req).read())
    if data:
        taules = re.findall('<table class="tablaPrincipal.*?</table>', data, re.I)
        for taula in taules:
            n = 0
            trs = re.findall('<tr.*?</tr>', taula, re.I)
            for tr in trs:
                if 'class="pTabla"' in tr: continue # ads
                if n == 0:
                    x = re.findall('<td colspan="5">(.*?)</td>', tr, re.I)
                    if not x: break
                    d_dia = re.findall('\d{2}/\d{2}/\d{4}', x[0], re.I)[0]
                    es_avui = True if 'hoy' in x[0] else False
                else:
                    x = re.findall('<td class="hora ">(.*?)</td>', tr, re.I)
                    if not x: continue
                    lin_hora = x[0].strip()
                    
                    competicio = None
                    if mostrar_competicio:
                        x = re.findall('<td class="detalles ">(.*?)</td>', tr, re.I)
                        if x:
                            x = re.findall('title="([^"]*)"', x[0].strip(), re.I)
                            if x: competicio = unescape('(' + x[0].strip() + ')')

                    x = re.findall('<td class="local">.*?<span title="([^"]*)"', tr, re.I)
                    if x:
                        lin_local = x[0].strip()

                        x = re.findall('<td class="visitante">.*?<span title="([^"]*)"', tr, re.I)
                        lin_visitant = x[0].strip()

                        titol = unescape(lin_local + ' - ' + lin_visitant)
                    else:
                        x = re.findall('<span class="eventoUnico">(.*?)</span>', tr, re.I)
                        titol = unescape(x[0].strip())

                    if competicio: titol = competicio + ' ' + titol
                    titol = re.sub(re.compile('<.*?>'), '', titol)

                    ul = re.findall('<ul class="listaCanales">(.*?)</ul>', tr, re.I)
                    canals = re.findall('title="([^"]*)"', ul[0], re.I)
                    descartar_canals = ['DAZN (Regístrate)', 'DAZN (Reg&#237;strate)', 'Amazon Prime Video (Prueba gratis)', 'GolStadium Premium (acceder)', 'GolStadium (acceder)', 'GOL PLAY (Síguelo en directo)']
                    for can in descartar_canals:
                        if can in canals: canals.remove(can)
                    
                    lbl = '[COLOR yellow]' + d_dia[:5] + ' ' + lin_hora + '[/COLOR] ' + titol + ' [COLOR blue]' + ' , '.join([unescape(c) for c in canals]) + '[/COLOR]'
                    if es_avui: lbl = '[B]' + lbl + '[/B]'

                    plot = '[COLOR yellow]' + (translate(30052) if es_avui else '') + d_dia + ' ' + lin_hora + '[/COLOR][CR]'
                    plot += titol + '[CR]'
                    plot += '[COLOR blue]' + '[CR]'.join([unescape(c) for c in canals]) + '[/COLOR][CR]'

                    if get_setting("agenda_link_all"):
                        new_item = Item(label= lbl, action='search_deportes', filtro="Todos", plot=plot)
                    else:
                        new_item = Item(label= lbl, action='search_deportes', plot=plot)

                    itemlist.append(new_item)
                n += 1

    # except: pass

    return itemlist


def search_deportes(item):

    if not item.filtro:
        itemlist = list()
        itemlist.append(Item(label=translate(30053), action='search_deportes', filtro='Todos'))
        itemlist.append(Item(label='DAZN', action='search_deportes', filtro='DAZN'))
        itemlist.append(Item(label='DAZN LaLiga', action='search_deportes', filtro='DAZN LaLiga'))
        itemlist.append(Item(label='M+ Deportes', action='search_deportes', filtro='M+ Deportes'))
        itemlist.append(Item(label='Movistar Plus+', action='search_deportes', filtro='Movistar Plus+'))
        itemlist.append(Item(label='M+ #Vamos', action='search_deportes', filtro='M+ #Vamos'))
        itemlist.append(Item(label='M+ LaLiga', action='search_deportes', filtro='M+ LaLiga'))
        itemlist.append(Item(label='M+ LaLiga TV BAR', action='search_deportes', filtro='M+ LaLiga TV BAR'))
        itemlist.append(Item(label='M+ Liga de Campeones', action='search_deportes', filtro='M+ Liga de Campeones'))
        itemlist.append(Item(label='Golf', action='search_deportes', filtro='Golf'))
        itemlist.append(Item(label='NBA', action='search_deportes', filtro='NBA'))
        itemlist.append(Item(label='Eurosport', action='search_deportes', filtro='Eurosport'))
        itemlist.append(Item(label='DAZN F1', action='search_deportes', filtro='DAZN F1'))
        return itemlist
    else:
        url = 'https://dl.dropbox.com/s/x4ox82fwbhfb2sg/lista1.m3u'
        return do_search_deportes(url, filtro=item.filtro)

def do_search_deportes(url, filtro=None):
    from six.moves import urllib_request

    itemlist = list()
    ids = list()
    if filtro == 'Todos': filtro = None

    try:
        data = six.ensure_str(urllib_request.urlopen(url).read())

        if data:
            for lin in data.splitlines():
                if lin.startswith('#EXTM3U'): continue

                if lin.startswith('#EXTINF:'):
                    r = re.findall('group-title="([^"]*)"', lin, re.I)
                    group_title = r[0].strip() if r else ''
                    
                    r = re.findall('tvg-logo="([^"]*)"', lin, re.I)
                    tvg_logo = r[0].strip() if r else ''

                    r = re.findall('tvg-id="([^"]*)"', lin, re.I)
                    tvg_id = r[0].strip() if r else ''

                    r = re.findall(' ,(.*)', lin, re.I)
                    if not r: r = re.findall(', (.*)', lin, re.I)
                    descripcio = r[0].strip() if r else ''

                if lin.startswith('acestream://'):
                    r = re.findall('acestream://([0-9a-f]{40})', lin, re.I)
                    if not r: continue
                    id = r[0]
                    if id in ids: continue
                    # if filtro and filtro != group_title: continue
                    if filtro:
                        if filtro == 'DAZN F1':
                            if not group_title.startswith(filtro): continue
                        else:
                            if filtro != group_title: continue
                    ids.append(id)

                    lbl = ''
                    if group_title: lbl += '[COLOR yellow]' + group_title + '[/COLOR] '
                    if tvg_id: lbl += '[COLOR red]' + tvg_id + '[/COLOR] '
                    if descripcio: lbl += '[COLOR blue][B]' + descripcio + '[/B][/COLOR] '
                    lbl += '[COLOR gray]' + id + '[/COLOR] '

                    plot = '[COLOR yellow]' + group_title + '[/COLOR][CR]'
                    plot += '[COLOR red]' + tvg_id + '[/COLOR][CR]'
                    plot += '[COLOR blue][B]' + descripcio + '[/B][/COLOR][CR]'
                    plot += '[COLOR gray]' + id + '[/COLOR]'

                    new_item = Item(label=lbl, action='play', id=id, plot=plot)
                    if tvg_logo: new_item.icon = tvg_logo

                    itemlist.append(new_item)

    except: pass

    return itemlist


def run(item):
    itemlist = list()

    if not item.action:
        logger("Item sin acción")
        return

    if item.action == "mainmenu":
        itemlist = mainmenu()

    elif item.action == "historial":
        for it in get_historial():
            itemlist.append(Item(label= it.get('title'),
                                 action='play',
                                 url=it.get('url'),
                                 icon=it.get('icon'),
                                 plot=it.get('plot')))

    elif item.action == "agenda_deportes":
        itemlist = agenda_deportes(item)

    elif item.action == "search_deportes":
        itemlist = search_deportes(item)

    elif item.action == 'open_settings':
        xbmcaddon.Addon().openSettings()

    elif item.action == 'play':
        id = url = None

        if item.id:
            id = item.id
            set_setting("last_id", id)
        elif item.url:
            url = item.url
        else:
            last_id = get_setting("last_id", "a0270364634d9c49279ba61ae3d8467809fb7095")
            input = xbmcgui.Dialog().input(translate(30022), last_id)
            if re.findall('^(http|magnet)', input, re.I):
                url = input
            else:
                id = input
        if id:
            url = 'http://127.0.0.1:6878/ace/manifest.m3u8?id=' + id

        if url:
            add_historial({'url': url,
                           'title': item.label,
                           'icon': item.icon if item.icon else '',
                           'plot': item.plot})

            #xbmc.Player().play(url)
            listitem = xbmcgui.ListItem()
            title = item.label or url or id
            info = {'title': title}
            if item.plot:
                info['plot'] = item.plot
            listitem.setInfo('video', info ) #TODO
            art = {'icon': item.icon if item.icon else os.path.join(runtime_path, 'resources', 'media', 'icono_aces_horus.png')}
            listitem.setArt(art)
            xbmc.Player().play(url, listitem)

        #xbmc.executebuiltin('Container.Refresh')


    if itemlist:
        for item in itemlist:
            listitem = xbmcgui.ListItem(item.label or item.title)
            listitem.setInfo('video', {'title': item.label or item.title, 'mediatype': 'video'})
            listitem.setArt(item.getart())
            if item.plot:
                listitem.setInfo('video', {'plot': item.plot})

            if item.isPlayable:
                listitem.setProperty('IsPlayable', 'true')
                isFolder = False

            elif isinstance(item.isFolder, bool):
                isFolder = item.isFolder

            elif not item.action:
                isFolder = False

            else:
                isFolder = True

            xbmcplugin.addDirectoryItem(
                handle=int(sys.argv[1]),
                url='%s?%s' % (sys.argv[0], item.tourl()),
                listitem=listitem,
                isFolder= isFolder,
                totalItems=len(itemlist)
            )
        
        xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)


if __name__ == '__main__':
    if sys.argv[2]:
        try:
            item = Item().fromurl(sys.argv[2])
        except:
            argumentos = dict()
            for c in sys.argv[2][1:].split('&'):
                k, v = c.split('=')
                argumentos[k] = urllib_parse.unquote_plus(six.ensure_str(v))

            logger("Llamada externa: %s" %argumentos)
            # tractar petició externa !?
            action = argumentos.get('action', '').lower()
            # ... !?
            exit (0)

    else:
        item = Item(action='mainmenu')

    run(item)
