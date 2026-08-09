# Bulgaria — Passive Reconnaissance Report
**Date:** February 2026  
**Scope:** Government digital infrastructure (.bg TLD)  
**Method:** 100% passive — no active exploitation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Subdomains discovered | 135 |
| Live hosts fingerprinted | 42 |
| DNS/DMARC records analyzed | 14 |
| Historical URLs (GAU) | 430738 |

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
incolab.vt.riew.gov.bg
mail.plovdiv.riew.gov.bg
ob.kovachevci.gov.bg
apostille.gov.bg
ns1.moew.gov.bg
stg2.cixpbg.gov.bg
mail.stz.riew.gov.bg
cpanel.sars.gov.bg
plovdiv.riew.gov.bg
smtp.vt.riew.gov.bg
ob.strumiani.gov.bg
riew.gov.bg
popeinbulgaria.gov.bg
soc.nssa.gov.bg
test-sipbg.gov.bg
login.iamn.gov.bg
ns1.plovdiv.gov.bg
www.msoft.gov.bg
gw.plovdiv.gov.bg
mgt.stg2.cixpbg.gov.bg
```
<details><summary>Full list (135 subdomains)</summary>

```
incolab.vt.riew.gov.bg
mail.plovdiv.riew.gov.bg
ob.kovachevci.gov.bg
apostille.gov.bg
ns1.moew.gov.bg
stg2.cixpbg.gov.bg
mail.stz.riew.gov.bg
cpanel.sars.gov.bg
plovdiv.riew.gov.bg
smtp.vt.riew.gov.bg
ob.strumiani.gov.bg
riew.gov.bg
popeinbulgaria.gov.bg
soc.nssa.gov.bg
test-sipbg.gov.bg
login.iamn.gov.bg
ns1.plovdiv.gov.bg
www.msoft.gov.bg
gw.plovdiv.gov.bg
mgt.stg2.cixpbg.gov.bg
autodiscover.stz.riew.gov.bg
sipbg.gov.bg
eagle.gov.bg
mail.plovdiv.gov.bg
bs.gov.bg
owa.iamn.gov.bg
logan.cixpbg.gov.bg
bm.cixpbg.gov.bg
jastice.gov.bg
vt.riew.gov.bg
autodiscover.sars.gov.bg
truenas.gov.bg
cixpbg.gov.bg
manager.cixpbg.gov.bg
manager-stg.cixpbg.gov.bg
stg-mgt.cixpbg.gov.bg
bm.mgt.cixpbg.gov.bg
sars.gov.bg
auth-stg.cixpbg.gov.bg
www.ukraine.gov.bg
bg-eupresidency.gov.bg
www.md.gov.bg
apo.gov.bg
backend.cixpbg.gov.bg
www.new.stz.riew.gov.bg
webdisk.stz.riew.gov.bg
mh.gov.bg
www.mjeli.gov.bg
new.gov.bg
jellyfin.gov.bg
ocp-reg.soc.nssa.gov.bg
bg11norwaygrants.gov.bg
www.popeinbulgaria.gov.bg
sun450.gov.bg
www.sars.gov.bg
internet.moew.gov.bg
www.vt.riew.gov.bg
cpcontacts.stz.riew.gov.bg
webmail.stz.riew.gov.bg
www.bulgaria.gov.bg
mail.sars.gov.bg
www.gov.bg
cpcalendars.stz.riew.gov.bg
leo.gov.bg
srv23.plovdiv.gov.bg
srv23.pd.gov.bg
islastor.gov.bg
www.stz.riew.gov.bg
pd.gov.bg
internet.riew.gov.bg
plovdiv.gov.bg
auth.cixpbg.gov.bg
auth-cixpbg.gov.bg
smtp2.vt.riew.gov.bg
www.bs.gov.bg
stg.cixpbg.gov.bg
manager-cixpbg.gov.bg
mgt.stg.cixpbg.gov.bg
mail.bs.gov.bg
cpanel.stz.riew.gov.bg
gis.sars.gov.bg
survey.ukraine.gov.bg
is.la.gov.bg
ftptv.gov.bg
mail.pd.gov.bg
mig.gov.bg
sir.nssa.gov.bg
mgt.cixpbg.gov.bg
www.gosi.gov.bg
ukraine.gov.bg
stz.riew.gov.bg
mail.gov.bg
www.sipbg.gov.bg
www.bg-eupresidency.gov.bg
justice.gov.bg
msoft.gov.bg
new.stz.riew.gov.bg
bul.gov.bg
ns2.parliament.bg
ns.parliament.bg
nagate.parliament.bg
mail.abatnt.parliament.bg
viper.parliament.bg
mail.parliament.bg
dv.parliament.bg
oldlibrary.parliament.bg
www1.parliament.bg
www2.parliament.bg
intranet.parliament.bg
halls.abatnt.parliament.bg
vco.parliament.bg
fs.parliament.bg
snake.parliament.bg
old.parliament.bg
students.parliament.bg
satory.parliament.bg
jury.parliament.bg
library.parliament.bg
www.parliament.bg
valinor.parliament.bg
autodiscover.mil.bg
webdisk.mil.bg
webmail.mil.bg
army.mil.bg
www.af.mil.bg
cpanel.mil.bg
www.navy.mil.bg
www.jfc.mil.bg
navy.mil.bg
www.army.mil.bg
af.mil.bg
jfc.mil.bg
mx.mil.bg
www.mil.bg
mail.mil.bg
```
</details>

### Live Host Fingerprinting
```
https://autodiscover.sars.gov.bg [[33m302[0m] [BigIP] [[35mF5 BigIP[0m]
https://dv.parliament.bg [[32m200[0m] []
https://apostille.gov.bg [[32m200[0m] [[36mCheck apostille - DocSys Perfect V3 GSL[0m] [nginx/1.18.0 (Ubuntu)] [[35mBootstrap,Express,Nginx:1.18.0,Node.js,Ubuntu,jQuery[0m]
https://apo.gov.bg [[33m307[0m] [nginx/1.18.0 (Ubuntu)] [[35mExpress,Nginx:1.18.0,Node.js,Ubuntu[0m]
https://gis.sars.gov.bg [[32m200[0m] [Microsoft-IIS/10.0] [[35mHSTS,IIS:10.0,Microsoft ASP.NET,Windows Server[0m]
https://library.parliament.bg [[33m302[0m] []
https://mail.mil.bg [[33m301[0m] [[36m301 Moved Permanently[0m] [Apache/2.4.66 (Debian)] [[35mApache HTTP Server:2.4.66,Debian[0m]
https://mail.pd.gov.bg [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mNginx[0m]
https://mail.sars.gov.bg [[33m302[0m] [BigIP] [[35mF5 BigIP[0m]
https://mail.plovdiv.riew.gov.bg [[32m200[0m] [[36mРИОСВ - Пловдив :: Официален сайт[0m] [LiteSpeed] [[35mBootstrap:5.3.3,Cloudflare,Font Awesome,HSTS,HTTP/3,LiteSpeed,PHP,Slick:1.9.0,cdnjs,jQuery CDN,jQuery:3.7.1,jsDelivr[0m]
https://mail.plovdiv.gov.bg [[31m403[0m] [[36m403 Forbidden[0m] [nginx] [[35mNginx[0m]
https://mail.stz.riew.gov.bg [[33m301[0m] [[36m301 Moved Permanently[0m] [Apache] [[35mApache HTTP Server[0m]
https://bs.gov.bg [[32m200[0m] [[36mОбластна администрация Бургас – Полезна информация за 13-те общини в област Бургас, новини за дейността на областната администрация и предлаганите услуги.[0m] [Apache] [[35mApache HTTP Server,Contact Form 7:6.1.5,Google Maps,HSTS,Max Mega Menu:3.7,MySQL,PHP,Packery:3.20.3,WordPress,jQuery,jQuery Migrate:3.4.1[0m]
http://auth-stg.cixpbg.gov.bg [[31m403[0m] [[36m403 Forbidden[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
http://auth.cixpbg.gov.bg [[31m404[0m] [[36m404 Not Found[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
https://mig.gov.bg [[33m301[0m] [Apache] [[35mApache HTTP Server,PHP:7.4.3,Ubuntu[0m]
https://oldlibrary.parliament.bg [[32m200[0m] [[36mGoto ABS[0m] []
https://old.parliament.bg [[32m200[0m] [[36mНародно събрание на Република България - Начало[0m] [] [[35mBootstrap:3.1.1,BootstrapCDN:3.1.1,Google Hosted Libraries,SWFObject,SyntaxHighlighter,jQuery CDN,jQuery UI,jQuery:1.8.1,parallax.js[0m]
https://plovdiv.riew.gov.bg [[32m200[0m] [[36mРИОСВ - Пловдив :: Официален сайт[0m] [LiteSpeed] [[35mBootstrap:5.3.3,Cloudflare,Font Awesome,HSTS,HTTP/3,LiteSpeed,PHP,Slick:1.9.0,cdnjs,jQuery CDN,jQuery:3.7.1,jsDelivr[0m]
https://sars.gov.bg [[33m301[0m] [nginx/1.20.1] [[35mHSTS,Nginx:1.20.1,PHP:8.3.30[0m]
https://sipbg.gov.bg [[32m200[0m] [Microsoft-IIS/10.0] [[35mIIS:10.0,Windows Server[0m]
http://cixpbg.gov.bg [[31m404[0m] [[36m404 Not Found[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
http://manager-stg.cixpbg.gov.bg [[31m403[0m] [[36m403 Forbidden[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
https://pd.gov.bg [[32m200[0m] [[36mОбластна администрация Пловдив[0m] [Apache/2.4.58 (Ubuntu)] [[35mApache HTTP Server:2.4.58,Contact Form 7:6.1.5,Cookie Notice:2.5.13,Font Awesome,HSTS,Modernizr,MySQL,PHP,Polylang,Ubuntu,WordPress Block Editor,WordPress:6.9.1,imagesLoaded:5.0.0,jQuery,jQuery Migrate:3.4.1,reCAPTCHA[0m]
http://manager.cixpbg.gov.bg [[31m404[0m] [[36m404 Not Found[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
http://mgt.cixpbg.gov.bg [[31m404[0m] [[36m404 Not Found[0m] [nginx/1.26.2] [[35mNginx:1.26.2[0m]
https://stz.riew.gov.bg [[32m200[0m] [[36mРегионална инспекция по околната среда и водите - РИОСВ -Стара Загора[0m] [Apache] [[35mApache HTTP Server,PHP,jQuery[0m]
https://test-sipbg.gov.bg [[32m200[0m] [nginx/1.18.0 (Ubuntu) https://test-sipbg.gov.bg] [[35mHSTS,Microsoft ASP.NET,Nginx:1.18.0,Ubuntu[0m]
https://vt.riew.gov.bg [[32m200[0m] [[36mSite Maintenance[0m] [Apache] [[35mApache HTTP Server[0m]
https://ukraine.gov.bg [[32m200[0m] [[36mБългария с грижа за хората от Украйна | Bulgaria for Ukraine[0m] [Apache/2.4.52 (Unix) OpenSSL/1.0.2k-fips] [[35mApache HTTP Server:2.4.52,Azure Edge Network,Bootstrap,Complianz,Elementor:3.6.6,Google Analytics,Ivory Search:5.4.7,Modernizr,MySQL,OpenSSL:1.0.2k,PHP:7.4.28,Slick,Slider Revolution:6.5.14,UIKit,UNIX,Underscore.js:1.13.3,WPForms:1.7.4.2,WordPress:6.0.11,Yoast SEO:19.2,imagesLoaded:4.1.4,jQuery,jQuery Migrate:3.3.2[0m]
```

### DNS / DMARC Analysis
```
--- gov.bg ---
--- parliament.bg ---
10 snake.parliament.bg.
20 viper.parliament.bg.
"v=DMARC1; p=quarantine; rua=mailto:dmarc@parliament.bg; ruf=mailto:dmarc@parliament.bg"
"v=spf1 ip4:193.109.54.90/32 ip4:193.109.54.91/32 -all"
--- mil.bg ---
10 mx.mil.bg.
"v=spf1 include:_spf.mboxhosting.com ~all"
--- finance.gov.bg ---
--- health.gov.bg ---
--- mfa.gov.bg ---
--- police.gov.bg ---
--- justice.gov.bg ---
```

### Historical URLs (Sample)
```
http://www.gov.bg:80/
http://www.gov.bg/%D0%90%D0%B4%D1%80%D0%B5%D1%81
https://www.gov.bg/%E2%80%A6/BG%20RRP%20final%20presentation.pdf
https://www.gov.bg/&sa=U&ved=2ahUKEwiNxIevydiJAxUKEVkFHbwdFhAQFnoECAIQAg&usg=AOvVaw3vMKH16D3_PVcsVqBnYzqp
https://www.gov.bg//)
https://www.gov.bg/.well-known/ai-plugin.json
https://www.gov.bg/.well-known/assetlinks.json
https://www.gov.bg/.well-known/dnt-policy.txt
https://www.gov.bg/.well-known/gpc.json
https://www.gov.bg/.well-known/nodeinfo
https://www.gov.bg/.well-known/openid-configuration
https://www.gov.bg/.well-known/security.txt
https://www.gov.bg/.well-known/trust.txt
http://gov.bg/2022/11/16/%D1%81%D1%80%D0%BE%D0%BA%D1%8A%D1%82-%D0%BD%D0%B0-%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B0%D1%82%D0%B0-%D0%B7%D0%B0-%D1%85%D1%83/
https://www.gov.bg/?locale=bg
https://gov.bg/?ref=university.heavnn.io
https://gov.bg/?trk=organization_guest_main-feed-card-text
https://www.gov.bg/a
http://www.gov.bg/ads.txt
https://www.gov.bg/app-ads.txt
```

## Video Documentation
🎬 [OSINT Tourism: Bulgaria](https://archive.org/details/odint-bulgaria-passive-recon-2026)

## Disclosure
This research is purely observational. No systems were accessed, no credentials tested,  
no exploitation attempted. All data was obtained from publicly available sources.

---
*Contributed by [OptinAmpOut](https://optinampout.com) — Archonic Sentinel*
