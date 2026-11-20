// =====================================================================
// CÓDIGO DA PÁGINA (Velo) - Página "Nível 1 · O Meu Ano Inicia Agora" (A Travessia)
// Vem da página do site atual; mudou só o caminho das outras páginas
// e a carteirinha, que aqui abre sempre como página (sem janela).
// Precisa do arquivo backend/travessia.web.js.
//
// 20/11/2026 - Consentimento (LGPD): as respostas dos exercícios só são
// guardadas depois que a pessoa marca "concordo" na tela que o HTML mostra
// no começo do nível. O "concordo" fica guardado junto com o progresso:
//   progresso.consentimento = { aceito, quando, versao }
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
const PAGINA_DA_TRAVESSIA = '/a-travessia';      // para onde vai quem responde "agora não"
const PAGINA_PRIVACIDADE = '/politica-de-privacidade';
const VERSAO_DO_CONSENTIMENTO = '2026-11-20';    // mude quando o texto do pedido mudar

// Consentimento desta pessoa (null = ainda não concordou)
let consentimento = null;
// Último progresso que chegou antes do "concordo" (fica só na memória, não é guardado)
let esperandoConsentimento = null;

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
            if (consentimento) {
                salvarEmFila(msg.estado);
            } else {
                // Sem o "concordo" nada é guardado: segura na memória e pede de novo
                esperandoConsentimento = msg.estado;
                html.postMessage({ origem: 'wix-travessia', tipo: 'pedir-consentimento' });
            }
        } else if (msg.tipo === 'consentimento') {
            if (msg.aceito) {
                consentimento = { aceito: true, quando: new Date().toISOString(), versao: VERSAO_DO_CONSENTIMENTO };
                if (esperandoConsentimento) {
                    const estado = esperandoConsentimento;
                    esperandoConsentimento = null;
                    salvarEmFila(estado);
                }
            } else {
                wixLocation.to(PAGINA_DA_TRAVESSIA);
            }
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
                // o "concordo" vai junto com o progresso, para ficar registrado
                r = await salvarMeuProgresso(Object.assign({}, atual, { consentimento: consentimento }));
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
        consentimento = null;
        esperandoConsentimento = null;
        return { origem: 'wix-travessia', status: 'nao-logado' };
    }
    try {
        const resposta = await buscarMinhaCarteirinha();
        if (resposta && resposta.status === 'ok') {
            const salvo = resposta.progresso && resposta.progresso.consentimento;
            if (salvo && salvo.aceito) consentimento = salvo;
        }
        return {
            origem: 'wix-travessia',
            ...resposta,
            consentimento: !!consentimento,
            urlPrivacidade: wixLocation.baseUrl + PAGINA_PRIVACIDADE
        };
    } catch (erro) {
        console.error('Erro ao buscar carteirinha:', erro);
        return { origem: 'wix-travessia', status: 'erro', detalhe: String((erro && erro.message) || erro) };
    }
}
