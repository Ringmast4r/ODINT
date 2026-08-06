# ODINT Collection Checklist

**Total items: 1,265**

---

## Identity & Personnel
1. Usernames (from APIs, WP enumeration, documents, error messages, URL paths, code comments)
2. Email addresses (from APIs, WHOIS, SSL certs, documents, source code, JS files, contact pages, mailing lists)
3. Display names / full names
4. Gravatar hashes (MD5/SHA256 of emails from WordPress avatar_urls)
5. Personnel org charts & roles
6. Phone numbers
7. Physical addresses
8. National ID numbers
9. Dates of birth
10. Social media accounts & profiles

## Hashes & Credentials
11. MD5 hashes
12. SHA1 hashes
13. SHA256 hashes
14. bcrypt/scrypt hashes
15. Password hashes (from database dumps, backups, logs)
16. Gravatar MD5 hashes (from WP REST API avatar_urls)
17. Gravatar SHA256 hashes (newer implementations)
18. Cracked hash values (reversed emails/passwords)
19. Cross-site hash correlations (same hash on multiple domains)
20. Exposed API keys & tokens
21. OAuth/JWT/session tokens (decode JWTs for claims)
22. Exposed passwords (in configs, logs, JS, .env, database dumps, URL params, debug output)
23. SSH public keys
24. PGP keys
25. Encryption keys
26. Password reset tokens
27. Webhook secrets
28. AWS access keys
29. Azure keys
30. Google API keys
31. Stripe/payment keys
32. File integrity hashes
33. Session token hashes

## Domains & Subdomains
34. Primary domains
35. Subdomain enumeration results

### Subdomain Enumeration Sources
36. Certificate Transparency logs (crt.sh)
37. Censys certificate search
38. Google CT logs
39. Facebook CT logs
40. Passive DNS lookups
41. SecurityTrails historical data
42. DNSdumpster results
43. Amass passive mode output
44. Subfinder results
45. Assetfinder results
46. MassDNS passive results
47. Wildcard certificate SAN entries
48. Historical/pre-certificates
49. Staging/dev subdomains (dev., staging., test., beta., uat.)
50. Mobile subdomains (m., mobile., app.)
51. API subdomains (api., rest., graphql.)
52. Mail subdomains (mail., smtp., imap., pop., webmail., owa.)
53. Admin subdomains (admin., portal., dashboard., cpanel.)
54. CDN subdomains (cdn., static., assets., media.)
55. Internal subdomains (intranet., internal., vpn.)

## DNS Records (Complete Enumeration)
56. A records (IPv4)
57. AAAA records (IPv6)
58. MX records (mail servers)
59. TXT records (SPF, DKIM, DMARC, domain verification tokens)
60. NS records (nameservers)
61. SOA records (authority)
62. CNAME records (aliases)
63. SRV records (services)
64. CAA records (certificate authority authorization)
65. PTR records (reverse DNS)
66. SPF record parsing
67. DKIM selector enumeration
68. DMARC policy check

## IP & Network Infrastructure
69. Resolved IP addresses (IPv4 + IPv6)
70. IP netblocks / ranges
71. ASN number & organization
72. BGP routing data & peering relationships
73. Reverse DNS (PTR records)
74. IP geolocation (country, city, coordinates)
75. Hosting provider identification
76. CDN identification & mapping
77. Load balancer identification
78. WAF / DDoS protection detection
79. Network topology
80. Proxy/reverse proxy detection

## Port Scanning (via Port Scanner tool)
81. Open TCP ports per target
82. Service identification per port
83. Port scan timestamps
84. Service banners
85. Common ports: 21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 143 (IMAP), 443 (HTTPS), 445 (SMB), 993 (IMAPS), 995 (POP3S), 1433 (MSSQL), 3306 (MySQL), 3389 (RDP), 5432 (PostgreSQL), 5900 (VNC), 6379 (Redis), 8080 (HTTP-alt), 8443 (HTTPS-alt), 27017 (MongoDB)

## Passive OSINT Intelligence (via Silent Eye)
86. Censys exposed infrastructure data
87. Shodan device/service data
88. crt.sh certificate transparency data
89. VirusTotal domain/IP intelligence
90. SecurityTrails DNS history & subdomains
91. Hunter.io email discovery
92. BGPView network/ASN data
93. ipinfo.io IP metadata

## TLS/SSL
94. SSL certificate subject (CN, O, OU, L, ST, C)
95. SSL certificate issuer (full chain)
96. Certificate serial number
97. Certificate validity dates (from/to)
98. Signature algorithm
99. Public key algorithm & size (bits)
100. Subject Alternative Names (SANs) - reveals other domains
101. Certificate fingerprint (SHA256)
102. Full certificate chain
103. OCSP stapling status
104. Certificate Transparency SCTs
105. TLS version (1.0, 1.1, 1.2, 1.3)
106. Cipher suite used
107. Key exchange algorithm
108. Perfect Forward Secrecy (PFS) support
109. ALPN (HTTP/2, HTTP/3 support)
110. Session resumption support
111. Certificate revocation status
112. SSL security issues (SSLv2/v3 enabled, TLS 1.0/1.1, weak ciphers, self-signed, name mismatch, incomplete chain, expiring)
113. HSTS status & preload

## DNS Resolution & HTTP Probing (via Frankenstein)
114. DNS resolution results per domain (A, AAAA, CNAME)
115. HTTP/HTTPS reachability probing
116. TLS certificate analysis per domain
117. Live vs dead domain classification
118. Retry pass results for flaky targets

---

## Full Tech Stack

### Web Server
119. Web server software & version (Apache, Nginx, IIS, LiteSpeed, Caddy, Tomcat)
120. Server OS fingerprint (Linux distro, Windows Server version)
121. Web server modules (mod_ssl, mod_rewrite, mod_pagespeed, mod_deflate, mod_security)

### Reverse Proxy & Load Balancer
122. Reverse proxy detection & identification
123. HAProxy (SERVERID cookie, X-Haproxy-* headers)
124. Envoy proxy (x-envoy-* headers)
125. Traefik (X-Traefik-* headers)
126. F5 BIG-IP (BIGipServer* cookies)
127. AWS ALB/ELB (AWSALB cookies, X-Amzn-* headers)
128. Azure Application Gateway (ARRAffinity cookie)
129. Google Cloud Load Balancing

### API Gateway
130. Kong (X-Kong-* headers)
131. AWS API Gateway (x-amzn-requestid, x-amz-apigw-id)
132. Azure API Management
133. Apigee (Google)
134. Traefik as API gateway
135. Tyk
136. MuleSoft

### Hosting Control Panels (exposed login pages)
137. cPanel
138. Plesk
139. DirectAdmin
140. Webmin
141. CyberPanel
142. ISPConfig
143. Virtualmin

### Serverless Indicators
144. AWS Lambda (x-amzn-requestid, API Gateway patterns)
145. Azure Functions
146. Google Cloud Functions
147. Cloudflare Workers
148. Vercel Edge Functions / Serverless Functions
149. Netlify Functions

### Container & Orchestration
150. Docker indicators (/.dockerenv, docker-compose.yml, Dockerfile exposed)
151. Kubernetes (K8s) indicators (ingress patterns, pod headers, /healthz endpoints)
152. Amazon ECS / EKS
153. Google GKE
154. Azure AKS
155. Docker Swarm indicators
156. HashiCorp Nomad
157. Exposed Docker registries
158. Container image tags / version info in headers

