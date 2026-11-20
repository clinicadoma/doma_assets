# -*- coding: utf-8 -*-
"""Textos e blocos que vêm do plano "Melhorias a partir da entrevista com a criadora" (13/11/2026).

Princípio: a plataforma é material de autoconhecimento; domar é acolher; a Travessia tem
3 capítulos de 4 níveis (12 níveis) e o Nível 1 é a introdução gratuita O Meu Ano Inicia Agora.
"""

PAGINA_NIVEL_1 = '/nivel-1'


def troca(c, antigo, novo, vezes=1):
    """Troca um trecho conferindo quantas vezes ele aparece (para o protótipo não mudar sem a gente ver)."""
    n = c.count(antigo)
    if n != vezes:
        raise SystemExit('esperava %d vez(es), achei %d: %s' % (vezes, n, antigo[:70]))
    return c.replace(antigo, novo)


# ---------------------------------------------------------------- HOME
def _cartao_domador(emoji, titulo, texto):
    return ('<div style="background: #ffffff; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; gap: 6px; border-left: 5px solid #f7d774">'
            '<span style="font-size: 28px; line-height: 1">%s</span>'
            '<strong style="color: #0f2744; font-size: 17px">%s</strong>'
            '<span style="font-size: 15px; color: #475569">%s</span></div>') % (emoji, titulo, texto)


DOMADOR_HTML = '''<!-- O QUE É UM DOMADOR -->
      <section style="background: #fffbeb; border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; gap: 18px">
        <div style="text-align: center; display: flex; flex-direction: column; gap: 8px">
          <h2 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 3.2vw, 32px); line-height: 1.2; font-weight: 800; color: #0f2744">O que é um Domador? 🤝</h2>
          <p style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(18px, 2.2vw, 22px); font-style: italic; font-weight: 700; color: #b45309">Domar não é controlar. É acolher.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px">
          %s
          %s
          %s
          %s
        </div>
      </section>

      ''' % (
    _cartao_domador('👾', 'O monstrinho é um sentimento',
                    'Você não é ansioso. Existe um monstrinho da ansiedade agindo em você, e dá para entender por quê.'),
    _cartao_domador('🛡️', 'Ele quer te proteger',
                    'Todo monstrinho tem uma história. Ele não quer te atrapalhar: quer te proteger de algo que você já viveu.'),
    _cartao_domador('🫶', 'Domador e monstrinho são uma dupla',
                    'Domador não é quem usa chicote. É quem escuta, entende e acolhe o seu monstrinho.'),
    _cartao_domador('🌱', 'Ele não some: ele soma',
                    'O objetivo não é eliminar os seus monstrinhos. É fazer as pazes com eles e crescer junto.'),
)


def home(c):
    c = troca(c, '🧠✨ Quando a gente não doma esses bichos, eles bagunçam a nossa vida inteira. 🌪️🐾',
              '🧠✨ Quando a gente não acolhe esses bichinhos, eles gritam cada vez mais alto. 🌪️🐾')
    c = troca(c, 'Que tal conhecer de perto quem anda bagunçando a sua vida?',
              'Que tal conhecer de perto quem anda pedindo a sua atenção?')
    c = troca(c, 'Comece hoje pela introdução, grátis com a sua Carteira Doma.',
              'Comece hoje pelo Nível 1, grátis com a sua Carteira Doma.')
    c = troca(c, 'COMEÇAR MINHA INTRODUÇÃO 🚀', 'COMEÇAR MEU NÍVEL 1 🚀')
    # "O que é um Domador?" logo depois da campanha (a campanha termina no convite da carteira)
    i = c.find('<!-- MOMENTO DE PAUSA -->')
    assert i > 0
    return c[:i] + DOMADOR_HTML + c[i:]


# ---------------------------------------------------------------- A TRAVESSIA
def _item(emoji, texto):
    return '<li style="display: flex; gap: 8px; align-items: flex-start"><span>%s</span><span>%s</span></li>' % (emoji, texto)


def _nivel(rotulo, nome, itens, fundo='#f0f9ff', cor='#0b7cb8'):
    return ('''<div style="background: %s; border-radius: 14px; padding: 16px; display: flex; flex-direction: column; gap: 8px">
              <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; color: %s">%s</span>
              <strong style="color: #0f2744; font-size: 17px">%s</strong>
              <ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 4px; font-size: 14px; color: #475569">%s</ul>
            </div>''') % (fundo, cor, rotulo, nome, ''.join(_item(e, t) for e, t in itens))


