#!/usr/bin/env python3
# Gera os blocos únicos (HTML) das páginas do site novo a partir dos protótipos.
# Uso: python3 build.py  -> escreve out/<pagina>.html (para o Wix) e out/<pagina>.local.html (teste local)
import re, os, sys, html

PROTO = '/home/claude/doma/project'
OUT = '/home/claude/site_v2/out'
WIX = 'https://static.wixstatic.com/media/'
GH = 'https://raw.githubusercontent.com/clinicadoma/doma_assets/main/site/'
LOCAL = 'file:///home/claude/doma/img/'

# blob do protótipo -> (arquivo, url pública, largura, altura)
IMGS = {
    '19fbeee13f3f57f41608447b08222d94': ('logo.webp', WIX + '253e81_0452afd60bae4cfda9e23427567f0f36~mv2.webp', 320, 384),
    '872437608d5a552867bb64fe5989085b': ('triste.jpg', GH + 'triste.jpg', 601, 645),
    # carteirinha recortada do fundo cinza (PNG com fundo transparente)
    'da00a53a7610fafd4a4e9bee6a020cd2': ('carteira.png', GH + 'carteira.png', 376, 244),
    '20f9af3c72c176045c52bd25596f4132': ('bemvindo.jpg', WIX + '253e81_c6676319d5ef428ea6b9f400fa34be32~mv2.jpg', 685, 814),
    'a487a747692a79d70e2a5bad98e977a3': ('meuano.jpg', WIX + '253e81_9655ef93855746b39a7b16b0a62081b6~mv2.jpg', 712, 533),
    '7cc4dd1cc1139745e121573e3582997c': ('sala.jpg', GH + 'sala.jpg', 793, 704),
    'd7662f6f0254a47315e85a69b305ee82': ('polvo.jpg', WIX + '253e81_5ef317b6eca6490991a21f40eb217cf9~mv2.jpg', 711, 406),
    '4ad881a428016f9c83ff8a72869761e3': ('livro.jpg', GH + 'livro.jpg', 330, 340),
    'afe8c7c379830770624b40e86f2cbcdc': ('terapia.jpg', WIX + '253e81_2d86b45f7e1e480fa722f8c9d724ad24~mv2.jpg', 667, 702),
}
AUDIO_VITROLA = 'https://static.wixstatic.com/mp3/253e81_54b19efb74c5463e8ce371a49cd82da5.mp3'

import plano  # textos e blocos do plano de melhorias (13/11)
import paginas_novas  # páginas novas do passo 3 do plano
import paginas_legais  # passo 5: perguntas frequentes, política de privacidade e termos de uso

# Para onde cada link do protótipo leva no site novo
LINKS = {
    '/carteira-d': '/carteira-d',
    '#carteira': '/carteira-doma',
    '#planos': '/planos',
    '#indique': '/indique',
    '#inicio': '/',
    'Main.dc.html': '/',
    'Travessia.dc.html': '/a-travessia',
    'Bets.dc.html': '/vicio-bets',
    '/vicio-bets': '/vicio-bets',
    '/pricing-plans/list': '/pricing-plans/plans-pricing',
    '/category/all-products': '/category/all-products',
    '/comiss%C3%A3o': '/indique',
    '/doma-membro': '/doma-membro',
    '/a-travessia': '/a-travessia',
    '/planos': '/planos',
    '/indique': '/indique',
    '/carteira-doma': '/carteira-doma',
    '/livro-a-travessia': '/livro-a-travessia',
    '/nivel-1': '/nivel-1',
    '/conheca-os-monstrinhos': '/conheca-os-monstrinhos',
    '/monstrinho-polvo': '/monstrinho-polvo',
    '/para-pacientes': '/para-pacientes',
    '/perguntas-frequentes': '/perguntas-frequentes',
    '/politica-de-privacidade': '/politica-de-privacidade',
    '/termos-de-uso': '/termos-de-uso',
    '#privacidade': '/politica-de-privacidade',
}

