# Georgia — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.ge TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 920 |
| Live hosts fingerprinted | 427 |
| DNS/DMARC records analyzed | 46 |
| Historical URLs (GAU) | 567414 |

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
student.hrajara.gov.ge
www.tetritskaro.gov.ge
www.baghdati.gov.ge
mail.abkhazia.gov.ge
www.mail.probation.gov.ge
jus-lyncfe01.justice.gov.ge
www.qsb.gov.ge
winnie.tskaltubo.gov.ge
webdisk.events.gov.ge
webdisk.tsageri.gov.ge
mmr.reestri.gov.ge
tbilisi.gov.ge
autodiscover.khashuri.gov.ge
mail.khashuri.gov.ge
nam.archive.gov.ge
digital.archive.gov.ge
webdisk.apa.gov.ge
tskaltubo.gov.ge
www.saras.gov.ge
nsc.gov.ge
```
<details><summary>Full list (920 subdomains)</summary>

```
student.hrajara.gov.ge
www.tetritskaro.gov.ge
www.baghdati.gov.ge
mail.abkhazia.gov.ge
www.mail.probation.gov.ge
jus-lyncfe01.justice.gov.ge
www.qsb.gov.ge
winnie.tskaltubo.gov.ge
webdisk.events.gov.ge
webdisk.tsageri.gov.ge
mmr.reestri.gov.ge
tbilisi.gov.ge
autodiscover.khashuri.gov.ge
mail.khashuri.gov.ge
nam.archive.gov.ge
digital.archive.gov.ge
webdisk.apa.gov.ge
tskaltubo.gov.ge
www.saras.gov.ge
nsc.gov.ge
atlas.mepa.gov.ge
www.kaspi.gov.ge
www.gecommission.gov.ge
autodiscover.archives-ajara.gov.ge
cpanel.mea.gov.ge
www.gdi.gov.ge
ichange.gov.ge
elearning.dea.gov.ge
www.khashuri.gov.ge
cpanel.baghdati.gov.ge
www.ex2010.mta.gov.ge
webmail.mes.gov.ge
mail.gardabani.gov.ge
fb.government.gov.ge
ftp.nplg.gov.ge
webdisk.kaspi.gov.ge
mail.delta.gov.ge
reestri.gov.ge
archival-services.gov.ge
mail.apa.gov.ge
www.ecnoba.mrdi.gov.ge
autodiscover.dea.gov.ge
www.scara.gov.ge
mail.mestia.gov.ge
webdisk.dusheti.gov.ge
autodiscover.fablab.gov.ge
autodiscover.mes.gov.ge
ex-cas.justice.gov.ge
golbet.ge.hrajara.gov.ge
www.news.old.abkhazia.gov.ge
oz.gov.ge
s-j.gov.ge
www.mail.archives-ajara.gov.ge
webdisk.tskaltubo.gov.ge
app.stajireba.gov.ge
mail2.moh.gov.ge
autodiscover.scara.gov.ge
mail.tsageri.gov.ge
mail.hrajara.gov.ge
webdisk.marneuli.gov.ge
webdisk.gardabani.gov.ge
webdisk.keda.gov.ge
keda.gov.ge
webmail.mestia.gov.ge
www.gov.ge
autodiscover.mfa.gov.ge
webmail.qsb.gov.ge
autodiscover.dmanisi.gov.ge
dmanisi.gov.ge
autodiscover.baghdati.gov.ge
webdisk.old.abkhazia.gov.ge
webmail.archives-ajara.gov.ge
cpanel.qsb.gov.ge
webdisk.boulevard.gov.ge
cpanel.marneuli.gov.ge
mail.dmanisi.gov.ge
webmail.soa.gov.ge
mail.medeamuseum.gov.ge
www.oni.gov.ge
test-api.bfd.gov.ge
diaspora.gov.ge
iec.gov.ge
www.stream.mrg.gov.ge
www.medeamuseum.gov.ge
www.megzuri.gov.ge
test.kaspi.gov.ge
www.coworking.gov.ge
ssg.gov.ge
www.123.hrajara.gov.ge
1.marneuli.gov.ge
www.marneuli.gov.ge
cpanel.apa.gov.ge
acc1.mfa.gov.ge
webdisk.coworking.gov.ge
webmail.gdi.gov.ge
www.zugdidi.gov.ge
online.moc.gov.ge
lentekhi.gov.ge
www.my.gov.ge
www.mkhileba.gov.ge
tbsakrebulo.gov.ge
mail.mta.gov.ge
webmail.gori.gov.ge
webmail.hrajara.gov.ge
gardabani.gov.ge
indiapeople.hrajara.gov.ge
moh.gov.ge
www.sa.gov.ge
dialin.cloud.gov.ge
stream.mrg.gov.ge
mail.oz.gov.ge
nbg.gov.ge
dotr.gov.ge
borjomi.gov.ge
navigation.napr.gov.ge
ehealth.moh.gov.ge
www.gsc.gov.ge
www.mestia.gov.ge
www.golbet.ge.hrajara.gov.ge
www.soa.gov.ge
mail.lentekhi.gov.ge
cpanel.mestia.gov.ge
www.old.abkhazia.gov.ge
georoad.gov.ge
coworking.gov.ge
autodiscover.marneuli.gov.ge
webdisk.qsb.gov.ge
cpanel.scara.gov.ge
pwd.hrajara.gov.ge
mail.old.abkhazia.gov.ge
www.eugeo-readmission.gov.ge
www.internet.gov.ge
www.trainer.hrajara.gov.ge
apps.municipal.gov.ge
mail.ozurgeti.gov.ge
autodiscover.mrdi.gov.ge
www.mail.delta.gov.ge
webmail.tsalka.gov.ge
autodiscover.soa.gov.ge
old.abkhazia.gov.ge
webdisk.gdi.gov.ge
davlogs.archive.gov.ge
nea.gov.ge
mail.tskaltubo.gov.ge
mail.events.gov.ge
mx2.justice.gov.ge
mail.ssps.gov.ge
forum.hrajara.gov.ge
www.mail.tsalka.gov.ge
autodiscover.zestafoni.gov.ge
skype-sip.archives.gov.ge
mail2.gardabani.gov.ge
www.dmanisi.gov.ge
webdisk.kids.gov.ge
pifc.gov.ge
mail.dea.gov.ge
cpanel.gita.gov.ge
autodiscover.moh.gov.ge
greg.reestri.gov.ge
www.hrajara.gov.ge
e.gov.ge
email.mfa.gov.ge
mail.boulevard.gov.ge
www.aspindza.gov.ge
webmail.gardabani.gov.ge
tkibuli.gov.ge
sda.gov.ge
skype-webconf.archives.gov.ge
khashuri.gov.ge
marneuli.gov.ge
www.bolnisi.gov.ge
cpanel.kids.gov.ge
www.rustavi.gov.ge
www.legacy.nea.gov.ge
www.gori.mun.gov.ge
admin.bsa.gov.ge
autodiscover.geo.gov.ge
mail.kids.gov.ge
rustavi.gov.ge
webmail.fablab.gov.ge
jus-lyncedge.justice.gov.ge
webmail.probation.gov.ge
mail.soa.gov.ge
webdisk.gori.mun.gov.ge
webdisk.zugdidi.gov.ge
mail.technology.gov.ge
www.keda.keda.gov.ge
akhaltsikhe.gov.ge
abkhazia.gov.ge
accreditation.mfa.gov.ge
mx5.cloud.gov.ge
msy.gov.ge
api.my.gov.ge
mail.kvemokartli.gov.ge
webmail.kvemokartli.gov.ge
events.gita.gov.ge
www.test.kaspi.gov.ge
webconf.justice.gov.ge
test.my.gov.ge
cpanel.internet.gov.ge
shop.archives.gov.ge
webmail.zestafoni.gov.ge
webdisk.terjola.gov.ge
registration.test.my.gov.ge
naprweb.reestri.gov.ge
cpanel.boulevard.gov.ge
thebambo.hrajara.gov.ge
5g.gov.ge
mail.emsc.gov.ge
www.ozurgeti.gov.ge
mail.gita.gov.ge
mail.archives.gov.ge
78044_78044_798397_smr.gov.ge
probation.probation.gov.ge
cybercube.cert.gov.ge
www.dusheti.gov.ge
webmail.tsageri.gov.ge
www.hebbe.tsageri.gov.ge
internet.gov.ge
autodiscover.mestia.gov.ge
terjola.gov.ge
webdisk.garemo-adjara.gov.ge
www.chiatura.gov.ge
barracuda.mfa.gov.ge
archive.gov.ge
www.kids.gov.ge
exchange.expertiza.gov.ge
zugdidicity.gov.ge
www.moneymuseum.nbg.gov.ge
webdisk.khashuri.gov.ge
autodiscover.boulevard.gov.ge
mail.tsalka.gov.ge
autodiscover.5g.gov.ge
webmail.idea.gov.ge
www.evisa.gov.ge
www.fb.government.gov.ge
av.justice.gov.ge
webmail.khashuri.gov.ge
autodiscover.kaspi.gov.ge
landregistration.gov.ge
cpanel.chiatura.gov.ge
mail.chiatura.gov.ge
www.abkhazia.gov.ge
mrdi.gov.ge
mail.security.gov.ge
78044_78044_487335_moh.gov.ge
gmdss.mta.gov.ge
autodiscover.gori.gov.ge
webmail.boulevard.gov.ge
tsageri.gov.ge
webmail.zugdidicity.gov.ge
publish.matsne.gov.ge
lync.cloud.gov.ge
webmail.terjola.gov.ge
autodiscover.gita.gov.ge
join.cloud.gov.ge
cpanel.gori.gov.ge
hebbe.tsageri.gov.ge
medeamuseum.gov.ge
webmail.5g.gov.ge
webmail.garemo-adjara.gov.ge
eugeo-readmission.gov.ge
admin.test.ems.dea.gov.ge
autodiscover.terjola.gov.ge
www.thebambo.hrajara.gov.ge
api.bfd.gov.ge
webdisk.abkhazia.gov.ge
zugdidi.gov.ge
app.nplg.gov.ge
cpanel.diaspora.gov.ge
webdisk.hrajara.gov.ge
retraining1.hrajara.gov.ge
www.rionimaps.nea.gov.ge
www.lentekhi.gov.ge
www.mail.eco.gov.ge
cpanel.zugdidicity.gov.ge
adfs.mes.gov.ge
webdisk.probation.gov.ge
www.nea.gov.ge
mod.gov.ge
grants.gov.ge
www.zugdidicity.gov.ge
complaint.napr.gov.ge
ms.emoe.gov.ge
tetritskaro.gov.ge
baghdati.gov.ge
autodiscover.old.abkhazia.gov.ge
test.marneuli.gov.ge
admin.bfd.gov.ge
webmail.bolnisi.gov.ge
www.tkibuli.gov.ge
old.tskaltubo.gov.ge
megzuri.gov.ge
webmail.ozurgeti.gov.ge
www.mea.gov.ge
economy.napr.gov.ge
www.mail.mta.gov.ge
mail.nsc.gov.ge
scara.gov.ge
www.retraining.hrajara.gov.ge
www.gis.gov.ge
cdn.trainings.gov.ge
cpanel.zugdidi.gov.ge
webdisk.dmanisi.gov.ge
cpanel.rustavi.gov.ge
bti.reestri.gov.ge
upload.matsne.gov.ge
ex-ch01.justice.gov.ge
webmail.dmanisi.gov.ge
webdisk.akhaltsikhe.gov.ge
fba.mfa.gov.ge
mail.georoad.gov.ge
ssa.gov.ge
www.imereti.gov.ge
www.geoconsul.gov.ge
gori.mun.gov.ge
republic.archival-services.gov.ge
mail.marneuli.gov.ge
news.old.abkhazia.gov.ge
videos.mfa.gov.ge
autodiscover.zugdidicity.gov.ge
my.gov.ge
mail.gdi.gov.ge
kids.gov.ge
mail.akhaltsikhe.gov.ge
www.akhaltsikhe.gov.ge
cpanel.lentekhi.gov.ge
oldnaprweb.reestri.gov.ge
app.iec.gov.ge
trainings.hrajara.gov.ge
davlogsrepository.archive.gov.ge
www.tskaltubo.gov.ge
www.training.hrajara.gov.ge
davshop.archives.gov.ge
mestia.gov.ge
cpanel.khashuri.gov.ge
digiflow.archive.gov.ge
garemo-adjara.gov.ge
mail.eco.gov.ge
www.events.gov.ge
autodiscover.cloud.gov.ge
email.justice.gov.ge
webdisk.mestia.gov.ge
mail.tkibuli.gov.ge
www.terjola.gov.ge
cpanel.garemo-adjara.gov.ge
www.idea.gov.ge
dspace.nplg.gov.ge
www.auto.sa.gov.ge
www.egmc.gov.ge
autodiscover.ssps.gov.ge
news.abkhazia.gov.ge
nplg.gov.ge
naprlmr.reestri.gov.ge
www.pwd.hrajara.gov.ge
webdisk.tsalka.gov.ge
soa.gov.ge
www.georoad.gov.ge
declaration.gov.ge
mail.mrdi.gov.ge
mail.coworking.gov.ge
cpanel.events.gov.ge
webmail.apa.gov.ge
webexrproxy.napr.gov.ge
notary.reestri.gov.ge
sa.gov.ge
webconf.cloud.gov.ge
webmail.tkibuli.gov.ge
www.matsne.gov.ge
www.myprofession.gov.ge
cpanel.gdi.gov.ge
78044_78044_300278_mrdi.gov.ge
davais.archive.gov.ge
chiatura.gov.ge
checkingeorgia.gov.ge
mes.gov.ge
drive.cloud.gov.ge
cat.archive.gov.ge
kakheti.gov.ge
maradimaradi.hrajara.gov.ge
webmail.zugdidi.gov.ge
server.mod.gov.ge
mail.probation.gov.ge
samtredia.gov.ge
gecommission.gov.ge
webmail.bfd.gov.ge
webmail.tskaltubo.gov.ge
www.cagareli.hrajara.gov.ge
chat.declaration.gov.ge
www.old.tskaltubo.gov.ge
4phouse.tsageri.gov.ge
mail.gov.ge
www.fondi.gov.ge
webmail.scara.gov.ge
eid.dea.gov.ge
www.tsageri.gov.ge
oni.gov.ge
kvemokartli.gov.ge
data.mepa.gov.ge
www.trainings.gov.ge
vpn.cec.gov.ge
webdisk.idea.gov.ge
edocument.cec.gov.ge
handi.hrajara.gov.ge
edu.hrajara.gov.ge
webmail.marneuli.gov.ge
davrepository.archive.gov.ge
support.mrg.gov.ge
www.news.abkhazia.gov.ge
www.mail.mrdi.gov.ge
cagareli.hrajara.gov.ge
gdi.gov.ge
ex2010.mta.gov.ge
78044_78044_380617_.mes.gov.ge
test.psh.dea.gov.ge
autodiscover.samtredia.gov.ge
autodiscover.chiatura.gov.ge
www.hr.gov.ge
archives-ajara.gov.ge
autodiscover.events.gov.ge
files.archive.gov.ge
mail.fablab.gov.ge
sip.cloud.gov.ge
matsne.gov.ge
webmail.gsc.gov.ge
dusheti.gov.ge
www.app.stajireba.gov.ge
www.probation.probation.gov.ge
cpanel.old.abkhazia.gov.ge
geoconsul.gov.ge
republic.archive.gov.ge
webmail.mea.gov.ge
cpanel.bolnisi.gov.ge
eims.eiec.gov.ge
www.gori.gov.ge
autodiscover.keda.gov.ge
autodiscover.idea.gov.ge
exchange01.mrdi.gov.ge
mail.water.gov.ge
meet.cloud.gov.ge
www.mes.gov.ge
www.maradimaradi.hrajara.gov.ge
bsa.gov.ge
www.archives-ajara.gov.ge
mail.idea.gov.ge
events.gov.ge
nbof.reestri.gov.ge
www.boulevard.gov.ge
hrajara.gov.ge
rionimaps.nea.gov.ge
legacy.nea.gov.ge
davshoplogs.archives.gov.ge
nom.reestri.gov.ge
webmail.diaspora.gov.ge
trainings.gov.ge
www.elearning.dea.gov.ge
boulevard.gov.ge
training.hrajara.gov.ge
sr.archive.gov.ge
davlogsais.archive.gov.ge
cpanel.medeamuseum.gov.ge
dms.archive.gov.ge
access.mrg.gov.ge
www.tsalka.gov.ge
wifi.mrg.gov.ge
www.garemo-adjara.gov.ge
mepa.gov.ge
mail.megzuri.gov.ge
autodiscover.abkhazia.gov.ge
cpanel.probation.gov.ge
www.student.hrajara.gov.ge
cpanel.5g.gov.ge
cpanel.tsageri.gov.ge
dea.gov.ge
www.nbg.gov.ge
mail.cloud.gov.ge
www.4phouse.tsageri.gov.ge
webmail.events.gov.ge
chat.eugeo-readmission.gov.ge
addreg.reestri.gov.ge
mail.zugdidi.gov.ge
mms.gov.ge
cloud.delta.gov.ge
webdisk.internet.gov.ge
trainer.hrajara.gov.ge
mail.zestafoni.gov.ge
mail.oni.gov.ge
webdisk.megzuri.gov.ge
skype.delta.gov.ge
av.cloud.gov.ge
mail.rustavi.gov.ge
gis.gov.ge
mail.terjola.gov.ge
webmail.gita.gov.ge
emoe.gov.ge
www.apa.gov.ge
www.edu.hrajara.gov.ge
mail.mia.gov.ge
webdisk.mea.gov.ge
crp.napr.gov.ge
enreg.reestri.gov.ge
www.tenders.procurement.gov.ge
cpanel.tsalka.gov.ge
app.culturalroutes.gov.ge
webmail.abkhazia.gov.ge
ozurgeti.gov.ge
vpn.delta.gov.ge
visit-notary.reestri.gov.ge
www.dea.gov.ge
webdisk.gori.gov.ge
www.keda.gov.ge
webmail.megzuri.gov.ge
www.fablab.gov.ge
bs.napr.gov.ge
bfd.gov.ge
webdisk.scara.gov.ge
nam-geofund.archival-services.gov.ge
sr.archives-ajara.gov.ge
www.diaspora.gov.ge
www.gardabani.gov.ge
mail.internet.gov.ge
stajireba.gov.ge
tsalka.gov.ge
www.mail.marneuli.gov.ge
www.satesto2.marneuli.gov.ge
webdisk.rustavi.gov.ge
webdisk.5g.gov.ge
webmail.dusheti.gov.ge
www.mail.technology.gov.ge
napr.gov.ge
www.trainings.hrajara.gov.ge
mail.keda.gov.ge
cpanel.akhaltsikhe.gov.ge
imereti.gov.ge
evisa.gov.ge
webex.napr.gov.ge
webdisk.kvemokartli.gov.ge
cpanel.keda.gov.ge
cpanel.gori.mun.gov.ge
apa.gov.ge
chiragdani.tskaltubo.gov.ge
mail.diaspora.gov.ge
www.archive.gov.ge
www.zestafoni.gov.ge
webdisk.chiatura.gov.ge
test-admin.bfd.gov.ge
fablab.gov.ge
auto.sa.gov.ge
portal.cloud.gov.ge
dav.archive.gov.ge
cpanel.gsc.gov.ge
testapi.my.gov.ge
img.bsa.gov.ge
cpanel.samtredia.gov.ge
hr.gov.ge
www.nplg.gov.ge
tskaltubo.tskaltubo.gov.ge
mx1.mfa.gov.ge
mail.qsb.gov.ge
incidents.dea.gov.ge
gita.gov.ge
cpanel.oz.gov.ge
webmail.coworking.gov.ge
autodiscover.zugdidi.gov.ge
autodiscover.gardabani.gov.ge
www.kvemokartli.gov.ge
autodiscover.medeamuseum.gov.ge
webdisk.medeamuseum.gov.ge
www.samtredia.gov.ge
www.test.marneuli.gov.ge
mail.dusheti.gov.ge
cpanel.bfd.gov.ge
smr.gov.ge
mail.kaspi.gov.ge
mail.gori.mun.gov.ge
zestafoni.gov.ge
autodiscover.tkibuli.gov.ge
mea.gov.ge
join.justice.gov.ge
mail.5g.gov.ge
www.5g.gov.ge
cpanel.idea.gov.ge
webdisk.bfd.gov.ge
autodiscover.ozurgeti.gov.ge
cpanel.ozurgeti.gov.ge
saras.gov.ge
bolnisi.gov.ge
webdisk.soa.gov.ge
webdisk.zestafoni.gov.ge
startupfriendly.gov.ge
mail.imereti.gov.ge
webdisk.lentekhi.gov.ge
mail.mes.gov.ge
www.stajireba.gov.ge
78044_78044_986293_mfa.gov.ge
mail.archive.gov.ge
webmail.akhaltsikhe.gov.ge
cpanel.dusheti.gov.ge
webdisk.gsc.gov.ge
ais-dashboard.archive.gov.ge
www.kakheti.gov.ge
webmail.chiatura.gov.ge
mail.reestri.gov.ge
gsc.gov.ge
webmail.kaspi.gov.ge
sp.gov.ge
confluence.es.gov.ge
webmail.old.abkhazia.gov.ge
cpanel.kaspi.gov.ge
kaspi.gov.ge
retraining.hrajara.gov.ge
123.hrajara.gov.ge
csbd.gov.ge
www.archival-services.gov.ge
cpanel.zestafoni.gov.ge
webdisk.ozurgeti.gov.ge
autodiscover.bolnisi.gov.ge
autodiscover.apa.gov.ge
fms.gov.ge
nbeibank.reestri.gov.ge
lync.justice.gov.ge
webmail.keda.gov.ge
www.pifc.gov.ge
autodiscover.megzuri.gov.ge
autodiscover.dusheti.gov.ge
www.handi.hrajara.gov.ge
catalog.nplg.gov.ge
www.forum.hrajara.gov.ge
webmail.baghdati.gov.ge
webmail.oz.gov.ge
www.oz.gov.ge
webdisk.archives-ajara.gov.ge
autodiscover.coworking.gov.ge
mail.moh.gov.ge
public.reestri.gov.ge
tbilisi.control.mrg.gov.ge
webmail.gori.mun.gov.ge
cpanel.megzuri.gov.ge
webdisk.gita.gov.ge
tbilisi-ebrd.gov.ge
doc-eco.archive.gov.ge
test.bfd.gov.ge
cpanel.archives-ajara.gov.ge
des.gov.ge
www.borjomi.gov.ge
www.1.marneuli.gov.ge
webdisk.bolnisi.gov.ge
mail.kakheti.gov.ge
www.mail.georoad.gov.ge
mkhileba.gov.ge
moa.gov.ge
mail.scara.gov.ge
probation.gov.ge
webexadmin.napr.gov.ge
debt.reestri.gov.ge
tenders.procurement.gov.ge
zip.justice.gov.ge
geo.gov.ge
aspindza.gov.ge
webmail.kids.gov.ge
satesto2.marneuli.gov.ge
test-geoserver.napr.gov.ge
mail.gori.gov.ge
mail.bolnisi.gov.ge
mail.nea.gov.ge
www.gita.gov.ge
cloud.gov.ge
moodle.cloud.gov.ge
repository.archive.gov.ge
webmail.lentekhi.gov.ge
cpanel.coworking.gov.ge
www.dotr.gov.ge
78078_78078_693722_mepa.gov.ge
ais.archive.gov.ge
webmail.internet.gov.ge
cpanel.tkibuli.gov.ge
webdisk.samtredia.gov.ge
cpanel.terjola.gov.ge
info.mrdi.gov.ge
idea.gov.ge
webmail.rustavi.gov.ge
srbo.archive.gov.ge
www.retraining1.hrajara.gov.ge
webmail.samtredia.gov.ge
webdisk.oz.gov.ge
cpanel.tskaltubo.gov.ge
www.mail2.moh.gov.ge
smtp-10.cloud.gov.ge
mail2.geo.gov.ge
cpanel.kvemokartli.gov.ge
cec.gov.ge
cpanel.fablab.gov.ge
www.house.gov.ge
autodiscover.tsalka.gov.ge
api.sp.gov.ge
webdisk.fablab.gov.ge
mobileapi.napr.gov.ge
intra.napr.gov.ge
dns.cloud.gov.ge
house.gov.ge
ex-ch02.justice.gov.ge
webdisk.diaspora.gov.ge
gori.gov.ge
kutaisi.gov.ge
mail.archives-ajara.gov.ge
autodiscover.delta.gov.ge
webdisk.zugdidicity.gov.ge
lyncweb.cloud.gov.ge
belgium.mfa.gov.ge
cpanel.hrajara.gov.ge
cpanel.gardabani.gov.ge
webmail.medeamuseum.gov.ge
mail.garemo-adjara.gov.ge
ecnoba.mrdi.gov.ge
mia.gov.ge
webexuser.napr.gov.ge
www.probation.gov.ge
cpanel.dmanisi.gov.ge
webdisk.baghdati.gov.ge
eredvi.gov.ge
www.indiapeople.hrajara.gov.ge
www.bfd.gov.ge
www.declaration.gov.ge
mcat.nplg.gov.ge
78078_78078_594427_mes.gov.ge
mail.gsc.gov.ge
president.gov.ge
webexproxy.napr.gov.ge
mail.zugdidicity.gov.ge
municipal.gov.ge
egmc.gov.ge
sts.mes.gov.ge
cpanel.soa.gov.ge
mail.baghdati.gov.ge
webdisk.tkibuli.gov.ge
rev1-ext.cloud.gov.ge
mail.ccg.gov.ge
www.winnie.tskaltubo.gov.ge
www.online.moc.gov.ge
mail.bfd.gov.ge
www.es.gov.ge
government.gov.ge
keda.keda.gov.ge
mail.samtredia.gov.ge
es.gov.ge
justice.gov.ge
www.emoe.gov.ge
autodiscover.justice.gov.ge
sip.justice.gov.ge
www.justice.gov.ge
www.mail2.gardabani.gov.ge
myprofession.gov.ge
cpanel.abkhazia.gov.ge
mail.nplg.gov.ge
www.server.mod.gov.ge
qsb.gov.ge
ns2.parliament.ge
constitution.parliament.ge
votes.parliament.ge
mobileiron2.parliament.ge
petitions.parliament.ge
info.parliament.ge
dialin.parliament.ge
meet.parliament.ge
www.data.parliament.ge
sip.parliament.ge
www.sip.parliament.ge
http--www.parliament.ge
web-api.parliament.ge
vpn.parliament.ge
esignature.parliament.ge
www.parliament.ge
ns1.parliament.ge
mobileiron1.parliament.ge
www.mobileiron1.parliament.ge
sipexternal.parliament.ge
streaming.parliament.ge
www.communicator.parliament.ge
www.info.parliament.ge
autodiscover.parliament.ge
mail.parliament.ge
lyncdiscover.parliament.ge
mail01.parliament.ge
data.parliament.ge
stream.parliament.ge
www.mail.parliament.ge
www.parl.parliament.ge
communicator.parliament.ge
parl.parliament.ge
edoc.parliament.ge
adfs.parliament.ge
pbo.parliament.ge
new.parliament.ge
bbb.parliament.ge
ftp.mfa.gov.ge
ukraine.mfa.gov.ge
newyork.mfa.gov.ge
turkey.mfa.gov.ge
www.greece.mfa.gov.ge
www.coe.mfa.gov.ge
barracuda.mfa.gov.ge
www.acc1.mfa.gov.ge
www.estonia.mfa.gov.ge
fba.mfa.gov.ge
azerbaijan.mfa.gov.ge
nginx.mfa.gov.ge
ethiopia.mfa.gov.ge
austria.mfa.gov.ge
www.brazil.mfa.gov.ge
www.austria.mfa.gov.ge
www.moldova.mfa.gov.ge
acc1.mfa.gov.ge
live-was.mfa.gov.ge
www.argentina.mfa.gov.ge
autodiscover.mfa.gov.ge
mx1.mfa.gov.ge
www.mfa.gov.ge
kuwait.mfa.gov.ge
cyprus.mfa.gov.ge
uae.mfa.gov.ge
www.slovenia.mfa.gov.ge
www.poland.mfa.gov.ge
btia-api.mfa.gov.ge
domino.mfa.gov.ge
intranet.mfa.gov.ge
edocument.mfa.gov.ge
spain.mfa.gov.ge
www.un.mfa.gov.ge
geochairmanshipcoe.mfa.gov.ge
germany.mfa.gov.ge
hungary.mfa.gov.ge
australia.mfa.gov.ge
mx2.mfa.gov.ge
www.japan.mfa.gov.ge
geopresidencycoe.mfa.gov.ge
www.app.mfa.gov.ge
videos.mfa.gov.ge
test-cms.mfa.gov.ge
app.mfa.gov.ge
www.australia.mfa.gov.ge
btia.mfa.gov.ge
www.intranet.mfa.gov.ge
email.mfa.gov.ge
ibm-web.mfa.gov.ge
bpm.mfa.gov.ge
www.bpm.mfa.gov.ge
www.accreditation.mfa.gov.ge
accreditation.mfa.gov.ge
emaildownload.mfa.gov.ge
mantis.mfa.gov.ge
denmark.mfa.gov.ge
gc-api.mfa.gov.ge
test1.mfa.gov.ge
geneva.mfa.gov.ge
thessaloniki.mfa.gov.ge
brazil.mfa.gov.ge
ex-edge1.mfa.gov.ge
www.turkey.mfa.gov.ge
coe-experts.mfa.gov.ge
armenia.mfa.gov.ge
japan.mfa.gov.ge
www.geopresidencycoe.mfa.gov.ge
www.videos.mfa.gov.ge
www.malaysia.mfa.gov.ge
canada.mfa.gov.ge
www.germany.mfa.gov.ge
coeadmin.mfa.gov.ge
www.domino.mfa.gov.ge
china.mfa.gov.ge
www.nato.mfa.gov.ge
naprweb.justice.gov.ge
ms.justice.gov.ge
join.justice.gov.ge
zip.justice.gov.ge
ex-cas.justice.gov.ge
sstp.justice.gov.ge
new.justice.gov.ge
archive.justice.gov.ge
addressreest.justice.gov.ge
ms-dev.justice.gov.ge
ex-ch01.justice.gov.ge
help.justice.gov.ge
www.conference.justice.gov.ge
kancelaria.justice.gov.ge
cyrus.justice.gov.ge
mail.justice.gov.ge
ntp1.justice.gov.ge
atom.justice.gov.ge
techbiuro.justice.gov.ge
autodiscover.justice.gov.ge
api-conference.justice.gov.ge
ex-ch02.justice.gov.ge
webconf.justice.gov.ge
fbapp.justice.gov.ge
kanoni.justice.gov.ge
mx3.justice.gov.ge
www.justice.gov.ge
mx2.justice.gov.ge
conference.justice.gov.ge
lmr.justice.gov.ge
email.justice.gov.ge
jus-lyncfe01.justice.gov.ge
test.justice.gov.ge
sip.justice.gov.ge
vpn.justice.gov.ge
sea.justice.gov.ge
summaryproceedingeventsnbe.justice.gov.ge
jus-lyncedge.justice.gov.ge
lync.justice.gov.ge
nbe.justice.gov.ge
lyncdiscover.justice.gov.ge
mirror.justice.gov.ge
ns1.justice.gov.ge
av.justice.gov.ge
ns2.justice.gov.ge
pre-prod.justice.gov.ge
old.justice.gov.ge
sdoc.justice.gov.ge
fbapp1.justice.gov.ge
ftp.justice.gov.ge
```
</details>

### Live Host Fingerprinting
```
https://abkhazia.gov.ge [[33m302[0m] [[36mRedirecting to https://abkhazia.gov.ge/home[0m] [Apache] [[35mApache HTTP Server[0m]
https://5g.gov.ge [[32m200[0m] [[36m5G – Connecting everything[0m] [Apache] [[35mApache HTTP Server,MySQL,PHP,WordPress:5.2.21,jQuery,jQuery Migrate:1.4.1[0m]
https://accreditation.mfa.gov.ge [[32m200[0m] [[36mMinistry of Foreign Affairs of Georgia[0m] [Microsoft-IIS/8.5] [[35mBootstrap,Cloudflare,HSTS,IIS:8.5,Microsoft ASP.NET:4.0.30319,Moment.js,Windows Server,cdnjs,jQuery,jQuery UI[0m]
https://addreg.reestri.gov.ge [[33m302[0m] [Microsoft-IIS/7.5] [[35mHSTS,IIS:7.5,Windows Server[0m]
https://apps.municipal.gov.ge [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mNginx[0m]
https://archival-services.gov.ge [[31m403[0m] [[36m403 Forbidden[0m] [Apache/2.4.6 (CentOS)] [[35mApache HTTP Server:2.4.6,CentOS,HSTS[0m]
https://ais-dashboard.archive.gov.ge [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mNginx[0m]
https://api-conference.justice.gov.ge [[32m200[0m] [[36mLaravel[0m] [] [[35mLaravel,PHP[0m]
https://archives-ajara.gov.ge [[32m200[0m] [Apache/2] [[35mApache HTTP Server:2[0m]
https://apa.gov.ge [[33m301[0m] [Apache] [[35mApache HTTP Server,PHP:5.5.38[0m]
https://ais.archive.gov.ge [[32m200[0m] [[36mais[0m] [Apache/2.4.34 (Red Hat)] [[35mApache HTTP Server:2.4.34,Red Hat[0m]
https://akhaltsikhe.gov.ge [[32m200[0m] [[36mახალციხის მუნიციპალიტეტი[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,Drupal:7,Google Maps,HSTS,HTTP/3,LiteSpeed,LiteSpeed Cache,Litespeed Cache,PHP[0m]
https://api.my.gov.ge [[31m404[0m] [[36mThe resource cannot be found.[0m] []
https://archive.gov.ge [[32m200[0m] [[36mსაქართველოს ეროვნული არქივი[0m] [nginx] [[35mGoogle Analytics,HSTS,Mapbox GL JS,Nginx[0m]
https://atlas.mepa.gov.ge [[32m200[0m] [[36matlas.mepa.gov.ge[0m] [] [[35mHSTS[0m]
https://autodiscover.5g.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://app.iec.gov.ge [[32m200[0m] [[36mგანათლების საერთაშორისო ცენტრი[0m] [] [[35mBootstrap,HSTS,jQuery[0m]
https://autodiscover.bolnisi.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://armenia.mfa.gov.ge [[32m200[0m] [[36mსაქართველოს საელჩო სომხეთის რესპუბლიკაში[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,HSTS,HTTP/3,React[0m]
https://autodiscover.apa.gov.ge [[33m302[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Windows Server[0m]
https://autodiscover.boulevard.gov.ge [[31m400[0m] [LiteSpeed] [[35mHTTP/3,LiteSpeed,LiteSpeed Cache,Litespeed Cache[0m]
https://australia.mfa.gov.ge [[32m200[0m] [[36mსაქართველოს საელჩო ავსტრალიის თანამეგობრობაში[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,HSTS,HTTP/3,React[0m]
https://austria.mfa.gov.ge [[32m200[0m] [[36mსაქართველოს საელჩო ავსტრიის რესპუბლიკაში[0m] [cloudflare] [[35mCloudflare,Cloudflare Browser Insights,HSTS,HTTP/3,React[0m]
https://autodiscover.dmanisi.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
http://access.mrg.gov.ge [[32m200[0m] [[36mIIS Windows Server[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Windows Server[0m]
https://autodiscover.gardabani.gov.ge [[31m400[0m] [nginx] [[35mNginx[0m]
https://autodiscover.keda.gov.ge [[31m400[0m] [LiteSpeed] [[35mHTTP/3,LiteSpeed,LiteSpeed Cache,Litespeed Cache[0m]
https://autodiscover.idea.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.medeamuseum.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://autodiscover.mestia.gov.ge [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
```

### DNS / DMARC Analysis
```
--- gov.ge ---
10 mail.gov.ge.
"v=DMARC1; p=quarantine; rua=mailto:dmarc@gov.ge; ruf=mailto:dmarc@gov.ge; adkim=r; aspf=r; sp=none"
"v=spf1 mx a ip4:92.51.96.187 -all"
--- parliament.ge ---
10 mail01.parliament.ge.
"v=DMARC1; p=none; rua=mailto:geoparliament2019@gmail.com"
"v=spf1 mx ip4:85.118.102.138 -all"
--- mil.ge ---
--- finance.gov.ge ---
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
--- health.gov.ge ---
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
--- mfa.gov.ge ---
5 mx2.mfa.gov.ge.
10 mx1.mfa.gov.ge.
"v=DMARC1; p=none; rua=mailto:dmarc@mfa.gov.ge; ruf=mailto:dmarc@mfa.gov.ge; fo=s"
"v=spf1 a mx a:mx1.mfa.gov.ge a:mx2.mfa.gov.ge ip4:109.234.112.141 ip4:94.43.61.142 include:spf.mandrillapp.com -all"
--- police.gov.ge ---
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
```

### Historical URLs (Sample)
```
http://gov.ge
http://gov.ge/%22%22+atributes+imagesize+%22/%22
http://gov.ge/%22%22+pstyle+%22/%22
http://gov.ge/%20%20les/38298_38298_595238_georgia_in_transi-%20tion-hammarberg1.pdf
https://www.gov.ge/%20index.php?lang_id=GEO&sec_id=596&info_id=88171
https://www.gov.ge/%C3%BB
https://www.gov.ge/%D0%90%D2%A7%D1%8B%D0%B7a-%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%20%D0%A8%D3%99a%D0%BD%D1%82%D3%99%D1%8B%D0%BBa%20%D0%B4%D1%8B%D2%9F%D0%BE%D1%83%D0%BF
https://www.gov.ge/%D2%9A%D1%8B%D1%80%D2%AD%D1%82%D3%99%D1%8B%D0%BBa%20%D0%90%D2%A7%D1%8B%D0%B7a-%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%20%D0%90%D1%88%D1%8B%D2%9B%D3%99%D1%81%20%D2%BF%D1%8B%D1%86%D1%82%D3%99%D0%B8%20a%D0%B4%D0%BA%D1%8B%D0%BBa%D1%80a%20%D0%BC%D2%A9a%D2%A7%D0%B8%D0%B3%D0%B5%D0%B8%D1%82
http://gov.ge/%E1%83%91%E1%83%98%E1%83%91%E1%83%9A%E1%83%98%E1%83%9D%E1%83%97%E1%83%94%E1%83%99%E1%83%90
https://gov.ge/%E1%83%94%E1%83%95%E1%83%A0%E1%83%9D%E1%83%25
https://gov.ge/%E1%83%97%E1%83%94%E1%83%9B%E1%83%94%E1%83%91%E1%83%98/Soil/Documents/Training-module/91044treningmoduli.aspx
https://gov.ge/%E1%83%9D
http://gov.ge/%E1%83%9D%E1%83%A0%E1%83%90%E1%83%A2%E1%83%94%E1%83%92%E1%83%98%E1%83%A3%E1%83%9A%E1%83%98
https://www.gov.ge/%E1%83%A0%E1%83%94%E1%83%92%E1%83%98%E1%83%A1%E1%83%A2%E1%83%A0%E1%83%90%E1%83%AA%E1%83%98%E1%83%98%E1%83%A1%E1%83%97%E1%83%98%E1%83%A1%20%E1%83%92%E1%83%90%E1%83%93%E1%83%90%E1%83%93%E1%83%98%E1%83%97%20%E1%83%91%E1%83%9B%E1%83%A3%E1%83%9A%E1%83%96%E1%83%94:/http/www.fondi.gov.ge/%E1%83%92%E1%83%A0%E1%83%90%E1%83%9C%E1%83%A2%E1%83%94%E1%83%91%E1%83%98-%E1%83%93%E1%83%90-%E1%83%99%E1%83%9D%E1%83%9C%E1%83%99%E1%83%A3%E1%83%A0%E1%83%A1%E1%83%94%E1%83%91%E1%83%98/%E1%83%99%E1%83%9D%E1%83%9C%E1%83%99%E1%83%A3%E1%83%A0%E1%83%A1%E1%83%98%E1%83%A1-%E1%83%A4%E1%83%9D%E1%83%A0%E1%83%9B%E1%83%90/%20%E1%83%A1%E1%83%90%E1%83%92%E1%83%A0%E1%83%90%E1%83%9C%E1%83%A2%E1%83%9D%20%E1%83%90%E1%83%9E%E1%83%9A%E1%83%98%E1%83%99%E1%83%90%E1%83%AA%E1%83%98%E1%83%98%E1%83%A1%20%E1%83%A8%E1%83%94%E1%83%95%E1%83%A1%E1%83%94%E1%83%91%E1%83%98%E1%83%A1%20%E1%83%92%E1%83%96%E1%83%90%E1%83%9B%E1%83%99%E1%83%95%E1%83%9A%E1%83%94%E1%83%95%E1%83%98%20http:/www.youtube.com/watch?v=zTrE3SIsVTs
https://www.gov.ge/%E1%83%A1%E1%83%90%E1%83%A5%E1%83%90%E1%83%A0%E1%83%97%E1%83%95%E1%83%94%E1%83%9A%E1%83%9D%E1%83%A1%20%E1%83%9E%E1%83%A0%E1%83%94%E1%83%9B%E1%83%98%E1%83%94%E1%83%A0-%E1%83%9B%E1%83%98%E1%83%9C%E1%83%98%E1%83%A1%E1%83%A2%E1%83%A0%E1%83%98%20TATA%20Group-%E1%83%98%E1%83%A1%20%E1%83%AE%E1%83%94%E1%83%9A%E1%83%9B%E1%83%AB%E1%83%A6%E1%83%95%E1%83%90%E1%83%9C%E1%83%94%E1%83%9A%E1%83%97%E1%83%90%20%E1%83%AF%E1%83%92%E1%83%A3%E1%83%A4%E1%83%A1%20%E1%83%A8%E1%83%94%E1%83%AE%E1%83%95%E1%83%93%E1%83%90
http://gov.ge/%E1%83%A1%E1%83%9D%E1%83%A4%E1%83%9A%E1%83%98%E1%83%A1
https://www.gov.ge/%E1%83%A1%E1%83%A2%E1%83%A0%E1%83%90%E1%83%A2%E1%83%94%E1%83%92%E1%83%98%E1%83%94%E1%83%91%E1%83%98-%E1%83%93%E1%83%90-%E1%83%99%E1%83%9D%E1%83%9C%E1%83%AA%E1%83%94%E1%83%A4%E1%83%AA%E1%83%98-2
https://www.gov.ge/%E1%83%AC%E1%83%9A%E1%83%98%E1%83%A3%E1%83%A0%E1%83%98-%E1%83%90%E1%83%9C%E1%83%92%E1%83%90%E1%83%A0%E1%83%98%E1%83%A8%E1%83%94%E1%83%91%E1%83%98
https://www.gov.ge/%E2%80%A2http:/www.consilium.europa.eu/en/press/press-releases/2015/07/20-tusk-meeting-georgia-margvelashvili/
https://www.gov.ge/%E2%80%A2http:/www.consilium.europa.eu/en/press/press-releases/2015/07/21-pec-remarks-meeting-prime-minister-garibashvili/
```

## Video Documentation
🎬 [OSINT Tourism: Georgia](https://archive.org/details/odint-georgia-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