### Protocols
159. HTTP/1.1 support
160. HTTP/2 support (h2, h2c)
161. HTTP/3 (QUIC) support (Alt-Svc header)
162. WebSocket endpoints (ws://, wss://)
163. gRPC-web indicators
164. Server-Sent Events (SSE) endpoints
165. SPDY (legacy, if still present)

### CMS
166. WordPress (version, theme name & version, all plugins & versions)
167. Drupal (version, modules)
168. Joomla (version, extensions)
169. Sitecore (version)
170. Umbraco (version)
171. Adobe Experience Manager
172. Headless CMS (Contentful, Strapi, Directus, Ghost)
173. Typo3
174. Kentico
175. DotNetNuke (DNN)
176. Craft CMS
177. Concrete CMS
178. Custom CMS identification

### WordPress Ecosystem
179. Page builders (Elementor, Divi, WPBakery, Beaver Builder, Gutenberg blocks)
180. SEO plugins (Yoast, Rank Math, All in One SEO, SEOPress)
181. Backup plugins (UpdraftPlus, BackWPup, VaultPress/Jetpack Backup, WPvivid)
182. Cache plugins (WP Super Cache, W3 Total Cache, LiteSpeed Cache, WP Rocket, WP Fastest Cache)
183. Security plugins (Wordfence, Sucuri, iThemes Security, All In One WP Security)
184. Multilingual plugins (WPML, Polylang, Weglot, TranslatePress)
185. Form plugins (Contact Form 7, WPForms, Gravity Forms, Ninja Forms)
186. Slider/gallery plugins (Slider Revolution, MetaSlider, NextGEN Gallery)
187. Membership/paywall plugins

### Backend Framework & Language
188. PHP version
189. Python version (Django, Flask)
190. Node.js version (Express, Koa, Fastify)
191. .NET version (ASP.NET, .NET Core)
192. Java version (Spring Boot, Struts)
193. Ruby (Rails)
194. Go frameworks (Gin, Echo, Fiber)
195. Rust frameworks (Actix, Rocket, Axum)

### Additional PHP Frameworks
196. CodeIgniter
197. CakePHP
198. Yii / Yii2
199. Slim
200. Lumen (lightweight Laravel)
201. FuelPHP
202. Phalcon

### Additional Python Frameworks
203. FastAPI
204. Tornado
205. Pyramid
206. Starlette
207. Bottle
208. Falcon
209. Sanic

### Frontend Framework & Libraries
210. React / React version
211. Vue.js / Nuxt.js
212. Angular / AngularJS
213. Next.js
214. Svelte / SvelteKit
215. Gatsby
216. jQuery version
217. Bootstrap version
218. Tailwind CSS
219. Material UI / MUI
220. Chakra UI
221. Ant Design
222. Foundation (Zurb)
223. Bulma
224. Semantic UI
225. Alpine.js
226. HTMX
227. Lit / Web Components
228. Stimulus (Hotwire)
229. Turbo (Hotwire)

### Static Site Generators
230. Hugo
231. Jekyll
232. Eleventy (11ty)
233. Pelican
234. Hexo
235. Astro
236. Docusaurus
237. MkDocs
238. VuePress / VitePress

### Database Indicators
239. MySQL / MariaDB
240. PostgreSQL
241. Microsoft SQL Server
242. MongoDB
243. Redis
244. Elasticsearch
245. Oracle
246. SQLite indicators

### Additional Database Types
247. Graph databases: Neo4j, ArangoDB, Amazon Neptune
248. Time-series databases: InfluxDB, TimescaleDB, Prometheus TSDB
249. Search engines: Apache Solr, Algolia, Meilisearch, Typesense
250. Object storage: MinIO (self-hosted S3-compatible)
251. Key-value stores: DynamoDB, Etcd, Consul KV
252. Column stores: Cassandra, ScyllaDB, HBase
253. Document stores: CouchDB, Couchbase, RavenDB

### Message Queue & Streaming (exposed management UIs / indicators)
254. RabbitMQ (management UI, AMQP indicators)
255. Apache Kafka (indicators, Kafka Connect)
256. NATS
257. Redis Pub/Sub / Redis Streams
258. Amazon SQS / SNS indicators
259. Azure Service Bus
260. Google Pub/Sub

### Hosting & Cloud
261. AWS (S3, EC2, CloudFront, Lambda, ELB, RDS, etc.)
262. Azure services
263. Google Cloud Platform
264. DigitalOcean
265. Cloudflare
266. Vercel / Netlify
267. Heroku
268. OVH / Hetzner / other VPS
269. Linode / Akamai Connected Cloud
270. Vultr
271. On-premise indicators

### DNS Providers (from NS records)
272. Cloudflare DNS
273. AWS Route 53
274. Azure DNS
275. Google Cloud DNS
276. NS1
277. DNSimple
278. GoDaddy DNS
279. Local/self-hosted DNS

### CDN & Caching
280. Cloudflare
281. Akamai
282. Fastly
283. AWS CloudFront
284. Azure CDN
285. Google Cloud CDN
286. StackPath / MaxCDN
287. KeyCDN
288. BunnyCDN

### Application-Level Caching
289. Varnish cache (X-Varnish header)
290. Redis cache
291. Memcached indicators
292. PHP OPcache
293. APCu (PHP user cache)
294. Cloudflare Rocket Loader / Polish / Mirage / APO
295. WordPress cache plugins (WP Super Cache, W3 Total Cache, LiteSpeed Cache, WP Rocket, WP Fastest Cache)
296. Nginx FastCGI cache / microcaching
297. Page cache indicators (X-Cache, X-Cache-Status headers)

### Build Tools & Bundlers
298. Webpack (bundle filenames, chunk patterns, runtime.js)
299. Vite (_vite folder, module preload)
300. Parcel
301. Rollup
302. esbuild indicators
303. Turbopack (Next.js)
304. Source map exposure (.js.map, .css.map)

### Authentication & SSO
305. OAuth providers
306. SAML endpoints
307. OpenID Connect
308. LDAP/Active Directory indicators
309. Custom auth systems
310. MFA indicators
311. National ID systems (NemID, BankID, etc.)
312. CAS (Central Authentication Service)
313. Kerberos indicators
314. Auth0 / Okta / OneLogin / Ping Identity indicators

### Session Management
315. PHP sessions (PHPSESSID cookie)
316. Java sessions (JSESSIONID cookie)
317. .NET sessions (ASP.NET_SessionId cookie)
318. Redis-backed sessions
319. Memcached-backed sessions
320. JWT-based sessions (token in cookie or header)
321. Sticky sessions / session affinity (load balancer cookies)

### Ecommerce
322. WooCommerce
323. Shopify
324. Magento / Adobe Commerce
325. PrestaShop
326. OpenCart
327. Shopify Hydrogen (headless)
328. Medusa
329. Saleor
330. Custom cart systems

### Payment Gateways
331. Stripe
332. PayPal
333. Square
334. Adyen
335. Braintree
336. Razorpay
337. PayU
338. 2Checkout / Verifone
339. Klarna
340. Mollie
341. Authorize.net
342. WorldPay

### Email Infrastructure
343. Mail server (from MX records)
344. Microsoft 365 / Exchange
345. Google Workspace
346. SMTP services (SendGrid, Mailchimp/Mandrill, Amazon SES, Postmark, SparkPost)
347. Webmail portals (OWA, Roundcube, Horde, SOGo, Zimbra)
348. Exchange autodiscover
349. Mimecast / Barracuda email security

### Marketing & Newsletter Platforms
350. HubSpot (tracking script, forms)
351. Marketo (Munchkin tracking)
352. Pardot (Salesforce)
353. Mailchimp (embedded forms, tracking)
354. Constant Contact
355. ActiveCampaign
356. Klaviyo
357. Drip
358. ConvertKit

### Security Tools & WAF
359. Wordfence (WordPress)
360. Sucuri (WAF + monitoring)
361. reCAPTCHA v2/v3 (site key extractable)
362. hCaptcha
363. Cloudflare Turnstile
364. Rate limiting indicators
365. ModSecurity rules
366. Imperva / Incapsula WAF
367. AWS WAF
368. Azure WAF
369. Barracuda WAF
370. Fortinet FortiWeb

### Bot Protection (beyond WAF)
371. Cloudflare Bot Management
372. PerimeterX / HUMAN Security
373. DataDome
374. Shape Security (F5)
375. Kasada
376. Akamai Bot Manager

### DDoS Protection
377. Cloudflare DDoS protection
378. Akamai Prolexic
379. AWS Shield
380. Radware
381. Arbor Networks / Netscout

### Cookie Consent & Privacy
382. OneTrust
383. Cookiebot
384. CookieYes
385. Osano
386. TrustArc
387. Complianz (WordPress)
388. GDPR Cookie Consent plugins

### VPN / Remote Access (exposed login portals)
389. Pulse Secure / Ivanti Connect Secure
390. Citrix Gateway / NetScaler
391. GlobalProtect (Palo Alto)
392. Fortinet VPN (FortiGate SSL-VPN)
393. OpenVPN Access Server
394. Cisco AnyConnect / ASA WebVPN
395. SonicWall VPN
396. WireGuard (public endpoint indicators)

### Firewall / Network Appliances (exposed login pages)
397. Palo Alto Networks (PAN-OS login)
398. Fortinet FortiGate
399. Check Point
400. pfSense / OPNsense
401. Sophos XG / UTM
402. Cisco ASA / Firepower
403. SonicWall
404. Juniper SRX
405. MikroTik RouterOS (Winbox/WebFig)
406. Ubiquiti UniFi

### Collaboration & Document Management (exposed portals)
407. SharePoint
408. Confluence
409. Jira
410. Bitbucket Server
411. Nextcloud / ownCloud
412. Alfresco
413. Moodle (education LMS)
414. Canvas LMS
415. GitLab self-hosted
416. Redmine
417. Wiki.js / MediaWiki / DokuWiki

### Ticketing & Helpdesk
418. ServiceNow
419. Zendesk (support portal URLs)
420. Freshdesk / Freshservice
421. OTRS
422. osTicket
423. Jira Service Management
424. ManageEngine ServiceDesk

### CRM / ERP (exposed portals)
425. Salesforce
426. SAP (Fiori, NetWeaver, S/4HANA portals)
427. Oracle (EBS, Cloud portals)
428. Microsoft Dynamics 365
429. SugarCRM
430. Odoo
431. Zoho

### Exposed Management UIs & Dashboards
432. phpMyAdmin
433. Adminer
434. pgAdmin
435. MongoDB Compass Web / Mongo Express
436. Redis Commander / RedisInsight
437. Kibana (Elasticsearch dashboards)
438. Grafana (monitoring dashboards)
439. Prometheus UI
440. Jenkins (CI/CD)
441. GitLab CI dashboards
442. Drone CI
443. ArgoCD
444. RabbitMQ Management UI
445. Flower (Celery task monitor)
446. Nagios / Icinga
447. Zabbix
448. Datadog (agent indicators)
449. New Relic (agent indicators)
450. Sentry (error tracking, DSN in JS)
451. Portainer (Docker management)
452. Kubernetes Dashboard
453. Rancher
454. Consul UI
455. Vault UI (HashiCorp)
456. MinIO Console
457. Solr Admin UI
458. Elasticsearch Head / Cerebro
459. Traefik Dashboard

### Monitoring & Observability (indicators)
460. Datadog (dd-agent, dd-trace headers)
461. New Relic (newrelic.js agent, NREUM)
462. Dynatrace (dtagent, dtcookie)
463. AppDynamics
464. Elastic APM
465. Jaeger (tracing)
466. Zipkin (tracing)
467. OpenTelemetry indicators

### Log Management (exposed or indicators)
468. ELK Stack (Elasticsearch + Logstash + Kibana)
469. Splunk (exposed search head)
470. Graylog
471. Loki (Grafana)
472. Fluentd / Fluent Bit indicators
473. Papertrail
474. Loggly

### Analytics & Tracking (extract IDs)
475. Google Analytics ID (UA-*, G-*)
476. Google Tag Manager (GTM-*)
477. Facebook Pixel ID
478. Hotjar site ID
479. Microsoft Clarity project ID
480. Matomo/Piwik instance URL & site ID
481. Adobe Analytics (s_code, AppMeasurement)
482. Mixpanel token
483. Segment write key
484. Heap app ID
485. Amplitude API key
486. Plausible Analytics
487. Fathom Analytics
488. Tealium (tag manager)
489. Adobe Launch (tag manager)

### Third-Party Chat & Support Widgets
490. Intercom (app ID extractable)
491. Drift
492. Zendesk Chat / Zopim
493. Tawk.to
494. LiveChat
495. Crisp
496. HubSpot Chat
497. Tidio
498. Olark
499. Freshchat

### Comment Systems
500. Disqus (shortname extractable)
501. Commento
502. Isso
503. Hyvor Talk
504. GraphComment
505. Native WordPress comments
506. Facebook Comments plugin

### Push Notifications
507. OneSignal (app ID extractable)
508. Firebase Cloud Messaging (FCM config)
509. Pusher
510. PushEngage
511. WebPush / Service Worker registration (sw.js)
512. Apple Push Notification indicators

### Image & Media Optimization
513. Cloudinary (cloud name in URLs)
514. imgix (subdomain in URLs)
515. Thumbor
516. Imagify (WordPress)
517. ShortPixel (WordPress)
518. Smush (WordPress)
519. Lazy loading libraries (lazysizes, lozad, vanilla-lazyload)
520. Cloudflare Polish / Image Resizing
521. Akamai Image Manager

### Font Services
522. Google Fonts (fonts.googleapis.com URLs, font families loaded)
523. Adobe Fonts / Typekit (use.typekit.net)
524. Font Awesome version (kit or CDN)
525. Custom @font-face declarations (font file URLs)
526. Font file formats served (.woff, .woff2, .ttf, .otf, .eot)

### Accessibility Tools & Overlays
527. AccessiBe (widget)
528. UserWay (widget)
529. AudioEye
530. EqualWeb
531. ARIA roles/landmarks in HTML

### Social Media Integrations
532. Facebook SDK / Like buttons / Login
533. Twitter/X widgets / Follow buttons / Login
534. Google Sign-In
535. LinkedIn widgets
536. Instagram embeds
537. Pinterest widgets
538. AddThis / ShareThis share buttons

### Maps & Geolocation Services
539. Google Maps API key (extractable from JS)
540. Mapbox access token (extractable)
541. OpenStreetMap / Leaflet.js
542. Bing Maps
543. HERE Maps
544. MapTiler
545. ESRI / ArcGIS

### Video & Media Hosting
546. YouTube embeds (channel IDs, video IDs)
547. Vimeo embeds (user/video IDs)
548. Wistia (account indicators)
549. JW Player
550. Brightcove
551. Kaltura
552. Self-hosted video (video.js, plyr, mediaelement)

### Form & Survey Tools
553. Google Forms (embedded)
554. Typeform (embedded)
555. JotForm
556. SurveyMonkey
557. Google reCAPTCHA site keys (v2/v3)
558. hCaptcha site keys
559. Cloudflare Turnstile site keys

### A/B Testing & Experimentation
560. Optimizely
561. VWO (Visual Website Optimizer)
562. Google Optimize (sunset but may still appear)
563. LaunchDarkly (feature flags)
564. Split.io
565. Unleash

### Error Tracking & Performance
566. Sentry (DSN in JS source)
567. Bugsnag
568. Rollbar
569. LogRocket (session replay)
570. FullStory (session replay)
571. Datadog RUM
572. SpeedCurve
573. Web Vitals indicators

### Internationalization & Localization
574. i18n framework indicators
575. WPML (WordPress)
576. Polylang (WordPress)
577. Weglot
578. TranslatePress
579. Crowdin integration
580. Transifex integration
581. hreflang tags (alternate language URLs)
582. Language switcher UI patterns

### Java Application Servers
583. Apache Tomcat (version from error pages, /manager)
584. Jetty (Server header, error pages)
585. JBoss / WildFly (X-Powered-By, /console)
586. GlassFish / Payara (Server header, /asadmin)
587. IBM WebSphere (LTPA cookies, /ibm/console)
588. Oracle WebLogic (Server header, /console)

### Additional JVM & Other Language Frameworks
589. Grails (Groovy/Java)
590. Micronaut (Java)
591. Quarkus (Java)
592. Vert.x (Java)
593. Play Framework (Scala/Java)
594. Phoenix (Elixir)
595. Mojolicious (Perl)
596. Dancer (Perl)
597. Catalyst (Perl)

### Service Mesh
598. Istio (x-envoy-* headers, istio-specific routing)
599. Linkerd (l5d-* headers)
600. Consul Connect (HashiCorp)
601. AWS App Mesh

### Firebase & Backend-as-a-Service (BaaS)
602. Firebase Hosting (firebaseapp.com, web.app domains)
603. Firebase Auth (config objects in JS: apiKey, authDomain, projectId)
604. Firebase Firestore / Realtime Database (firebaseio.com URLs)
605. Firebase Cloud Messaging (FCM config in JS)
606. Firebase Storage (firebasestorage.googleapis.com)
607. Supabase (supabase.co domains, anon key in JS)
608. AWS Amplify (aws-amplify config, Cognito pool IDs)
609. Parse Server (self-hosted, X-Parse-* headers)
610. PlanetScale (database-as-a-service indicators)
611. Neon (serverless Postgres indicators)
612. CockroachDB Cloud indicators
613. MongoDB Atlas indicators

### Additional Headless CMS
614. Prismic (prismic.io API calls)
615. Sanity (sanity.io, GROQ queries)
616. Storyblok (storyblok.com API)
617. Hygraph / GraphCMS (graphcms.com / hygraph.com API)
618. DatoCMS (datocms.com API)
619. ButterCMS (buttercms.com API)
620. Agility CMS
621. Keystone.js (self-hosted)

### Identity Providers (specific platforms)
622. Keycloak (self-hosted, /auth/realms/ paths)
623. AWS Cognito (cognito-idp URLs, pool IDs in JS)
624. Azure AD B2C (b2clogin.com redirects)
625. Firebase Auth (see BaaS section)
626. FusionAuth
627. ForgeRock (Access Management)

### BI / Reporting Dashboards (exposed)
628. Metabase (/question/, /dashboard/ paths)
629. Apache Superset
630. Redash
631. Tableau Server (exposed views)
632. Power BI Embedded (powerbi.com embeds)
633. Looker (looker.com embeds)
634. Jasper Reports / JasperServer

### GIS / Mapping Servers (exposed)
635. GeoServer (/geoserver/web/, WMS/WFS endpoints)
636. MapServer
637. PostGIS indicators (in API responses)
638. QGIS Server
639. ArcGIS Server (/arcgis/rest/services/)
640. GeoNode

### Media Streaming Servers
641. Wowza Streaming Engine
642. Nginx-RTMP module
643. Icecast (audio streaming)
644. SHOUTcast (audio streaming)
645. Red5 (Flash/RTMP)
646. HLS/DASH streaming indicators (.m3u8, .mpd manifests)

### Exposed Notebook / ML UIs
647. Jupyter Notebook / JupyterHub
648. MLflow (experiment tracking UI)
649. TensorFlow Serving (REST/gRPC endpoints)
650. Kubeflow
651. Apache Zeppelin

### CI/CD Platforms (exposed or indicators)
652. GitHub Actions (.github/workflows/ files exposed)
653. GitLab CI (.gitlab-ci.yml exposed)
654. Jenkins (/jenkins/, blue ocean UI)
655. CircleCI indicators
656. Travis CI indicators
657. TeamCity (/teamcity/ login)
658. Bamboo (Atlassian)
659. Azure DevOps / Azure Pipelines
660. Drone CI
661. ArgoCD (/argocd/ UI)
662. Spinnaker
663. GoCD

### Scheduling / Task Management UIs (exposed)
664. Apache Airflow (/airflow/ web UI)
665. Sidekiq (Ruby — /sidekiq/ web UI)
666. Bull Board (Node.js — /admin/queues)
667. Celery + Flower (/flower/ UI)
668. Hangfire (.NET — /hangfire dashboard)
669. Quartz Scheduler indicators

### Virtualization Management UIs (exposed)
670. VMware vCenter / ESXi (VMRC, /ui login)
671. Proxmox VE (/pve login, port 8006)
672. oVirt / RHEV
673. Hyper-V Manager (web interface)
674. XenServer / XCP-ng

### SIEM / Security Monitoring (exposed)
675. IBM QRadar
676. HP ArcSight
677. AlienVault / OSSIM / USM
678. Wazuh (Kibana-based UI)
679. Splunk Enterprise Security
680. FortiSIEM
681. LogRhythm

### Network Management / Monitoring (exposed)
682. NetBox (DCIM/IPAM)
683. phpIPAM
684. Infoblox
685. LibreNMS
686. Observium
687. PRTG Network Monitor
688. Cacti
689. OpenNMS
690. Checkmk

### Managed WordPress / CMS Hosting
691. WP Engine (wpenginepowered.com, X-Powered-By: WP Engine)
692. Kinsta (kinsta.cloud domains)
693. Flywheel (flywheelsites.com)
694. Acquia (Drupal hosting — acquia.com, X-AH-Environment header)
695. Pantheon (Drupal/WP — pantheonsite.io, X-Pantheon-* headers)
696. WordPress.com VIP (vip.wordpress.com)
697. Pressable
698. Pagely
699. Cloudways
700. SiteGround (sg-optimizer indicators)

### Prerendering / SSR Services
701. Prerender.io (X-Prerender header)
702. Rendertron (Google)
703. Puppeteer-based prerendering indicators

### Node.js Process Managers (from errors/headers)
704. PM2 (X-PM2-* headers, error output)
705. Forever
706. StrongLoop / LoopBack indicators

### Document Signing Platforms (embedded/integrated)
707. DocuSign (embedded signing, powerforms)
708. Adobe Sign (echosign)
709. SignNow
710. HelloSign (Dropbox Sign)
711. PandaDoc

### Telemetry / Customer Data Platforms
712. Snowplow Analytics (collector endpoints)
713. RudderStack
714. mParticle
715. Treasure Data

### Review / Rating Widgets
716. Trustpilot (widget embeds, business unit ID)
717. Google Reviews widget
718. Bazaarvoice (product reviews)
719. Yotpo (e-commerce reviews)
720. Stamped.io

### WebRTC / Conferencing (exposed)
721. Jitsi Meet (self-hosted /jitsi)
722. BigBlueButton (self-hosted /b/)
723. STUN/TURN server indicators
724. OpenVidu

### Print Management (exposed)
725. CUPS web interface (port 631)
726. PaperCut

### Exposed Infrastructure-as-Code Files
727. Terraform state files (.tfstate)
728. Ansible playbooks (ansible.cfg, playbook.yml)
729. Puppet manifests
730. Chef cookbooks/recipes
731. Kubernetes manifests (*.yaml with kind: Deployment, etc.)
732. Helm charts (Chart.yaml)

### Backup Solutions (exposed portals)
733. Veeam Backup & Replication (web console)
734. Acronis Cyber Protect (web console)
735. Bareos / Bacula (web UI)
736. Commvault

### GraphQL-Specific Platforms
737. Apollo Server (apollo-server-* indicators, Apollo Studio)
738. Hasura Console (/console, X-Hasura-* headers)
739. PostGraphile
740. Yoga (GraphQL server)

### Minification / Optimization Indicators
741. UglifyJS patterns (mangled variable names)
742. Terser output signatures
743. cssnano (minified CSS patterns)
744. HTML minification (removed whitespace/comments)
745. Google Closure Compiler indicators

### Database-as-a-Service Indicators
746. Amazon RDS (endpoint patterns: *.rds.amazonaws.com)
747. Azure SQL Database (*.database.windows.net)
748. Google Cloud SQL
749. ElephantSQL (PostgreSQL)
750. Redis Cloud (Redislabs)
751. Aiven (managed data services)

### E-Learning Platforms
752. Moodle (already in collaboration, but specific indicators)
753. Canvas LMS (already listed)
754. Blackboard / Blackboard Ultra
755. LearnDash (WordPress plugin)
756. Teachable
757. Thinkific

### Government-Specific Platforms & Indicators
758. Gov.uk publishing platform
759. e-Government frameworks
760. Electronic signature portals
761. Single Sign-On for government services (citizen portals)
762. National PKI / digital certificate infrastructure
763. Open data portals (CKAN, Socrata, DKAN)

---

## HTTP Response Headers (Capture Everything)

### Server Identification Headers
764. Server:
765. X-Powered-By:
766. X-AspNet-Version: / X-AspNetMvc-Version:
767. X-Generator:
768. X-Drupal-Cache: / X-Drupal-Dynamic-Cache:
769. X-Varnish:
770. Via: (proxy info)
771. X-Served-By: / X-Backend-Server: / X-Server-ID:

### CDN & Caching Headers
772. X-Cache: / X-Cache-Status:
773. CF-Ray: (Cloudflare ray ID)
774. CF-Cache-Status:
775. X-CDN: / X-Edge-IP:
776. X-Akamai-* / X-Fastly-* / X-Amz-Cf-*
777. Age: / Cache-Control: / Expires: / ETag: / Last-Modified: / Vary: / Pragma:

### Security Headers (presence AND values)
778. Strict-Transport-Security: (HSTS)
779. Content-Security-Policy: / CSP-Report-Only:
780. X-Content-Type-Options:
781. X-Frame-Options:
782. X-XSS-Protection:
783. Referrer-Policy:
784. Permissions-Policy: / Feature-Policy:
785. Cross-Origin-Opener-Policy:
786. Cross-Origin-Embedder-Policy:
787. Cross-Origin-Resource-Policy:
788. Expect-CT:
789. Public-Key-Pins:
790. X-Permitted-Cross-Domain-Policies:

### CORS Headers
791. Access-Control-Allow-Origin:
792. Access-Control-Allow-Methods:
793. Access-Control-Allow-Headers:
794. Access-Control-Allow-Credentials:
795. Access-Control-Expose-Headers:
796. Access-Control-Max-Age:

### Authentication Indicators
797. WWW-Authenticate:
798. X-Auth-Token:
799. Authorization schemes accepted
800. Set-Cookie: (session cookies)
801. X-CSRF-Token: / X-Request-Id: / X-Correlation-Id:

### Cloud Provider Headers
802. AWS: X-Amz-Request-Id, X-Amz-Id-2, X-Amz-Bucket-Region, X-Amz-Cf-Pop
803. Azure: X-Azure-Ref, X-MS-Request-Id
804. GCP: X-Cloud-Trace-Context, X-GFE-*, X-Google-*
805. Cloudflare: CF-Ray, CF-Cache-Status, CF-Request-ID

### WAF/Protection Headers
806. X-Sucuri-* / X-Mod-Security / X-Firewall / X-Protected-By / X-WAF-*

### Rate Limiting Headers
807. X-RateLimit-Limit / X-RateLimit-Remaining / X-RateLimit-Reset / Retry-After

### Other Headers
808. Content-Type (+ charset) / Content-Length / Content-Encoding
809. Transfer-Encoding / Connection / Keep-Alive / Date
810. Link: (preload/prefetch hints)
811. Alt-Svc: (HTTP/3, QUIC)
812. NEL: (Network Error Logging)
813. Report-To:
814. X-DNS-Prefetch-Control / X-Download-Options / X-Robots-Tag

## Cookies (Capture All)
815. Cookie name, value, domain, path, expires/max-age
816. Secure flag / HttpOnly flag / SameSite attribute
817. First-party vs third-party
818. PHPSESSID (PHP), JSESSIONID (Java), ASP.NET_SessionId (.NET)
819. wordpress_logged_in_*, wp-settings-*
820. __cfduid (Cloudflare)
821. _ga, _gid (Google Analytics), _fbp (Facebook)
822. AWSALB/AWSALBCORS (AWS), ARRAffinity (Azure)
823. BIGipServer* (F5), SERVERID (HAProxy)
824. incap_ses_*, visid_incap_* (Incapsula/Imperva)
825. dtCookie (Dynatrace), NREUM (New Relic)

## HTML Meta Tags & Page Head
826. `<title>`
827. `<meta name="description">`
828. `<meta name="keywords">`
829. `<meta name="author">`
830. `<meta name="generator">` (CMS version disclosure)
831. `<meta name="robots">`
832. `<meta name="viewport">`
833. `<meta charset="">`

### Open Graph Tags
834. og:title, og:description, og:image, og:url, og:type, og:site_name, og:locale

### Twitter Card Tags
835. twitter:card, twitter:site (handle), twitter:creator (handle), twitter:title, twitter:image

### Other Meta/Link Tags
836. `<meta name="msapplication-*">`
837. `<meta name="theme-color">`
838. `<meta name="apple-mobile-web-app-*">`
839. `<meta http-equiv="*">`
840. `<link rel="canonical">`
841. `<link rel="alternate" hreflang="">`
842. `<link rel="manifest">` (web app manifest)
843. `<link rel="icon">` (favicon)
844. `<link rel="apple-touch-icon">`
845. `<link rel="preconnect">` (reveals third-party origins)
846. `<link rel="dns-prefetch">` (reveals third-party domains)
847. `<link rel="preload">` (reveals critical resources)

### Schema.org / JSON-LD
848. `<script type="application/ld+json">` (organization, people, addresses, events)

### XML Files
849. sitemap.xml / sitemap_index.xml (all URLs, lastmod dates)
850. robots.txt
851. crossdomain.xml (Flash cross-domain policy)
852. clientaccesspolicy.xml (Silverlight)
853. browserconfig.xml (IE/Edge tile config)
854. manifest.json / site.webmanifest (PWA config, app name, icons, theme)
855. RSS feeds (rss.xml, feed.xml, atom.xml)
856. opensearch.xml (search plugin descriptor)
857. BingSiteAuth.xml / google-site-verification
858. WSDL files (SOAP service definitions)
859. SVG files (can contain embedded metadata, scripts, links)
860. XML data feeds / API responses
861. XSD schema files
862. XSLT stylesheets

## JavaScript Analysis

### Framework Detection
863. React (_reactRoot, react-dom)
864. Vue (__vue__, Vue.config)
865. Angular (ng-version, angular.module)
866. jQuery ($, jQuery version)
867. Next.js (_next folder, __NEXT_DATA__)
868. Nuxt.js (_nuxt folder, __NUXT__)
869. Gatsby
870. Svelte
871. Alpine.js
872. HTMX
873. Stimulus / Turbo (Hotwire)

### Inline Scripts & Hardcoded Data
874. Hardcoded API keys / tokens
875. Hardcoded internal URLs / endpoints
876. Configuration objects (window.config, __CONFIG__, __APP_STATE__)
877. Environment variables exposed (process.env leaks)
878. Debug flags (debug=true, verbose, NODE_ENV=development)
879. User data / session tokens in JS
880. Nonce values
881. Feature flag configurations

### Source Maps
882. .js.map files (can reveal original source code)
883. .css.map files
884. //# sourceMappingURL= comments

## Connection & Network Details
885. HTTP version (1.1, 2, 3/QUIC)
886. Response time (TTFB)
887. DNS lookup time
888. TLS handshake time
889. Full redirect chain (301, 302, 303, 307, 308) with all URLs
890. HTTP to HTTPS redirect behavior
891. www to non-www (or vice versa)

## Error Page Responses (Info Goldmine)
892. 400 Bad Request response
893. 401 Unauthorized response
894. 403 Forbidden response
895. 404 Not Found response
896. 405 Method Not Allowed response
897. 500 Internal Server Error response
898. 502 Bad Gateway response
899. 503 Service Unavailable response
900. Server software revealed in errors
901. Framework/file paths revealed
902. Stack traces / database errors
903. Internal IP addresses in errors
904. Developer names in errors
905. Custom vs default error pages

---

## Paths to Check

### Standard Files
906. /robots.txt
907. /sitemap.xml / /sitemap_index.xml
908. /.well-known/ (entire directory)
909. /.well-known/security.txt
910. /.well-known/openid-configuration
911. /humans.txt
912. /ads.txt / /app-ads.txt
913. /crossdomain.xml
914. /clientaccesspolicy.xml
915. /favicon.ico
916. /apple-touch-icon.png
917. /manifest.json / /site.webmanifest
918. /browserconfig.xml
919. /LICENSE / /LICENSE.txt
920. /README / /README.md / /README.txt
921. /CHANGELOG / /CHANGELOG.txt
922. /VERSION

### Admin & Login Paths
923. /admin/ , /administrator/
924. /login/ , /signin/
925. /wp-admin/ , /wp-login.php
926. /user/login , /admin/login
927. /panel/ , /dashboard/
928. /cpanel/ , /webmail/
929. /portal/ , /console/

### Sensitive / Config Paths
930. /.git/ , /.git/config , /.git/HEAD
931. /.gitignore
932. /.env , /.env.local , /.env.production , /.env.backup
933. /config.php , /configuration.php , /config.json , /settings.json
934. /wp-config.php , /wp-config.php.bak
935. /web.config
936. /.htaccess , /.htpasswd
937. /config/database.yml , /config/secrets.yml
938. /.dockerenv , /docker-compose.yml , /Dockerfile

### Backup & Archive Paths
939. /backup/ , /backups/ , /bak/ , /old/
940. /archive/ , /temp/ , /tmp/
941. /dump/ , /sql/ , /database/ , /db/
942. /data/ , /export/
943. /uploads/ , /files/ , /documents/ , /private/

### Log & Debug Paths
944. /logs/ , /log/ , /error.log , /access.log , /debug.log , /application.log
945. /wp-content/debug.log
946. /phpinfo.php , /info.php
947. /server-status , /server-info (Apache)
948. /.DS_Store , /Thumbs.db
949. /elmah.axd , /trace.axd (.NET)
950. /debug/ , /test/ , /testing/ , /dev/ , /development/ , /staging/ , /beta/

### CMS-Specific Paths
951. WordPress: /wp-content/ , /wp-content/uploads/ , /wp-content/plugins/ , /wp-content/themes/ , /wp-includes/ , /xmlrpc.php , /wp-cron.php , /readme.html , /license.txt , /wp-includes/version.php
952. Drupal: /core/ , /modules/ , /sites/default/ , /CHANGELOG.txt , /update.php
953. Joomla: /components/ , /modules/ , /plugins/ , /administrator/ , /configuration.php , /administrator/manifests/files/joomla.xml

### Source Code / Package Paths
954. /.svn/ , /.hg/ , /.bzr/ , /CVS/
955. /.idea/ , /.vscode/
956. /node_modules/ , /vendor/
957. /composer.json , /composer.lock
958. /package.json , /package-lock.json , /yarn.lock
959. /Gemfile , /Gemfile.lock
960. /requirements.txt , /Pipfile

### Cloud & Static Asset Paths
961. /s3/ , /storage/ , /blob/ , /cdn/
962. /assets/ , /static/ , /media/
963. /images/ , /img/ , /css/ , /js/ , /fonts/

### Path Enumeration (via PathFinder tool)
964. Recursive directory discovery with wildcard detection
965. Hidden paths found via BFS scanning
966. Custom wordlist-based path brute forcing

## Predictive URL Enumeration (via LOKI tool)
967. Predicted URLs from filename patterns
968. Recursive URL enumeration from discovered endpoints
969. Multi-target domain recon results
970. Downloaded data from discovered API endpoints

---

## API Paths

### WordPress REST API
971. /wp-json/ (root namespace discovery — list all namespaces)
972. /wp-json/wp/v2/users , /wp-json/wp/v2/users?per_page=100
973. /wp-json/wp/v2/posts , /wp-json/wp/v2/pages
974. /wp-json/wp/v2/media
975. /wp-json/wp/v2/categories , /wp-json/wp/v2/tags
976. /wp-json/wp/v2/comments
977. /wp-json/wp/v2/taxonomies , /wp-json/wp/v2/types , /wp-json/wp/v2/statuses
978. /wp-json/wp/v2/settings
979. /wp-json/wp/v2/themes , /wp-json/wp/v2/plugins
980. /wp-json/wp/v2/block-types
981. /wp-json/wp/v2/search
982. /wp-json/oembed/1.0/
983. /wp-json/jetpack/
984. /wp-json/wc/v3/ (WooCommerce)
985. /wp-json/yoast/v1/
986. /wp-json/acf/v3/ (Advanced Custom Fields)
987. /wp-json/wpml/v1/ (WPML)
988. Custom namespaces (enumerate from root)

### GraphQL
989. /graphql , /graphiql
990. /v1/graphql , /api/graphql , /query
991. Introspection query (__schema, __type)
992. Field enumeration, mutation discovery, subscription endpoints

### General REST API
993. /api/ , /api/v1/ , /api/v2/ , /api/v3/
994. /api/users , /api/user , /api/me , /api/profile , /api/account , /api/accounts
995. /api/admin , /api/auth , /api/login , /api/token
996. /api/config , /api/settings , /api/info , /api/status , /api/health , /api/version
997. /api/docs , /api/swagger , /api/search
998. /api/data , /api/export , /api/import
999. /api/upload , /api/download , /api/files , /api/documents , /api/reports
1000. /rest/ , /_api/ , /services/ , /webservices/

### Statistics & Data APIs
1001. /api/v1/tables , /api/v1/tableinfo , /api/v1/data
1002. /pxweb/api/v1/
1003. /statbank/ , /database/ , /data/ , /dataset/ , /catalog/ , /metadata/

### Auth Endpoints
1004. /oauth/ , /oauth/authorize , /oauth/token , /oauth2/
1005. /auth/ , /auth/login , /auth/logout , /auth/register , /auth/reset , /auth/verify
1006. /login , /logout , /signin , /signout , /signup , /register
1007. /token , /jwt/ , /saml/ , /sso/ , /cas/ , /openid/
1008. /.well-known/openid-configuration

### API Documentation
1009. /swagger.json , /swagger.yaml
1010. /openapi.json , /openapi.yaml
1011. /api-docs , /api-docs.json , /v1/api-docs , /v2/api-docs , /v3/api-docs
1012. /docs , /documentation , /redoc , /rapidoc
1013. /swagger-ui , /swagger-ui.html , /swagger-resources , /api/swagger-resources

### Drupal JSONAPI
1014. /jsonapi , /jsonapi/node/article , /jsonapi/user/user
1015. /jsonapi/taxonomy_term/ , /jsonapi/file/file , /jsonapi/media/ , /jsonapi/paragraph/

### SOAP/WSDL
1016. /ws/ , /wsdl/ , /soap/ , /services/ , /webservices/
1017. ?wsdl , ?WSDL , /Service.asmx , /WebService.asmx

### Mobile/App API
1018. /mobile/ , /app/ , /ios/ , /android/ , /m/api/ , /mobile-api/ , /app-api/

### Debug & Health Endpoints
1019. /health , /status , /metrics , /prometheus
1020. /debug/ , /test/ , /dev/ , /staging/ , /beta/
1021. WordPress readme.html (version), wp-includes/version.php
1022. Drupal CHANGELOG.txt
1023. Joomla administrator/manifests/files/joomla.xml
1024. Apache /server-status , phpinfo() pages
1025. .NET elmah.axd , trace.axd
1026. /healthz (Kubernetes)
1027. /ready , /readiness (Kubernetes readiness probes)

### API Parameters to Observe
1028. ?page= , ?per_page= , ?limit= , ?offset= , ?skip= , ?take=
1029. ?sort= , ?order= , ?filter= , ?search= , ?q= , ?query=
1030. ?fields= , ?include= , ?exclude= , ?expand= , ?embed=
1031. ?format= , ?callback= , ?id= , ?ids=

### API Discovery via Recon Suite (API Hunter tool)
1032. Automated API endpoint discovery per domain
1033. API namespace enumeration
1034. API response archiving
1035. API schema extraction

---

## WordPress Audit (via WordPress Determiner + Hash Hunter)
1036. WordPress detection (is site WP or not)
1037. WordPress version number
1038. Theme name & version
1039. All plugins & versions
1040. User enumeration via /wp-json/wp/v2/users
1041. All usernames (slug field)
1042. All display names
1043. All user IDs
1044. All gravatar MD5 hashes (from avatar_urls)
1045. All gravatar SHA256 hashes (if present)
1046. User descriptions, URLs, registration dates, roles (if exposed)
1047. Comments with commenter gravatar hashes
1048. WPvivid vulnerability check (CVE-2026-1357)

## Hash Operations (via Hash Hunter + Hash Cracker + HASH MONSTER)
1049. Automated hash extraction from WordPress APIs
1050. Hash type identification (hashid)
1051. Hash cracking attempts (rainbow tables, wordlists)
1052. Cross-reference with online hash lookup services
1053. Hash-to-identity correlation mapping
1054. Master hash database storage and cross-referencing

---

## Files & Documents
1055. PDFs
1056. Word docs (.doc/.docx)
1057. Excel files (.xls/.xlsx)
1058. PowerPoint (.ppt/.pptx)
1059. OpenDocument (.odt/.ods/.odp)
1060. RTF files
1061. Plain text (.txt)
1062. CSV/TSV data files
1063. JSON files
1064. XML files
1065. SQL dumps
1066. Database files (.db, .sqlite)
1067. YAML/TOML/INI config files
1068. Archive files (.zip, .rar, .7z, .tar, .tar.gz, .bz2)
1069. Log files (.log)
1070. Backup files (.bak, .backup, .old, .orig, .save, .swp, .tmp)
1071. Config files (.env, .config)
1072. Key files (.key, .pem, .crt, .p12)
1073. HTML pages (raw archived)
1074. Exposed source code (PHP, ASP, JSP, Python, JS, CSS)
1075. Source maps (.js.map, .css.map)
1076. .git directory dumps

## Images, Video, Audio
1077. JPG/JPEG (check EXIF)
1078. PNG
1079. GIF
1080. TIFF/TIF
1081. BMP
1082. WebP
1083. SVG (check for embedded data)
1084. ICO (favicon — can contain metadata)
1085. RAW camera files (.raw, .cr2, .nef)
1086. MP4, MOV, AVI, WMV, WebM, MKV, FLV, M4V
1087. MP3, WAV, OGG, M4A, FLAC, WMA
1088. Favicons, apple-touch-icons

## Metadata & GPS
1089. EXIF from all images (camera model, date/time, software, author, GPS)
1090. GPS coordinates from EXIF
1091. GPS coordinates from documents, APIs, JavaScript, KML/GeoJSON
1092. GPS from embedded maps, PDF maps
1093. Document metadata (author, organization, software, edit history, creation date)
1094. Video/audio metadata (GPS, camera, timestamps)
1095. Embedded thumbnails in images/documents
1096. Printer/scanner metadata
1097. IP geolocation data
1098. Facility location coordinates

## Filenames & Patterns
1099. Raw filenames from /uploads/, directory listings, sitemaps, APIs, download links, galleries
1100. Naming conventions (date formats, project codes, personnel initials, department abbreviations, version numbers)
1101. Filename-based intelligence (hierarchy, backup schedules, location intel, payroll, classification schemes, codenames)
1102. Directory listing contents

---

## Archives & History
1103. Wayback Machine snapshots (systematic, all pages)
1104. Archive.today captures
1105. Google Cache / Bing Cache
1106. Common Crawl data
1107. Historical DNS records
1108. Historical WHOIS ownership changes
1109. Registrant changes, nameserver changes
1110. Deleted/changed content recovery
1111. Historical SSL certificates

## External Sources
1112. Social media (Twitter/X, Facebook, Instagram, YouTube, TikTok, LinkedIn, Telegram, WhatsApp groups, VK, Weibo) — posts, images, videos, follower lists
1113. Code repositories (GitHub orgs, repos, gists, commits, issues, PRs, actions/workflows, secrets exposure)
1114. GitLab, Bitbucket, self-hosted Git servers
1115. Package registries (npm, PyPI, Docker Hub)
1116. Mobile apps (APK/IPA download, decompiled analysis, embedded endpoints & keys & certs)
1117. Exposed cloud storage (S3 buckets, Azure Blob, GCS, DigitalOcean Spaces)
1118. Breach/leak database hits (HIBP, DeHashed, LeakCheck, Snusbase, IntelX)
1119. Paste site mentions (Pastebin, GitHub Gists, Ghostbin, JustPaste.it, Dpaste)
1120. Google dorking results (filetype:pdf/xls/doc/sql/log/bak/env, "index of", inurl:admin/login/api)
1121. Shodan/Censys/ZoomEye/BinaryEdge/GreyNoise/FOFA scan data
1122. Job postings & procurement/tender/RFP documents (reveals tech stack, vendors, org structure)
1123. Legal/public records, court records, corporate registries, sanctions lists, FOIA, government gazettes, parliamentary records, budget documents
1124. Reverse image search (Google Images, TinEye, Yandex, Bing, PimEyes)
1125. Geospatial/satellite imagery (Google Earth, Sentinel Hub, OpenStreetMap, Mapillary)
1126. WHOIS history (DomainTools, WhoisXML API, SecurityTrails)
1127. RSS/Atom feeds
1128. HTML comments (view-source)
1129. CSS files (background image URLs, @import URLs)
1130. Print stylesheets
1131. Password reset / registration / login pages (version hints, backend clues)
1132. Contact forms (may reveal backend)
1133. Search functionality (may expose internal data)

## Sensitive Finds
1134. Classified/internal documents & memos
1135. Financial records & payroll data
1136. Contracts & agreements
1137. Security policies & incident reports
1138. Surveillance records & communications logs
1139. Internal IP addresses & hostnames
1140. Database connection strings
1141. LDAP/AD structure
1142. Internal URLs, VPN configs, network diagrams, staging/dev URLs
1143. PII (passports, SSN-equivalents, bank accounts, biometrics, driver's licenses)
1144. Security findings by severity (critical/high/medium/low/info)
1145. Personnel files & audit logs

---

## CSP Header as Intelligence
1146. Parse Content-Security-Policy script-src (reveals allowed JS origins, internal APIs)
1147. Parse CSP connect-src (reveals allowed API/XHR/WebSocket destinations)
1148. Parse CSP img-src (reveals image CDNs, internal image servers)
1149. Parse CSP frame-src / frame-ancestors (reveals allowed embed origins, partner domains)
1150. Parse CSP font-src (reveals font CDN origins)
1151. Parse CSP style-src (reveals CSS origins)
1152. Parse CSP media-src (reveals media hosting origins)
1153. Parse CSP default-src (baseline allowed origins)
1154. Parse CSP report-uri / report-to (reveals internal monitoring/reporting infrastructure)
1155. Discover unlisted internal domains from CSP whitelists

## iframe / Embed Source Analysis
1156. All iframe src URLs (third-party services, embedded dashboards, internal tools)
1157. Embedded objects (Flash .swf, Silverlight .xap, Java applets — legacy government sites)
1158. Nested iframe chains (iframes within iframes)
1159. Sandboxed vs unsandboxed iframes (sandbox attribute analysis)
1160. Embedded PDF viewers (pdf.js, Google Docs viewer, Office Online)

## Robots.txt Disallow Intelligence
1161. Disallow paths as hidden directory roadmap (what they don't want crawled)
1162. Crawl-delay values (reveals server capacity concerns)
1163. Sitemap references in robots.txt (may point to additional sitemaps)
1164. User-agent specific rules (reveals awareness of specific bots)
1165. Allow exceptions within Disallow blocks (reveals publicly intended paths)

## Virtual Host / SNI Enumeration
1166. Reverse IP lookup (other domains hosted on same IP)
1167. SNI (Server Name Indication) hostnames on shared servers
1168. Co-hosted domains on same infrastructure
1169. Shared SSL certificates across virtual hosts
1170. Default/fallback vhost content (accessing IP directly)

## Additional Image Metadata (beyond EXIF)
1171. IPTC data (caption, copyright, photographer name, location text, keywords)
1172. XMP metadata (Adobe metadata standard — embedded in images, PDFs, videos)
1173. ICC color profiles (reveals software chain, editing tools)
1174. Photoshop metadata (layer info, edit history if embedded)
1175. Maker notes (camera-specific proprietary EXIF extensions)

## PDF Internal Analysis
1176. PDF form fields (pre-filled data, field names reveal internal terminology)
1177. PDF embedded JavaScript (scripts, auto-actions)
1178. PDF internal links / cross-references / bookmarks
1179. PDF embedded files / attachments (hidden files inside PDFs)
1180. PDF digital signatures (signer identity, certificate chain, timestamp)
1181. PDF Producer field (creation tool: wkhtmltopdf, Puppeteer, Prince XML, Adobe, LibreOffice)
1182. PDF Creator field (originating application)
1183. PDF linearization (web-optimized indicator)
1184. PDF annotations / comments (reviewer names, notes)
1185. PDF redaction analysis (improperly redacted content — text still extractable)
1186. PDF XFA forms (XML Forms Architecture — complex form data)

## Office Document Internals
1187. VBA macros in .doc/.xls/.ppt (code analysis)
1188. OLE embedded objects (other files inside documents)
1189. Tracked changes / revision history (previous authors, deleted content)
1190. Document properties — custom fields (internal project codes, department names)
1191. Document properties — Company name, Manager field
1192. Template reference (.dot, .dotx, .xlt — reveals internal template library)
1193. Embedded fonts (reveals software/locale)
1194. Comments and annotations (reviewer names, internal discussion)
1195. External data connections in Excel (linked databases, external URLs)
1196. Named ranges / defined names in Excel (internal naming conventions)

## Email Security DNS Records
1197. MTA-STS (Mail Transfer Agent Strict Transport Security — _mta-sts TXT record)
1198. BIMI (Brand Indicators for Message Identification — _bimi TXT record, logo URL)
1199. DANE / TLSA records (DNS-based TLS authentication for mail)
1200. _dmarc record details (policy, rua/ruf reporting addresses)
1201. SMTP TLS Reporting (_smtp._tls TXT record)

## Client-Side Storage Analysis
1202. localStorage key names and values (config, tokens, user data, feature flags)
1203. sessionStorage patterns
1204. IndexedDB database names and object store names
1205. Service Worker routes and scope (sw.js, service-worker.js analysis)
1206. Service Worker cache names and cached URLs
1207. Service Worker offline fallback pages
1208. Cache API / Cache Storage contents
1209. Cookies set by JavaScript (not just HTTP Set-Cookie)

## URL Structure & Pattern Analysis
1210. CMS routing patterns (reveals content types, URL scheme)
1211. Pagination total record counts (?page=1 response reveals total_pages/total_records)
1212. Sequential ID patterns in URLs (user IDs, document IDs — reveals total count)
1213. Query parameter naming conventions (reveals framework/internal terminology)
1214. Clean URL vs query string patterns (reveals URL rewriting)
1215. Locale/language URL patterns (/en/, /es/, ?lang=)
1216. Date-based URL patterns (/2026/01/20/ — reveals content timeline)
1217. File path patterns in URLs (reveals directory structure)

## AMP (Accelerated Mobile Pages)
1218. /amp/ page variants
1219. ?amp=1 query parameter variants
1220. amp-* custom HTML elements (amp-img, amp-video, amp-analytics)
1221. AMP cache URLs (cdn.ampproject.org cached versions)
1222. AMP analytics configuration (reveals tracking setup)

## Calendar / Contact / Data Files
1223. .ics calendar files (events, meetings, locations, attendees)
1224. .vcf vCard files (contact names, emails, phones, addresses, organizations)
1225. .opml files (RSS/feed subscription lists)
1226. .torrent files (sometimes on government download pages)
1227. .gpx files (GPS track data)
1228. .kml / .kmz files (Google Earth geographic data)
1229. .geojson files (geographic feature data)
1230. .shp / shapefile data (GIS data)

## Webhook URLs in Code
1231. Slack webhook URLs (hooks.slack.com/services/*)
1232. Discord webhook URLs (discord.com/api/webhooks/*)
1233. Microsoft Teams webhook URLs
1234. Generic webhook endpoints in JavaScript/config
1235. Zapier / IFTTT / Make webhook URLs

## Timezone & Locale Intelligence
1236. Server timezone from HTTP Date header
1237. JavaScript timezone references (Intl.DateTimeFormat, moment.tz)
1238. Timestamp format patterns across the site (ISO 8601, locale-specific)
1239. Default language vs available languages (content negotiation, Accept-Language)
1240. Character encoding patterns (UTF-8 vs legacy encodings — reveals system age)
1241. Number/currency formatting (reveals locale configuration)
1242. Date formatting patterns (DD/MM/YYYY vs MM/DD/YYYY — reveals origin)

## Digital Watermarks & Steganography
1243. Invisible digital watermarks in documents (Digimarc, etc.)
1244. Steganography indicators (unusual file size relative to image dimensions)
1245. Document tracking identifiers (Machine Identification Code / printer dots)
1246. Hidden metadata layers in images
1247. Audio watermarks in video/audio files

## QR Codes
1248. QR codes embedded on government web pages (decode for URLs/data)
1249. QR codes in downloadable documents/PDFs
1250. QR code destination URLs (may reveal internal systems)

## Structured Data Beyond JSON-LD
1251. Microdata (itemscope, itemprop, itemtype attributes)
1252. RDFa attributes (typeof, property, about)
1253. Open Graph protocol data (beyond basic og: tags — product, article, profile types)
1254. Dublin Core metadata (DC.title, DC.creator, DC.date)

## Domain Registration Patterns
1255. Domain age / original registration date
1256. Bulk registration patterns (multiple domains same date, same registrar)
1257. Registrar identification (reveals procurement patterns)
1258. Registration expiry dates (reveals renewal practices)
1259. Registrant organization patterns (same org across domains)
1260. Privacy/proxy registration (reveals what they're hiding)

## Reporting & Monitoring Endpoints
1261. report-uri destinations in CSP headers
1262. report-to endpoints (Reporting API group definitions)
1263. NEL (Network Error Logging) collector URLs
1264. Expect-CT report-uri
1265. HPKP report-uri (deprecated but may exist)

---

**Total items: 1265**
