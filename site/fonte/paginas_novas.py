# -*- coding: utf-8 -*-
"""Páginas novas do plano de melhorias (passo 3): Conheça os Monstrinhos, O Monstrinho Polvo
e Para pacientes da clínica.

De onde vêm os textos:
- perguntas, sinais no corpo e frases dos 9 monstrinhos: Roleta Interna do livro (resumidos);
- Polvo: capítulos "Acolhendo o Polvo", "Superpoder", "Malabarista", "Aliviando a Mochila" e "A Ponte de Cristal" (para quem cuida) do livro;
- o resto foi escrito a partir do plano e precisa da aprovação da Daniela.
Filtro: material de autoconhecimento; nada de "diagnóstico", "cura" ou "tratar" para a plataforma;
nunca desencorajar remédio; sintoma que persiste é assunto de médico.
"""

H2 = "margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 3.2vw, 32px); line-height: 1.2; font-weight: 800; color: #0f2744"
GRADE = "display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr)); gap: 12px"
GRADE3 = "display: grid; grid-template-columns: repeat(auto-fit, minmax(min(180px, 100%), 1fr)); gap: 12px"
AVISO = "margin: 0; padding: 14px 16px; border-radius: 14px; background: #f8fafc; border: 1px solid #cbd5e1; font-size: 14px; line-height: 1.55; color: #334155"
BOTAO_AZUL = "display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border-radius: 999px; background: #0b7cb8; color: #ffffff; font-size: 16px; font-weight: 800; text-decoration: none; box-shadow: 0 8px 20px rgba(11, 124, 184, 0.35)"
BOTAO_CLARO = "display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border-radius: 999px; background: #ffffff; color: #0f2744; border: 2px solid #0f2744; font-size: 16px; font-weight: 800; text-decoration: none"
BOTAO_OURO = "display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border-radius: 999px; background: #f7d774; color: #0f2744; font-size: 16px; font-weight: 800; text-decoration: none; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25)"


def titulo(texto, sub=None):
    s = '<div style="text-align: center; display: flex; flex-direction: column; gap: 8px"><h2 style="%s">%s</h2>' % (H2, texto)
    if sub:
        s += '<p style="margin: 0 auto; max-width: 640px; color: #475569">%s</p>' % sub
    return s + '</div>'


def cartao(emoji, nome, texto, borda='#f7d774', fundo='#ffffff'):
    return ('<div style="background: %s; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; gap: 6px; border-left: 5px solid %s">'
            '<span style="font-size: 28px; line-height: 1">%s</span>'
            '<strong style="color: #0f2744; font-size: 17px">%s</strong>'
            '<span style="font-size: 15px; color: #475569">%s</span></div>') % (fundo, borda, emoji, nome, texto)


# ================================================================== CONHEÇA OS MONSTRINHOS
def _monstrinho(emoji, nome, pergunta, sinais, frase, cor):
    return ('''<div style="background: #ffffff; border-radius: 16px; padding: 18px; display: flex; flex-direction: column; gap: 10px; border-top: 6px solid %s; box-shadow: 0 6px 16px rgba(15, 39, 68, 0.06)">
            <div style="display: flex; align-items: center; gap: 10px"><span style="font-size: 32px; line-height: 1">%s</span><strong style="color: #0f2744; font-size: 19px">%s</strong></div>
            <p style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: 17px; font-style: italic; font-weight: 700; color: #0f2744">“%s”</p>
            <p style="margin: 0; font-size: 14px; color: #475569"><strong style="color: #0b7cb8">Sinais comuns no corpo:</strong> %s</p>
            <p style="margin: 0; font-size: 14px; color: #475569"><strong style="color: #b45309">Para pensar:</strong> %s</p>
          </div>''') % (cor, emoji, nome, pergunta, sinais, frase)


def _em_preparo(emoji, nome, texto, cor):
    return ('''<div style="background: #ffffff; border-radius: 16px; padding: 18px; display: flex; flex-direction: column; gap: 10px; border-top: 6px solid %s; box-shadow: 0 6px 16px rgba(15, 39, 68, 0.06)">
            <div style="display: flex; align-items: center; gap: 10px"><span style="font-size: 32px; line-height: 1">%s</span><strong style="color: #0f2744; font-size: 19px">%s</strong></div>
            <p style="margin: 0; font-size: 15px; color: #475569">%s</p>
          </div>''') % (cor, emoji, nome, texto)


