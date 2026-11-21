# -*- coding: utf-8 -*-
"""Passo 5 do plano de melhorias: Perguntas frequentes, Política de privacidade e Termos de uso.

De onde vêm os textos:
- Perguntas frequentes: as 5 perguntas do FAQ do site atual (plataforma, planos, afiliados, recebimento,
  qual plano escolher), reescritas com os nomes de hoje, mais as respostas da Daniela no plano (13/11)
  e os cuidados do plano (não é terapia, teste não é diagnóstico, nunca desencorajar remédio).
- Política de privacidade e Termos de uso: o site atual só tem o modelo vazio do Wix. Estes textos são
  um RASCUNHO escrito a partir do que o site realmente guarda (conta, carteira, progresso e respostas da
  Travessia, pedidos, indicações e saques) e precisam da revisão da Daniela e de um advogado.
Filtro: material de autoconhecimento; nada de "diagnóstico", "cura" ou "tratar" para a plataforma.
"""
from paginas_novas import H2, AVISO, BOTAO_AZUL, BOTAO_CLARO, titulo

EMAIL = 'atendimento.clinicadoma@gmail.com'
ZAP = 'https://wa.me/5511963272059'
ZAP_TXT = '(11) 96327-2059'
ATUALIZADO = '20 de novembro de 2026'

LINK = 'color: #0b7cb8; font-weight: 700'
FALTA = 'background: #fef3c7; border-radius: 6px; padding: 1px 6px; color: #92400e; font-weight: 700'


def a(href, texto):
    return '<a href="%s" style="%s">%s</a>' % (href, LINK, texto)


MAIL = a('mailto:' + EMAIL, EMAIL)
WHATS = a(ZAP, 'WhatsApp ' + ZAP_TXT)

RASCUNHO = ('<p style="margin: 0; padding: 14px 16px; border-radius: 14px; background: #fffbeb; border: 1px dashed #d97706; '
            'font-size: 14px; line-height: 1.55; color: #92400e">📝 <strong>Texto em revisão.</strong> Esta página é um rascunho do site novo. '
            'Ela ainda vai passar pela revisão da Clínica Doma e de um advogado antes do lançamento.</p>\n\n      ')


# ================================================================== PERGUNTAS FREQUENTES
def _pergunta(p, r, cor):
    return ('''<div style="background: #ffffff; border-radius: 14px; padding: 16px 18px; display: flex; flex-direction: column; gap: 6px; border-left: 5px solid %s; box-shadow: 0 4px 12px rgba(15, 39, 68, 0.05)">
            <strong style="color: #0f2744; font-size: 17px; line-height: 1.3">%s</strong>
            <div style="font-size: 15px; line-height: 1.6; color: #475569; display: flex; flex-direction: column; gap: 8px">%s</div>
          </div>''') % (cor, p, r)


def _p(*partes):
    return ''.join('<p style="margin: 0">%s</p>' % x for x in partes)


def _lista(itens):
    return '<ul style="margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 4px">%s</ul>' % ''.join('<li>%s</li>' % i for i in itens)


def _grupo(ident, emoji, nome, fundo, cor, perguntas):
    return ('''<section id="%s" style="background: %s; border-radius: 18px; padding: clamp(20px, 3.4vw, 30px) clamp(16px, 3.4vw, 30px); display: flex; flex-direction: column; gap: 12px">
        <h2 style="margin: 0 0 4px; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(22px, 2.8vw, 28px); line-height: 1.2; font-weight: 800; color: #0f2744">%s %s</h2>
        %s
      </section>

      ''') % (ident, fundo, emoji, nome, '\n        '.join(_pergunta(p, r, cor) for p, r in perguntas))