def _nivel_curto(rotulo, nome, texto, fundo, cor):
    return ('''<div style="background: %s; border-radius: 14px; padding: 16px; display: flex; flex-direction: column; gap: 6px">
              <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; color: %s">%s</span>
              <strong style="color: #0f2744; font-size: 17px">%s</strong>
              <span style="font-size: 14px; color: #475569">%s</span>
            </div>''') % (fundo, cor, rotulo, nome, texto)


def _casa(n):
    if n == 1:
        estilo = 'background: #f7d774; color: #0f2744'
    elif n <= 4:
        estilo = 'background: #0b7cb8; color: #ffffff'
    elif n <= 8:
        estilo = 'background: #fef3c7; color: #92400e'
    else:
        estilo = 'background: #ffe4e6; color: #9f1239'
    return '<span style="%s; border-radius: 8px; padding: 8px 0; text-align: center; font-size: 13px; font-weight: 800">%d</span>' % (estilo, n)


BARRA_HTML = '''<!-- BARRA DOS 12 NÍVEIS -->
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 18px; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px">
          <div style="display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 6px">
            <strong style="color: #0f2744; font-size: 17px">🏅 Pequenas vitórias, nível por nível</strong>
            <span style="font-size: 13px; font-weight: 700; color: #64748b">12 níveis · 3 capítulos</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(12, 1fr); gap: 4px" role="img" aria-label="Os 12 níveis da Travessia: 1 a 4 no capítulo O Acolhimento, 5 a 8 na Caverna dos Monstros e 9 a 12 na Ressignificação">%s</div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; text-align: center; font-size: 12px; font-weight: 800; line-height: 1.3">
            <span style="color: #0b7cb8">O Acolhimento</span>
            <span style="color: #92400e">A Caverna dos Monstros</span>
            <span style="color: #9f1239">A Ressignificação</span>
          </div>
          <p style="margin: 0; font-size: 14px; color: #475569">Muita coisa muda e a sensação ainda é de que “está tudo igual”. Os níveis existem para isso: cada um que você conclui vira uma graduação na sua carteira, para você enxergar o quanto já caminhou.</p>
        </div>''' % ''.join(_casa(n) for n in range(1, 13))