def _grupo(rotulo, nome, fundo, cartoes, nota=None):
    return ('''<section style="background: %s; border-radius: 18px; padding: clamp(20px, 3.4vw, 30px) clamp(16px, 3.4vw, 30px); display: flex; flex-direction: column; gap: 14px">
        <div style="display: flex; flex-direction: column; gap: 4px">
          <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; color: #64748b">%s</span>
          <h3 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(20px, 2.6vw, 26px); font-weight: 800; color: #0f2744">%s</h3>%s
        </div>
        <div style="%s">
          %s
        </div>
      </section>

      ''') % (fundo, rotulo, nome,
              ('\n          <p style="margin: 0; font-size: 14px; color: #475569">%s</p>' % nota) if nota else '',
              GRADE3, '\n          '.join(cartoes))


def monstrinhos_blocos():
    abertura = '''<section style="display: flex; flex-direction: column; gap: 14px">
        %s
        <div style="%s">
          %s
          %s
          %s
        </div>
        <p style="margin: 0; padding: 14px 18px; border-radius: 14px; border: 2px dashed #bae6fd; background: #f0f9ff; color: #0b7cb8; font-size: 16px; font-weight: 700; text-align: center">🏛️ A palavra “monstro” vem do latim <em>monstrare</em>: “aquele que mostra”. 👁️</p>
        <p style="%s">ℹ️ <strong>Importante:</strong> os sinais desta página são comuns e servem para você se observar. Eles não são um diagnóstico e não substituem uma avaliação médica: se um sintoma persiste ou preocupa, procure um médico. A Travessia é um material de autoconhecimento e não substitui a terapia.</p>
      </section>

      ''' % (titulo('O que é um monstrinho? 👾', 'É o nome que a gente dá a um sentimento, para olhar para ele de fora, sem rótulo.'),
             GRADE3,
             cartao('🏷️', 'Sem rótulo', 'Você não é ansioso. Existe um monstrinho da ansiedade agindo em você, e dá para entender por quê.'),
             cartao('🛡️', 'Ele quer te proteger', 'Todo monstrinho tem uma história. Ele não quer te atrapalhar: quer te proteger de algo que você já viveu.'),
             cartao('🌱', 'Ele não some: ele soma', 'O objetivo não é eliminar os seus monstrinhos. É fazer as pazes com eles e crescer junto.'),
             AVISO)

    alarme = _grupo('NÍVEL 5 DA TRAVESSIA', '🚨 Os Monstrinhos do Alarme', '#f0f9ff', [
        _monstrinho('🛡️', 'Medo', 'Seu medo já trancou a porta da sua vida por dentro?',
                    'coração acelerado, mãos frias e suadas, respiração curta, boca seca.',
                    'o medo existe para te proteger de um perigo real. O primeiro passo é perceber se o perigo está do lado de fora ou só dentro da mente.', '#5CD1FF'),
        _monstrinho('⏳', 'Ansiedade', 'Se parasse agora, o que sobraria dos seus planos?',
                    'aperto no peito, pernas que não param, respiração rápida, tremores leves, ranger de dentes.',
                    'estar o tempo todo ocupado não é o mesmo que ser produtivo. Muitas vezes é só a ansiedade ditando o ritmo.', '#FFB74D'),
        _monstrinho('🎭', 'Insegurança', 'Você é humilde ou tem pavor de que descubram que não sabe o que faz?',
                    'mãos inquietas, roer unhas, ombros encolhidos, voz vacilante, fugir do olhar do outro.',
                    'não é que você seja incapaz. É o medo de não ser suficiente que paralisa antes mesmo de tentar.', '#FF85B3'),
    ])
    espelho = _grupo('NÍVEL 6 DA TRAVESSIA', '🪞 Os Monstrinhos do Espelho', '#fffbeb', [
        _monstrinho('🪞', 'Autoestima', 'Se falasse com amigos como fala consigo, teria amigos?',
                    'postura curvada, fugir de espelhos, voz mais baixa, vontade de se esconder.',
                    'é como viver pedindo desculpas por ocupar espaço. A sua existência, por si só, já merece amor e respeito.', '#FFD54F'),
        _monstrinho('❄️', 'Rejeição', 'Decidiu se retirar antes que tivessem a chance de te mandar embora?',
                    'nó na garganta, frio no peito, peso no estômago, braços cruzados para se proteger.',
                    'a rejeição dói menos pelo ato em si e mais pela história que a gente conta sobre o que o outro pensa.', '#B388FF'),
        _monstrinho('⛓️', 'Culpa', 'Carrega esse peso por conforto no papel de culpado?',
                    'peso nos ombros, olhar para baixo, aperto no estômago, suspiros, um cansaço que não passa.',
                    'a responsabilidade corrige o erro e ensina algo novo. A culpa só castiga e prende no passado.', '#81D4FA'),
    ])
    fogo = _grupo('NÍVEL 7 DA TRAVESSIA', '🔥 Os Monstrinhos do Fogo e do Vazio', '#fff1f2', [
        _monstrinho('🔥', 'Raiva', 'Quem é o dono da sua voz: você ou o monstro?',
                    'calor no rosto, mandíbula travada, punhos cerrados, respiração forte.',
                    'explosão não é sinal de força. Cuidar da raiva não é engolir: é levar essa energia para algo que construa.', '#FF5252'),
        _monstrinho('🌌', 'Vazio', 'Está preenchendo o tempo ou distraindo o buraco no peito?',
                    'apatia, sensação de oco no peito, movimentos lentos, pouca energia, olhar parado.',
                    'o vazio não é falta de pessoas ou de coisas. É a ausência de você na sua própria história.', '#CE93D8'),
        _monstrinho('🕯️', 'O Monstrinho Sem Nome', 'Qual dor você carrega por medo de que ela te devore?',
                    'mal-estar difícil de explicar, frio e calor que se alternam, um aperto que muda de lugar.',
                    'nem toda dor já ganhou um nome, mas toda dor ocupa um espaço dentro de você. Dar atenção a ela é o começo.', '#A5D6A7'),
    ])
    rotina = _grupo('NÍVEL 8 DA TRAVESSIA · EM PREPARAÇÃO', '🗓️ Os Monstrinhos da Rotina', '#f8fafc', [
        _em_preparo('⏰', 'Procrastinação', 'O “depois eu faço” que fica esperando a data perfeita para começar.', '#94a3b8'),
        _em_preparo('🎯', 'Perfeccionismo', 'O “só vale se ficar perfeito”, que quase nunca deixa nada ficar pronto.', '#94a3b8'),
        _em_preparo('🥸', 'Síndrome do Impostor', 'A sensação de que, a qualquer momento, vão descobrir que você não é tão bom assim.', '#94a3b8'),
    ], 'Eles já aparecem no Nível 1, O Meu Ano Inicia Agora. O mergulho em cada um está sendo preparado.')

    caverna = '''<section style="background: linear-gradient(180deg, #0f2744 0%%, #1b3d63 100%%); border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; color: #e2e8f0">
        <h2 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 3.2vw, 32px); line-height: 1.2; font-weight: 800; color: #ffffff">🕯️ O convite para a Caverna dos Monstros</h2>
        <p style="margin: 0; max-width: 620px">A Caverna é o Capítulo 2 da Travessia do Domador: quatro níveis para conhecer cada monstrinho de perto, saber do que ele se alimenta, quando acorda e quando adormece. Ela está em construção. O caminho até lá começa pelo Nível 1, que é grátis com a Carteira Doma.</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px">
          <a href="/a-travessia" style="%s">🗺️ VER O MAPA DA TRAVESSIA</a>
        </div>
      </section>

      <a href="/monstrinho-polvo" style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px; padding: 20px 22px; border-radius: 18px; background: #f5f3ff; border: 2px solid #ddd6fe; color: #0f2744; text-decoration: none">
        <span style="flex: none; font-size: 44px; line-height: 1">🐙</span>
        <span style="flex: 1 1 240px; min-width: 0; display: flex; flex-direction: column; gap: 4px">
          <strong style="font-size: 18px">Convive com uma doença crônica?</strong>
          <span style="font-size: 15px; color: #475569">Conheça o Monstrinho Polvo: o malabarismo com remédios, horários e aquele cansaço que só você sente.</span>
          <span style="font-size: 15px; font-weight: 800; color: #6d28d9">Conhecer o Polvo →</span>
        </span>
      </a>

      ''' % BOTAO_OURO
    return [abertura, alarme, espelho, fogo, rotina, caverna]