def faq_blocos():
    temas = [('faq-sobre', '🏡', 'Sobre a Doma'), ('faq-travessia', '🗺️', 'A Travessia'), ('faq-carteira', '🪪', 'Carteira e conta'),
             ('faq-planos', '📚', 'Planos'), ('faq-indique', '🤝', 'Indique Doma'), ('faq-clinica', '🛋️', 'Atendimento'),
             ('faq-dados', '🔒', 'Dados e ajuda')]
    chip = ('display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border-radius: 999px; background: #ffffff; '
            'border: 2px solid #cbd5e1; color: #0f2744; font-size: 15px; font-weight: 700; text-decoration: none')
    indice = ('''<section style="display: flex; flex-direction: column; gap: 12px; align-items: center">
        <p style="margin: 0; font-size: 15px; color: #475569">Escolha um assunto:</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px">
          %s
        </div>
      </section>

      ''') % '\n          '.join('<a href="#%s" style="%s">%s %s</a>' % (i, chip, e, n) for i, e, n in temas)

    sobre = _grupo('faq-sobre', '🏡', 'Sobre a Clínica Doma', '#fffbeb', '#f7d774', [
        ('O que é a Clínica Doma?',
         _p('A Clínica Doma tem duas frentes. Uma é a clínica de terapia presencial, no Centro de Osasco/SP. A outra é a plataforma online de autoconhecimento, em formato de jogo: a Travessia do Domador, com o livro interativo A Clínica dos Monstros, a Carteira Doma e os Jogos dos Monstrinhos.')),
        ('A Travessia é terapia?',
         _p('Não. A Travessia e os conteúdos online da Clínica Doma são um material de autoconhecimento. Eles não são terapia e não substituem as sessões com um psicólogo, psicanalista ou médico.',
            'A terapia acontece nas sessões presenciais da clínica.')),
        ('O que é um monstrinho? E um Domador?',
         _p('Monstrinho é uma metáfora para um sentimento difícil, como o medo, a ansiedade ou a culpa. Ela ajuda a olhar para o sentimento de fora, sem rótulo: você não é ansioso, existe um monstrinho da ansiedade agindo em você.',
            'Domador é quem aprende a entender e acolher os seus monstrinhos. Domar não é controlar. É acolher. ' + a('/conheca-os-monstrinhos', 'Conheça os monstrinhos'))),
    ])

    travessia = _grupo('faq-travessia', '🗺️', 'A Travessia', '#f0f9ff', '#0b7cb8', [
        ('Como funciona a Travessia?',
         _p('São 12 níveis, divididos em 3 capítulos: O Acolhimento, A Caverna dos Monstros e A Ressignificação.',
            'O Nível 1, O Meu Ano Inicia Agora, é gratuito para quem tem a Carteira Doma. A partir do Nível 2, cada mês de plano libera um nível novo. ' + a('/a-travessia', 'Ver o mapa da Travessia'))),
        ('Quanto tempo leva? E depois do Nível 12?',
         _p('A Travessia foi pensada para 12 meses, um nível por mês, no seu ritmo.',
            'Ao terminar o Nível 12, você pode recomeçar a Travessia como manutenção: novos monstrinhos aparecem ao longo da vida, e o método pode ser revisitado sempre.')),
        ('Posso fazer pelo celular?',
         _p('Sim. A Travessia funciona no celular, no tablet e no computador. O seu progresso fica salvo na sua conta: você pode parar e continuar depois, em qualquer aparelho.')),
        ('Para qual idade é a Travessia?',
         _p('A Travessia foi pensada para adultos. Menores de 18 anos podem participar com a autorização e o acompanhamento de um responsável.')),
        ('Os testes de sintomas dão um diagnóstico?',
         _p('Não. Os testes e quizzes são convites para você se observar. Eles não substituem uma avaliação médica ou psicológica. Se um sintoma persiste ou preocupa, procure um médico.')),
        ('Tomo remédio. Posso fazer a Travessia?',
         _p('Pode. A Travessia não substitui remédio nem acompanhamento médico. Nunca pare ou mude um remédio por conta própria: essa decisão é sua com o seu médico.')),
    ])

    carteira = _grupo('faq-carteira', '🪪', 'Carteira Doma e conta', '#f8fafc', '#b8860b', [
        ('O que é a Carteira Doma? Quanto custa?',
         _p('É a sua carteira de Domador, e é gratuita. Você preenche nome, WhatsApp e e-mail, coloca uma foto e ela sai na hora, em cerca de 2 minutos.',
            'Com ela você faz o Nível 1 completo da Travessia, ganha as suas primeiras Doma Coins e recebe o seu link de indicação. ' + a('/carteira-doma', 'Emitir minha carteira grátis'))),
        ('Preciso criar uma conta no site?',
         _p('Sim. Para emitir a carteira e fazer o Nível 1 você precisa da conta no site (botão Login, no alto da página) e da Carteira Doma. É a conta que guarda o seu progresso.')),
    ])

    planos = _grupo('faq-planos', '📚', 'Planos e pagamento', '#fffbeb', '#f7d774', [
        ('Quais são os planos?',
         _lista(['<strong style="color: #0f2744">Carteira Doma (grátis):</strong> Nível 1 da Travessia e link de indicação.',
                 '<strong style="color: #0f2744">Doma Básico (R$ 149,99 por mês):</strong> livro completo online com exercícios, comunidade exclusiva, 40% de desconto nas terapias presenciais e sorteios mensais.',
                 '<strong style="color: #0f2744">Doma Premium (R$ 629,99 por mês):</strong> tudo do Básico, mais 2 sessões presenciais por mês (a cada 15 dias), Carteira Doma Premium, arteterapia e jogos terapêuticos, aulas de bambolê terapia, descontos nos Sábados de Conexão e o Kit Domador de boas-vindas.'])
         + _p(a('/planos', 'Ver os planos'))),
        ('Qual plano escolher?',
         _p('Para conhecer a Doma sem pagar nada, comece pela Carteira gratuita. Para fazer a Travessia completa no seu ritmo, escolha o Básico. Para fazer a Travessia com sessões presenciais a cada 15 dias, escolha o Premium.')),
        ('Como cancelo? E se eu me arrepender da compra?',
         _p('Você pode pedir o cancelamento do plano quando quiser, pelo WhatsApp ou pelo e-mail da clínica.',
            'Pela lei, toda compra feita pela internet pode ser desfeita em até 7 dias, com a devolução do valor pago. Os detalhes estão nos ' + a('/termos-de-uso', 'Termos de uso') + '.')),
    ])

    indique = _grupo('faq-indique', '🤝', 'Indique Doma', '#f0fdfa', '#0f766e', [
        ('Como funciona o Indique Doma?',
         _p('Quem tem a Carteira Doma recebe um link de indicação. Cada pessoa que entra para a Doma pelo seu link gera uma comissão para você:')
         + _lista(['<strong style="color: #0f2744">37%</strong> sobre os planos de assinatura, na primeira compra e em cada renovação, enquanto o plano da pessoa indicada estiver ativo;',
                   '<strong style="color: #0f2744">10%</strong> sobre os produtos físicos da Loja Doma.'])
         + _p(a('/indique', 'Conhecer o Indique Doma'))),
        ('Como recebo as minhas comissões?',
         _p('Com a Carteira gratuita, as comissões viram créditos Doma. Os créditos não viram dinheiro: servem para usar em produtos e serviços da plataforma, inclusive nas suas sessões, ou para abater parte de um plano pago.',
            'Com um plano pago ativo (Básico ou Premium), você passa a receber as comissões em dinheiro.')),
    ])

    clinica = _grupo('faq-clinica', '🛋️', 'Atendimento presencial', '#f8fafc', '#0b7cb8', [
        ('Como agendo uma sessão? Onde fica a clínica?',
         _p('O atendimento é presencial, no Centro de Osasco/SP. Para agendar, chame a clínica no ' + WHATS + '.')),
        ('Que tipo de atendimento a clínica oferece?',
         _p('Psicanálise, hipnose clínica, PNL, arteterapia, jogos terapêuticos com os monstrinhos e bambolê terapia. A terapeuta escolhe com você o que faz sentido em cada momento.')),
    ])

    dados = _grupo('faq-dados', '🔒', 'Seus dados e ajuda', '#eff6ff', '#1e3a8a', [
        ('O que a Clínica Doma faz com os meus dados?',
         _p('Usamos os seus dados para criar a sua conta e a sua carteira, salvar o seu progresso na Travessia, cuidar dos planos e do programa de indicação e falar com você. Não vendemos os seus dados.',
            'Você pode pedir para ver, corrigir ou apagar os seus dados quando quiser. Está tudo explicado na ' + a('/politica-de-privacidade', 'Política de privacidade') + '.')),
        ('As minhas respostas dos exercícios ficam guardadas?',
         _p('Ficam guardadas na sua conta, para você continuar de onde parou. Como elas podem falar da sua saúde e da sua vida emocional, recebem um cuidado maior: não são usadas para propaganda nem vendidas a ninguém, e você pode pedir para apagar tudo.')),
        ('Estou em crise. O que eu faço?',
         _p('A plataforma não é um serviço de emergência. Se você está em crise ou pensando em se machucar, ligue <strong style="color: #1e3a8a">188</strong> (CVV): 24 horas e gratuito. Em emergência, ligue <strong style="color: #1e3a8a">192</strong> (SAMU).')),
    ])

    fim = ('''<section style="display: flex; flex-direction: column; gap: 14px; align-items: center; text-align: center">
        %s
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px">
          <a href="%s" style="%s">💬 CHAMAR NO WHATSAPP</a>
          <a href="mailto:%s" style="%s">✉️ MANDAR UM E-MAIL</a>
        </div>
      </section>

      ''') % (titulo('Não achou a sua dúvida? 💬', 'Fale com a clínica. A gente responde com carinho.'), ZAP, BOTAO_AZUL, EMAIL, BOTAO_CLARO)
    return [indice, sobre, travessia, carteira, planos, indique, clinica, dados, fim]