CSS_BASE = r'''
html,body{margin:0;padding:0;background:#f1f5f9;overflow:hidden}
body{-webkit-text-size-adjust:100%;text-size-adjust:100%}
#palco{position:absolute;top:0;left:0;width:1280px;--dw:1280px;transform-origin:0 0;visibility:hidden}
a{color:#0b7cb8}a:hover{color:#0f2744}
a[data-ir],a[data-rolar],a[target]{cursor:pointer;transition:transform .15s ease,filter .15s ease}
a[data-ir]:hover,a[data-rolar]:hover,a[target]:hover{filter:brightness(1.05)}
button{cursor:pointer}
/* vitrola */
.vit-disco{animation:vit-gira 2.6s linear infinite;animation-play-state:paused}
.vit-tocando .vit-disco{animation-play-state:running}
.vit-braco{transition:transform .7s ease}
.vit-tocando .vit-braco{transform:rotate(24deg) !important}
@keyframes vit-gira{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.vit-barra{width:200px;height:6px;border-radius:999px;background:#eadfce;overflow:hidden}
.vit-barra>i{display:block;height:100%;width:0;background:#c2410c;border-radius:999px}
@media (prefers-reduced-motion:reduce){.vit-disco{animation:none}}
'''

JS_BASE = r'''
(function(){
  var palco=document.getElementById('palco');
  // largura de desenho por faixa de tela (as mesmas faixas do Wix Studio)
  function larguraDeDesenho(w){ return w>1000?1280:(w>750?820:390); }
  var ultimo='';
  function ajustar(){
    var w=window.innerWidth,h=window.innerHeight; if(!w||!h) return;
    var d=larguraDeDesenho(w);
    palco.style.width=d+'px'; palco.style.setProperty('--dw',d+'px');
    var H=palco.offsetHeight; if(!H) return;
    var zl=w/d, z=Math.min(zl,h/H);
    var cabe=true;
    if(z<zl*0.9){ z=zl*0.9; cabe=false; }           // quadro curto demais: não encolhe além de 10%
    document.documentElement.style.overflowY=cabe?'hidden':'auto';
    document.body.style.overflowY=cabe?'hidden':'auto';
    var x=Math.max(0,(w-d*z)/2);
    palco.style.transform='translate('+x+'px,0) scale('+z+')';
    palco.style.visibility='visible';
    var chave=[d,H,w,h].join(',');
    if(chave!==ultimo){ ultimo=chave; try{ parent.postMessage({acao:'domaTamanho',desenho:d,altura:H,quadroL:w,quadroA:h,proporcao:+(H/d).toFixed(4)},'*'); }catch(e){} }
  }
  var t=null; function agendar(){ if(t) cancelAnimationFrame(t); t=requestAnimationFrame(ajustar); }
  window.addEventListener('resize',agendar);
  window.addEventListener('load',agendar);
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(agendar);
  if(window.ResizeObserver) new ResizeObserver(agendar).observe(palco);
  ajustar();

  // links internos: quem navega (ou rola a tela) é a página do Wix
  function rolarPara(id){
    var alvo=document.getElementById(id); if(!alvo) return;
    var topo=alvo.getBoundingClientRect().top;
    if(!window.IntersectionObserver){ return; }
    var io=new IntersectionObserver(function(es){
      io.disconnect();
      var vis=(es[0]&&es[0].intersectionRect)?es[0].intersectionRect.top:0;   // primeira linha do bloco que está visível na tela
      try{ parent.postMessage({acao:'rolar',dy:Math.round(topo-vis-70)},'*'); }catch(e){}
    });
    io.observe(palco);
  }
  document.addEventListener('click',function(ev){
    var a=ev.target.closest?ev.target.closest('a[data-ir],a[data-rolar]'):null; if(!a) return;
    ev.preventDefault();
    if(a.hasAttribute('data-rolar')){ rolarPara(a.getAttribute('data-rolar')); return; }
    try{ parent.postMessage({acao:'irPara',destino:a.getAttribute('data-ir'),voltar:a.getAttribute('data-voltar')||''},'*'); }catch(e){}
  });
})();
'''