# ================================================================== O MONSTRINHO POLVO
def polvo_blocos():
    quem = '''<section style="display: flex; flex-direction: column; align-items: center; gap: 18px; text-align: center">
        <img src="/_blob/d7662f6f0254a47315e85a69b305ee82" alt="Na Clínica dos Monstros, um polvo roxo sai de uma mochila fazendo malabarismo com relógio, calendário, remédios e consultas, ao lado de uma criança e de um monstrinho azul" style="width: 100%%; max-width: 560px; height: auto; display: block; border-radius: 18px; box-shadow: 0 10px 24px rgba(15, 39, 68, 0.12)">
        %s
        <p style="margin: 0; max-width: 640px; padding: 18px 20px; border-radius: 16px; background: #f5f3ff; border-left: 5px solid #8b5cf6; text-align: left; font-size: 16px; color: #334155">“Sei bem como é cansativo fazer malabarismo com horários de remédios, exames e aquela fadiga que só você sente. Não precisa se desgastar tentando me explicar; eu estou aqui para caminhar junto com você.”<br><strong style="color: #6d28d9">Daniela Pinheiros, psicanalista</strong></p>
      </section>

      ''' % titulo('Quem é o Polvo? 🐙', 'Às vezes a gente guarda na bagagem um Polvo muito especial: silencioso, invisível, mas que pede um pouquinho de atenção. Você já sentiu ele por aí?')

    desafios = '''<section style="background: #f5f3ff; border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; gap: 18px">
        %s
        <div style="%s">
          %s
          %s
          %s
          %s
        </div>
      </section>

      ''' % (titulo('Os desafios do malabarista 🤹', 'Quatro pesos que quase ninguém vê, e um jeito mais gentil de olhar para cada um.'),
             GRADE,
             cartao('⏱️', 'O relógio que não para', 'A exaustão de ter a mente sempre alerta aos horários e cuidados. Essa vigilância também é a prova de que você cuida muito bem de si.', '#8b5cf6'),
             cartao('🛡️', 'O escudo contra pitacos', 'O cansaço de ter que justificar o seu corpo o tempo todo. Dá para aprender a colocar limites com elegância.', '#8b5cf6'),
             cartao('🔍', 'O espelho mais gentil', 'A vergonha de se sentir “marcado”. O convite é trocar a autocrítica pela admiração por um corpo que luta por você.', '#8b5cf6'),
             cartao('📦', 'Recriando a espontaneidade', 'A sensação de sonhos roubados. A vida não parou: ela pediu um novo roteiro.', '#8b5cf6'))

    superpoder = '''<section style="background: linear-gradient(180deg, #0f2744 0%%, #1b3d63 100%%); border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; color: #e2e8f0">
        <h2 style="margin: 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 3.2vw, 32px); line-height: 1.2; font-weight: 800; color: #f7d774">🧭 O superpoder da autonomia</h2>
        <p style="margin: 0; max-width: 620px; font-size: 17px">A medicina entrega o mapa. Mas quem guia a Travessia é você. Cuidar da sua mente e seguir o tratamento são os maiores gestos de amor que você pode se dar hoje.</p>
        <p style="margin: 0; max-width: 620px">O Polvo não define quem você é. Ele é aquele cansaço que às vezes surge. Tudo bem não precisar sorrir o tempo todo para poupar os outros.</p>
      </section>

      <p style="%s">ℹ️ <strong>Importante:</strong> esta página e a Travessia são material de autoconhecimento. Elas não substituem o acompanhamento do seu médico nem o tratamento que ele indicou. Nunca mude ou interrompa um remédio por conta própria: converse antes com quem cuida de você.</p>

      ''' % AVISO

    mochila = '''<section style="display: flex; flex-direction: column; gap: 16px">
        %s
        <div style="%s">
          <div style="background: #fffbeb; border-radius: 14px; padding: 16px; font-size: 16px; font-weight: 700; color: #0f2744">1. O que o meu corpo mais pede hoje é…</div>
          <div style="background: #fffbeb; border-radius: 14px; padding: 16px; font-size: 16px; font-weight: 700; color: #0f2744">2. O comentário que não vou absorver mais é…</div>
          <div style="background: #fffbeb; border-radius: 14px; padding: 16px; font-size: 16px; font-weight: 700; color: #0f2744">3. O sonho que eu vou adaptar (sem desistir) é…</div>
          <div style="background: #fffbeb; border-radius: 14px; padding: 16px; font-size: 16px; font-weight: 700; color: #0f2744">4. O que eu mais preciso ouvir de mim hoje é…</div>
        </div>
        <p style="margin: 0; text-align: center; color: #475569">Esse exercício faz parte do Nível 3 da Travessia, <strong>Acolher, Não Domar</strong>, onde o Polvo aparece.</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px">
          <a href="/a-travessia" style="%s">🗺️ CONHECER A TRAVESSIA</a>
        </div>
      </section>

      ''' % (titulo('Aliviando a mochila 🎒', 'Colocar em palavras ajuda a desatar os nós do peito. Complete as frases, no papel ou só em pensamento.'),
             GRADE, BOTAO_AZUL)

    def fala(n, evitar, verdade, diga):
        return ("""<div style="background: #ffffff; border-radius: 14px; padding: 16px 18px; display: flex; gap: 14px; align-items: flex-start; border-left: 5px solid #14b8a6">
            <span style="flex: none; width: 36px; height: 36px; border-radius: 999px; background: #ccfbf1; color: #0f766e; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800">%d</span>
            <span style="display: flex; flex-direction: column; gap: 4px"><strong style="color: #0f2744; font-size: 17px">%s</strong><span style="font-size: 15px; color: #475569">%s</span><span style="font-size: 15px; font-weight: 700; color: #0f766e">%s</span></span>
          </div>""") % (n, evitar, verdade, diga)

    familia = """<section style="background: #f0fdfa; border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; gap: 16px">
        %s
        <div style="display: flex; flex-direction: column; gap: 10px">
          %s
          %s
          %s
          %s
          %s
        </div>
        <p style="margin: 0; text-align: center; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(17px, 2vw, 20px); font-style: italic; font-weight: 700; color: #0f766e">Cuidar de alguém é o ato mais puro de humanidade. Lembre-se de ser gentil consigo mesmo também.</p>
      </section>

      """ % (titulo('Para a família e para quem cuida 💛', 'Quem cuida também carrega um peso invisível. Às vezes, na tentativa de ajudar, as palavras tropeçam. Cinco falas comuns, e o que dizer no lugar.'),
             fala(1, '“Eu sei como você se sente.”', 'Ninguém sente a dor na pele do outro. O monstrinho dele tem um peso que só ele conhece.', 'Diga: “Não imagino seu cansaço, mas estou aqui.”'),
             fala(2, 'O “fiscal médico”', 'Não decida o que a pessoa pode comer ou fazer. Ela já sente que perdeu o controle sobre o próprio corpo; não tire o controle das escolhas dela.', 'Pergunte: “Onde você precisa da minha força hoje?”'),
             fala(3, 'A “exclusão protetora”', 'Não pare de convidar para passeios achando que é melhor a pessoa descansar. Ser esquecido dói mais do que a própria fadiga.', 'Diga: “Adoraríamos que você fosse. Se não der hoje, sem pressão.”'),
             fala(4, 'A “positividade tóxica”', 'Não exija que a pessoa pense positivo o tempo todo. O medo e a raiva também são hóspedes que precisam ser ouvidos.', 'Diga: “É normal se sentir frustrado hoje. Estou aqui com você mesmo nos dias difíceis.”'),
             fala(5, 'O “comparador de batalhas”', 'Não compare com quem “teve o mesmo e melhorou rápido”. O caminho é único para cada um.', 'Diga: “Cada passo que você dá no seu ritmo é uma grande vitória.”'))
    return [quem, desafios, superpoder, mochila, familia]