MAPA_HTML = '''<!-- A TRILHA DOS 12 NÍVEIS -->
      <section style="display: flex; flex-direction: column; gap: 18px">
        <div style="text-align: center; display: flex; flex-direction: column; gap: 6px">
          <h2 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 3.2vw, 32px); font-weight: 800; color: #0f2744">O mapa da sua Travessia 🗺️</h2>
          <p style="margin: 0; color: #475569">São 12 níveis em 3 capítulos. O Nível 1 é grátis com a Carteira Doma. Depois, cada mês de plano libera um nível novo: o Mês 1 é o mês em que você começa, seja ele qual for.</p>
        </div>

        %(barra)s

        <!-- CAPÍTULO 1 -->
        <div style="border: 2px solid #bae6fd; border-radius: 18px; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: #ffffff">
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px">
            <h3 style="margin: 0; font-size: 18px; color: #0f2744">🌅 Capítulo 1 · O Acolhimento · Níveis 1 a 4</h3>
            <span style="padding: 3px 10px; border-radius: 999px; background: #dcfce7; color: #166534; font-size: 12px; font-weight: 800">DISPONÍVEL</span>
          </div>
          <div style="background: #0f2744; border-radius: 14px; padding: 18px; display: flex; flex-wrap: wrap; align-items: center; gap: 16px; color: #e2e8f0">
            <span style="flex: none; width: 56px; height: 56px; border-radius: 999px; background: #f7d774; display: flex; align-items: center; justify-content: center; font-size: 28px">📖</span>
            <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 4px">
              <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; color: #f7d774">NÍVEL 1 · GRÁTIS COM A CARTEIRA 🪪</span>
              <strong style="color: #ffffff; font-size: 18px">O Meu Ano Inicia Agora</strong>
              <span style="font-size: 14px">Um olhar sincero para o seu solo e o fim das ilusões: termo de compromisso, Raio-X de Energia Vital, Mochila de Descarte, Ritual Final e Roleta de Boas-Vindas.</span>
            </div>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px">
            %(n2)s
            %(n3)s
            %(n4)s
          </div>
        </div>

        <!-- CAPÍTULO 2 -->
        <div style="border: 2px dashed #cbd5e1; border-radius: 18px; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: #f8fafc">
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px">
            <h3 style="margin: 0; font-size: 18px; color: #0f2744">🕯️ Capítulo 2 · A Caverna dos Monstros · Níveis 5 a 8</h3>
            <span style="padding: 3px 10px; border-radius: 999px; background: #fef3c7; color: #92400e; font-size: 12px; font-weight: 800">EM CONSTRUÇÃO</span>
          </div>
          <p style="margin: 0; font-size: 15px; color: #475569">A elaboração: o mergulho em cada um dos seus monstrinhos, três por nível.</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%%), 1fr)); gap: 10px">
            %(n5)s
            %(n6)s
            %(n7)s
            %(n8)s
          </div>
        </div>

        <!-- CAPÍTULO 3 -->
        <div style="border: 2px solid #fde68a; border-radius: 18px; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: #fffdf5">
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px">
            <h3 style="margin: 0; font-size: 18px; color: #0f2744">🏆 Capítulo 3 · A Ressignificação · Níveis 9 a 12</h3>
            <span style="padding: 3px 10px; border-radius: 999px; background: #fef3c7; color: #92400e; font-size: 12px; font-weight: 800">EM CONSTRUÇÃO</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%%), 1fr)); gap: 10px">
            %(n9)s
            %(n10)s
            %(n11)s
            %(n12)s
          </div>
        </div>

        <!-- A TRAVESSIA CONTINUA -->
        <div style="background: #0f2744; border-radius: 18px; padding: 22px; display: flex; flex-direction: column; gap: 8px; color: #e2e8f0">
          <h3 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 800; color: #f7d774">🔁 A Travessia continua</h3>
          <p style="margin: 0; font-size: 15px">No fim do Nível 12 você faz a sua autoavaliação dos 12 meses e coloca tudo em prática. Novos monstrinhos vão aparecer pela vida, e o caminho pode ser revisitado sempre: quem segue no plano recomeça a Travessia como manutenção, e novos conteúdos estão nos planos da Clínica Doma.</p>
          <p style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: 17px; font-style: italic; font-weight: 700; color: #ffffff">A Travessia é um caminho para a vida toda.</p>
        </div>
      </section>

      ''' % {
    'barra': BARRA_HTML,
    'n2': _nivel('NÍVEL 2 · MÊS 1', 'Conhecendo os Monstrinhos',
                 [('👋', 'Boas-vindas, Doma Coins e Carteira Digital'), ('🃏', 'Jogo da Memória'),
                  ('📜', 'O Papel de Pão'), ('🏡', 'Triagem de Vida')]),
    'n3': _nivel('NÍVEL 3 · MÊS 2', 'Acolher, Não Domar',
                 [('🎩', 'Não é Domar'), ('🎒', 'A Bagagem do Domador'), ('🎡', 'A Roleta Interna'),
                  ('🐙', 'Acolhendo o Polvo'), ('⚖️', 'A Magia da Desidentificação'), ('🥚', 'Vamos chocar? O meu ovo')]),
    'n4': _nivel('NÍVEL 4 · MÊS 3', 'As Vozes de Dentro',
                 [('🏛️', 'O Tribunal Interno'), ('🗣️', 'De quem é essa voz?'), ('🌳', 'A origem da voz'),
                  ('🖼️', 'O Retrato Falado'), ('🧸', 'Resgate da Criança Interior'), ('✉️', 'Uma Carta ao Domador')]),
    'n5': _nivel_curto('NÍVEL 5', 'Os Monstrinhos do Alarme', 'Medo, Ansiedade e Insegurança.', '#ffffff', '#92400e'),
    'n6': _nivel_curto('NÍVEL 6', 'Os Monstrinhos do Espelho', 'Autoestima, Rejeição e Culpa.', '#ffffff', '#92400e'),
    'n7': _nivel_curto('NÍVEL 7', 'Os Monstrinhos do Fogo e do Vazio', 'Raiva, Vazio e o Monstrinho Sem Nome.', '#ffffff', '#92400e'),
    'n8': _nivel_curto('NÍVEL 8', 'Os Monstrinhos da Rotina', 'Procrastinação, Perfeccionismo e Síndrome do Impostor.', '#ffffff', '#92400e'),
    'n9': _nivel_curto('NÍVEL 9', 'Do Outro Lado da Caverna',
                       'Autoavaliação: os monstrinhos que você já ressignificou, os que ainda não aceita e os que são de quem convive com você.', '#ffffff', '#9f1239'),
    'n10': _nivel_curto('NÍVEL 10', 'Os Monstrinhos dos Outros',
                        'Convivência e família: limites, jogos para fazer junto e o ritual do chá.', '#ffffff', '#9f1239'),
    'n11': _nivel_curto('NÍVEL 11', 'O Que Eu Realmente Preciso',
                        'Check-up da vida e planner: o que você precisa, não só o que você quer.', '#ffffff', '#9f1239'),
    'n12': _nivel_curto('NÍVEL 12', 'O Tesouro do Domador',
                        'O Tesouro do Domador, A Jornada pelos Insights e a chegada ao final.', '#ffffff', '#9f1239'),
}


