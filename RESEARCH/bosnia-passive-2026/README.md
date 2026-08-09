# Bosnia — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.ba TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 723 |
| Live hosts fingerprinted | 502 |
| DNS/DMARC records analyzed | 12 |
| Historical URLs (GAU) | 6625 |

## Tools & Methodology

| Tool | Purpose | Rate Limit |
|------|---------|------------|
| `subfinder` | Passive subdomain enumeration (all sources) | 5 req/s |
| `httpx` | HTTP fingerprinting — tech detect, status, title, server | 5 req/s |
| `dig` | DNS record analysis — MX, SPF, DMARC | N/A (DNS) |
| `gau` | Historical URL discovery via Wayback/CommonCrawl/OTX | 2 threads |

All reconnaissance was passive. No vulnerability scanning. No exploitation attempts.  
Rate-limited to 5 requests/second maximum.

## Key Findings

### Subdomain Enumeration
```
www.ekonsultacije.gov.ba
ms.almbih.gov.ba
ejs.fpu.gov.ba
www.obuke.adsfbih.gov.ba
cpanel.fucz.gov.ba
privreda.sbk-ksb.gov.ba
webmail.olovo.gov.ba
zis.ks.gov.ba
mupk10.gov.ba
mrsri.ks.gov.ba
bosanskipetrovac.gov.ba
www.eaip.bhansa.gov.ba
mail.fmoit.gov.ba
autodiscover.policijabdbih.gov.ba
www.mft.gov.ba
www.fzzp.gov.ba
webmail.doboj.gov.ba
cpanel.bpkg.gov.ba
webdisk.fmp.gov.ba
trezorbih.gov.ba
```
<details><summary>Full list (723 subdomains)</summary>

