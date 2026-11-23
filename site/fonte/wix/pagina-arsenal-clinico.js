// Arsenal Clínico: cada cartão do bloco avisa qual produto a pessoa quer,
// e a página leva para o produto certo da Loja Doma.
import wixLocation from 'wix-location-frontend';

const PRODUTOS = {
    abrirAncora: 'caneca-doma-varias-opções',
    abrirJogo: 'jogo-de-memoria-terapêutico-em-mdf',
    abrirFoco: 'jogo-da-velha-tamanho-família',
    abrirAbrigo: 'necessaire-personalizada-doma',
    abrirPacien: 'quebra-cabeça-terapêutico',
    abrirMinFor: 'camiseta-doma',
    abrirMeuTro: 'camiseta-doma',
    abrirConexa: 'camiseta-doma',
    abrirAlivio: 'copo-domadores-de-monstros-internos',
    abrirSuport: 'bloco-de-anotações-doma-capa-dura',
    abrirFerram: 'caneta-doma'
};

$w.onReady(function () {
    $w('#html1').onMessage((event) => {
        const acao = (event.data && event.data.acao) || '';
        if (acao === 'fecharMenu') {
            // O ponteiro entrou no bloco: fecha a lista aberta do "Mais".
            $w('#menu1').hide().then(() => $w('#menu1').show());
            return;
        }
        if (acao === 'abrirLojCom') {
            wixLocation.to('/category/all-products');
            return;
        }
        const produto = PRODUTOS[acao];
        if (produto) {
            wixLocation.to('/product-page/' + encodeURIComponent(produto));
        }
    });
});