def travessia(c, bloco_fechado):
    # mapa novo: 3 capítulos, 12 níveis, barra de pequenas vitórias e "A Travessia continua"
    a, b = bloco_fechado(c, '<!-- A TRILHA DOS 12 NÍVEIS -->', 'section')
    assert 'ÚLTIMO NÍVEL' in c[a:b] and 'O QUE VOCÊ VAI APRENDER' not in c[a:b]
    c = c[:a] + MAPA_HTML.rstrip() + c[b:]
    # o Nível 1 é a introdução gratuita (nada de "Nível Introdutório")
    c = troca(c, '📖 INTRODUÇÃO · O MEU ANO INICIA AGORA', '📖 NÍVEL 1 · O MEU ANO INICIA AGORA')
    c = troca(c, 'E a sua introdução começa hoje.', 'E o seu Nível 1 começa hoje.')
    c = troca(c, '🚀 COMEÇAR MINHA INTRODUÇÃO GRÁTIS', '🚀 COMEÇAR MEU NÍVEL 1 GRÁTIS')
    c = troca(c, 'depois da introdução, um nível novo por mês', 'depois do Nível 1, um nível novo por mês')
    c = troca(c, 'O que te espera no Nível Introdutório 🎒', 'O que te espera no Nível 1 🎒')
    c = troca(c, '✅ Nível Introdutório completo', '✅ Nível 1 completo: O Meu Ano Inicia Agora')
    c = troca(c, 'Já tenho carteira: entrar na minha introdução →', 'Já tenho carteira: entrar no meu Nível 1 →')
    c = troca(c, '🚀 COMEÇAR MINHA INTRODUÇÃO</a>', '🚀 COMEÇAR MEU NÍVEL 1</a>')
    # domar é acolher
    c = troca(c, 'Mapear e desarmar seus Monstros Internos:', 'Mapear e acolher os seus monstrinhos internos:')
    assert 'Introdut' not in c, 'sobrou "Nível Introdutório" na Travessia'
    return c


# ---------------------------------------------------------------- VÍCIO (BETS)
def bets(c):
    return troca(c, 'Existe um monstro invisível que destrói mentes, lares e patrimônios inteiros: o vício silencioso em apostas online 🎰. Se você caiu nessa armadilha e não consegue sair, ou vê alguém que ama afundando nesse ciclo, saiba que ',
                 'O vício em apostas online 🎰 é um monstrinho que cresce em silêncio. Quase sempre ele aparece tentando aliviar uma dor (ansiedade, solidão, aperto financeiro) e acaba pesando na mente, na família e no bolso. Se você entrou nesse ciclo e não consegue sair, ou vê alguém que ama afundando nele, saiba que ')


# ---------------------------------------------------------------- PLANOS e CARTEIRA (textos de abertura)
PLANOS_TEXTO = ('Todos os planos dão acesso à Travessia do Domador: cada mês de plano libera um nível novo, além da comunidade e dos sorteios. '
                'O Premium inclui também sessões presenciais a cada 15 dias, em que você pode retomar com a terapeuta o nível do mês. '
                'Os conteúdos online são material de autoconhecimento e não substituem a terapia.')

CARTEIRA_TEXTO = ('Com a sua carteira gratuita você vira um Domador, faz o Nível 1 completo da Travessia (O Meu Ano Inicia Agora), '
                  'ganha suas primeiras Doma Coins e tem o seu progresso salvo na sua conta. '
                  'A carteira e os conteúdos online são material de autoconhecimento e não substituem a terapia.')
