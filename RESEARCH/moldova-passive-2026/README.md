# Moldova — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.md TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 905 |
| Live hosts fingerprinted | 353 |
| DNS/DMARC records analyzed | 56 |
| Historical URLs (GAU) | 20 |

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
100.gov.md
100zile.gov.md
25.army.md
373.gov.md
43859880a3b5403a9352ac35003537d2.mpass.gov.md
9.www.descentralizare.gov.md
aamv.gov.md
aap2.gov.md
aap.gov.md
academy.army.md
acc-congresuldiasporei.gov.md
achizitii.parlament.md
actelocale.gov.md
actpermisiv.gov.md
adfs.parlament.md
adjaj.justice.gov.md
adma.gov.md
adminbac.gov.md
admin.compensatii.gov.md
adminevinieta.gov.md
```
<details><summary>Full list (905 subdomains)</summary>

```
100.gov.md
100zile.gov.md
25.army.md
373.gov.md
43859880a3b5403a9352ac35003537d2.mpass.gov.md
9.www.descentralizare.gov.md
aamv.gov.md
aap2.gov.md
aap.gov.md
academy.army.md
acc-congresuldiasporei.gov.md
achizitii.parlament.md
actelocale.gov.md
actpermisiv.gov.md
adfs.parlament.md
adjaj.justice.gov.md
adma.gov.md
adminbac.gov.md
admin.compensatii.gov.md
adminevinieta.gov.md
admin-particip.gov.md
admin.particip.gov.md
admin.servicii.gov.md
adr-edocs.gov.md
adr.gov.md
aee.gov.md
af.gov.md
agcc.gov.md
age.gov.md
agent.gov.md
agepi.gov.md
agrm.gov.md
aiib.gov.md
aim2.mfa.gov.md
aipa.gov.md
ajutoare.gov.md
alfa-rsa.gov.md
amdm.gov.md
amfa.army.md
amfsa.gov.md
am.gov.md
amp.gov.md
ams.gov.md
anad.gov.md
ana.justice.gov.md
ancd.gov.md
ance.gov.md
anp.gov.md
anranr.gov.md
ansa.gov.md
ansc.sigedia.gov.md
ansp.gov.md
antaeat.anta.gov.md
anta.gov.md
antitrafic.gov.md
antiviolenta.gov.md
apelemoldovei.gov.md
api.cnddcm.gov.md
apievinieta.gov.md
api.mtender.gov.md
api-testsgpe.gov.md
apostila.gov.md
app.gov.md
app.transplant.gov.md
arfc.gov.md
argentina.mfa.gov.md
arhiva.gov.md
ari.gov.md
arij.justice.gov.md
arme.igp.gov.md
army.gov.md
asa.mmpsf.gov.md
asp.gov.md
aspm.mc.gov.md
ast.gov.md
asv.gov.md
atas.gov.md
auction.mtender.gov.md
audientateritoriu.gov.md
austria.mfa.gov.md
autodiscover.parlament.md
autorizatiiauto.gov.md
autorizatiimediu.gov.md
avls.mai.gov.md
azerbaidjan.mfa.gov.md
bacalaureat.gov.md
bac.gov.md
backoffice-eservicii.gov.md
barcelona.mfa.gov.md
baza-auto.gov.md
belarus.mfa.gov.md
belgia.mfa.gov.md
bi-siarsa.gov.md
bizradar.gov.md
bma.gov.md
bma.migrare.gov.md
border.gov.md
brd.gov.md
bridge.invest.gov.md
bri.gov.md
britania.mfa.gov.md
buget.mf.gov.md
bulgaria.mfa.gov.md
caa.gov.md
canada.mfa.gov.md
cancelaria.gov.md
capcs.ms.gov.md
ca.pki.gov.md
carabinier.gov.md
careers.gov.md
cariera.army.md
cariere.gov.md
ca.siaas.gov.md
catalog.aap.gov.md
cazier.gov.md
cbi.gov.md
cbn.mecc.gov.md
cccec.gov.md
ccp.anta.gov.md
cehia.mfa.gov.md
cert.gov.md
certificate-covid.gov.md
cge.sigedia.gov.md
chicago.mfa.gov.md
china.mfa.gov.md
cim.mcloud.gov.md
cim.mediu.gov.md
cio.gov.md
cis.gov.md
civila.gov.md
cloud.gov.md
cna.gov.md
cnam.gov.md
cnapss.gov.md
cnas.gov.md
cncnc.gov.md
cnddcm.gov.md
cnddcm.msmps.gov.md
cnej.gov.md
cnej.justice.gov.md
cnm.justice.gov.md
cnpdc.gov.md
coe.mfa.gov.md
colegiiagricole.madrm.gov.md
compensatii.gov.md
conference.army.md
consecon.gov.md
construct-permits.gov.md
consumator.gov.md
contingente.trade.gov.md
controale.gov.md
controlezfactura.gov.md
covidinfo.gov.md
cpanel.old.parlament.md
cpanel.test.cariere.gov.md
cpcalendars.old.parlament.md
cpcalendars.test.cariere.gov.md
cpcontacts.old.parlament.md
cpcontacts.test.cariere.gov.md
crima-organizata.mai.gov.md
crm.invest.gov.md
crm.primacasa.gov.md
csaa.mf.gov.md
csa.gov.md
csa.madrm.gov.md
csa.mediu.gov.md
csm.justice.gov.md
cspa.gov.md
cspa.mf.gov.md
ctice.gov.md
ctif.gov.md
ct.mai.gov.md
cub.gov.md
customs.gov.md
data.gov.md
dataset.gov.md
date.gov.md
db.agepi.gov.md
_dc-mx.e046e1e3a5e4.army.md
ddp.aap.gov.md
declaratie.mai.gov.md
demografie.cnpd.gov.md
demo.transplant.gov.md
descentralizare.gov.md
devecazier.gov.md
develop.sipc.gov.md
devetender.gov.md
dev-justice.gov.md
dev.mai.gov.md
dev.mediu.gov.md
dip.gov.md
diplome-arhiva-dev.mec.gov.md
diplome-arhiva.mec.gov.md
doc.anta.gov.md
doc.igc.gov.md
doc.mai.gov.md
doc.mei.gov.md
doc.ms.gov.md
doc.parlament.md
docs.aipa.gov.md
docs-mai.gov.md
docs.msmps.gov.md
doc.social.gov.md
documente.anp.gov.md
documente.mediu.gov.md
dopomoga.gov.md
drg.cnam.gov.md
drive.cloud.gov.md
drive.gov.md
dspace.aap.gov.md
dtc.gov.md
e-aipa.gov.md
e-alocatii.mf.gov.md
e-arme.igp.gov.md
eat.anta.gov.md
eca.asp.gov.md
ecabinet.gov.md
ecancelaria.cnas.gov.md
ecazier.gov.md
edge-cluster.gov.md
ednc.gov.md
e-doc.army.md
e-docplat.mf.gov.md
edocs.gov.md
educalitate.gov.md
educatiecivica.parlament.md
edu.gov.md
e-extras.cis.gov.md
ega.gov.md
ehgeom.gov.md
e.inseco.gov.md
elearning.agepi.gov.md
elearning.gov.md
elex.justice.gov.md
elicentiere.gov.md
e-management.justice.gov.md
e-management.madrm.gov.md
e-migrare.gov.md
emoldovata.gov.md
e-permis.border.gov.md
epermis.border.gov.md
e-pescuit.mediu.gov.md
e-petitii.parlament.md
eraportare.spcsb.gov.md
erra.gov.md
esbs.aipa.gov.md
eservice-web.asp.gov.md
e-servicii.agepi.gov.md
eservicii.gov.md
essc.gov.md
essc-pay.gov.md
essc.servicii.gov.md
essc-test.gov.md
essc-testpay.gov.md
estonia.mfa.gov.md
estudii.igc.gov.md
etender.gov.md
eumission.mfa.gov.md
evinieta.gov.md
evisa.gov.md
exchange.parlament.md
exedge.parlament.md
experti.parlament.md
familia.gov.md
finantare.gov.md
fisa-covid.gov.md
fism.gov.md
fito.gov.md
fmis.mf.gov.md
formular-b1.mfa.gov.md
formular-b2.mfa.gov.md
frankfurt.mfa.gov.md
franta.mfa.gov.md
freenas.parlament.md
frontiera.gov.md
fs.army.md
ftp.gov.md
geneva.mfa.gov.md
geodata.gov.md
geologie.gov.md
geoportalinds.gov.md
germania.mfa.gov.md
ggs.gov.md
ghana.mfa.gov.md
gismediu.gov.md
gov.gov.md
grecia.mfa.gov.md
green.gov.md
gu.justice.gov.md
harta-ig.agepi.gov.md
harta-iipt.madrm.gov.md
harta-ipt.mec.gov.md
hosting.epermis.border.gov.md
iap.gov.md
iasi.mfa.gov.md
id.mfa.gov.md
ies.gov.md
if.gov.md
igp.gov.md
igsu.gov.md
ilias.academy.army.md
ilias.army.md
imap.gov.md
imc.ms.gov.md
incluziune.edu.gov.md
india.mfa.gov.md
inds.gov.md
inj.gov.md
inm.gov.md
inovatii.gov.md
inp.gov.md
inseco.gov.md
intern.epermis.border.gov.md
interop.gov.md
intranet.ancd.gov.md
invatam-limba-romana.mec.gov.md
investgagauzia.gov.md
invest.gov.md
ip.army.md
iplatforms.gov.md
ipm.gov.md
ipt.mec.gov.md
irlanda.mfa.gov.md
isc.gov.md
ism.gov.md
is.msmps.gov.md
israel.mfa.gov.md
iss.gov.md
isspa.gov.md
isspnpc.gov.md
istanbul.mfa.gov.md
italia.mfa.gov.md
izmv.gov.md
izmv.madrm.gov.md
japonia.mfa.gov.md
jbmo2021.ance.gov.md
jobmarket.gov.md
justice.gov.md
kazahstan.mfa.gov.md
keycloak.develop.sipc.gov.md
kube.gov.md
letonia.mfa.gov.md
licentiere.gov.md
lituania.mfa.gov.md
locatiivaccinare.gov.md
locuintesociale.gov.md
maccess.gov.md
madrm.gov.md
maia.gov.md
mai.gov.md
mail1.gov.md
mail2.gov.md
mail4.gov.md
mail6.gov.md
mail8.gov.md
mail9.gov.md
mail-adrchisinau.gov.md
mail.agepi.gov.md
mail-atas.gov.md
mail-bma.gov.md
mail-ctif.gov.md
mail.ctif.gov.md
mail.customs.gov.md
mail.gov.md
mail-igm.gov.md
mail-igp.gov.md
mail.justice.gov.md
mail-mai.gov.md
mail.mca.gov.md
mail.mtic.gov.md
mail.old.parlament.md
mail.parlament.md
mail.sp.gov.md
mail.test.cariere.gov.md
mail.uipm.gov.md
mcabinet.gov.md
mca.gov.md
mcdr.gov.md
mc.gov.md
mci.gov.md
mcloud.gov.md
mconnect.gov.md
mded.gov.md
mdelivery.gov.md
mdrc.gov.md
mecc.gov.md
mec.gov.md
mediaserver.border.gov.md
mediere.gov.md
mediu.gov.md
me.gov.md
mei.gov.md
mfa.gov.md
mfa.sites.mfa.gov.md
mf.gov.md
midr.gov.md
migrare.gov.md
milano.mfa.gov.md
minfin.gov.md
minio.develop.sipc.gov.md
misiuni.mfa.gov.md
missions.army.md
mlearn.gov.md
mlis.aipa.gov.md
mm.gov.md
mmpsf.gov.md
mmps.gov.md
mmuncii.gov.md
mnotify.gov.md
moldovaportal.sites.mfa.gov.md
moldsilva.gov.md
monitorizare.gov.md
monitorul.gov.md
mpass.gov.md
mpay.gov.md
mpay-mc.gov.md
mpower.gov.md
ms.gov.md
msign.gov.md
msmps.gov.md
mstyle.gov.md
mtender.gov.md
mts.gov.md
multimedia.parlament.md
mx1.army.md
mx1.gov.md
mx1.justice.gov.md
mx1.mca.gov.md
mx2.gov.md
mx2.justice.gov.md
mx2.mca.gov.md
mx3.gov.md
mx4.gov.md
mx.parlament.md
ncu.gov.md
new.border.gov.md
new.gov.md
new.moldsilva.gov.md
new.parlament.md
news.gov.md
new.statistica.gov.md
nisa.mfa.gov.md
nomenclator.amdm.gov.md
ns1.gov.md
ns1.justice.gov.md
ns1.penitenciar.gov.md
ns2.gov.md
ns2.justice.gov.md
ns3.gov.md
ns.gov.md
odesa.mfa.gov.md
ogpae.gov.md
olanda.mfa.gov.md
old1.parlament.md
old.aaij.justice.gov.md
old.aai.justice.gov.md
old.aap.gov.md
old.amdm.gov.md
old.ansa.gov.md
old.app.gov.md
old.arfc.gov.md
old.asp.gov.md
old.azerbaidjan.mfa.gov.md
old.belarus.mfa.gov.md
old.belgia.mfa.gov.md
old.bma.gov.md
old.border.gov.md
old.britania.mfa.gov.md
old.bulgaria.mfa.gov.md
old.cancelaria.gov.md
old.cnpdc.gov.md
old.consumator.gov.md
old-controale.gov.md
old.ctif.gov.md
old.gov.md
old.madrm.gov.md
old.maia.gov.md
old.mai.gov.md
old.mc.gov.md
old.mcloud.gov.md
old.mded.gov.md
old.mdrc.gov.md
old.mec.gov.md
old.mediu.gov.md
old.mei.gov.md
old.mfa.gov.md
old.mf.gov.md
old.mmpsf.gov.md
old.ms.gov.md
old.msmps.gov.md
old.mtic.gov.md
old.mtid.gov.md
old.mts.gov.md
old.parlament.md
old.rusia.mfa.gov.md
oldservicii.gov.md
old.stisc.gov.md
oldwebpage.aipa.gov.md
ondrl.gov.md
onipm.gov.md
opencontracting.date.gov.md
ordine.mediu.gov.md
owa.army.md
padova.mfa.gov.md
particip.gov.md
pcs.gov.md
penitenciar.gov.md
permits.gov.md
petitii.parlament.md
pim.mai.gov.md
politie.gov.md
polonia.mfa.gov.md
pop.gov.md
pops.mediu.gov.md
portal.gov.md
portal.mai.gov.md
portal.mcloud.gov.md
portugalia.mfa.gov.md
porumbeni.gov.md
postmaster.gov.md
press.army.md
pr.gov.md
primacasa.gov.md
primacasa.mf.gov.md
probatiune.gov.md
profesii.justice.gov.md
prog.amdm.gov.md
programare-apostila.justice.gov.md
programare.asp.gov.md
programaredl.asp.gov.md
programare-vaccinare.gov.md
protectietemporara.gov.md
proxya.parlament.md
proxy.army.md
proxyb.parlament.md
proxyd.parlament.md
psp.gov.md
public.amp.gov.md
public.mtender.gov.md
qatar.mfa.gov.md
rancher.cnddcm.gov.md
rapc.gov.md
rapoarte.siddcm.cnddcm.gov.md
raportare.gov.md
raven.mediu.gov.md
reformaasistenteisociale.gov.md
regatulunit.mfa.gov.md
registru.ansa.gov.md
registru.anta.gov.md
registrulagricol.gov.md
registruparl57q.parlament.md
registruparl.parlament.md
regunic.justice.gov.md
repc.gov.md
restart.gov.md
resurse-educationale.mec.gov.md
retp.gov.md
rezerve.gov.md
romania.mfa.gov.md
rpic.gov.md
rponu.mfa.gov.md
rponuny.mfa.gov.md
rsal.gov.md
rsc.gov.md
rusia.mfa.gov.md
ru.sport.gov.md
rvc19.gov.md
rvv.gov.md
sacramento.mfa.gov.md
sapd.gov.md
satuleuropean.gov.md
scb.ms.gov.md
s.cloud.gov.md
scoliauto.gov.md
scoreboard.mfa.gov.md
scorecard.cancelaria.gov.md
sda.gov.md
secret.gov.md
semantic.gov.md
seq.cnddcm.gov.md
service-desk.gov.md
services.gov.md
servicii.gov.md
sgpe.gov.md
siaas.gov.md
siadr-mdrc.gov.md
siagds.gov.md
sia.im.gov.md
siamd.gov.md
siamecf.gov.md
siarsa.gov.md
siddcm.cnddcm.gov.md
sigedia.gov.md
sigv.gov.md
silva.gov.md
simbase.parlament.md
sip.parlament.md
siradb.gov.md
sirsm.cnam.gov.md
smtp.gov.md
smtp.parlament.md
social.gov.md
spania.mfa.gov.md
spcsb.gov.md
sp.gov.md
sport.gov.md
srsj.justice.gov.md
ss.cnts.gov.md
sscwebarchive.gov.md
stage.parlament.md
stagii.gov.md
staging.actpermisiv.gov.md
staging-api.cnddcm.gov.md
staging.cnddcm.gov.md
staging-css.permits.gov.md
staging.permits.gov.md
staging.profesii.justice.gov.md
staging-seq.cnddcm.gov.md
stare-civila.gov.md
starecivila.gov.md
statistica.gov.md
stisc-cert.gov.md
stisc.gov.md
storage.mtender.gov.md
studyinmd.mec.gov.md
sua.mfa.gov.md
suedia.mfa.gov.md
temp-antaeat.anta.gov.md
temp-eat.anta.gov.md
temporaryprotection.gov.md
tender.gov.md
test1.maia.gov.md
test-admin.particip.gov.md
testamfsa.gov.md
test.asp.gov.md
test.ast.gov.md
test.cariere.gov.md
testccp.anta.gov.md
testetender.gov.md
test-gdej.justice.gov.md
test.interop.gov.md
testmnotify.gov.md
testmpass.gov.md
test.parlament.md
test.particip.gov.md
testregistrulagricol.gov.md
test-sapd.gov.md
testsgpe.gov.md
trade.gov.md
training.interop.gov.md
transplant.gov.md
tratate-intern-mdwww.mfa.gov.md
turcia.mfa.gov.md
turism.gov.md
uae.mfa.gov.md
ucraina.mfa.gov.md
ue.mfa.gov.md
ungaria.mfa.gov.md
vaccinare.gov.md
verifica.anta.gov.md
videoconf.aap.gov.md
videogw.parlament.md
vinieta.gov.md
virtualtur.parlament.md
vizite.parlament.md
vpn.asp.gov.md
vpn.customs.gov.md
vsa.cnam.gov.md
web1.elearning.ansa.gov.md
webcon.parlament.md
webdisk.old.parlament.md
webdisk.test.cariere.gov.md
webinfo.cis.gov.md
webmail.old.parlament.md
webmail.parlament.md
webmail.test.cariere.gov.md
ww2.parlament.md
www.100.gov.md
www.25.army.md
www.373.gov.md
www.aap.gov.md
www.academy.army.md
www.achizitii.parlament.md
www.actelocale.gov.md
www.actpermisiv.gov.md
www.adjaj.justice.gov.md
www.adma.gov.md
www.adminbac.gov.md
www.adminevinieta.gov.md
www.admin.particip.gov.md
www.aee.gov.md
www.af.gov.md
www.agcc.gov.md
www.age.gov.md
www.agent.gov.md
www.agepi.gov.md
www.agrm.gov.md
www.aiib.gov.md
www.aipa.gov.md
www.amdm.gov.md
www.amfsa.gov.md
www.am.gov.md
www.anad.gov.md
www.ana.justice.gov.md
www.ancd.gov.md
www.ance.gov.md
www.anp.gov.md
www.anranr.gov.md
www.ansa.gov.md
www.ansp.gov.md
www.anta.gov.md
www.antitrafic.gov.md
www.antiviolenta.gov.md
www.apievinieta.gov.md
www.apostila.gov.md
www.app.gov.md
www.arfc.gov.md
www.ari.gov.md
www.arij.justice.gov.md
www.arme.igp.gov.md
www.army.md
www.asp.gov.md
www.aspm.mc.gov.md
www.ast.gov.md
www.autorizatiimediu.gov.md
www.avls.mai.gov.md
www.bac.gov.md
www.belarus.mfa.gov.md
www.bma.gov.md
www.bma.migrare.gov.md
www.border.gov.md
www.brd.gov.md
www.bri.gov.md
www.britania.mfa.gov.md
www.bulgaria.mfa.gov.md
www.caa.gov.md
www.canada.mfa.gov.md
www.capcs.ms.gov.md
www.carabinier.gov.md
www.careers.gov.md
www.cariere.gov.md
www.cazier.gov.md
www.cbi.gov.md
www.cbn.mecc.gov.md
www.ccp.anta.gov.md
www.cert.gov.md
www.cio.gov.md
www.cis.gov.md
www.cna.gov.md
www.cnapss.gov.md
www.cnas.gov.md
www.cncnc.gov.md
www.cnddcm.gov.md
www.cnddcm.msmps.gov.md
www.cnej.gov.md
www.cnpdc.gov.md
www.compensatii.gov.md
www.conference.army.md
www.consumator.gov.md
www.covidinfo.gov.md
www.crm.invest.gov.md
www.crm.primacasa.gov.md
www.csa.gov.md
www.cub.gov.md
www.customs.gov.md
www.ddp.aap.gov.md
www.devecazier.gov.md
www.dip.gov.md
www.doc.ms.gov.md
www.dopomoga.gov.md
www.dspace.aap.gov.md
www.dtc.gov.md
www.e-aipa.gov.md
www.e-arme.igp.gov.md
www.eca.asp.gov.md
www.ecazier.gov.md
www.edu.gov.md
www.ega.gov.md
www.elearning.agepi.gov.md
www.e-management.justice.gov.md
www.e-management.madrm.gov.md
www.e-migrare.gov.md
www.emoldovata.gov.md
www.e-pescuit.mediu.gov.md
www.eraportare.spcsb.gov.md
www.e-servicii.agepi.gov.md
www.etender.gov.md
www.evinieta.gov.md
www.evisa.gov.md
www.fism.gov.md
www.geoportalinds.gov.md
www.gov.md
www.grecia.mfa.gov.md
www.gu.justice.gov.md
www.harta-ig.agepi.gov.md
www.if.gov.md
www.igp.gov.md
www.incluziune.edu.gov.md
www.inds.gov.md
www.intranet.ancd.gov.md
www.invest.gov.md
www.ip.army.md
www.iplatforms.gov.md
www.ipm.gov.md
www.isc.gov.md
www.ism.gov.md
www.justice.gov.md
www.licentiere.gov.md
www.madrm.gov.md
www.maeie.gov.md
www.maia.gov.md
www.mai.gov.md
www.mca.gov.md
www.mc.gov.md
www.mecc.gov.md
www.mec.gov.md
www.mediere.gov.md
www.mediu.gov.md
www.me.gov.md
www.mei.gov.md
www.mfa.gov.md
www.mf.gov.md
www.midr.gov.md
www.migrare.gov.md
www.misiuni.mfa.gov.md
www.mmpsf.gov.md
www.mmuncii.gov.md
www.monitorizare.gov.md
www.mpass.gov.md
www.ms.gov.md
www.msign.gov.md
www.msmps.gov.md
www.mts.gov.md
www.multimedia.parlament.md
www.nisa.mfa.gov.md
www.ogpae.gov.md
www.old1.parlament.md
www.old.aap.gov.md
www.old.ansa.gov.md
www.old.asp.gov.md
www.old.cancelaria.gov.md
www.old.cnpdc.gov.md
www.old.gov.md
www.old.mai.gov.md
www.old.mcloud.gov.md
www.old.mdrc.gov.md
www.old.mediu.gov.md
www.old.mf.gov.md
www.old.msmps.gov.md
www.old.mtic.gov.md
www.old.mtid.gov.md
www.old.mts.gov.md
www.old.parlament.md
www.ondrl.gov.md
www.padova.mfa.gov.md
www.parlament.md
www.particip.gov.md
www.penitenciar.gov.md
www.permits.gov.md
www.petitii.parlament.md
www.portugalia.mfa.gov.md
www.press.army.md
www.pr.gov.md
www.primacasa.mf.gov.md
www.programare-apostila.justice.gov.md
www.raportare.gov.md
www.registru.anta.gov.md
www.repc.gov.md
www.resurse-educationale.mec.gov.md
www.retp.gov.md
www.rezerve.gov.md
www.rvv.gov.md
www.scb.ms.gov.md
www.scoliauto.gov.md
www.services.gov.md
www.servicii.gov.md
www.sgpe.gov.md
www.siadr-mdrc.gov.md
www.siamd.gov.md
www.sigv.gov.md
www.silva.gov.md
www.sip.parlament.md
www.social.gov.md
www.sp.gov.md
www.starecivila.gov.md
www.statistica.gov.md
www.test.cariere.gov.md
www.testccp.anta.gov.md
www.test.parlament.md
www.testsgpe.gov.md
www.transplant.gov.md
www.turism.gov.md
www.vaccinare.gov.md
www.videoconf.aap.gov.md
www.vinieta.gov.md
www.vizite.parlament.md
www.vpn.asp.gov.md
www.webcon.parlament.md
zc7.gov.md
zg2c.gov.md
zmf.gov.md
zmj.gov.md
zpg.gov.md
zsec.gov.md
ztst.gov.md
```
</details>

### Live Host Fingerprinting
```
https://100zile.gov.md [[1;33m503[0m] [[36mÎn Mentenanță - I.P. STISC[0m] [nginx] [[35mBootstrap,Google Hosted Libraries,Nginx,jQuery:1.12.4[0m]
https://43859880a3b5403a9352ac35003537d2.mpass.gov.md [[31m404[0m] [[36m404 Not Found[0m] [nginx] [[35mNginx[0m]
https://100.gov.md [[33m303[0m] [nginx] [[35mNginx[0m]
https://373.gov.md [[32m200[0m] [[36m373.gov.md[0m] [openresty] [[35mGoogle Analytics,HSTS,Nginx,OpenResty[0m]
https://aap.gov.md [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mNginx,Plesk[0m]
https://actelocale.gov.md [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mHSTS,Nginx[0m]
https://actpermisiv.gov.md [[32m200[0m] [[36mDotGov Server[0m] [nginx] [[35mHSTS,Microsoft ASP.NET,Nginx[0m]
https://adjaj.justice.gov.md [[31m403[0m] [nginx] [[35mNginx[0m]
https://adfs.parlament.md [[31m404[0m] [[36mNot Found[0m] [Microsoft-HTTPAPI/2.0] [[35mMicrosoft HTTPAPI:2.0[0m]
https://aee.gov.md [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mNginx,Plesk[0m]
https://adma.gov.md [[32m200[0m] [[36mWeb Server's Default Page[0m] [nginx] [[35mNginx,Plesk[0m]
https://admin-particip.gov.md [[33m302[0m] [[36mRedirecting to https://admin-particip.gov.md/login[0m] [nginx/1.14.0 (Ubuntu)] [[35mHSTS,Nginx:1.14.0,Ubuntu[0m]
https://achizitii.parlament.md [[32m200[0m] [[36mPortal Informativ – Achizitii Publice Parlamentul Republicii Moldova[0m] [nginx] [[35mMySQL,Nginx,PHP:8.3.30,WPML:4.5.12,WordPress Block Editor,WordPress:6.9.1,imagesLoaded:5.0.0,jQuery,jQuery Migrate:3.4.1[0m]
https://academy.army.md [] [[36mDatabase Error[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,HSTS,HTTP/3,PHP:5.4.37[0m]
https://adminbac.gov.md [[31m404[0m] [[36m404 Not Found[0m] [nginx] [[35mHSTS,Nginx[0m]
https://admin.compensatii.gov.md [[32m200[0m] [[36mAdmin[0m] [nginx] [[35mGoogle Tag Manager,HSTS,Nginx[0m]
https://admin.particip.gov.md [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx/1.14.0 (Ubuntu)] [[35mNginx:1.14.0,Ubuntu[0m]
https://admin.servicii.gov.md [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mNginx[0m]
https://adr-edocs.gov.md [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mNginx[0m]
https://age.gov.md [[33m301[0m] [nginx] [[35mDrupal,HSTS,Nginx,PHP:7.4.33[0m]
https://amp.gov.md [[33m302[0m] [[36m302 Found[0m] [nginx] [[35mNginx[0m]
https://ana.justice.gov.md [[31m403[0m] [nginx] [[35mNginx[0m]
https://amfsa.gov.md [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mHSTS,Nginx[0m]
https://amdm.gov.md [[33m302[0m] [[36mRedirecting to https://amdm.gov.md/ro[0m] [nginx] [[35mLaravel,Nginx,PHP:7.3.33[0m]
https://agcc.gov.md [[32m200[0m] [[36mAgenția Geodezie, Cartografie și Cadastru[0m] [nginx] [[35mDrupal:7,Google Analytics,Nginx,PHP:7.4.33,jQuery CDN,jQuery:1.12.4[0m]
https://anranr.gov.md [[33m301[0m] [[36mRedirecting to https://anranr.gov.md/ro[0m] [nginx] [[35mDrupal,Nginx,PHP:8.3.30[0m]
https://agrm.gov.md [[33m303[0m] [nginx] [[35mNginx,PHP:5.6.40[0m]
https://agepi.gov.md [[32m200[0m] [[36mAGENȚIA DE STAT PENTRU PROPRIETATEA INTELECTUALĂ | MINISTERUL JUSTIȚIEI AL REPUBLICII MOLDOVA[0m] [nginx] [[35mDrupal,Google Analytics,Lightbox,Nginx,PHP:5.6.40,jQuery CDN,jQuery UI:1.10.2,jQuery:1.7.2[0m]
https://anp.gov.md [[32m200[0m] [nginx] [[35mNginx,PHP:8.0.30[0m]
https://alfa-rsa.gov.md [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mHSTS,Nginx[0m]
```

### DNS / DMARC Analysis
```
--- gov.md ---
MX: 20 mx2.gov.md.
10 mx1.gov.md.
SPF: "v=spf1 redirect=_spf.stisc.md"
DMARC: "v=DMARC1; p=reject; sp=reject; pct=100; ruf=mailto:dmarc@stisc.gov.md; rua=mailto:dmarc@stisc.gov.md; adkim=r; aspf=r; fo=1"

