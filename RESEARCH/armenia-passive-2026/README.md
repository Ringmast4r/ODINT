# Armenia — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.am TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 425 |
| Live hosts fingerprinted | 84 |
| DNS/DMARC records analyzed | 26 |
| Historical URLs (GAU) | 0 |

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
mul2-taxservice.gov.am
mul2-mnpinsp.gov.am
mul2-ararat.gov.am
www.mul2-raed.gov.am
mul.minfin.gov.am
www.elearning.cso.gov.am
mul2-lori.gov.am
mul2-sif.gov.am
mul2-georgia.gov.am
mul2-bsec.gov.am
www.mul2-kotayk.gov.am
mul.scws.gov.am
mul.spm.gov.am
mul.gdca.gov.am
mul2-utfsib.gov.am
webdisk.ai.gov.am
www.auction.mia.gov.am
www.mul2-mnp.gov.am
www.mul2-romania.gov.am
mul.fsss.gov.am
```
<details><summary>Full list (425 subdomains)</summary>

```
mul2-taxservice.gov.am
mul2-mnpinsp.gov.am
mul2-ararat.gov.am
www.mul2-raed.gov.am
mul.minfin.gov.am
www.elearning.cso.gov.am
mul2-lori.gov.am
mul2-sif.gov.am
mul2-georgia.gov.am
mul2-bsec.gov.am
www.mul2-kotayk.gov.am
mul.scws.gov.am
mul.spm.gov.am
mul.gdca.gov.am
mul2-utfsib.gov.am
webdisk.ai.gov.am
www.auction.mia.gov.am
www.mul2-mnp.gov.am
www.mul2-romania.gov.am
mul.fsss.gov.am
mail.utfsib.gov.am
cso.gov.am
mul2-nl.gov.am
mip-zz.gov.am
www.mip-zz.gov.am
ns.gov.am
mul.agri.gov.am
mul2-indonesia.gov.am
mul2-unesco.gov.am
www.mul2-harkadir.gov.am
mul2-dmr.gov.am
mul.msy.gov.am
mul2-mnp.gov.am
mul2-syunik.gov.am
mul2-supervision.gov.am
mul2-msib.gov.am
mul2-eib.gov.am
gov-zz.gov.am
www.mul2-mtc.gov.am
mul2-armavir.gov.am
mul2-ccc.gov.am
environment.gov.am
www.mul2-ccc.gov.am
mulbackup.agri.gov.am
mul2-fsss.gov.am
mul2-pmc.gov.am
cpcalendars.ai.gov.am
www.mul2-cis.gov.am
www.mul2-moj.gov.am
cadastre-zz.gov.am
soc-zz.gov.am
mul.lori.gov.am
benefits.hightech.gov.am
auction.mia.gov.am
ogp.gov.am
mul.ararat.gov.am
ca1.gov.am
mul2-mud.gov.am
mul2-china.gov.am
www.mul2-msib.gov.am
www.mul2-utfsib.gov.am
mul.mud.gov.am
mul2-aviation.gov.am
mul2-spm.gov.am
mul2-mfa.gov.am
mul2-rostov.gov.am
www.mul2-sif.gov.am
mul2-gdca.gov.am
mail.echr.gov.am
www.mul2-fsss.gov.am
mul.sif.gov.am
www.hightech.gov.am
www.mul2-edu.gov.am
www.mul2-kazakhstan.gov.am
en.gov.am
www.migration-zz.gov.am
mul.edu.gov.am
vdzor.gov.am
mail2.gov.am
mulbackup.msy.gov.am
mul2-spain.gov.am
www.mail.echr.gov.am
mul.ema.gov.am
cert.gov.am
www.anti-corruption.gov.am
mul2-police.gov.am
www.mul2-anra.gov.am
covid19.gov.am
www.mul.taxservice.gov.am
mx101.trade.gov.am
mx201.trade.gov.am
drive-echr.gov.am
mul2-gallery.gov.am
mul2-swiss.gov.am
mul2-cz.gov.am
www.api-stayhome.gov.am
mail.diaspora.gov.am
kotayk.gov.am
mul2-turkmenistan.gov.am
www.minfin.gov.am
mul2-edu.gov.am
sw.gov.am
prelive.cso.gov.am
mul2-sgo.gov.am
mul2-greece.gov.am
new.hightech.gov.am
www.mul2-supervision.gov.am
www.mul2-mfa.gov.am
mul2-tavush.gov.am
www.mul2-armarchives.gov.am
www.mul2-indonesia.gov.am
mul.kotayk.gov.am
mul.gegh.gov.am
mul-scws.gov.am
mul2-nato.gov.am
www.mul2-scws.gov.am
www.mul2-moh.gov.am
mail.cso.gov.am
elearning.cso.gov.am
trade201.gov.am
www.mul2-minfin.gov.am
mul.mineconomy.gov.am
mul2-romania.gov.am
mul2-mcs.gov.am
rescue.mia.gov.am
www.zangezor.gov.am
www.mul2-armavir.gov.am
www.mul2-france.gov.am
mta.gov.am
mul.mindiaspora.gov.am
mail.ecoinspect.gov.am
hightech.gov.am
mul2-mia.gov.am
migration.mia.gov.am
www.ai.gov.am
www.mul2-aviation.gov.am
admin.car.mia.gov.am
www.gov-zz.gov.am
www.mul2-syunik.gov.am
www.mail.cso.gov.am
mul.mta.gov.am
mul.syunik.gov.am
mul.psrc.gov.am
mul2-sochi.gov.am
mul2-cadastre.gov.am
www.hartak.cso.gov.am
www.mul2-mineconomy.gov.am
www.mul2-mexico.gov.am
www.mul2-nl.gov.am
mul2-justexpert.gov.am
syunik.gov.am
mul2-cec.gov.am
ai.gov.am
www.mul2-dubai.gov.am
www.mul2-vdzor.gov.am
mul.mtc.gov.am
mul2-shirak.gov.am
elections.mia.gov.am
www.mul2-sweden.gov.am
www.mul2-taxservice.gov.am
stayhome-covid19.gov.am
mul2-psrc.gov.am
mul2-mta.gov.am
mul2-harkadir.gov.am
www.mul2-police.gov.am
www.mul2-mcs.gov.am
www.mul.gov.am
mail.eib.gov.am
mul2-lithuania.gov.am
notify.tourism.gov.am
minurban-zz.gov.am
mul.moj.gov.am
mul-fsss.gov.am
mail.msib.gov.am
www.ogp.gov.am
www.api-ac19.gov.am
www.mta.gov.am
mul2-poland.gov.am
www.mail.gov.am
erepo.gov.am
www.mul2-egypt.gov.am
www.support-ac19.gov.am
mul2.gov.am
standards.hightech.gov.am
www.mul2-usa.gov.am
www.mul2-mud.gov.am
www.mul2-belarus.gov.am
mul.nsc.gov.am
office-echr.gov.am
env.gov.am
mul2-coe.gov.am
mul2-la.gov.am
stream.cso.gov.am
mulbackup.ema.gov.am
mul.culture.gov.am
mia.gov.am
www.minurban-zz.gov.am
www.mul2-spm.gov.am
www.mul2.gov.am
www.mul2-dmr.gov.am
mul2-cis.gov.am
mul2-uk.gov.am
www.sw.gov.am
api-ac19.gov.am
www.stayhome-covid19.gov.am
mail1.gov.am
mul.aragatsotn.gov.am
ns201.trade.gov.am
mul2-usa.gov.am
mul2-vatican.gov.am
mul2-raed.gov.am
www.mul2-aatm.gov.am
mul.cadastre.gov.am
mul.mnp.gov.am
drive.gov.am
www.mul2-eib.gov.am
mul.minenergy.gov.am
mul.tavush.gov.am
hartak.cso.gov.am
mul2-belgium.gov.am
www.mul2-italy.gov.am
www.mul2-spain.gov.am
www.mul2-ema.gov.am
www.mul2-ukraine.gov.am
www.gov.am
www.mul2-tavush.gov.am
www.mul2-germany.gov.am
mul-eec.gov.am
mul.mfa.gov.am
mul2-mexico.gov.am
zz-minfin.gov.am
www.mul2-mia.gov.am
www.mul2-turkmenistan.gov.am
www.mul2-austria.gov.am
support-ac19.gov.am
www.cert.gov.am
mail.gov.am
aragatsotn.gov.am
mul2-germany.gov.am
mul2-ema.gov.am
www.mul2-gegh.gov.am
www.mul2-cec.gov.am
mul.aviation.gov.am
mul2-isc.gov.am
prelive.hartak.cso.gov.am
mul2-ecopatrolservice.gov.am
mul2-kazakhstan.gov.am
mul2-austria.gov.am
mul.moh.gov.am
mul2-armarchives.gov.am
mul2-ukraine.gov.am
mul2-dubai.gov.am
www.mail.eib.gov.am
www.mul2-bulgaria.gov.am
www.mul2-psrc.gov.am
mul.gov.am
webmail.ai.gov.am
trade.gov.am
mul2-armroad.gov.am
mul2-marseille.gov.am
www.mul2-investigative.gov.am
www.mul2-competition.gov.am
www.mul2-gallery.gov.am
www.mul2-cz.gov.am
www.gegharkunik.gov.am
mulbackup.mindiaspora.gov.am
mul2-sweden.gov.am
autodiscover.ai.gov.am
www.standards.hightech.gov.am
cms-ogp.gov.am
www.mul2-russia.gov.am
multimedia.gov.am
mul2-batumi.gov.am
mul2-moh.gov.am
migration-zz.gov.am
www.mul2-aragatsotn.gov.am
api-stayhome.gov.am
mul2-egypt.gov.am
www.api-covid.gov.am
mul2-mtc.gov.am
mul2-un.gov.am
mul2-spb.gov.am
www.mul2-atdf.gov.am
www.mul2-ararat.gov.am
www.mul2-isc.gov.am
www.mul2-sochi.gov.am
mul2-minfin.gov.am
api-covid.gov.am
www.trade201.gov.am
regions-karavarum.gov.am
mul2-csto.gov.am
mul2-moj.gov.am
www.mul2-armroad.gov.am
www.mul.mta.gov.am
www.mul2-mnpinsp.gov.am
www.mul-mil.gov.am
www.covid19.gov.am
mul2-gegh.gov.am
mulbackup.moh.gov.am
mulbackup.mud.gov.am
mul2-lyon.gov.am
www.mul2-justexpert.gov.am
www.mul-scws.gov.am
mul.dmr.gov.am
regions.gov.am
mul2-scws.gov.am
mul2-investigative.gov.am
www.mul2-ecopatrolservice.gov.am
car.mia.gov.am
mul2-italy.gov.am
www.zz-minfin.gov.am
zangezor.gov.am
www.mul2-lori.gov.am
minfin.gov.am
www.mul2-rostov.gov.am
mul.vdzor.gov.am
mul2-kotayk.gov.am
shirak.gov.am
mul2-aragatsotn.gov.am
www.trade.gov.am
moj.gov.am
mail-gw.gov.am
mul.csc.gov.am
mul.mieir.gov.am
mail.mta.gov.am
mul2-anra.gov.am
armavir.gov.am
mul2-france.gov.am
adams.gov.am
www.mul-eec.gov.am
mul.armavir.gov.am
mul2-vdzor.gov.am
anti-corruption.gov.am
www.mul2-china.gov.am
www.mul2-cadastre.gov.am
mul.mss.gov.am
mul-mil.gov.am
api.car.mia.gov.am
mul2-atdf.gov.am
mul2-mss.gov.am
www.mul2-mss.gov.am
mul.competition.gov.am
mul2-russia.gov.am
www.cso.gov.am
www.mul2-mta.gov.am
mul2-forestcommittee.gov.am
www.mul2-uk.gov.am
www.mul-fsss.gov.am
mul.shirak.gov.am
ararat.gov.am
mul2-belarus.gov.am
mail.ai.gov.am
www.mul2-shirak.gov.am
echr.gov.am
mul.taxservice.gov.am
cpanel.ai.gov.am
cpcontacts.ai.gov.am
www.mul2-forestcommittee.gov.am
mul2-bulgaria.gov.am
mul2-aatm.gov.am
www.mia.gov.am
www.mul2-belgium.gov.am
diaspora.gov.am
elearning.mta.gov.am
mul2-mineconomy.gov.am
mul2-cyprus.gov.am
mul2-competition.gov.am
elearning.parliament.am
www.parliament.am
library.parliament.am
ns1.parliament.am
mail.parliament.am
ns2.parliament.am
mul2.parliament.am
gitlab.parliament.am
www.mil.am
atmk.mil.am
ns1.mil.am
edu.mil.am
taiga.mil.am
monitoring.mil.am
nexus.mil.am
mail.mil.am
ns.mil.am
www.mail.mil.am
rapk.mil.am
mul.mfa.gov.am
mulbackup.mfa.gov.am
www.army.am
cms.edu.am
forum.edu.am
armavir.school.edu.am
ysuac.edu.am
mail.edu.am
www.edu.am
new.edu.am
art.school.edu.am
yvn149.school.edu.am
yvn83.school.edu.am
chat.edu.am
hrz13.school.edu.am
seua.edu.am
ysitc.edu.am
yvn51.school.edu.am
dl.edu.am
apr.school.edu.am
hrz8.school.edu.am
kapan.school.edu.am
yvn132.school.edu.am
blog.edu.am
gorec.edu.am
gyumrisp.school.edu.am
yvn27.school.edu.am
download.edu.am
gps.edu.am
artik.school.edu.am
kech.school.edu.am
vancoll1.school.edu.am
yvn55.school.edu.am
yvn78.school.edu.am
www.stanfort.edu.am
webmail.edu.am
proxy.edu.am
vardans.school.edu.am
ysu.edu.am
```
</details>

### Live Host Fingerprinting
```
https://admin.car.mia.gov.am [[33m302[0m] [] [[35mHSTS,HTTP/3[0m]
https://api.car.mia.gov.am [[31m404[0m] [] [[35mHSTS,HTTP/3[0m]
https://adams.gov.am [[32m200[0m] [] [[35mExpress,Node.js,jQuery,particles.js[0m]
https://auction.mia.gov.am [[33m302[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,PHP:8.1.27,Windows Server[0m]
https://benefits.hightech.gov.am [[32m200[0m] [[36mMendix[0m] [nginx] [[35mNginx[0m]
https://autodiscover.ai.gov.am [[31m400[0m] [Apache] [[35mApache HTTP Server[0m]
https://anti-corruption.gov.am [[32m200[0m] [[36mՀակակոռուպցիոն մոնիթորինգի հարթակ[0m] [] [[35mHSTS,Node.js,Nuxt.js,Vue.js[0m]
https://car.mia.gov.am [[33m302[0m] [] [[35mHSTS,HTTP/3[0m]
https://ai.gov.am [[32m200[0m] [[36mՀայաստանի Հանրապետության Նախարարություն[0m] [] [[35mAmazon CloudFront,Amazon Web Services,HSTS,Node.js,Nuxt.js,Vue.js[0m]
https://cert.gov.am [[32m200[0m] [[36mՀամակարգչային միջադեպերի արձագանքման պետական կենտրոն[0m] [nginx] [[35mNginx,reCAPTCHA[0m]
https://cpcalendars.ai.gov.am [[31m401[0m] [cPanel] [[35mBasic[0m]
https://diaspora.gov.am [[31m403[0m] [[36m403 Forbidden[0m] [Apache] [[35mApache HTTP Server[0m]
https://cpcontacts.ai.gov.am [[31m401[0m] [cPanel] [[35mBasic[0m]
https://cpanel.ai.gov.am [[32m200[0m] [[36mcPanel Login[0m] [Apache] [[35mApache HTTP Server,cPanel[0m]
https://env.gov.am [[33m301[0m] [Caddy] [[35mAmazon CloudFront,Amazon Web Services,Caddy,HSTS,HTTP/3[0m]
https://elearning.cso.gov.am [[32m200[0m] [[36mՔաղաքացիական ծառայողների վերապատրաստման հարթակ[0m] [Apache/2.4.29 (Ubuntu)] [[35mApache HTTP Server:2.4.29,Moodle,PHP,RequireJS,Slick,Ubuntu,jQuery:3.2.1[0m]
https://hightech.gov.am [[33m301[0m] [Apache] [[35mApache HTTP Server[0m]
https://elections.mia.gov.am [[32m200[0m] [[36mՀՀ ներքին գործերի նախարարություն Ընտրողների ցուցակ[0m] [] [[35mAmazon CloudFront,Amazon Web Services,HSTS,HTTP/3,Node.js,Nuxt.js,Vue.js[0m]
https://mail.diaspora.gov.am [[32m200[0m] [[36mZimbra Web Client Sign In[0m] [nginx] [[35mJava,Nginx,Zimbra[0m]
https://elearning.mta.gov.am [[32m200[0m] [[36mԳլխավոր | ՀՀ ՏԿԵՆ հեռավար ուսուցման կառավարման համակարգ[0m] [Apache/2.4.58 (Ubuntu)] [[35mApache HTTP Server:2.4.58,MathJax:2.7.9,Moodle,PHP,RequireJS,Tiny Slider,Ubuntu,jsDelivr[0m]
https://environment.gov.am [[32m200[0m] [[36mՀայաստանի Հանրապետության շրջակա միջավայրի նախարարություն[0m] [] [[35mAmazon CloudFront,Amazon Web Services,HSTS,HTTP/3,Node.js,Nuxt.js,Vue.js[0m]
https://mail.ecoinspect.gov.am [[32m200[0m] [[36mZimbra Web Client Sign In[0m] [] [[35mJava,Zimbra[0m]
http://mail.ai.gov.am [[31m403[0m] [[36mERROR: The request could not be satisfied[0m] [CloudFront] [[35mAmazon CloudFront,Amazon Web Services[0m]
https://mail.msib.gov.am [[32m200[0m] [[36mZimbra Web Client Sign In[0m] [] [[35mJava,Zimbra[0m]
https://mail.utfsib.gov.am [[32m200[0m] [[36mZimbra Web Client Sign In[0m] [] [[35mJava,Zimbra[0m]
http://mail.mta.gov.am [[33m301[0m] [[36m301 Moved Permanently[0m] [nginx] [[35mNginx[0m]
http://migration.mia.gov.am [[33m301[0m] [[36m301 Moved Permanently[0m] [CloudFront] [[35mAmazon CloudFront,Amazon Web Services,HTTP/3[0m]
https://mul.mieir.gov.am [[31m403[0m] [nginx] [[35mNginx[0m]
https://moj.gov.am [[32m200[0m] [[36mՀայաստանի Հանրապետության արդարադատության նախարարություն[0m] [] [[35mAmazon CloudFront,Amazon Web Services,HSTS,HTTP/3,Node.js,Nuxt.js,Vue.js[0m]
https://mia.gov.am [[32m200[0m] [[36mMinistry of Internal Affairs of the Republic of Armenia – Official website[0m] [Apache/2.4.54 (Debian)] [[35mApache HTTP Server:2.4.54,Debian,Google Analytics,MySQL,PHP,Site Kit:1.171.0,WPML:4.5.14,WordPress:6.2,jQuery[0m]
```

### DNS / DMARC Analysis
```
--- gov.am ---
20 mail2.gov.am.
10 mail.gov.am.
"v=DMARC1; p=reject; rua=mailto:postmaster@gov.am;ruf=mailto:postmaster@gov.am;"
--- parliament.am ---
10 mail.parliament.am.
"v=DMARC1; p=reject; pct=100; rua=mailto:admin@parliament.am; fo=1"
--- mil.am ---
10 mail.mil.am.
"v=DMARC1; p=quarantine; rua=mailto:failed@mil.am; ruf=mailto:failed@mil.am; aspf=s; adkim=s;"
--- finance.gov.am ---
--- health.gov.am ---
--- mfa.gov.am ---
--- police.gov.am ---
--- justice.gov.am ---
--- army.am ---
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; communications error to 127.0.0.53#53: timed out
;; no servers could be reached
--- edu.am ---
10 webmail.edu.am.
```

### Historical URLs (Sample)
```

```

## Video Documentation
🎬 [OSINT Tourism: Armenia](https://archive.org/details/odint-armenia-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