```
www.ekonsultacije.gov.ba
ms.almbih.gov.ba
ejs.fpu.gov.ba
www.obuke.adsfbih.gov.ba
cpanel.fucz.gov.ba
privreda.sbk-ksb.gov.ba
webmail.olovo.gov.ba
zis.ks.gov.ba
mupk10.gov.ba
mrsri.ks.gov.ba
bosanskipetrovac.gov.ba
www.eaip.bhansa.gov.ba
mail.fmoit.gov.ba
autodiscover.policijabdbih.gov.ba
www.mft.gov.ba
www.fzzp.gov.ba
webmail.doboj.gov.ba
cpanel.bpkg.gov.ba
webdisk.fmp.gov.ba
trezorbih.gov.ba
api.ads.gov.ba
olovo.gov.ba
webmail.kakanj.gov.ba
fazuoi.gov.ba
ekonsultacije.gov.ba
goprocure.javnenabavke.gov.ba
mail.vladafbih.gov.ba
admin.ads.gov.ba
api.admin.adsbih.gov.ba
www.mz.ks.gov.ba
fpu.gov.ba
mail.vladahbz.gov.ba
vladahbz.gov.ba
basmp.gov.ba
info.vm.gov.ba
ns.adsfbih.gov.ba
ap.ks.gov.ba
www.fzzpr.gov.ba
nalozi.bdbih.gov.ba
mail.iddeea.gov.ba
jira.javnenabavke.gov.ba
webmail.mupusk.gov.ba
webdisk.fsa.gov.ba
admin.adsfbih.gov.ba
www.fipa.gov.ba
www.met.gov.ba
www.faco.mupsbk-ksb.gov.ba
webdisk.stolac.gov.ba
webdisk.kakanj.gov.ba
webdisk.velikakladusa.gov.ba
webmail.cip.gov.ba
www.egov.ads.gov.ba
www.sbk-ksb.gov.ba
mail.ozp.gov.ba
lms.ilearn.gov.ba
abc.gov.ba
autodiscover.fpu.gov.ba
www.fmpvs.gov.ba
webmail.fmoit.gov.ba
zpr.ks.gov.ba
servisi.sanskimost.gov.ba
webmail.srebrenica.gov.ba
mail.sipa.gov.ba
www.iddeea.gov.ba
ada.gov.ba
adsf.gov.ba
eprijava.adsfbih.gov.ba
cpanel.mupusk.gov.ba
pb.ks.gov.ba
www.skupstina.ks.gov.ba
webdisk.muptk.gov.ba
fsa.gov.ba
fmrpo.gov.ba
mail.ks.gov.ba
n0va.sanskimost.gov.ba
www.zbpp.ks.gov.ba
fmp.gov.ba
cpanel.velikakladusa.gov.ba
casht01-srv.vm.gov.ba
cpcalendars.ada.gov.ba
adsbih.gov.ba
mreza-fucz.gov.ba
ankete.sanskimost.gov.ba
www.kucz.ks.gov.ba
cpanel.dijaspora.mhrr.gov.ba
www.ecdl.ads.gov.ba
monkshnk.gov.ba
webmail.policijabdbih.gov.ba
webdisk.mft.gov.ba
www.mp.ks.gov.ba
muptk.gov.ba
autodiscover.fzzpr.gov.ba
www.parco.gov.ba
www.help.ads.gov.ba
kpzptsarajevo.gov.ba
test.mupsbk-ksb.gov.ba
www.savjetministara.gov.ba
help.ads.gov.ba
fop.fhmzbih.gov.ba
webmail.sanskimost.gov.ba
banovici.gov.ba
webmail.parlamentfbih.gov.ba
www.fmt.gov.ba
investindoboj.doboj.gov.ba
mail.fazuoi.gov.ba
e-id.gov.ba
hrmis.ads.gov.ba
www.visit.doboj.gov.ba
webmail.vukosavlje.gov.ba
www.mkt.gov.ba
files.ads.gov.ba
cpanel.mreza-fucz.gov.ba
www.fmoit.gov.ba
ms.ks.gov.ba
www.mpu.ks.gov.ba
webdisk.aposo.gov.ba
www.predstavnickidom-pfbih.gov.ba
www.mupzdk.gov.ba
dei.gov.ba
mft.gov.ba
webmail.ads.gov.ba
www.trezorbih.gov.ba
cpanel.doboj.gov.ba
www.fmks.gov.ba
webdisk.sanskimost.gov.ba
mail-01.bdbih.gov.ba
mupsbk-ksb.gov.ba
mail.gracanica.gov.ba
transportnedozvole.gov.ba
www.transportnedozvole.gov.ba
fiskal.fisk.fpu.gov.ba
www.szzp.gov.ba
cpanel.ada.gov.ba
webdisk.ada.gov.ba
www.mreza-fucz.gov.ba
mki.ks.gov.ba
gradcazin.gov.ba
icis-portal.vijeceministara.gov.ba
videoarhiv.gov.ba
mhrr.gov.ba
www.72h.doboj.gov.ba
www.nova.fmks.gov.ba
www.ministarstvo-financija-zzh.gov.ba
autodiscover.sbk-ksb.gov.ba
www.szdp.gov.ba
webdisk.arsbih.gov.ba
www.fbdd.mupsbk-ksb.gov.ba
cpanel.fmp.gov.ba
cip.gov.ba
fbihpotpredsjednik.gov.ba
ads.gov.ba
www.ankete.sanskimost.gov.ba
www.registri.uzzb.gov.ba
www.videoarhiv.gov.ba
www.velikakladusa.gov.ba
npis.fpu.gov.ba
cips.gov.ba
ekonkurs.adsfbih.gov.ba
mail.eaip.bhansa.gov.ba
vlada.ks.gov.ba
www.mon.ks.gov.ba
srebrenica.gov.ba
www.zik.ks.gov.ba
mf.ks.gov.ba
fmks.gov.ba
nadzornitimovi.parco.gov.ba
new.parco.gov.ba
cpanel.fzzpr.gov.ba
autodiscovery.sipa.gov.ba
vigilansa.almbih.gov.ba
arz.gov.ba
annt.gov.ba
konkursi.ads.gov.ba
cpanel.tomislavgrad.gov.ba
cpanel.fsa.gov.ba
www.start.sanskimost.gov.ba
mail.skupstina.tk.gov.ba
webmail.bhdca.gov.ba
infopult.sanskimost.gov.ba
skupstina.tk.gov.ba
webmail.mupk10.gov.ba
cpanel.stolac.gov.ba
www.smtp.parco.gov.ba
mail.kakanj.gov.ba
www.fazuoi.gov.ba
www.mp.bpkg.gov.ba
arhiva.sbk-ksb.gov.ba
webdisk.mupk10.gov.ba
cpanel.fmks.gov.ba
www.euprava.velikakladusa.gov.ba
mail.szdp.gov.ba
www.javnenabavke.gov.ba
www.dei.gov.ba
my.adsfbih.gov.ba
mupusk.gov.ba
www.rju.parco.gov.ba
www.nadzornitimovi.parco.gov.ba
cpanel.aposo.gov.ba
www.mail.parlamentfbih.gov.ba
www.mpz.ks.gov.ba
www.mpr.bpkg.gov.ba
www.adresar.ads.gov.ba
fbdd.mupsbk-ksb.gov.ba
tsg.vladafbih.gov.ba
mpr.gov.ba
www.privreda.sbk-ksb.gov.ba
mail.policijabdbih.gov.ba
www.mks.ks.gov.ba
www.fgu.gov.ba
webdisk.mreza-fucz.gov.ba
www.eregistar.sanskimost.gov.ba
fzzp.gov.ba
webmail.aposo.gov.ba
ozp.gov.ba
email.sipa.gov.ba
autodiscover.javnenabavke.gov.ba
uzzb.gov.ba
box2.adsfbih.gov.ba
autodiscover.tomislavgrad.gov.ba
api.admin.ads.gov.ba
fmpuio.gov.ba
agenrzbh.gov.ba
hrmis.adsfbih.gov.ba
vijece.sanskimost.gov.ba
cpanel.mupk10.gov.ba
webdisk.bosanskipetrovac.gov.ba
www.ombudsmen.gov.ba
cest.gov.ba
www.policijabdbih.gov.ba
www.ipr.gov.ba
www.homologacija.gov.ba
www.fzzg.gov.ba
webdisk.parco.gov.ba
mail.cfcu.gov.ba
www.arz.gov.ba
mojkonkurs.ads.gov.ba
ministarstvo-financija-zzh.gov.ba
mail.parco.gov.ba
aeptm.gov.ba
webmail.mft.gov.ba
mail.fmp.gov.ba
www.turizam.fmoit.gov.ba
fipa.gov.ba
arhivfbih.gov.ba
met.gov.ba
webdisk.predsjednikfbih.gov.ba
www.zpr.ks.gov.ba
ombudsmen.gov.ba
nova.fmp.gov.ba
dijaspora.mhrr.gov.ba
obukeold.adsfbih.gov.ba
www.aeptm.gov.ba
webmail.fmp.gov.ba
webmail.velikakladusa.gov.ba
lync01-srv.vm.gov.ba
fondzapov.gov.ba
mail.trezorbih.gov.ba
www.mupk10.gov.ba
ippfbih.gov.ba
webdisk.fzzpr.gov.ba
curriculum.aposo.gov.ba
hrm.adsfbih.gov.ba
www.test.mupsbk-ksb.gov.ba
zik.ks.gov.ba
mbp.ks.gov.ba
fmeri.gov.ba
webmail.bpkg.gov.ba
www.mhrr.gov.ba
fbihvlada.gov.ba
www.konkursi.ads.gov.ba
www.kpzptsarajevo.gov.ba
cpanel.fmoit.gov.ba
sjednice.tomislavgrad.gov.ba
mail.aposo.gov.ba
mail.velikakladusa.gov.ba
webmail.sudbih.gov.ba
mail.ada.gov.ba
www.fucz.gov.ba
www.test.stolac.gov.ba
webdisk.mupusk.gov.ba
mail.sps.gov.ba
mail.almbih.gov.ba
webmail.fhmzbih.gov.ba
1107press.srebrenica.gov.ba
smtp.parco.gov.ba
rju.parco.gov.ba
www.ejn.gov.ba
mail.mupusk.gov.ba
www.arhiva.sbk-ksb.gov.ba
mmail.ks.gov.ba
www.uzzb.gov.ba
webmail.sbk-ksb.gov.ba
www.epi.secrs.gov.ba
webmail.adsfbih.gov.ba
webmail.gradcazin.gov.ba
szdp.gov.ba
www.almbih.gov.ba
sigurno.policijabdbih.gov.ba
cpanel.sbk-ksb.gov.ba
www.dep.gov.ba
webmail.tomislavgrad.gov.ba
webmail.fucz.gov.ba
fmoit.gov.ba
www.arsbih.gov.ba
velikakladusa.gov.ba
www.zis.ks.gov.ba
webmail.dijaspora.mhrr.gov.ba
webdisk.ozp.gov.ba
revizija.gov.ba
wwww.ads.gov.ba
start.sanskimost.gov.ba
webmail.muptk.gov.ba
sslvpn.vladafbih.gov.ba
epi.secrs.gov.ba
www.mpr.gov.ba
cpanel.kpzptsarajevo.gov.ba
zbpp.ks.gov.ba
wisppa.javnenabavke.gov.ba
www.mupsbk-ksb.gov.ba
webdisk.almbih.gov.ba
webdisk.trezorbih.gov.ba
ks105.ks.gov.ba
www.cloud.sanskimost.gov.ba
webmail.ozp.gov.ba
mail.sbk-ksb.gov.ba
tim.ads.gov.ba
webmail.kpzzt.gov.ba
www.vlada.ks.gov.ba
www.policija.mupusk.gov.ba
webdisk.parlamentfbih.gov.ba
obuke.adsfbih.gov.ba
www.breza.gov.ba
mks.ks.gov.ba
www.forum.sanskimost.gov.ba
www.invest.kakanj.gov.ba
webmail.fmpik.gov.ba
ms.bpkg.gov.ba
listelijekova.ks.gov.ba
drr.ks.gov.ba
vukosavlje.gov.ba
cpanel.parco.gov.ba
eservisi.fbih.gov.ba
registar.ajn.gov.ba
webdisk.fhmzbih.gov.ba
mail.fmks.gov.ba
webdisk.dijaspora.mhrr.gov.ba
autodiscover.fmoit.gov.ba
doboj.gov.ba
mail.mupk10.gov.ba
bpkg.gov.ba
www.pubserver.ipr.gov.ba
test2.ks.gov.ba
cpanel.mupsbk-ksb.gov.ba
cpanel.eaip.bhansa.gov.ba
www.kuip.ks.gov.ba
mail.doboj.gov.ba
www.mki.ks.gov.ba
cpanel.vukosavlje.gov.ba
www.mb.bpkg.gov.ba
www.dkpt.gov.ba
cpanel.gradcazin.gov.ba
fzzg.gov.ba
icis-sts.vijeceministara.gov.ba
www.eservisiappi.fbih.gov.ba
www.ilearn.gov.ba
jira.ads.gov.ba
admin.adsbih.gov.ba
webdisk.fucz.gov.ba
webdisk.fmks.gov.ba
uplate.ipr.gov.ba
cas-srv-01.mvp.gov.ba
www.predsjednikfbih.gov.ba
cpanel.mft.gov.ba
webdisk.vukosavlje.gov.ba
mail.srebrenica.gov.ba
cpanel.fmt.gov.ba
mpr.bpkg.gov.ba
sps.gov.ba
agncijawww.adsfbih.gov.ba
mapa.parco.gov.ba
autodiscover.vukosavlje.gov.ba
edoprinosi.fpu.gov.ba
ilias.adsfbih.gov.ba
registar.ads.gov.ba
api.adsbih.gov.ba
webdisk.sbk-ksb.gov.ba
www.investindoboj.doboj.gov.ba
ll.ks.gov.ba
www.pbr.gov.ba
egov.ads.gov.ba
arsbih.gov.ba
mz.ks.gov.ba
jn.ks.gov.ba
webmail.bosanskipetrovac.gov.ba
www.bosanskipetrovac.gov.ba
mo.bpkg.gov.ba
icis-services.vijeceministara.gov.ba
rs.cest.gov.ba
es.tomislavgrad.gov.ba
www.sanskimost.gov.ba
azobih.gov.ba
skupstina.ks.gov.ba
www.aposo.gov.ba
mf.bpkg.gov.ba
mail.mupzdk.gov.ba
s1.adsfbih.gov.ba
webdisk.tomislavgrad.gov.ba
www.mupusk.gov.ba
eopc.fmt.gov.ba
www.v2.srebrenica.gov.ba
sigurno1.policijabdbih.gov.ba
kakanj.kakanj.gov.ba
www.ms.bpkg.gov.ba
bhdca.gov.ba
bas.gov.ba
webdisk.kpzptsarajevo.gov.ba
mail.banovici.gov.ba
il.ks.gov.ba
mail.breza.gov.ba
v2.srebrenica.gov.ba
mail.fzzg.gov.ba
webmail.arsbih.gov.ba
aposo.gov.ba
sanskimost.gov.ba
webdisk.fazuoi.gov.ba
autodiscover.cip.gov.ba
www.kpzptor.gov.ba
webmail.bdbih.gov.ba
fmoit.fmoit.gov.ba
cpanel.olovo.gov.ba
mail.fhmzbih.gov.ba
autodiscover.stolac.gov.ba
webmail.stolac.gov.ba
www.nova.fmp.gov.ba
it.bpkg.gov.ba
mailserver.fmf.gov.ba
cas-srv-02.mvp.gov.ba
www.sigurno.policijabdbih.gov.ba
cpanel.sanskimost.gov.ba
vladafbih.gov.ba
kpztuzla.gov.ba
mail.muptk.gov.ba
webmail.fazuoi.gov.ba
bims.fuzip.gov.ba
www.e-id.gov.ba
www.banovici.gov.ba
autodiscover.olovo.gov.ba
cpanel.trezorbih.gov.ba
www.mrsri.ks.gov.ba
mail.fpu.gov.ba
www.mcp.gov.ba
mail.kpztuzla.gov.ba
webdisk.kpzzt.gov.ba
ks135.ks.gov.ba
mail.komvp.gov.ba
casht02-srv.vm.gov.ba
tuzilastvobih.gov.ba
policijabdbih.gov.ba
www.drr.ks.gov.ba
www.servisi.sanskimost.gov.ba
autodiscover.gradcazin.gov.ba
webmail.cfcu.gov.ba
www.fhmzbih.gov.ba
kucz.ks.gov.ba
www.stolac.gov.ba
mail.bpkg.gov.ba
www.new.parco.gov.ba
mail.nova.fmp.gov.ba
www.mf.bpkg.gov.ba
tomislavgrad.gov.ba
webdisk.policijabdbih.gov.ba
www.doboj.gov.ba
www.meteo.fhmzbih.gov.ba
webdisk.ministarstvo-financija-zzh.gov.ba
webdisk.fmpik.gov.ba
arhivbih.gov.ba
webmail.trezorbih.gov.ba
www.mail.parco.gov.ba
webdisk.fmt.gov.ba
cfcu.gov.ba
turizam.fmoit.gov.ba
webmail.javnenabavke.gov.ba
owis.bhdca.gov.ba
webmail.kpzptsarajevo.gov.ba
mail.mreza-fucz.gov.ba
www.kpzzt.gov.ba
www.n0va.sanskimost.gov.ba
meteoalarm.fhmzbih.gov.ba
iss.fmpvs.gov.ba
visit.doboj.gov.ba
mail.cip.gov.ba
konsultacijeads.gov.ba
www.fmrpo.gov.ba
webmail.fsa.gov.ba
cpanel.ministarstvo-financija-zzh.gov.ba
stolac.gov.ba
autodiscover.bpkg.gov.ba
www.ozp.gov.ba
predstavnickidom-pfbih.gov.ba
www.pravni-eksperti.ads.gov.ba
forum.sanskimost.gov.ba
javnenabavke.gov.ba
bihkonk.gov.ba
fzzpr.gov.ba
fmpik.gov.ba
icis-sts.vladafbih.gov.ba
www.vladahbz.gov.ba
www.monkshnk.gov.ba
www.kpztuzla.gov.ba
webmail.almbih.gov.ba
kpzzt.gov.ba
www.pb.ks.gov.ba
webmail.ministarstvo-financija-zzh.gov.ba
www.skupstina.tk.gov.ba
docs.ejn.gov.ba
www.adc.gov.ba
adsfbih.gov.ba
cpanel.fhmzbih.gov.ba
www.infopult.sanskimost.gov.ba
www.fmp.gov.ba
www.kakanj.kakanj.gov.ba
mail.sanskimost.gov.ba
cpanel.ozp.gov.ba
www.olovo.gov.ba
mail.mft.gov.ba
webdisk.srebrenica.gov.ba
www.adfsbih.gov.ba
autodiscover.predsjednikfbih.gov.ba
agropedologija.gov.ba
autodiscover.bosanskipetrovac.gov.ba
webmail.fzzpr.gov.ba
cpanel.fmpik.gov.ba
www.ippfbih.gov.ba
mu.bpkg.gov.ba
ipr.gov.ba
mail.kpzptsarajevo.gov.ba
webdisk.fmoit.gov.ba
entermail.parco.gov.ba
www.dijaspora.mhrr.gov.ba
mup.bpkg.gov.ba
fmfmailserver.fmf.gov.ba
mail.kpzptor.gov.ba
www.hrm.adsfbih.gov.ba
mail.mupsbk-ksb.gov.ba
webmail.mupsbk-ksb.gov.ba
www.parlamentfbih.gov.ba
www.mail.banovici.gov.ba
www.ads.gov.ba
mon.ks.gov.ba
cpanel.muptk.gov.ba
hea.gov.ba
almbih.gov.ba
mail.kpzzt.gov.ba
invest.doboj.gov.ba
www.mail.velikakladusa.gov.ba
cpanel.cfcu.gov.ba
test.stolac.gov.ba
mail.dijaspora.mhrr.gov.ba
www.uplate.ipr.gov.ba
icis-services.vladafbih.gov.ba
eispit.adsfbih.gov.ba
mail.predsjednikfbih.gov.ba
cpcontacts.ada.gov.ba
bata.gov.ba
ecdl.ads.gov.ba
webmail.dep.gov.ba
www.dev.parco.gov.ba
www.ms.ks.gov.ba
mail.ipr.gov.ba
webmail.fmt.gov.ba
webmail.aeptm.gov.ba
webmail.vladafbih.gov.ba
adresar.ads.gov.ba
webdisk.doboj.gov.ba
autodiscover.fmks.gov.ba
mail.bosanskipetrovac.gov.ba
www.sigurno1.policijabdbih.gov.ba
fmt.gov.ba
www.vijece.sanskimost.gov.ba
cpanel.arsbih.gov.ba
mpu.ks.gov.ba
www.vet.gov.ba
pbr.gov.ba
eregistar.sanskimost.gov.ba
mail.vukosavlje.gov.ba
server02.javnenabavke.gov.ba
webmail.predsjednikfbih.gov.ba
www.invest.doboj.gov.ba
invest.kakanj.gov.ba
ejn.gov.ba
webdisk.mupsbk-ksb.gov.ba
autodiscover.mupk10.gov.ba
sbk-ksb.gov.ba
mb.bpkg.gov.ba
www.mod.gov.ba
predsjednikfbih.gov.ba
cpanel.kpzzt.gov.ba
www.fsa.gov.ba
mail.parlamentfbih.gov.ba
esv.ks.gov.ba
www.ada.gov.ba
fmpvs.gov.ba
mail.fsa.gov.ba
www.mbp.ks.gov.ba
www.mapa.parco.gov.ba
mail.fmpik.gov.ba
www.it.bpkg.gov.ba
icis-portal.vladafbih.gov.ba
www.adsfbih.gov.ba
faco.mupsbk-ksb.gov.ba
www.fop.fhmzbih.gov.ba
gracanica.gov.ba
www.cfcu.gov.ba
kpzptor.gov.ba
www.mail.komvp.gov.ba
www.vijeceministara.gov.ba
registri.uzzb.gov.ba
fhmzbih.gov.ba
www.registar.ajn.gov.ba
mvp.gov.ba
www.law-drafters.ads.gov.ba
cpanel.predsjednikfbih.gov.ba
cloud.sanskimost.gov.ba
www.mf.ks.gov.ba
mail.gradcazin.gov.ba
skola.monkshnk.gov.ba
fmf.gov.ba
mail.stolac.gov.ba
cpanel.bosanskipetrovac.gov.ba
webdisk.bpkg.gov.ba
www.fmpik.gov.ba
lms.adsfbih.gov.ba
webmail.eaip.bhansa.gov.ba
autodiscover.fmt.gov.ba
srv1.adsfbih.gov.ba
webmail.registrarbih.gov.ba
uino.gov.ba
www.meteoalarm.fhmzbih.gov.ba
dep.gov.ba
cpanel.parlamentfbih.gov.ba
www.srebrenica.gov.ba
mail.tomislavgrad.gov.ba
72h.doboj.gov.ba
mail.fzzpr.gov.ba
mail.fmt.gov.ba
www.curriculum.aposo.gov.ba
www.mup.bpkg.gov.ba
www.msb.gov.ba
www.tomislavgrad.gov.ba
eservisiappi.fbih.gov.ba
dev.parco.gov.ba
www.mu.bpkg.gov.ba
mail.agropedologija.gov.ba
iddeea.gov.ba
ilias-dev.adsfbih.gov.ba
www.1107press.srebrenica.gov.ba
autodiscover.kakanj.gov.ba
cpanel.kakanj.gov.ba
autodiscover.vladafbih.gov.ba
policija.mupusk.gov.ba
autodiscover.srebrenica.gov.ba
cpanel.fazuoi.gov.ba
fgu.gov.ba
www.en.invest.doboj.gov.ba
www.muptk.gov.ba
mp.ks.gov.ba
mail.ministarstvo-financija-zzh.gov.ba
www.kakanj.gov.ba
www.ap.ks.gov.ba
autodiscover.fmf.gov.ba
nova.fmks.gov.ba
homologacija.gov.ba
www.gracanica.gov.ba
cpanel.policijabdbih.gov.ba
en.invest.doboj.gov.ba
kuip.ks.gov.ba
mail.uzzb.gov.ba
webdisk.cfcu.gov.ba
azlp.gov.ba
vet.gov.ba
webmail.mreza-fucz.gov.ba
www.agropedologija.gov.ba
www.webmail.adsfbih.gov.ba
webmail.tuzilastvobih.gov.ba
mp.bpkg.gov.ba
cpanel.almbih.gov.ba
ks5.ks.gov.ba
mpz.ks.gov.ba
mup.ks.gov.ba
www.entermail.parco.gov.ba
webmail.ada.gov.ba
webdisk.eaip.bhansa.gov.ba
mail.arsbih.gov.ba
euprava.velikakladusa.gov.ba
meteo.fhmzbih.gov.ba
www.bpkg.gov.ba
cpanel.srebrenica.gov.ba
webmail.parco.gov.ba
www.mup.ks.gov.ba
webmail.fmks.gov.ba
kakanj.gov.ba
propisi.ks.gov.ba
autodiscover.mvp.gov.ba
exchange.mvp.gov.ba
www.mvteo.gov.ba
parco.gov.ba
fucz.gov.ba
mail.fucz.gov.ba
pubserver.ipr.gov.ba
www.vukosavlje.gov.ba
eaip.bhansa.gov.ba
webdisk.gradcazin.gov.ba
www.gradcazin.gov.ba
parlamentfbih.gov.ba
www.mo.bpkg.gov.ba
www.abcfbih.gov.ba
breza.gov.ba
mail.olovo.gov.ba
webdisk.olovo.gov.ba
mupzdk.gov.ba
www.mfa.gov.ba
mail.mfa.gov.ba
is3.mfa.gov.ba
```
</details>