--- parlament.md ---
MX: 1 smtp.parlament.md.
SPF: "v=spf1 ip4:185.33.106.136 ip4:89.32.228.18 -all"
DMARC: "v=DMARC1; p=reject; sp=reject; pct=100; adkim=r; aspf=r; fo=1"

--- mf.gov.md ---
MX: 20 mx2.gov.md.
10 mx1.gov.md.
SPF: "v=spf1 redirect=_spf.stisc.md"
DMARC: 

--- army.md ---
MX: 10 _dc-mx.e046e1e3a5e4.army.md.
SPF: "v=spf1 +a +mx ~all"
DMARC: "v=DMARC1; p=quarantine; rua=mailto:a2d7054dbbb04e5f97a6bf3f06a7e660@dmarc-reports.cloudflare.net,mailto:ancloudns@army.md"

--- edu.gov.md ---
MX: 
SPF: 
DMARC: 

--- ms.gov.md ---
MX: 20 mx2.gov.md.
10 mx1.gov.md.
SPF: "v=spf1 redirect=_spf.stisc.md"
DMARC: 

--- justice.gov.md ---
MX: 10 mx1.justice.gov.md.
20 mx2.justice.gov.md.
SPF: "v=spf1 redirect=_spf.stisc.md"
DMARC: 