JS_VITROLA = r'''
(function(){
  var caixa=document.getElementById('vitrola'); if(!caixa) return;
  var audio=document.getElementById('vit-audio'), botao=document.getElementById('vit-botao'),
      dica=document.getElementById('vit-dica'), barra=document.getElementById('vit-progresso');
  var tocando=false;
  function estado(on,rotulo){ tocando=on; caixa.classList.toggle('vit-tocando',on); botao.textContent=rotulo; botao.setAttribute('aria-pressed',on?'true':'false'); }
  botao.addEventListener('click',function(){
    if(tocando){ audio.pause(); estado(false,'▶ Retomar'); return; }
    var p=audio.play();
    estado(true,'⏸ Pausar');
    if(p&&p.catch) p.catch(function(){ estado(false,'▶ Tocar'); dica.textContent='Não foi possível tocar agora. Toque de novo em instantes.'; });
  });
  audio.addEventListener('timeupdate',function(){ if(audio.duration) barra.style.width=(100*audio.currentTime/audio.duration)+'%'; });
  audio.addEventListener('ended',function(){
    estado(false,'▶ Ouvir novamente'); barra.style.width='100%';
    dica.textContent='🎉 Surpresa liberada! Continue a sua travessia para descobrir Quem Somos. ⬇️';
    dica.style.background='#fff7ed'; dica.style.color='#9a3412'; dica.style.fontWeight='700';
  });
  audio.addEventListener('error',function(){ estado(false,'▶ Tocar'); });
})();
'''

VITROLA_HTML = '''<section id="vitrola" style="background: #fdf8f0; border-radius: 18px; padding: 28px 20px; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center">
        <h2 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: 28px; font-weight: 700; color: #334155">Momento de Pausa</h2>
        <p id="vit-dica" aria-live="polite" style="margin: 0; padding: 6px 14px; border-radius: 999px; background: #ffffff; color: #b45309; font-size: 14px; font-weight: 600">🎧 Preste atenção na letra e relaxe. Escute até o final.</p>
        <div style="position: relative; width: 200px; height: 156px; border-radius: 12px; background: #9a4a1f; box-shadow: inset 0 0 0 4px #7c3a16, 0 8px 18px rgba(124, 58, 22, 0.3)">
          <div class="vit-disco" style="position: absolute; left: 18px; top: 14px; width: 128px; height: 128px; border-radius: 999px; background: repeating-radial-gradient(circle, #1f1f1f 0 2px, #2b2b2b 2px 4px); display: flex; align-items: center; justify-content: center">
            <img src="__IMG_LOGO__" alt="" width="320" height="384" style="width: 42px; height: 42px; object-fit: contain; border-radius: 999px; background: #ffffff; padding: 3px">
          </div>
          <div style="position: absolute; right: 18px; top: 16px; width: 18px; height: 18px; border-radius: 999px; background: #374151"></div>
          <div class="vit-braco" style="position: absolute; right: 24px; top: 30px; width: 6px; height: 72px; border-radius: 4px; background: #d1d5db; transform: rotate(-10deg); transform-origin: top center"></div>
        </div>
        <div class="vit-barra" aria-hidden="true"><i id="vit-progresso"></i></div>
        <button id="vit-botao" type="button" aria-pressed="false" style="min-height: 44px; padding: 0 24px; border-radius: 999px; border: none; background: #c2410c; color: #ffffff; font: inherit; font-size: 15px; font-weight: 700">▶ Tocar</button>
        <audio id="vit-audio" preload="metadata" src="__AUDIO__"></audio>
      </section>'''


def cortar(s, ini, fim):
    """Remove o trecho que começa em `ini` e termina logo antes de `fim` (marcadores de comentário)."""
    i = s.find(ini)
    if i < 0:
        raise SystemExit('marcador não achado: ' + ini)
    j = s.find(fim, i)
    if j < 0:
        raise SystemExit('marcador final não achado: ' + fim)
    return s[:i] + s[j:]


def bloco_fechado(s, ini, tag):
    """Devolve (inicio, fim) do primeiro elemento <tag ...> depois do marcador `ini`, contando aninhamento."""
    i = s.find(ini)
    if i < 0:
        raise SystemExit('marcador não achado: ' + ini)
    a = s.find('<' + tag, i)
    prof, p = 0, a
    for m in re.finditer(r'<(/?)' + tag + r'\b[^>]*>', s[a:]):
        prof += -1 if m.group(1) else 1
        if prof == 0:
            return a, a + m.end()
    raise SystemExit('elemento não fechado: ' + ini)