### Live Host Fingerprinting
```
https://72h.doboj.gov.ba [[32m200[0m] [nginx] [[35mEngintron,Nginx[0m]
https://admin.ads.gov.ba [[32m200[0m] [[36mApp[0m] [] [[35mHSTS[0m]
https://adresar.ads.gov.ba [[32m200[0m] [[36mAdresar državnih institucija u Bosni i Hercegovini[0m] [Microsoft-IIS/10.0] [[35mBootstrap:5.2.3,IIS:10.0,Microsoft ASP.NET,Windows Server,jsDelivr[0m]
https://admin.adsbih.gov.ba [[32m200[0m] [[36mApp[0m] [] [[35mHSTS[0m]
https://ada.gov.ba [[33m301[0m] [nginx] [[35mEngintron,Nginx,PHP:7.2.34[0m]
https://ads.gov.ba [[32m200[0m] [] [[35mHSTS[0m]
https://admin.adsfbih.gov.ba [[33m302[0m] [[36mObject moved[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Microsoft ASP.NET:4.0.30319,Windows Server[0m]
https://adsbih.gov.ba [[32m200[0m] [] [[35mHSTS[0m]
https://ankete.sanskimost.gov.ba [] [[36mInternal Server Error[0m] [nginx] [[35mNginx,PHP:7.2.34[0m]
https://api.admin.ads.gov.ba [[31m404[0m] [] [[35mHSTS[0m]
https://almbih.gov.ba [[32m200[0m] [[36mAgencija za lijekove i medicinska sredstva Bosne i Hercegovine[0m] [Apache] [[35mApache HTTP Server,HSTS,MySQL,PHP,Polylang,WordPress[0m]
https://aeptm.gov.ba [[32m200[0m] [[36mAEPTM |[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,Drupal:7,HTTP/3,PHP[0m]
https://api.admin.adsbih.gov.ba [[31m404[0m] [] [[35mHSTS[0m]
https://api.ads.gov.ba [[31m404[0m] [] [[35mHSTS[0m]
https://annt.gov.ba [[33m302[0m] [[36mObject moved[0m] [Microsoft-IIS/7.5] [[35mIIS:7.5,Microsoft ASP.NET:2.0.50727,Windows Server[0m]
https://aposo.gov.ba [[32m200[0m] [[36mDobrodošli na web stranicu Agencije - APOSO[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,Divi:4.4.1,Google Analytics,HTTP/3,LiteSpeed,LiteSpeed Cache,Litespeed Cache,MySQL,PHP,WPML:4.7.1,WordPress,Yoast SEO:24.7,jQuery,jQuery Migrate:3.4.1,jsDelivr[0m]
https://api.adsbih.gov.ba [[31m404[0m] [] [[35mHSTS[0m]
https://autodiscover.fpu.gov.ba [[33m301[0m] [Microsoft-IIS/8.0] [[35mIIS:8.0,Microsoft ASP.NET,Windows Server[0m]
https://agropedologija.gov.ba [[32m200[0m] [[36mFederalni zavod za agropedologiju[0m] [nginx] [[35mCloudways,Elementor:3.18.2,Font Awesome,MySQL,Nginx,PHP,Slick,Underscore.js:1.13.7,WPForms:1.8.5.3,WordPress:6.9.1,Yoast SEO:21.7,imagesLoaded:5.0.0,jQuery,jQuery Migrate:3.4.1,reCAPTCHA[0m]
https://autodiscover.kakanj.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://arhivfbih.gov.ba [[32m200[0m] [[36mHome[0m] [nginx] [[35mBootstrap:5,Joomla,Nginx,PHP:8.3.30,UIKit,jQuery,scrollreveal[0m]
https://arz.gov.ba [[33m302[0m] [[36mObject moved[0m] [Microsoft-IIS/7.5] [[35mIIS:7.5,Microsoft ASP.NET,Windows Server[0m]
https://autodiscover.bosanskipetrovac.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.olovo.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.fmf.gov.ba [[33m302[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Windows Server[0m]
https://autodiscover.srebrenica.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://arsbih.gov.ba [[32m200[0m] [[36mStart - ARS BiH[0m] [nginx] [[35mDivi,Engintron,FitVids.JS:4.27.5,Google Analytics,HSTS,MonsterInsights:9.11.1,MySQL,Nginx,PHP,WordPress:6.9.1,Yoast SEO:26.7,jQuery,jQuery Migrate:3.4.1[0m]
https://autodiscover.stolac.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.mupk10.gov.ba [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.vukosavlje.gov.ba [[31m400[0m] [nginx] [[35mNginx[0m]
```

