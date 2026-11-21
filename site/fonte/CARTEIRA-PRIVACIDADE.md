# Minha Carteira: caixa "Privacidade das suas respostas" (21/11/2026)

Na página Minha Carteira (endereço `/carteira-d`), embaixo da carteirinha, a pessoa
vê se concordou com a guarda das respostas da Travessia e pode **retirar o consentimento**.

## Onde está cada parte

| Parte | Arquivo aqui | Onde entra no Wix |
| --- | --- | --- |
| Caixa (HTML, estilo e script) | `carteira-privacidade.html` | No fim do código do bloco HTML `#html1` da página Minha Carteira |
| Código da página | `wix/pagina-minha-carteira-privacidade.js` | No fim do código da página (arquivo `y1vvf.js`), mais uma linha de `import` no começo |

## Como funciona

- O "concordo" fica junto do progresso do Nível 1: `progresso.consentimento = { aceito, quando, versao }`.
- Retirar grava `{ aceito: false, retiradoEm, aceitoEm, versao }` no mesmo lugar, sem mexer no resto do progresso.
- Depois disso o Nível 1 e o livro voltam a pedir o "concordo" e nada novo é guardado sem ele.
- O que já estava guardado **continua na conta**. Para apagar, a pessoa pede por e-mail (está na Política de privacidade).
- A caixa só aparece na tela da carteirinha pronta (pessoa logada e com carteirinha).

## Mensagens entre a caixa e a página

- Caixa → página: `{ tipo: 'doma-consentimento-ler' }` e `{ tipo: 'doma-consentimento-retirar' }`
- Página → caixa: `{ tipo: 'doma-consentimento-estado', estado: 'aceito' | 'retirado' | 'nenhum' | 'erro' | 'sem-login', quando, urlPrivacidade }`

## Alturas do bloco HTML

Com a caixa, o bloco ficou: computador 980 × 1000 (igual), tablet 753 × 940 (era 900), celular 375 × 860 (era 680).

## Teste

O teste com um Wix de mentira (nove situações) está descrito no fim deste arquivo; todas passaram em 21/11/2026.
Falta o teste com uma conta de verdade no site publicado.

Situações testadas: concordou e retira; cancela; progresso sem "concordo"; sem progresso; falha ao ler;
falha ao guardar; já tinha retirado; tela da carteirinha escondida; sem login.
