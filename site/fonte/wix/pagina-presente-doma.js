// Presente Doma: o bloco da página avisa quando a pessoa clica nos botões
// e a página leva para o endereço certo do site.
import wixLocation from 'wix-location-frontend';

$w.onReady(function () {
    $w('#html1').onMessage((event) => {
        if (event.data === 'redirecionarPagina') {
            wixLocation.to('/livro-a-travessia');
        }
        if (event.data === 'irParaPlanos') {
            wixLocation.to('/pricing-plans/plans-pricing');
        }
    });
});