### DNS / DMARC Analysis
```
--- gov.ba ---
--- parliament.ba ---
--- mil.ba ---
--- finance.gov.ba ---
--- health.gov.ba ---
--- mfa.gov.ba ---
10 mfa-gov-ba.mail.protection.outlook.com.
0 mfa-gov-ba.mail.protection.outlook.com.
"v=spf1 include:spf.protection.outlook.com -all"
"v=spf1 ip4:195.222.52.10 ip4:195.222.52.11  ip4:195.222.52.2 a - all  "
--- police.gov.ba ---
--- justice.gov.ba ---
```

### Historical URLs (Sample)
```
http://gov.ba
http://gov.ba/Clanci
http://gov.ba/robots.txt
http://www.mfa.gov.ba:80/
http://www.mfa.gov.ba:80/%20
http://www.mfa.gov.ba/)
http://www.mfa.gov.ba:80/aktuelnosti/arhiva/Archive.aspx
http://www.mfa.gov.ba:80/aktuelnosti/arhiva/Archive.aspx?template_id=16&pageIndex=1
http://www.mfa.gov.ba:80/aktuelnosti/Diplomatski_forum_2013/Default.aspx
http://www.mfa.gov.ba:80/aktuelnosti/Finansijska_pomoc/archive.aspx
http://www.mfa.gov.ba:80/aktuelnosti/Finansijska_pomoc/archive.aspx?template_id=54&pageIndex=1
http://mfa.gov.ba:80/aktuelnosti/iz_dkp_i_misija//aktuelnosti/iz_dkp_i_misija/default.aspx?template_id=16&pageIndex=1
http://www.mfa.gov.ba:80/aktuelnosti/iz_dkp_i_misija/Archive.aspx
http://www.mfa.gov.ba:80/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=1
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=10
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=11
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=2
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=3
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=4
http://mfa.gov.ba/aktuelnosti/iz_dkp_i_misija/Archive.aspx?template_id=16&pageIndex=5
```

## Video Documentation
🎬 [OSINT Tourism: Bosnia](https://archive.org/details/odint-bosnia-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