def ajustar_links(corpo, extras=None):
    mapa = dict(LINKS)
    if extras:
        mapa.update(extras)
    faltando = set()

    def troca(m):
        antes, href, depois = m.group(1), html.unescape(m.group(2)), m.group(3)
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:'):
            return '<a%shref="%s" target="_blank" rel="noopener"%s>' % (antes, m.group(2), depois)
        if href in mapa and mapa[href] is not None:
            if mapa[href].startswith('rolar:'):
                return '<a%shref="#" data-rolar="%s"%s>' % (antes, mapa[href][6:], depois)
            if '|voltar=' in mapa[href]:
                dest, volta = mapa[href].split('|voltar=')
                return '<a%shref="#" data-ir="%s" data-voltar="%s"%s>' % (antes, dest, volta, depois)
            return '<a%shref="#" data-ir="%s"%s>' % (antes, mapa[href], depois)
        faltando.add(href)
        return m.group(0)

    corpo = re.sub(r'<a(\s[^>]*?)href="([^"]*)"([^>]*)>', troca, corpo)
    return corpo, faltando


def montar(nome, titulo, corpo, js_extra='', css_extra=''):
    # imagens
    usados = set(re.findall(r'/_blob/([a-f0-9]{32})', corpo))
    for b in usados:
        if b not in IMGS:
            raise SystemExit('imagem sem mapeamento: ' + b)

    def img_attr(m):
        b = m.group(1)
        _, _, w, h = IMGS[b]
        return 'src="__BLOB_%s__" width="%d" height="%d"' % (b, w, h)

    # carteirinha sem fundo: mesma altura de antes (margem compensa o recorte) e selo por cima do cartão
    if 'da00a53a7610fafd4a4e9bee6a020cd2' in corpo:
        antes = corpo
        corpo = corpo.replace('style="position: absolute; top: 0; right: -8px; padding: 4px 12px;',
                              'style="position: absolute; top: 19px; right: -8px; z-index: 2; padding: 4px 12px;')
        corpo = corpo.replace('style="width: 100%; max-width: 300px; height: auto; display: block; border-radius: 14px; transform: rotate(-2deg);',
                              'style="width: 100%; max-width: 300px; height: auto; display: block; margin: 19px 0; border-radius: 10px; transform: rotate(-2deg);')
        assert corpo.count('margin: 19px 0; border-radius: 10px') == 1 and corpo.count('top: 19px; right: -8px; z-index: 2') == 1, 'bloco da carteira mudou'
    corpo = re.sub(r'src="/_blob/([a-f0-9]{32})"', img_attr, corpo)
    # vw do protótipo passa a seguir a largura de desenho (o quadro é ampliado por inteiro)
    corpo = re.sub(r'(\d+(?:\.\d+)?)vw', lambda m: 'calc(var(--dw) * %s / 100)' % m.group(1), corpo)

    doc = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>%s%s</style>
