// Agenda: a lista de serviços do site mostra a "imagem principal" de cada serviço,
// mas o formulário novo do Wix só grava a "imagem de capa". Esta função copia a
// capa para a imagem principal nos serviços que ainda não têm uma.
// Uso pontual, pelo editor, por quem administra o site.
import { Permissions, webMethod } from 'wix-web-module';
import { services } from 'wix-bookings.v2';
import { elevate } from 'wix-auth';

export const copiarCapaParaPrincipal = webMethod(Permissions.Admin, async () => {
    const resultado = [];
    const lista = await elevate(services.queryServices)().limit(50).find();
    for (const s of lista.items) {
        const media = s.media || {};
        const capa = media.coverMedia;
        if (!capa || (media.mainMedia && media.mainMedia.image)) {
            resultado.push(s.name + ': sem mudança');
            continue;
        }
        await elevate(services.updateService)(s._id, {
            revision: s.revision,
            media: { ...media, mainMedia: capa }
        });
        resultado.push(s.name + ': imagem principal = capa');
    }
    return resultado;
});
