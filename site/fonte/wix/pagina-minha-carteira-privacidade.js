// ---------------------------------------------------------------------
// 21/11/2026 - Privacidade (LGPD): retirar o consentimento
// Este trecho vai NO FIM do código da página Minha Carteira (carteira-d).
// No começo do arquivo, junto dos outros "import", entra esta linha:
//   import { buscarMinhaCarteirinha, salvarMeuProgresso } from 'backend/travessia.web';
//
// O "concordo" da Travessia fica guardado junto do progresso do Nível 1:
//   progresso.consentimento = { aceito, quando, versao }
// Retirar = guardar { aceito: false, retiradoEm, aceitoEm, versao }.
// Daí em diante o Nível 1 e o livro voltam a pedir o "concordo" e nada
// novo é guardado sem ele. O que já estava guardado continua na conta:
// para apagar, a pessoa pede por e-mail (está na Política de privacidade).
// ---------------------------------------------------------------------
$w.onReady(function () {
    const blocoPrivacidade = $w('#html1');
    const PAGINA_PRIVACIDADE = '/politica-de-privacidade';

    async function lerConsentimento() {
        if (!authentication.loggedIn()) return { estado: 'sem-login' };
        const r = await buscarMinhaCarteirinha();
        if (!r || r.status === 'erro') return { estado: 'erro' };
        if (r.status !== 'ok' || !r.progresso) return { estado: 'nenhum', progresso: null };
        const c = r.progresso.consentimento;
        if (c && c.aceito) return { estado: 'aceito', quando: c.quando || null, versao: c.versao || null, progresso: r.progresso };
        if (c && c.retiradoEm) return { estado: 'retirado', quando: c.retiradoEm, progresso: r.progresso };
        return { estado: 'nenhum', progresso: r.progresso };
    }

    function responder(dados) {
        blocoPrivacidade.postMessage({
            tipo: 'doma-consentimento-estado',
            estado: dados.estado,
            quando: dados.quando || null,
            urlPrivacidade: wixLocation.baseUrl + PAGINA_PRIVACIDADE
        });
    }

    blocoPrivacidade.onMessage(async (event) => {
        const msg = event.data;
        if (!msg || typeof msg.tipo !== 'string') return;

        if (msg.tipo === 'doma-consentimento-ler') {
            try {
                responder(await lerConsentimento());
            } catch (e) {
                console.error('[Privacidade] erro ao ler o consentimento:', e);
                responder({ estado: 'erro' });
            }
        } else if (msg.tipo === 'doma-consentimento-retirar') {
            try {
                const atual = await lerConsentimento();
                if (atual.estado !== 'aceito') { responder(atual); return; }
                const registro = {
                    aceito: false,
                    retiradoEm: new Date().toISOString(),
                    aceitoEm: atual.quando,
                    versao: atual.versao
                };
                const r = await salvarMeuProgresso(Object.assign({}, atual.progresso, { consentimento: registro }));
                if (r && r.ok) responder({ estado: 'retirado', quando: registro.retiradoEm });
                else responder({ estado: 'erro' });
            } catch (e) {
                console.error('[Privacidade] erro ao retirar o consentimento:', e);
                responder({ estado: 'erro' });
            }
        }
    });
});