--- mai.gov.md ---
```

### Historical URLs (Sample)
```
http://csn@parlament.md/LinkClick.aspx?fileticket=b3OKiVCqDRw%3d&tabid=37&mid=553&language=en-US
http://gov.md:80/albumpiro.php?
http://gov.md:80/albumpiro.php?l=ru&idc=533
http://gov.md:80/category.php?l=ru&idc=455
http://gov.md:80/content/ro/LEGEA_buget2007.files/filelist.xml
http://gov.md:80/doc.php?
http://gov.md:80/events.php?
http://gov.md:80/feedbacktxt.php?l=ru&idc=433
http://gov.md:80/feedbacktxt.php?l=ru&idc=434
http://gov.md:80/feedbacktxt.php?l=ru&idc=437
http://gov.md:80/feedbacktxt.php?l=ru&idc=439
http://gov.md:80/feedbacktxt.php?l=ru&idc=440
http://gov.md:80/homepage.php?
http://gov.md:80/homepage.php?l=en
http://gov.md:80/homepage.php?l=ro+
http://gov.md:80/homepage.php?l=ro%20
http://gov.md:80/homepage.php?l=ru
http://gov.md:80/index.php&
http://gov.md:80/index.php?
http://gov.md:80/index.php?a=apc_new&lng=en
```

## Video Documentation
🎬 [OSINT Tourism: Moldova](https://archive.org/details/odint-moldova-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