</head>
<body>
<div id="palco">
%s
</div>
<script>%s%s</script>
</body>
</html>
''' % (titulo, CSS_BASE, css_extra, corpo.strip(), JS_BASE, js_extra)

    os.makedirs(OUT, exist_ok=True)
    for variante, sufixo in (('pub', '.html'), ('local', '.local.html')):
        d = doc
        for b, (arq, url, w, h) in IMGS.items():
            d = d.replace('__BLOB_%s__' % b, url if variante == 'pub' else LOCAL + arq)
        d = d.replace('__IMG_LOGO__', IMGS['19fbeee13f3f57f41608447b08222d94'][1] if variante == 'pub' else LOCAL + 'logo.webp')
        d = d.replace('__AUDIO__', AUDIO_VITROLA)
        if '__BLOB_' in d or '/_blob/' in d:
            raise SystemExit('sobrou imagem sem trocar em ' + nome)
        open(os.path.join(OUT, nome + sufixo), 'w', encoding='utf-8').write(d)
    return doc


def raiz(arquivo):
    """Devolve o <div> raiz do protótipo (o conteúdo de <x-dc> depois do <helmet>)."""
    s = open(os.path.join(PROTO, arquivo), encoding='utf-8').read()
    i = s.find('</helmet>') + len('</helmet>')
    j = s.find('</x-dc>')
    return beneficios_dos_planos(s[i:j].strip())


def beneficios_dos_planos(c):
    """21/11/2026: devolve aos cartões dos planos três benefícios do site atual que tinham ficado de fora
    (Programa de Indicação, Carteira Premium e descontos nos Sábados de Conexão)."""
    trocas = [
        ('<li>🎁 Sorteios e prêmios mensais</li>',
         '<li>🎁 Sorteios e prêmios mensais</li>\n              <li>🤝 Programa de indicação</li>'),
        ('<li>✅ Tudo do Básico</li>',
         '<li>✅ Tudo do Básico</li>\n              <li>🪪 Carteira Doma Premium</li>'),
        ('<li>🪩 Aulas de bambolê terapia</li>',
         '<li>🪩 Aulas de bambolê terapia</li>\n              <li>🎉 Descontos nos Sábados de Conexão</li>'),
    ]
    for velho, novo in trocas:
        n = c.count(velho)
        assert n in (0, 1), (velho, n)
        c = c.replace(velho, novo)
    return c


def home():
    c = raiz('Main.dc.html')
    # o menu, o login e o rodapé são os do próprio site (cabeçalho e rodapé do Wix)
    c = cortar(c, '<!-- MENU EM PÍLULAS -->', '<!-- COLUNA PRINCIPAL')
    a, b = bloco_fechado(c, '<!-- RODAPÉ -->', 'footer')
    c = c[:a] + c[b:]
    c = plano.home(c)
    # vitrola de verdade
    a, b = bloco_fechado(c, '<!-- MOMENTO DE PAUSA -->', 'section')
    c = c[:a] + VITROLA_HTML + c[b:]
    # blocos que ainda dependem de dados da Daniela ficam fora até chegarem
    a, b = bloco_fechado(c, '<!-- A TERAPEUTA -->', 'div')
    c = c[:a] + c[b:]
    a, b = bloco_fechado(c, '<!-- DEPOIMENTOS -->', 'section')
    c = c[:a] + c[b:]
    c = c.replace('''<p style="margin: 8px 0 0; text-align: center; font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-style: italic; font-weight: 700; color: #0f2744">Afinal, nem todo monstro que assusta vem de fora.</p>''',
                  '''<p style="margin: 8px 0 0; text-align: center; font-family: 'Playfair Display', Georgia, serif; font-size: 20px; font-style: italic; font-weight: 700; color: #0f2744">Afinal, nem todo monstro que assusta vem de fora.</p>
        <div style="display: flex; justify-content: center; margin-top: 6px"><a href="/planos" style="display: inline-flex; align-items: center; justify-content: center; min-height: 50px; padding: 0 26px; border-radius: 999px; background: #0f2744; color: #ffffff; font-size: 15px; font-weight: 800; text-decoration: none; box-shadow: 0 8px 18px rgba(15, 39, 68, 0.25)">🌱 CONHEÇA OS PLANOS</a></div>''')
    assert 'CONHEÇA OS PLANOS' in c
    c, falta = ajustar_links(c, {'#planos': '/a-travessia', '/carteira-d': '/carteira-doma'})
    # respiro no fim da coluna (o protótipo tinha o rodapé logo abaixo)
    c = c.replace('padding: 20px 12px 0;', 'padding: 20px 12px 28px;', 1)
    if falta:
        print('home: links sem destino:', falta)
    return montar('home', 'Clínica Doma — Início', c, JS_VITROLA)


MARCAS_HOME = ['CAMPANHA', 'CARTEIRA', 'MOMENTO DE PAUSA', 'NEM TODO MONSTRO', 'OS MONSTRINHOS', 'O QUE VOCÊ DESTRAVA',
               'FAIXA DA TRAVESSIA', 'PLANOS', 'QUEM SOMOS', 'CANSADO DE DIAS DIFÍCEIS', 'MÉTODO + LIVRO',
               'TRAGA SEU MONSTRINHO', 'INDIQUE E PAGUE MENOS', 'DEPOIMENTOS', 'APOIO EM CRISE', 'INSTAGRAM']


def partes_home():
    """Pedaços da Home do protótipo (cada bloco entre um comentário de topo e o seguinte)."""
    c = raiz('Main.dc.html')
    fim = c.rfind('</div>', 0, c.find('</main>'))
    pos = [c.find('<!-- ' + m) for m in MARCAS_HOME]
    assert all(p > 0 for p in pos) and pos == sorted(pos), pos
    pos.append(fim)
    return {m: c[pos[i]:pos[i + 1]].rstrip() + '\n\n      ' for i, m in enumerate(MARCAS_HOME)}


def casca():
    """Abertura e fechamento da coluna (logo + moldura), iguais aos das páginas internas do protótipo."""
    c = raiz('Travessia.dc.html')
    c = cortar(c, '<!-- MENU EM PÍLULAS -->', '<main')
    abre = c[:c.find('<!-- ABERTURA -->')]
    abre = abre.replace('padding: 20px 12px 0;', 'padding: 20px 12px 28px;', 1)
    assert 'padding: 20px 12px 28px;' in abre
    return abre, '\n    </div>\n  </main>\n</div>'


def heroi(selo, titulo, texto, botao, destino, nota):
    return """<section style="background: linear-gradient(180deg, #0f2744 0%%, #1b3d63 100%%); border-radius: 18px; padding: clamp(24px, 4vw, 40px) clamp(18px, 4vw, 40px); display: flex; flex-direction: column; align-items: center; gap: 18px; text-align: center; color: #e2e8f0">
        <p style="margin: 0; padding: 6px 14px; border-radius: 999px; background: rgba(247, 215, 116, 0.16); border: 1px solid #f7d774; color: #f7d774; font-size: 13px; font-weight: 800; letter-spacing: 0.06em">%s</p>
        <h1 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(30px, 4.4vw, 46px); line-height: 1.12; font-weight: 800; color: #ffffff">%s</h1>
        <p style="margin: 0; max-width: 600px; font-size: clamp(16px, 2vw, 18px)">%s</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px">
          <a href="%s" style="display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border-radius: 999px; background: #f7d774; color: #0f2744; font-size: 16px; font-weight: 800; text-decoration: none; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25)">%s</a>
        </div>
        <p style="margin: 0; font-size: 14px; color: #b9c9da">%s</p>
      </section>

      """ % (selo, titulo, texto, destino, botao, nota)


def composta(nome, titulo, blocos, extras=None):
    abre, fecha = casca()
    c = abre + ''.join(blocos) + fecha
    c, falta = ajustar_links(c, extras)
    if falta:
        print(nome + ': links sem destino:', falta)
    return montar(nome, titulo, c)


def planos():
    p = partes_home()
    h = heroi('📚 PLANOS DOMA', 'Planos Doma: escolha como quer fazer a sua Travessia',
              plano.PLANOS_TEXTO,
              'QUERO MINHA CARTEIRA GRÁTIS 🚀', '/carteira-doma',
              '🪪 Comece grátis com a Carteira Doma. Quando quiser ir além, escolha um plano.')
    return composta('planos', 'Clínica Doma — Planos',
                    [h, p['PLANOS'], p['CARTEIRA'], p['O QUE VOCÊ DESTRAVA'], p['TRAGA SEU MONSTRINHO'],
                     p['INDIQUE E PAGUE MENOS'], p['APOIO EM CRISE'], p['INSTAGRAM']],
                    {'/carteira-d': '/carteira-doma'})


def carteira():
    p = partes_home()
    h = heroi('🪪 CARTEIRA OFICIAL DOMA', 'Carteira Oficial Doma: o seu primeiro passo na Travessia',
              plano.CARTEIRA_TEXTO,
              'QUERO MINHA CARTEIRA GRÁTIS 🚀', '/carteira-d',
              '✨ Emissão gratuita: leva 2 minutinhos e sai na hora!')
    return composta('carteira', 'Clínica Doma — Carteira Doma',
                    [h, p['CARTEIRA'], p['O QUE VOCÊ DESTRAVA'], p['INDIQUE E PAGUE MENOS'], p['APOIO EM CRISE'], p['INSTAGRAM']])


def indique():
    p = partes_home()
    h = heroi('🤝 PROGRAMA INDIQUE DOMA', 'Indique Doma: ajude alguém e deixe a sua Travessia mais leve',
              'Cada pessoa que você indica e entra para a Doma gera uma comissão para você, nas novas assinaturas e em cada renovação. Para participar, basta ter a sua Carteira Doma: é nela que fica o seu link de indicação.',
              '🔗 QUERO MEU LINK DE INDICAÇÃO', '/doma-membro',
              '🔗 1. Pegue seu link · 💌 2. Indique quem precisa · 🪙 3. Ganhe a cada renovação')
    ind = p['INDIQUE E PAGUE MENOS']
    # nesta página o bloco do programa chama para emitir a carteira (já estamos na página dos detalhes)
    ind, n1 = re.subn(r'<a href="/comiss%C3%A3o"([^>]*)>CONHEÇA TODOS OS DETALHES</a>', r'<a href="/carteira-d"\1>🪪 EMITIR MINHA CARTEIRA GRÁTIS</a>', ind)
    ind, n2 = re.subn(r'\s*<a href="/comiss%C3%A3o"[^>]*>✨ Sou influenciador</a>', '', ind)
    assert n1 == 1 and n2 == 1, (n1, n2)
    return composta('indique', 'Clínica Doma — Indique',
                    [h, ind, p['CARTEIRA'], p['O QUE VOCÊ DESTRAVA'], p['APOIO EM CRISE'], p['INSTAGRAM']])


def travessia():
    p = partes_home()
    c = raiz('Travessia.dc.html')
    c = cortar(c, '<!-- MENU EM PÍLULAS -->', '<main')
    a, b = bloco_fechado(c, '<!-- RODAPÉ -->', 'footer')
    c = c[:a] + c[b:]
    c = c.replace('padding: 20px 12px 0;', 'padding: 20px 12px 28px;', 1)
    c = plano.travessia(c, bloco_fechado)
    # planos depois do livro físico e método antes de "Como entrar" (como na página atual do site novo)
    i = c.find('<!-- A TRILHA DOS 12 NÍVEIS -->'); assert i > 0
    c = c[:i] + p['PLANOS'] + c[i:]
    i = c.find('<!-- ACESSO -->'); assert i > 0
    c = c[:i] + p['MÉTODO + LIVRO'] + c[i:]
    c, n = re.subn(r'<a href="Main\.dc\.html"([^>]*)>VER OS PLANOS</a>', r'<a href="/planos"\1>VER OS PLANOS</a>', c)
    assert n == 1, n
    # apoio em crise no fim (no protótipo ficava no rodapé)
    i = c.rfind('</div>', 0, c.find('</main>'))
    c = c[:i] + p['APOIO EM CRISE'].rstrip() + '\n\n    ' + c[i:]
    c, falta = ajustar_links(c, {'#comecar': 'rolar:comecar', '#nivel-1': plano.PAGINA_NIVEL_1,
                                 '/carteira-d': '/carteira-d|voltar=' + plano.PAGINA_NIVEL_1})
    if falta:
        print('travessia: links sem destino:', falta)
    return montar('travessia', 'Clínica Doma — A Travessia', c)


def bets():
    c = raiz('Bets.dc.html')
    c = cortar(c, '<!-- MENU EM PÍLULAS -->', '<main')
    a, b = bloco_fechado(c, '<!-- RODAPÉ -->', 'footer')
    c = c[:a] + c[b:]
    c = c.replace('padding: 20px 12px 0;', 'padding: 20px 12px 28px;', 1)
    c = plano.bets(c)
    # o Guia de Resgate fica numa página própria (o mesmo guia interativo do site atual)
    c, n = re.subn(r'\s*<div[^>]*>Embed atual: Guia de Resgate \(investigação do vício\)</div>', '', c)
    assert n == 1, n
    c, n = re.subn(r'<a href="#guia"([^>]*)>CLIQUE AQUI PARA INICIAR O RESGATE!</a>', r'<a href="/guia-de-resgate"\1>CLIQUE AQUI PARA INICIAR O RESGATE!</a>', c)
    assert n == 1, n
    c, n = re.subn(r'<a href="Main\.dc\.html"([^>]*)>VER OS PLANOS</a>', r'<a href="/planos"\1>VER OS PLANOS</a>', c)
    assert n == 1, n
    c, n = re.subn(r'<a href="Main\.dc\.html"([^>]*)>(Caso esta não seja)', r'<a href="/a-travessia"\1>\2', c)
    assert n == 1, n
    c, falta = ajustar_links(c, {'#guia': 'rolar:guia', '/guia-de-resgate': '/guia-de-resgate'})
    if falta:
        print('bets: links sem destino:', falta)
    return montar('bets', 'Clínica Doma — Vício em apostas', c)


def monstrinhos():
    p = partes_home()
    h = heroi('👾 CONHEÇA OS MONSTRINHOS', 'Conheça os 12 monstrinhos da Caverna',
              'Medo, ansiedade, culpa, raiva: cada sentimento difícil tem um monstrinho. Aqui você conhece os doze, com a pergunta que cada um faz e os sinais que ele costuma deixar no corpo.',
              '🚀 COMEÇAR MEU NÍVEL 1 GRÁTIS', '/a-travessia',
              '🪪 O Nível 1 da Travessia é gratuito para quem tem a Carteira Doma')
    return composta('monstrinhos', 'Clínica Doma — Conheça os Monstrinhos',
                    [h] + paginas_novas.monstrinhos_blocos() + [p['APOIO EM CRISE'], p['INSTAGRAM']])


def polvo():
    p = partes_home()
    h = heroi('🐙 O MONSTRINHO POLVO', 'O Monstrinho Polvo: para quem convive com uma doença crônica',
              'Remédios, horários, exames e aquele cansaço que só você sente. Esta página é para você que carrega esse malabarismo todos os dias, e para a sua família.',
              '🗺️ CONHECER A TRAVESSIA', '/a-travessia',
              '🐙 O Polvo aparece no Nível 3 da Travessia: Acolher, Não Domar')
    return composta('polvo', 'Clínica Doma — O Monstrinho Polvo',
                    [h] + paginas_novas.polvo_blocos() + [p['TRAGA SEU MONSTRINHO'], p['APOIO EM CRISE'], p['INSTAGRAM']])


def pacientes():
    p = partes_home()
    h = heroi('🛋️ PARA PACIENTES DA CLÍNICA', 'Boas-vindas à Clínica Doma: o que saber antes da primeira sessão',
              'Esta página é para você que vai começar o atendimento. Em poucos minutos você entende o nosso jeito de trabalhar e já pode dar o primeiro passo em casa.',
              '🪪 EMITIR MINHA CARTEIRA GRÁTIS', '/carteira-doma',
              '✨ A Carteira Doma é gratuita e abre o Nível 1 da Travessia')
    return composta('pacientes', 'Clínica Doma — Para pacientes da clínica',
                    [h] + paginas_novas.pacientes_blocos() + [p['TRAGA SEU MONSTRINHO'], p['APOIO EM CRISE']],
                    {'/carteira-d': '/carteira-doma'})


def faq():
    p = partes_home()
    h = heroi('❓ PERGUNTAS FREQUENTES', 'Perguntas frequentes sobre a Clínica Doma',
              'As dúvidas mais comuns sobre a Travessia, a Carteira Doma, os planos, o Indique Doma e o atendimento na clínica.',
              '💬 FALAR COM A CLÍNICA', paginas_legais.ZAP,
              '🪪 O Nível 1 da Travessia é gratuito para quem tem a Carteira Doma')
    rolar = {'#faq-' + t: 'rolar:faq-' + t for t in ('sobre', 'travessia', 'carteira', 'planos', 'indique', 'clinica', 'dados')}
    return composta('faq', 'Clínica Doma — Perguntas frequentes',
                    [h] + paginas_legais.faq_blocos() + [p['APOIO EM CRISE']], rolar)


def privacidade():
    h = heroi('🔒 POLÍTICA DE PRIVACIDADE', 'Política de privacidade: como cuidamos dos seus dados',
              'Aqui você vê, em linguagem simples, quais dados a Clínica Doma guarda, para que usa, com quem compartilha e como você pode ver, corrigir ou apagar tudo.',
              '✉️ FALAR SOBRE OS MEUS DADOS', 'mailto:' + paginas_legais.EMAIL,
              '🗓️ Última atualização: ' + paginas_legais.ATUALIZADO)
    return composta('privacidade', 'Clínica Doma — Política de privacidade', [h] + paginas_legais.privacidade_blocos())


def termos():
    h = heroi('📜 TERMOS DE USO', 'Termos de uso da Clínica Doma',
              'As regras para usar o site, a Carteira Doma, a Travessia, os planos, a loja e o Indique Doma, em linguagem simples.',
              '💬 FALAR COM A CLÍNICA', paginas_legais.ZAP,
              '🗓️ Última atualização: ' + paginas_legais.ATUALIZADO)
    return composta('termos', 'Clínica Doma — Termos de uso', [h] + paginas_legais.termos_blocos())


if __name__ == '__main__':
    home(); travessia(); bets(); planos(); carteira(); indique()
    monstrinhos(); polvo(); pacientes()
    faq(); privacidade(); termos()
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)))