# ================================================================== PARA PACIENTES DA CLÍNICA
def _passo(n, nome, texto):
    return ('''<div style="background: #ffffff; border-radius: 14px; padding: 16px 18px; display: flex; gap: 14px; align-items: flex-start; border: 1px solid #e2e8f0">
            <span style="flex: none; width: 40px; height: 40px; border-radius: 999px; background: #f7d774; color: #0f2744; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 800">%d</span>
            <span style="display: flex; flex-direction: column; gap: 4px"><strong style="color: #0f2744; font-size: 17px">%s</strong><span style="font-size: 15px; color: #475569">%s</span></span>
          </div>''') % (n, nome, texto)


def pacientes_blocos():
    metodo = '''<section style="background: #fffbeb; border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; gap: 18px">
        %s
        <div style="%s">
          %s
          %s
          %s
        </div>
        <p style="margin: 0; text-align: center; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(18px, 2.2vw, 22px); font-style: italic; font-weight: 700; color: #b45309">Domar não é controlar. É acolher.</p>
      </section>

      ''' % (titulo('O nosso método em 1 minuto ⏱️'),
             GRADE3,
             cartao('👾', 'Monstrinho é um sentimento', 'É um jeito de olhar para o medo, a ansiedade ou a culpa de fora, sem rótulo. Você não é ansioso: existe um monstrinho da ansiedade agindo em você.'),
             cartao('🛡️', 'Ele quer te proteger', 'Todo monstrinho tem uma história. Entender do que ele tenta te proteger é o começo da conversa.'),
             cartao('🏅', 'Níveis são pequenas vitórias', 'Muita coisa muda e a sensação é de que “está tudo igual”. Os 12 níveis da Travessia deixam o seu caminho visível.'))

    esperar = '''<section style="display: flex; flex-direction: column; gap: 18px">
        %s
        <div style="%s">
          %s
          %s
          %s
          %s
        </div>
        <p style="%s">ℹ️ <strong>Importante:</strong> a Travessia e os conteúdos online da Clínica Doma são um material de autoconhecimento. Eles não são terapia e não substituem as sessões com um psicólogo, psicanalista ou médico.</p>
      </section>

      ''' % (titulo('O que esperar 🛋️'),
             GRADE,
             cartao('🏡', 'Um espaço sem julgamentos', 'O atendimento é presencial, no Centro de Osasco/SP. Você não precisa chegar com tudo organizado: a gente começa de onde você está.', '#0b7cb8'),
             cartao('🧰', 'Várias ferramentas', 'Psicanálise, hipnose clínica, arteterapia, jogos dos monstrinhos e escrita. A terapeuta escolhe com você o que faz sentido em cada momento.', '#0b7cb8'),
             cartao('🗺️', 'A Travessia entre as sessões', 'Em casa, no seu ritmo, você faz os níveis do livro online. O que aparecer ali pode virar assunto na sessão.', '#0b7cb8'),
             cartao('👑', 'No Plano Premium', 'As sessões acontecem a cada 15 dias e podem retomar o nível do mês com a terapeuta.', '#0b7cb8'),
             AVISO)

    comecar = '''<section style="background: #f0f9ff; border-radius: 18px; padding: clamp(24px, 4vw, 36px) clamp(18px, 4vw, 36px); display: flex; flex-direction: column; gap: 16px">
        %s
        <div style="display: flex; flex-direction: column; gap: 10px">
          %s
          %s
          %s
          %s
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px">
          <a href="/carteira-doma" style="%s">🪪 EMITIR MINHA CARTEIRA GRÁTIS</a>
          <a href="/nivel-1" style="%s">🚀 JÁ TENHO: IR PARA O NÍVEL 1</a>
        </div>
      </section>

      ''' % (titulo('Como começar o Nível 1 🚀', 'O Nível 1, O Meu Ano Inicia Agora, é grátis. Dá para fazer antes da primeira sessão.'),
             _passo(1, 'Crie a sua conta', 'No botão Login, no alto do site. É a conta que guarda o seu progresso.'),
             _passo(2, 'Emita a sua Carteira Doma', 'É gratuita, leva 2 minutinhos e sai na hora.'),
             _passo(3, 'Faça o Nível 1', 'Termo de compromisso, Raio-X de Energia Vital, Mochila de Descarte, Ritual Final e Roleta de Boas-Vindas.'),
             _passo(4, 'Leve para a sessão', 'Anote o que mais mexeu com você. É um ótimo ponto de partida para a conversa.'),
             BOTAO_AZUL, BOTAO_CLARO)
    return [metodo, esperar, comecar]