# ================================================================== PÁGINAS DE TEXTO (PRIVACIDADE E TERMOS)
def _secao(n, nome, corpo):
    return ('''<section style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: clamp(18px, 3vw, 26px); display: flex; flex-direction: column; gap: 10px">
        <h2 style="margin: 0; display: flex; align-items: center; gap: 12px; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(20px, 2.6vw, 25px); line-height: 1.2; font-weight: 800; color: #0f2744"><span style="flex: none; width: 36px; height: 36px; border-radius: 999px; background: #f7d774; color: #0f2744; display: flex; align-items: center; justify-content: center; font-family: Inter, Arial, sans-serif; font-size: 16px; font-weight: 800">%d</span><span>%s</span></h2>
        <div style="font-size: 15.5px; line-height: 1.65; color: #334155; display: flex; flex-direction: column; gap: 10px">%s</div>
      </section>

      ''') % (n, nome, corpo)


def _texto(secoes, comeco=''):
    # as seções ficam mais juntas do que os blocos das outras páginas
    return ['<div style="display: flex; flex-direction: column; gap: 14px">\n      ' + comeco
            + ''.join(_secao(i + 1, nome, corpo) for i, (nome, corpo) in enumerate(secoes)) + '</div>\n\n      ']


def _forte(t):
    return '<strong style="color: #0f2744">%s</strong>' % t


