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
