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

Falta: o livro (Nível 2 em diante, página /livro-a-travessia) ainda não confere esse consentimento.
