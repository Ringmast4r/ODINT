# Montenegro — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.me TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 486 |
| Live hosts fingerprinted | 106 |
| DNS/DMARC records analyzed | 21 |
| Historical URLs (GAU) | 298024 |

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
adfs.gov.me
uisportalapi-test.gov.me
ngo.mju.gov.me
3r-epa.gov.me
stratlink.gov.me
uispriredjivac-test.gov.me
apivauceri.gov.me
dk.gov.me
kdi.gov.me
www.data.gov.me
mail.upfoj.gov.me
www.gov.me
eusluge.gov.me
kzcg.gov.me
mepg.gov.me
potpredsjednik.gov.me
upravazavode.gov.me
webmail.daro.servis.mup.gov.me
www.javninameti.gov.me
mvpvfs.gov.me
```
<details><summary>Full list (486 subdomains)</summary>

```
adfs.gov.me
uisportalapi-test.gov.me
ngo.mju.gov.me
3r-epa.gov.me
stratlink.gov.me
uispriredjivac-test.gov.me
apivauceri.gov.me
dk.gov.me
kdi.gov.me
www.data.gov.me
mail.upfoj.gov.me
www.gov.me
eusluge.gov.me
kzcg.gov.me
mepg.gov.me
potpredsjednik.gov.me
upravazavode.gov.me
webmail.daro.servis.mup.gov.me
www.javninameti.gov.me
mvpvfs.gov.me
mps.gov.me
mvp.gov.me
mail.ca.servis.mup.gov.me
legacy.gov.me
design.gov.me
www.kis.mfa.gov.me
uispriredjivac.gov.me
poreskauprava.gov.me
webmail.teste.servis.mup.gov.me
webdisk.ca.servis.mup.gov.me
portal.ujn.gov.me
testjiisuip.gov.me
edotestsys.gov.me
uisapi.gov.me
wis.gov.me
upravacarina.gov.me
eid2stageeuprava.gov.me
testobracunzarada.gov.me
dpcovid19.gov.me
public-3r-epa.gov.me
testeuprava.gov.me
mail.e.servis.mup.gov.me
cpanel.ca.servis.mup.gov.me
www.konkursimkm.gov.me
test.foj.gov.me
predsjednik.gov.me
www.voice.mvp.gov.me
kzcg.gsv.gov.me
3r-gitea-test-epa.gov.me
eiprevod.gov.me
ctr.gov.me
secret.gov.me
test-metaregistar.gov.me
ri.mju.gov.me
epeticije.gov.me
obestecenje.gov.me
3r-pentaho-epa.gov.me
mvpfin.mfa.gov.me
portal-pam.gov.me
ubh.gov.me
scc.anb.gov.me
smg.gov.me
rss.gov.me
test-eservisi.gov.me
3r-sso-epa.gov.me
cejnespd.gov.me
uisportal.gov.me
luckauprava.gov.me
www.cp.servis.mup.gov.me
cjn9bvrt.gov.me
stageuprava.gov.me
www.mail.mfa.gov.me
nics.mup.gov.me
e-socijala.gov.me
gsv.gov.me
srju.gov.me
uzd.gov.me
e-akademija.gov.me
public-3r-sso-epa.gov.me
ujn.gov.me
edotestportal.gov.me
testorigamimob.gov.me
mail.daro.servis.mup.gov.me
www.epeticije.gov.me
digitalnomads-api.gov.me
fitoskomisija.gov.me
ieces.gov.me
akvo.gov.me
mzd.gov.me
uzkd.gov.me
uzz.gov.me
www.idp.gov.me
inovacije.gov.me
cjn9bvrt-rss.gov.me
psc.gov.me
smtp2.anb.gov.me
cpcalendars.daro.servis.mup.gov.me
osint.foj.gov.me
public-3r-sso-test-epa.gov.me
mna.gov.me
uzs.gov.me
www.luckekapetanije.msp.gov.me
www.mvpfin.mvp.gov.me
eprijava.tax.gov.me
eid.gov.me
voice.mvp.gov.me
cpanel.e.servis.mup.gov.me
www.ipa.gov.me
www.rnkipe.mpa.gov.me
upitnik.foj.gov.me
esv.gov.me
public-3r-test-epa.gov.me
rsa.gov.me
e.servis.mup.gov.me
eiprevodi.gov.me
kinns.gov.me
upc.gov.me
cisee.gov.me
stageorgani.gov.me
cjn9bvrt-go.gov.me
ekontrola.gov.me
kis.mfa.gov.me
mek.gov.me
cjn9bvrt-sitemap.gov.me
mail.gov.me
www.mif.gov.me
crsport.gov.me
lamp.gov.me
test.upfoj.gov.me
webdisk.daro.servis.mup.gov.me
go.gov.me
www.mfa.gov.me
mojpersonalnidosije.gov.me
wapi.gov.me
tgs.gov.me
anb.gov.me
testutlisbpm.gov.me
ms.gov.me
cpcalendars.ca.servis.mup.gov.me
komisija-cejn.gov.me
nvotest.gov.me
obracunzarada.gov.me
kei.gov.me
ups.gov.me
cpcontacts.teste.servis.mup.gov.me
apollo-mdup.gov.me
test-eusluge.gov.me
adminn.gov.me
www.visa.gov.me
uzi.gov.me
cpcontacts.ca.servis.mup.gov.me
eplacanje-mpa-auth.gov.me
registarsporova.gov.me
mku.gov.me
mpr.gov.me
nvo.gov.me
cpcalendars.e.servis.mup.gov.me
public-3r-api-test-epa.gov.me
3r-penthao-epa.gov.me
www.upfoj.gov.me
api.gov.me
ca.gov.me
kkdp.gov.me
veterina.gov.me
provjeriuplate.gov.me
drzavniorgani.gov.me
nics-identity.mup.gov.me
stratlink-system.gov.me
test-pso.gov.me
webdisk.teste.servis.mup.gov.me
www.porodiljsko.mrs.gov.me
3r-api-epa.gov.me
3r-api-test-epa.gov.me
mpa.gov.me
nics-web.mup.gov.me
test-eplacanje-mpa-auth.gov.me
eis-api.epa.gov.me
cloud.mfa.gov.me
ipa.gov.me
3r-api.epa.gov.me
www.api.gov.me
edozvoleide.gov.me
eces.gov.me
ipard.gov.me
www.visa.mfa.gov.me
3r-pentaho-test-epa.gov.me
biznis-api.gov.me
javninameti.gov.me
predsjpol.gov.me
uip.gov.me
mmp.gov.me
registardrzavnepomoci.gov.me
up.gov.me
mmg1.gov.me
eideuprava.gov.me
tl.gov.me
ujr.gov.me
www.ngo.mju.gov.me
www.eid.gov.me
dms.gov.me
nvoprod.gov.me
fadn.gov.me
test-rso.gov.me
mzd-infomed.gov.me
nsa.gov.me
vojska.gov.me
3r.epa.gov.me
edozvole.gov.me
portal.foj.gov.me
upravaprihoda.gov.me
zzm.gov.me
www.mgw.mfa.gov.me
biznis.gov.me
mesph.gov.me
mod.gov.me
www.mvpfin.mfa.gov.me
www.ujn.gov.me
testportal.tax.gov.me
akademija.gov.me
donacije.gov.me
mki.gov.me
www.planovidozvole.mrt.gov.me
webmail.ca.servis.mup.gov.me
cejn.gov.me
ca.servis.mup.gov.me
uzkd.mku.gov.me
mif-ipa.gov.me
autodiscover.mfa.gov.me
csat-auth.gov.me
rnkipe.mpa.gov.me
visa.mfa.gov.me
mpnks.gov.me
api.mif-ipa.gov.me
daro.servis.mup.gov.me
antitrafficking.gov.me
szz.gov.me
mia.gov.me
devopendata.gov.me
mif.gov.me
vauceri.gov.me
info.mfa.gov.me
cjn9bvrt-api.gov.me
uisportal-test.gov.me
duemari.gov.me
organi.gov.me
uisportalapi.gov.me
vis.gov.me
3r-auth.epa.gov.me
ns.gov.me
edozvoleportalapi.gov.me
prtrepa.gov.me
autodiscover.gov.me
www.teste.servis.mup.gov.me
eis.epa.gov.me
eplacanje.gov.me
zarade.gov.me
konk.gov.me
data.gov.me
plate.gov.me
zavodzaskolstvo.gov.me
mmg2.gov.me
ispi.gov.me
cfcu.gov.me
safego.gov.me
mjucloud.gov.me
info.foj.gov.me
cpcontacts.e.servis.mup.gov.me
upfoj.gov.me
programi.gov.me
crs.gov.me
nics-data.mup.gov.me
ispimju.gov.me
public-3r-auth-epa.gov.me
uzk.gov.me
planovidozvole.mrt.gov.me
www.testportal.tax.gov.me
kbmp.gov.me
opendata.gov.me
vojska.mod.gov.me
visa.gov.me
test-eplacanje-mpa.gov.me
3r-auth-epa.gov.me
mju.gov.me
mail.teste.servis.mup.gov.me
edozvoleportal.gov.me
webdisk.e.servis.mup.gov.me
nics-map.mup.gov.me
mdm.gov.me
3r-gitea-epa.gov.me
idp.gov.me
csat.gov.me
portalujn.gov.me
ckan.gov.me
metrologija.gov.me
cirt.gov.me
nvokonkursi.gov.me
cjn9bvrt-media.gov.me
gismdup.gov.me
x-road.gov.me
digitalnomads-admin.gov.me
rso.gov.me
testesv.gov.me
eis-sso.epa.gov.me
mvpfin.mvp.gov.me
www.eprijava.tax.gov.me
www.mmp.gov.me
test-spi.gov.me
www.mail.gov.me
www.kei.gov.me
vpn.gov.me
potpredsjednikregraz.gov.me
e-peticije.gov.me
scms.mju.gov.me
deminimispomoc.gov.me
testdms.gov.me
mfa.gov.me
budzet.gov.me
misp.gov.me
www.ca.servis.mup.gov.me
metaregistar.gov.me
ziks.gov.me
uis.mif.gov.me
mapp-mdup.gov.me
kis.gov.me
vpn-uis.gov.me
mail.anb.gov.me
cpanel.teste.servis.mup.gov.me
cpcalendars.teste.servis.mup.gov.me
edotestsyside.gov.me
kzz.gov.me
patentniregistar.gov.me
tie.gov.me
www.mail.anb.gov.me
ispi.mju.gov.me
sitemap.gov.me
autodiscover.anb.gov.me
ca.elk.gov.me
admin.gov.me
dztpobuka.gov.me
fadntest.gov.me
proxmox.gov.me
sindikalnebpm.gov.me
cp.servis.mup.gov.me
share.gov.me
cp.foj.gov.me
aduvan.gov.me
spi.gov.me
tax.gov.me
eplacanje-mpa.gov.me
ortofoto2025.gov.me
pimfa.gov.me
startlink-system.gov.me
mesph-prevodi.gov.me
uismif.gov.me
vislab.gov.me
mrs.gov.me
api.vauceri.gov.me
www.daro.servis.mup.gov.me
educomm.gov.me
mesph-ppcg.gov.me
more.gov.me
mvpei.gov.me
fondrada.gov.me
potpredsjednikekon.gov.me
uzi.mrs.gov.me
ns1.gov.me
ti.gov.me
m-euprava.gov.me
pso.gov.me
uisapi-test.gov.me
webmail.gov.me
planpro.mju.gov.me
3r-sso-test-epa.gov.me
zmail.mfa.gov.me
mail.cp.servis.mup.gov.me
cms.gov.me
foj.gov.me
test-dijaspora-mdi.gov.me
www.e.servis.mup.gov.me
teste.servis.mup.gov.me
eid2euprava.gov.me
registri-is.gov.me
crsport.ms.gov.me
elastic.gov.me
mbezportfe.gov.me
dodksm.dodks.gov.me
fusion-mdup.gov.me
mesph-auth.gov.me
mzd-infomed-test.gov.me
trustlist.gov.me
usdi.gov.me
www.mia.gov.me
chatbot.gov.me
dijaspora-mdi.gov.me
mup.gov.me
mvpmki.gov.me
ngo.gov.me
www.jiis.uip.gov.me
media.gov.me
mrt.gov.me
zzs.gov.me
biznis-admin.gov.me
pam.gov.me
fzo.gov.me
svo.gov.me
szr.gov.me
mail.off.mfa.gov.me
jiisuip.gov.me
utilsbpm.gov.me
startlink.gov.me
edotestds.gov.me
szp.gov.me
chatai.gov.me
eidstageeuprava.gov.me
www.mdm.gov.me
origamimob.gov.me
porodiljsko.gov.me
safegomdw.gov.me
swis.mrs.gov.me
edozvoleds.gov.me
eidtesteuprava.gov.me
mha.gov.me
cpcontacts.daro.servis.mup.gov.me
smtp1.anb.gov.me
rso-admin.gov.me
test-rso-admin.gov.me
mcafeeepo.gov.me
evjencanje.gov.me
imunizacija.gov.me
srp.gov.me
jiis.uip.gov.me
eakademija.gov.me
edms.gov.me
eid2testeuprava.gov.me
psoadmin.gov.me
cso.gov.me
edotestportalapi.gov.me
mesph-report.gov.me
cpanel.daro.servis.mup.gov.me
mnevillage.gov.me
euprava.gov.me
public-3r-api-epa.gov.me
webmail.e.servis.mup.gov.me
www.edms.gov.me
fitos.gov.me
konkursimkm.gov.me
bookstarck.gov.me
mesph-planovi.gov.me
wsus.mfa.gov.me
veljebrdo.gov.me
msp.gov.me
mgw.mfa.gov.me
www.veterina.gov.me
digitalnomads.gov.me
3r-test-epa.gov.me
mpsv.gov.me
geo.mrt.gov.me
www.geo.mrt.gov.me
mail.mfa.gov.me
nvo.mju.gov.me
www.parliament.me
yey.mil.me
smtp1.mil.me
autodiscover.mil.me
smtp2.mil.me
mail.mil.me
scc.mil.me
www.mail.mil.me
www.camaradoslordes.blogspot.mil.me
visa.mfa.gov.me
mail.mfa.gov.me
www.mfa.gov.me
info.mfa.gov.me
autodiscover.mfa.gov.me
www.visa.mfa.gov.me
kis.mfa.gov.me
www.mail.mfa.gov.me
mvpfin.mfa.gov.me
www.mvpfin.mfa.gov.me
www.kis.mfa.gov.me
zmail.mfa.gov.me
mgw.mfa.gov.me
wsus.mfa.gov.me
cloud.mfa.gov.me
mail.off.mfa.gov.me
www.mgw.mfa.gov.me
```
</details>

### Live Host Fingerprinting
```
https://adfs.gov.me [[31m404[0m] [[36mNot Found[0m] [Microsoft-HTTPAPI/2.0] [[35mMicrosoft HTTPAPI:2.0[0m]
https://biznis-admin.gov.me [[32m200[0m] [[36mBiznis.gov.me - CMS[0m] [nginx] [[35mFont Awesome,Nginx[0m]
https://apollo-mdup.gov.me [[32m200[0m] [[36mIIS Windows Server[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://ca.elk.gov.me [[33m302[0m] [[36m302 Found[0m] [Apache] [[35mApache HTTP Server[0m]
https://cejn.gov.me [[32m200[0m] [[36mCeJN[0m] [Microsoft-IIS/10.0] [[35mFortinet FortiGate,HSTS,IIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://cejnespd.gov.me [] [[36mHTTP Status 500 – Internal Server Error[0m] []
https://biznis-api.gov.me [[32m200[0m] [nginx] [[35mNginx,PHP:8.0.21[0m]
https://cirt.gov.me [[32m200[0m] [[36mVladin CIRT - GOV.ME[0m] [Web Server]
https://biznis.gov.me [[32m200[0m] [[36mPočetna[0m] [nginx] [[35mGoogle Tag Manager,HSTS,Nginx[0m]
https://cp.foj.gov.me [[32m200[0m] [Apache] [[35mApache HTTP Server[0m]
https://crs.gov.me [[31m404[0m] [[36mNot Found[0m] [Microsoft-HTTPAPI/2.0] [[35mMicrosoft HTTPAPI:2.0[0m]
https://crsport.gov.me [[32m200[0m] [[36mCRSport[0m] [Microsoft-IIS/10.0] [[35mBootstrap,IIS:10.0,Microsoft ASP.NET,Windows Server,jQuery[0m]
https://ctr.gov.me [[32m200[0m] [[36mPregled registra[0m] [nginx/1.18.0 (Ubuntu)] [[35mBootstrap:df045a66741e03e9ca2ebbdfcbb709f7,DataTables,Nginx:1.18.0,Ubuntu,jQuery:3.3.1[0m]
https://design.gov.me [[31m401[0m] [[36m401 Authorization Required[0m] [nginx] [[35mBasic,Nginx[0m]
https://digitalnomads-api.gov.me [[32m200[0m] [nginx] [[35mHSTS,Nginx[0m]
https://digitalnomads-admin.gov.me [[32m200[0m] [[36mBase - Administrator's panel[0m] [nginx] [[35mFont Awesome,HSTS,Nginx[0m]
https://data.gov.me [[32m200[0m] [[36mPortal otvorenih podataka[0m] [nginx] [[35mBootstrap:4.0.0,BootstrapCDN:4.0.0,Ckan:2.11.0,Cloudflare,Google Analytics,Google Tag Manager,Java,Nginx,PostgreSQL,Python,Solr,Swiper,cdnjs,jQuery:3.2.1[0m]
https://dijaspora-mdi.gov.me [[32m200[0m] [[36mRegistar Dijaspore[0m] [nginx/1.24.0] [[35mNginx:1.24.0[0m]
https://digitalnomads.gov.me [[32m200[0m] [[36mDigital Nomads - GOV.me[0m] [nginx] [[35mHSTS,Nginx[0m]
https://donacije.gov.me [[32m200[0m] [[36mPomoć za sanaciju posljedica požara[0m] [nginx] [[35mExpress,Nginx,Node.js[0m]
https://dztpobuka.gov.me [[33m303[0m] [[36mPreusmeri[0m] [Apache/2.4.52 (Ubuntu)] [[35mApache HTTP Server:2.4.52,Moodle,PHP,Ubuntu[0m]
https://duemari.gov.me [[32m200[0m] [Apache/2.4.65 (Ubuntu)] [[35mApache HTTP Server:2.4.65,Ubuntu[0m]
https://e.servis.mup.gov.me [[32m200[0m] [[36mPortal za e-servise[0m] [nginx] [[35mHSTS,Next.js,Nginx,Node.js,React,Webpack[0m]
https://edotestds.gov.me [[31m403[0m] [nginx/1.14.1] [[35mNginx:1.14.1[0m]
https://edotestportal.gov.me [[32m200[0m] [[36me-Dozvole Portal[0m] [Microsoft-IIS/10.0] [[35mBlazor,Bootstrap,IIS:10.0,Material Design Lite,Microsoft ASP.NET,Windows Server[0m]
https://edotestportalapi.gov.me [[31m404[0m] [Microsoft-IIS/10.0] [[35mHSTS,IIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://edotestsyside.gov.me [[31m404[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://educomm.gov.me [[33m302[0m] [Apache] [[35mApache HTTP Server,PHP[0m]
https://edotestsys.gov.me [[33m302[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://eiprevod.gov.me [[32m200[0m] [[36mEnglesko-crnogorska terminološka baza[0m] [Apache/2.4.52 (Ubuntu)] [[35mApache HTTP Server:2.4.52,Ubuntu[0m]
```

### DNS / DMARC Analysis
```
--- gov.me ---
30 alt2.us.email.fireeyecloud.com.
40 alt3.us.email.fireeyecloud.com.
10 primary.us.email.fireeyecloud.com.
20 alt1.us.email.fireeyecloud.com.
"v=spf1 include:_spf.fireeyecloud.com -all"
--- parliament.me ---
5 mail.skupstina.me.
--- mil.me ---
10 smtp1.mil.me.
"v=DMARC1; p=reject; rua=mailto:dmarc.reports@mil.me; ruf=mailto:dmarc.reports@mil.me; sp=reject; fo=1"
"v=spf1 ip4:94.102.232.51 -all"
--- finance.gov.me ---
--- health.gov.me ---
--- mfa.gov.me ---
1 mgw.mfa.gov.me.
"v=DMARC1; p=quarantine; rua=mailto:2fa8c6930d7e4ac78c385855661067dd@dmarc-reports.cloudflare.net,mailto:postmaster@mfa.gov.me;"
"6db7j8ddrjsspfxjbcyjs5zvg70m8dx4"
"v=spf1 ip4:37.0.69.86 -all"
--- police.gov.me ---
--- justice.gov.me ---
```

### Historical URLs (Sample)
```
http://parliament.me/
http://parliament.me/favicon.ico
http://www.parliament.me/images/dokumenti/akcioni-
http://www.parliament.me/images/dokumenti/akcioni-plan/3.pdf
http://www.parliament.me/images/dokumenti/izvjestaji-
http://www.parliament.me/images/dokumenti/izvjestaji-o-radu/2.pdf
http://parliament.me/robots.txt
http://mil.me:80/
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=1204446177&back=http%3A%2F%2Fmil.me%2F
http://mil.me:80/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=1477208783&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=1519877913&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=1580369628&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=221925536&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=655124227&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=660735679&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=800656709&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=896371042&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=909277976&back=http%3A%2F%2Fmil.me%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=1419779&back=http%3A%2F%2Fmil.me%2Fabout%2F
http://mil.me/?dm=b58959ccf9cff23d99c0d130c7ebb4c9&action=load&blogid=45775&siteid=616&t=427357843&back=http%3A%2F%2Fmil.me%2Fabout%2F
```

## Video Documentation
🎬 [OSINT Tourism: Montenegro](https://archive.org/details/odint-montenegro-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
