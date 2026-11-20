// =====================================================================
// CÓDIGO DA PÁGINA (Velo) - Página "Nível 1 · O Meu Ano Inicia Agora" (A Travessia)
// Vem da página do site atual; mudou só o caminho das outras páginas
// e a carteirinha, que aqui abre sempre como página (sem janela).
// Precisa do arquivo backend/travessia.web.js.
// =====================================================================
import { authentication } from 'wix-members-frontend';
import wixLocation from 'wix-location-frontend';
import { session } from 'wix-storage-frontend';
import { buscarMinhaCarteirinha, salvarMeuProgresso } from 'backend/travessia.web';

const ID_DO_HTML = '#html1';
const PAGINA_PLANOS = '/planos';
const PAGINA_NIVEL_2 = '/livro-a-travessia';     // página do Livro A Travessia
const PAGINA_CRIAR_CARTEIRINHA = '/carteira-d';  // página Minha Carteira
const PAGINA_DESTE_NIVEL = '/nivel-1';

$w.onReady(function () {
    const html = $w(ID_DO_HTML);

    // Mensagens que chegam do HTML embutido
    html.onMessage(async (event) => {
        const msg = event.data;
        if (!msg || msg.origem !== 'travessia') return;

        if (msg.tipo === 'ir-planos') {
            wixLocation.to(PAGINA_PLANOS);
        } else if (msg.tipo === 'ir-nivel-2') {
            wixLocation.to(PAGINA_NIVEL_2);
        } else if (msg.tipo === 'salvar-progresso') {
            salvarEmFila(msg.estado);
        } else if (msg.tipo === 'pedir-carteirinha') {
            await enviarCarteirinha();
        } else if (msg.tipo === 'pedir-login') {
            try {
                await authentication.promptLogin({ mode: 'login' });
            } catch (e) {
                // o visitante fechou a janela de login
            }
            await enviarCarteirinha();
        } else if (msg.tipo === 'ir-criar-carteirinha') {
            abrirCriacaoCarteirinha();
        }
    });

    // Se a pessoa fizer login por outro lugar (ex: botão do cabeçalho)
    authentication.onLogin(() => enviarCarteirinha());

    function abrirCriacaoCarteirinha() {
        // Guarda (na sessão do navegador) para onde voltar depois.
        session.setItem('travessia-voltar', PAGINA_DESTE_NIVEL);
        wixLocation.to(PAGINA_CRIAR_CARTEIRINHA);
    }

    async function enviarCarteirinha() {
        html.postMessage(await buscarCarteirinha());
    }

    // Salva um de cada vez; se chegar outro pedido no meio, guarda só o mais recente
    let salvando = false;
    let pendente = null;
    async function salvarEmFila(estado) {
        pendente = estado;
        if (salvando) return;
        salvando = true;
        while (pendente) {
            const atual = pendente;
            pendente = null;
            let r;
            try {
                r = await salvarMeuProgresso(atual);
            } catch (e) {
                console.error('Erro ao salvar progresso:', e);
                r = { ok: false };
            }
            if (!pendente) {
                html.postMessage({ origem: 'wix-travessia', tipo: 'progresso-salvo', ok: !!(r && r.ok) });
            }
        }
        salvando = false;
    }
});

async function buscarCarteirinha() {
    if (!authentication.loggedIn()) {
        return { origem: 'wix-travessia', status: 'nao-logado' };
    }
    try {
        const resposta = await buscarMinhaCarteirinha();
        return { origem: 'wix-travessia', ...resposta };
    } catch (erro) {
        console.error('Erro ao buscar carteirinha:', erro);
        return { origem: 'wix-travessia', status: 'erro', detalhe: String((erro && erro.message) || erro) };
    }
}
