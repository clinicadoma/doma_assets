# Nível 1 · O Meu Ano Inicia Agora (página /nivel-1 do site novo)

O HTML do jogo do Nível 1 não está neste depósito: ele veio da página do site atual e
está só dentro do Wix (elemento `#html1` da página "Nível 1 · O Meu Ano Inicia Agora").

Em 20/11/2026 ele ganhou o pedido de consentimento (LGPD):

- `nivel1-consentimento.html` é colado, sem mudança, logo antes do único `</body>` do HTML do jogo
  (o jogo tinha 120434 caracteres; com o trecho ficou com 127020).
- `wix/pagina-nivel-1.js` é o código da página (arquivo `eetov.js` no Wix).

Como funciona: quando a página avisa que a pessoa está logada e tem carteira (`status: 'ok'`)
e ainda não existe `progresso.consentimento.aceito`, o HTML mostra a tela "Antes de começar".
Sem o "concordo" o código da página não chama `salvarMeuProgresso`; ele segura o último
progresso na memória e pede a tela de novo. Com o "concordo", o registro
`{ aceito, quando, versao }` vai junto em todo progresso salvo. "Agora não" leva para /a-travessia.

## Livro (Nível 2 em diante, página /livro-a-travessia) - 20/11/2026

O livro confere o mesmo registro. Os dois arquivos colados no Wix ficam só no depósito privado
livro_a_travessia_v2, pasta `wix/`: `wix-loader.html` (elemento `#html38`) e `pagina-livro.js`
(código da página, arquivo `aegbn.js` no Wix).

Sem o "concordo", a página do livro não chama `salvarChavesLivro`: segura as respostas na memória e
mostra a tela "Antes de continuar". Quem concorda no livro tem o registro gravado no progresso do
Nível 1, por `salvarMeuProgresso`. Quem não tem progresso do Nível 1 é levado para /nivel-1.

## 21/11/2026 - Imagem do "Doma diz"

A figura redonda ao lado do áudio "Doma diz" (e o fundo de um aviso) apontava para um endereço de imagem
que não existe mais (aparecia "image not found"). As quatro ocorrências passaram a usar o mascote da
Clínica Doma, o mesmo do cabeçalho das páginas novas
(`https://static.wixstatic.com/media/253e81_0452afd60bae4cfda9e23427567f0f36~mv2.webp`).

## 21/11/2026 - Imagem que vinha do depósito antigo do livro

O Nível 1 carregava uma imagem (`Captura-de-tela-2025-09-27-133248.png`) direto do depósito antigo e público
`clinicadoma/livro_a_travessia`. Se esse depósito for apagado ou ficar privado, a imagem some. Ela passou a vir
da mídia do site novo: `https://static.wixstatic.com/media/253e81_a793750068d44bc8b22777a30adbde05~mv2.png`
(mesmo arquivo, conferido ponto a ponto).

O que o Nível 1 ainda busca fora do Wix: as fontes (Google Fonts), a biblioteca que gera a foto da carteirinha
(cdnjs) e os sons (assets.mixkit.co).