def privacidade_blocos():
    secoes = [
        ('Quem cuida dos seus dados',
         _p('A responsável pelos seus dados é a Clínica Doma (<span style="%s">razão social e CNPJ: a preencher</span>), com endereço em <span style="%s">endereço: a preencher</span>, Centro, Osasco/SP.' % (FALTA, FALTA),
            'Esta política vale para o site e para a plataforma online da Clínica Doma. Para qualquer assunto sobre os seus dados, fale com a gente pelo e-mail ' + MAIL + ' ou pelo ' + WHATS + '. Este é o nosso canal de atendimento sobre privacidade.')),
        ('Quais dados coletamos',
         _lista([_forte('Conta no site:') + ' e-mail, nome e senha. A senha fica guardada de forma cifrada pela Wix, a empresa que hospeda o site: a gente não consegue ver. Se você entra com Google ou Facebook, recebemos os dados básicos do seu perfil, como nome e e-mail.',
                 _forte('Carteira Doma:') + ' nome completo, foto, WhatsApp, e-mail, data de emissão, número de registro, plano e o aceite do Juramento do Domador.',
                 _forte('Travessia:') + ' o nível em que você está, o seu progresso e as respostas que você escreve nos exercícios e testes.',
                 _forte('Planos e Loja Doma:') + ' os dados do pedido, o endereço de entrega e o histórico de compras. O pagamento é feito por uma empresa de pagamentos: a gente não guarda o número do seu cartão.',
                 _forte('Indique Doma:') + ' quem indicou quem, as comissões, os pedidos de saque e a chave Pix que você informar.',
                 _forte('Contato:') + ' as mensagens que você manda por WhatsApp, e-mail ou chat do site.',
                 _forte('Navegação:') + ' dados técnicos, como endereço IP, tipo de aparelho, páginas visitadas e cookies.'])),
        ('Para que usamos',
         _lista(['Criar e manter a sua conta e a sua Carteira Doma.',
                 'Liberar os níveis e salvar o seu progresso, para você continuar de onde parou.',
                 'Cuidar dos planos, dos pedidos da loja e das entregas.',
                 'Calcular e pagar as comissões do Indique Doma.',
                 'Responder às suas mensagens e avisar sobre a sua conta.',
                 'Se você é paciente da clínica, permitir que a sua terapeuta veja em que nível você está, para a sessão poder retomar o nível do mês.',
                 'Manter o site seguro e cumprir o que a lei exige.'])
         + _p(_forte('Não vendemos os seus dados') + ' e não usamos as suas respostas dos exercícios para propaganda.')),
        ('Dados sensíveis: as suas respostas',
         _p('O que você escreve nos exercícios e testes da Travessia pode falar da sua saúde e da sua vida emocional. A lei chama isso de dado sensível e pede um cuidado maior. Por isso:')
         + _lista(['pedimos o seu consentimento antes de guardar essas respostas;',
                   'elas servem para você continuar a sua Travessia de onde parou;',
                   'o acesso é restrito a você e à equipe autorizada da Clínica Doma;',
                   'você pode retirar o consentimento e pedir para apagar tudo a qualquer momento.'])),
        ('Com quem compartilhamos',
         _p('Para o site funcionar, alguns dados passam por empresas que prestam serviço para a Clínica Doma:')
         + _lista([_forte('Wix:') + ' hospeda o site, as contas, a loja e os dados da plataforma.',
                   _forte('Empresas de pagamento:') + ' processam os pagamentos dos planos e da loja.',
                   _forte('Google e Facebook:') + ' só se você escolher entrar com uma dessas contas. As letras do site também vêm de um serviço do Google.',
                   _forte('GitHub:') + ' guarda imagens e arquivos do livro. Recebe só dados técnicos de acesso, como o endereço IP.',
                   _forte('WhatsApp e Instagram:') + ' quando você fala com a gente por esses canais.',
                   _forte('Correios e transportadoras:') + ' para entregar os pedidos da loja.',
                   _forte('Autoridades:') + ' quando a lei ou uma ordem da Justiça exigir.'])
         + _p('Algumas dessas empresas guardam dados em computadores fora do Brasil.')),
        ('Por quanto tempo guardamos',
         _p('Guardamos os seus dados enquanto a sua conta existir. Se você pedir a exclusão, apagamos o que não somos obrigados a manter.',
            'Alguns registros precisam ficar guardados por mais tempo porque a lei exige, como notas fiscais e registros de acesso ao site.')),
        ('Os seus direitos',
         _p('Pela Lei Geral de Proteção de Dados (LGPD), você pode, a qualquer momento:')
         + _lista(['saber se usamos os seus dados e ver quais são;',
                   'corrigir dados incompletos, errados ou desatualizados;',
                   'pedir a exclusão dos dados desnecessários e dos que guardamos com o seu consentimento;',
                   'levar os seus dados para outro serviço (portabilidade);',
                   'saber com quem compartilhamos os seus dados;',
                   'saber o que acontece se você não der o consentimento, e retirar o consentimento que já deu.'])
         + _p('Para pedir, escreva para ' + MAIL + '. A gente responde dentro do prazo da lei. Se achar que não foi atendido, você também pode procurar a Autoridade Nacional de Proteção de Dados (ANPD).')),
        ('Crianças e adolescentes',
         _p('A plataforma foi pensada para adultos. Menores de 18 anos só devem usar com a autorização e o acompanhamento de um responsável.',
            'Para crianças com menos de 12 anos, a lei exige o consentimento de pelo menos um dos pais ou do responsável legal.')),
        ('Cookies',
         _p('Cookies são pequenos arquivos que o site guarda no seu aparelho. Usamos os essenciais, para manter o seu login e o seu carrinho, e os de medição, para entender como o site é usado.',
            'Você pode bloquear ou apagar os cookies nas configurações do seu navegador. Nesse caso, algumas partes do site podem deixar de funcionar.')),
        ('Segurança',
         _p('O site usa conexão segura (https), o acesso aos dados é restrito e as senhas ficam cifradas. Mesmo assim, nenhum sistema é totalmente à prova de falhas.',
            'Se acontecer um incidente que possa trazer risco para você, vamos avisar você e a ANPD.')),
        ('Mudanças nesta política',
         _p('Esta política pode ser atualizada. A data da última atualização fica no alto da página, e as mudanças importantes serão avisadas no site ou por e-mail.',
            'Veja também os ' + a('/termos-de-uso', 'Termos de uso') + ' e as ' + a('/perguntas-frequentes', 'Perguntas frequentes') + '.')),
    ]
    return _texto(secoes, RASCUNHO)


