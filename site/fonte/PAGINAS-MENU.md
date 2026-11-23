# Presente Doma, Ferramentas da Clínica e Arsenal Clínico

Trazidas do site atual em 21/11/2026, com o mesmo conteúdo e o mesmo endereço.

| Página | Endereço | Arquivo de origem no site atual | Tamanho no computador |
|---|---|---|---|
| Presente Doma | `/about-5` | `253e81_bbc341ad35d3eac0a579fd3edac1bc1a.html` | 1051 x 605, proporcional |
| Ferramentas da Clínica | `/ferramentas-da-clinica` | `253e81_fd4e1a39968ba3f18c8f93ee7b1a0ed1.html` | 966 x 663, fixo |
| Arsenal Clínico | `/arsenal-de-produtos` | `253e81_b4a6eae99df128de5c78bfecb112f6f1.html` | 1047 x 772, proporcional |

No tablet e no celular as três ficaram com 753 x 800 e 375 x 780.

## O que mudou em relação ao original

### Presente Doma

- 21/11: os dois botões de plano apontavam para `clinicadoma.com/pricing-plans/list`; agora avisam a página, que leva para `/pricing-plans/plans-pricing`. O botão do plano gratuito apontava para `clinicadoma.com/incio`; agora leva para `/livro-a-travessia`.
- 23/11: texto dos planos igual ao da página Planos (Básico: livro, Travessia, Carteira, comunidade, 40% nas terapias, sorteios e 37% de comissão; Premium: tudo do Básico, 2 sessões por mês, arteterapia, bambolê, 40% nos Sábados de Conexão e kit). A parte da Carteira e o plano gratuito (Nível 1 grátis) foram reescritos, com o aviso de que a plataforma é material de autoconhecimento e não é terapia. O bloco "Benefícios exclusivos" não foi mexido.
- 23/11: as 3 imagens saíram do postimg e passaram para a mídia do Wix.

O código da página está em `wix/pagina-presente-doma.js`.

### Arsenal Clínico

- 23/11: as 12 imagens saíram do postimg e passaram para a mídia do Wix.
- 23/11: os botões "Adquirir" dos 12 cartões agora levam ao produto certo da Loja Doma, e "O Arsenal Doma" leva à loja inteira. O código está em `wix/pagina-arsenal-clinico.js`.

## Imagens trazidas para o Wix (23/11)

O nome de cada arquivo na mídia do Wix começa com `doma-` e o código do postimg, para achar a origem.

| Código no postimg | Arquivo no Wix |
|---|---|
| xqD7M7yB (caneca) | 253e81_0e9bbd4f07f54b49a50d8c6232f166c0~mv2.png |
| rsSjM2gY | 253e81_c45d727bd3d84ce6ad16ee44a1366400~mv2.png |
| 6QgfZpm1 | 253e81_f18be25b14284490b22735dc53fc703b~mv2.png |
| vmJ5BS1s | 253e81_af7df6a3d5514ebaa14e95cdc2f60a74~mv2.png |
| Zn7R9CfK | 253e81_0301481720f348a28636c3c8edd883c2~mv2.png |
| 4dXNBzqx | 253e81_77f852df444047f18a0def906b6bcccf~mv2.png |
| 281jcjch | 253e81_c057010c9ede4ef093b72a616f51c622~mv2.png |
| nc9ZKRrW | 253e81_19ba3b90a5b34587a8570e3dc4eee659~mv2.png |
| ZRqzWjXc | 253e81_062c3d78ffa14b919c794e8b3952b892~mv2.png |
| XYKRxTbh | 253e81_00f1217718934164a284d46b1fd808d5~mv2.png |
| QNpvj2BM | 253e81_39a5804dc579408185437d8b9d406005~mv2.png |
| GhDP0R9X | 253e81_74fc71f1a32a4135af46251ef05a6aee~mv2.png |
| HLGxyf9V (Presente) | 253e81_d184790d188d4022ae978c6593b9fb29~mv2.png |
| LhKgwqY7 (Presente, foto da Daniela) | 253e81_a24b5c52a5bb4c43b63948672d3b1b30~mv2.jpg |
| XYctb0Tc (Presente) | 253e81_637f5f11a3d4405ab6cdbaec5916b9eb~mv2.png |

## Menu

O menu de cima tem o item "✨ Mais", com cinco páginas dentro: Presente Doma, Ferramentas da Clínica, Arsenal Clínico, 📅 Agendar sessão (`/book-online`) e 👥 Comunidade (`/groups`). As duas últimas entraram em 23/11.

## Agenda e Comunidade (23/11)

- A página de agendamento tinha uma seção branca vazia, criada junto com o aplicativo, que cobria a lista de serviços. Ela foi apagada.
- A lista de serviços mostra a "imagem principal" de cada serviço, mas o formulário do Wix só grava a "imagem de capa". A função de `wix/backend-servicosImagem.web.js` copiou a capa para a imagem principal dos quatro serviços. Ela foi usada uma vez e depois tirada do site; a cópia fica aqui para o caso de um serviço novo precisar do mesmo ajuste.
- Na Comunidade, só a administração pode criar grupos. O grupo Comunidade Doma é só para quem tem o Doma Básico ou o Doma Premium.

## Lista do "Mais" que não fechava (resolvido em 23/11)

Quando o ponteiro saía da lista do "Mais" direto para um bloco de página (Início, Presente Doma, Arsenal e as outras páginas montadas como bloco), a lista ficava aberta. O bloco é uma janela separada dentro da página, e o site deixava de "ver" o ponteiro.

A correção está no arquivo de estilos do site (`wix/global.css`): enquanto a lista está aberta, o conteúdo das páginas deixa o ponteiro passar. Assim o site percebe que ele saiu da lista e a fecha; logo depois os blocos voltam a responder normalmente. Testado no Início, no Presente Doma e no Arsenal, inclusive o clique nos itens da lista e nos botões dos blocos.