def termos_blocos():
    aviso = ('<p style="%s">ℹ️ <strong>Importante:</strong> a Travessia e os conteúdos online da Clínica Doma são um material de autoconhecimento. '
             'Eles não são terapia e não substituem as sessões com um psicólogo, psicanalista ou médico.</p>') % AVISO
    secoes = [
        ('O que é a plataforma',
         _p('A plataforma online da Clínica Doma reúne a Carteira Doma, a Travessia do Domador (com o livro interativo A Clínica dos Monstros), os Jogos dos Monstrinhos, a Loja Doma e o programa Indique Doma. Ao usar a plataforma, você concorda com estes termos.')
         + aviso
         + _p('A plataforma também não é um serviço de emergência. Se você está em crise, ligue ' + _forte('188') + ' (CVV) ou ' + _forte('192') + ' (SAMU).')),
        ('Quem pode usar',
         _p('A plataforma é para maiores de 18 anos. Menores de 18 anos só podem usar com a autorização e o acompanhamento de um responsável, que responde pelo uso.')),
        ('Conta e Carteira Doma',
         _p('Para usar a plataforma você cria uma conta no site e emite a sua Carteira Doma, que é gratuita.',
            'Informe dados verdadeiros e mantenha tudo atualizado. A conta e a carteira são pessoais: não empreste a sua conta e não compartilhe a sua senha.')),
        ('Planos, pagamento e renovação',
         _p('O Nível 1 da Travessia é gratuito para quem tem a Carteira Doma. Os planos Doma Básico e Doma Premium são mensais e se renovam a cada mês, até você cancelar. Cada mês de plano libera um nível novo da Travessia.',
            'Os preços e o que cada plano inclui estão na página ' + a('/planos', 'Planos') + '. Se um preço mudar, a gente avisa antes da renovação seguinte.')),
        ('Cancelamento e arrependimento',
         _p('Você pode cancelar o seu plano quando quiser, pelo WhatsApp ou pelo e-mail da clínica. O cancelamento vale a partir do ciclo seguinte: você continua com acesso até o fim do período que já pagou.',
            'Pela lei (artigo 49 do Código de Defesa do Consumidor), você pode desistir de uma compra feita pela internet em até 7 dias e receber de volta o valor pago.')),
        ('Sessões presenciais',
         _p('As sessões do plano Premium e as terapias com desconto do plano Básico acontecem na clínica, no Centro de Osasco/SP, com hora marcada. O agendamento e as remarcações são combinados direto com a clínica, pelo WhatsApp.')),
        ('Indique Doma',
         _p('Quem tem a Carteira Doma recebe um link de indicação e ganha comissão quando alguém entra para a Doma por esse link.',
            'Com a Carteira gratuita, as comissões viram créditos Doma: eles não viram dinheiro e servem para usar em produtos e serviços da plataforma. Com um plano pago ativo, as comissões podem ser recebidas em dinheiro, por saque.',
            'Indicações falsas, indicar a si mesmo ou qualquer tentativa de fraude cancelam as comissões e podem encerrar a participação no programa.')),
        ('Loja Doma',
         _p('Na Loja Doma, o prazo e o valor da entrega aparecem antes de você fechar o pedido. Você pode desistir da compra em até 7 dias depois de receber o produto. Produtos com defeito têm a garantia prevista em lei.')),
        ('Conteúdo e direitos autorais',
         _p('O livro A Clínica dos Monstros, os textos, os jogos, as imagens e os personagens da Clínica Doma são protegidos por direitos autorais. O acesso é para o seu uso pessoal.',
            'Não é permitido copiar, gravar, distribuir ou vender o conteúdo sem autorização por escrito.')),
        ('Convivência',
         _p('Na comunidade e nos canais da Doma, trate todo mundo com respeito. Não são permitidas ofensas, discriminação, propaganda ou a divulgação de dados de outras pessoas.',
            'O que os participantes escrevem na comunidade não é orientação profissional.')),
        ('Responsabilidade',
         _p('A Clínica Doma se esforça para manter a plataforma no ar e o conteúdo correto, mas o site pode ficar indisponível por manutenção ou por problemas técnicos.',
            'O conteúdo é de autoconhecimento. Decisões sobre a sua saúde, inclusive sobre remédios, devem ser tomadas com um profissional.')),
        ('Encerramento da conta',
         _p('Você pode encerrar a sua conta quando quiser, pelos nossos canais. A Clínica Doma pode suspender ou encerrar contas que descumpram estes termos.')),
        ('Mudanças, lei e foro',
         _p('Estes termos podem ser atualizados, e a data fica no alto da página. Vale a lei brasileira, e fica garantido a você o foro da sua cidade para resolver qualquer questão.')),
        ('Contato',
         _p('Dúvidas sobre estes termos? Fale com a gente pelo e-mail ' + MAIL + ' ou pelo ' + WHATS + '.',
            'Veja também a ' + a('/politica-de-privacidade', 'Política de privacidade') + ' e as ' + a('/perguntas-frequentes', 'Perguntas frequentes') + '.')),
    ]
    return _texto(secoes, RASCUNHO)
