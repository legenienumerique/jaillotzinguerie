"""Générateur de la maquette Jaillot Zinguerie. Usage : python build.py <dossier-du-projet>
Contenus relevés le 13/11/2026 sur jaillotzinguerie.fr (Jimdo) : textes, prestations, photos de chantiers, logo
(rouge #e04a50, noir), badges Qualibat et Maître artisan, police Open Sans, vert du site #367714 ; fiche Google (4,6/5, 5 avis)."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 1  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '06 27 04 80 08', 'tel:0627048008'
TEL2, TEL2H = '04 74 24 34 93', 'tel:0474243493'
ADR = ('57 chemin de Paulot', '01400 Condeissiat')

NAV = [('zinguerie.html', 'Zinguerie'), ('couverture.html', 'Couverture'), ('realisations.html', 'Réalisations')]
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg>'


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo jz {cls}" aria-hidden="true"><i><img src="{A}mark.png" alt=""></i><span><span class="wm">JAILLOT</span><small>Zinguerie · Couverture</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Contact', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#16191c">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div class="pipe" aria-hidden="true"><div class="pp"><i class="drop"></i></div></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Jaillot Zinguerie, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale">{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}">{PHONE_SVG}<span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Maître artisan couvreur zingueur à Condeissiat, aux portes de la Dombes, à 15 km de Bourg-en-Bresse. Rénovation et construction neuve.</p></div>
<div><h4 class="micro">Savoir-faire</h4><ul><li><a href="zinguerie.html">Zinguerie</a></li><li><a href="zinguerie.html#gouttieres">Gouttières et descentes</a></li><li><a href="zinguerie.html#habillages">Habillages de bandeaux</a></li><li><a href="couverture.html">Couverture</a></li><li><a href="realisations.html">Réalisations</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="{TEL2H}">{TEL2}</a></li><li><a href="contact.html">Décrire mon projet</a></li></ul></div>
<div><h4 class="micro">Atelier</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>SARL Jaillot Zinguerie</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">JAILLOT</div>
<div class="fb micro"><span class="pad">© SARL Jaillot Zinguerie</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Un toit, <em>un projet ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Rénovation ou construction · Condeissiat, la Dombes, Bourg-en-Bresse</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Appeler le ' + TEL, TELH, 'blue')}{pill('Décrire mon projet', 'contact.html', 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# seul avis Google publié avec un texte (relevé le 13/11/2026)
AVIS = [('Frédéric M.', '2021', 'Professionnel sérieux et de confiance.')]


def avis_cards(items):
    return '<div class="rcs">' + ''.join(f'<blockquote class="rc rv"><span class="micro mute">Google · {d}</span><p>« {t} »</p><footer><b>{n}</b><span>Avis Google</span><i>5/5</i></footer></blockquote>' for n, d, t in items) + '</div>'


GAL = [('gouttiere', 'Zinguerie', 'Gouttière zinc'), ('veranda', 'Couverture', 'Couverture joint debout, zinc quartz'),
       ('cheminee', 'Zinguerie', 'Abergement de cheminée en zinc'), ('canales', 'Couverture', 'Tuiles canales posées aux crochets inox'),
       ('cheneau', 'Zinguerie', 'Chéneau zinc sur couverture ardoise'), ('bandeau', 'Habillage', 'Habillage de bandeau'),
       ('maison', 'Zinguerie', 'Gouttière zinc sur couverture tuiles canales'), ('noue', 'Couverture', 'Noue en zinc sur ardoise'),
       ('cuivre', 'Zinguerie', 'Ouvrage en cuivre'), ('chateau', 'Couverture', 'Toiture en ardoise'),
       ('jointdebout', 'Couverture', 'Pose d’une couverture à joint debout'), ('pierre', 'Zinguerie', 'Gouttières sur maison en pierre'),
       ('cheminee2', 'Zinguerie', 'Cheminée habillée de zinc'), ('rive', 'Zinguerie', 'Gouttière et rive'),
       ('veranda2', 'Couverture', 'Véranda couverte en zinc'), ('cuivre2', 'Zinguerie', 'Gouttière et descente en cuivre'),
       ('abri', 'Habillage', 'Habillage de rive'), ('pignon', 'Habillage', 'Habillage de bandeau sur pignon')]


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, faqs, more=''):
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Appeler", TELH, "blue")}{pill("Décrire mon projet", "contact.html", "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Le métier</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_ZONE = ('Où intervenez-vous ?', 'Depuis Condeissiat, aux portes de la Dombes, à 15 km de Bourg-en-Bresse, dans l’Ain. Zone exacte à confirmer avec l’entreprise.')
FAQ_NEUF = ('Neuf ou rénovation ?', 'Les deux : Laurent Jaillot est à votre disposition pour vos travaux de rénovation comme pour vos projets de construction.')
FAQ_CONTACT = ('Comment vous présenter mon projet ?', f'Appelez le {TEL} ou le {TEL2}, ou décrivez votre projet et son lieu dans le formulaire de contact.')


def sec(id_, kicker, h, p, img, alt):
    return f'''
<section class="sec" id="{id_}" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">{kicker}</span><h2 class="sp">{h}</h2>
<p class="lead rv" style="margin-top:1.4rem">{p}</p></div>{tile(PH + img, '', par=8, alt=alt)}</div></section>'''


def pages():
    P = {}
    hero_tiles = [('t1', 'logo'), ('t4', 'gouttiere'), ('t5', 'veranda')]
    ht = ''.join(f'<figure class="tile {c}{" lg" if f == "logo" else ""}"><div class="fl"><div class="in"><img src="{A + "mark.png" if f == "logo" else PH + f + ".webp"}" alt=""></div></div></figure>' for c, f in hero_tiles)
    items = [('zinguerie.html#gouttieres', '01', 'Gouttières', 'Chéneaux et descentes en zinc, cuivre, tôle laquée.', 'gouttiere'),
             ('zinguerie.html', '02', 'Raccords de toit', 'Abergements de cheminée, noues, solins, lucarnes.', 'cheminee'),
             ('zinguerie.html#habillages', '03', 'Habillages', 'Bandeaux et frisettes en alu, zinc ou cuivre.', 'bandeau'),
             ('couverture.html', '04', 'Couverture', 'Ardoise, tuiles plates et canales, zinc, bacs acier.', 'canales'),
             ('couverture.html#service', '05', 'Entretien', 'Démoussage, entretien de toiture, pose de Velux.', 'veranda')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}</span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    steps = [('Sur mesure', 'Un travail personnalisé, adapté à votre toiture et à vos besoins.'),
             ('Tradition', 'Les méthodes traditionnelles, soudures à l’étain et au plomb.'),
             ('Le bon métal', 'Zinc, cuivre, plomb, aluminium laqué ou tôle laquée.'),
             ('Longévité', 'Un toit étanche qui dure, et qui reste beau.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Gouttières', 'Chéneaux', 'Noues', 'Abergements', 'Habillages', 'Ardoise', 'Tuiles', 'Zinc', 'Cuivre'] * 2)

    P['index.html'] = head('Jaillot Zinguerie — Maître artisan couvreur zingueur à Condeissiat (Ain)', 'Jaillot Zinguerie, maître artisan couvreur zingueur à Condeissiat, près de Bourg-en-Bresse : gouttières, chéneaux, abergements, habillages, couverture ardoise, tuiles et zinc.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Maître artisan</b>couvreur zingueur</div>
<div class="cap micro c2"><b>4,6 / 5</b>sur Google</div>
<div class="cap micro c3"><b>15 km</b>de Bourg-en-Bresse</div>
<div class="go">{pill('Appeler', TELH)}</div>
{ht}
<p class="para">La zinguerie traditionnelle, aux portes de la Dombes. Zinc, cuivre, plomb.</p>
<h1 class="word">JAILLOT</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Condeissiat, aux portes de la Dombes</span><h2 class="sp">Le garant du confort <em>de votre maison</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Laurent Jaillot, maître artisan couvreur zingueur, a appris le métier dans différentes régions. Il vous offre un travail personnalisé, de qualité, qui allie longévité et esthétique de votre toit.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Spécialiste de la zinguerie</b>, dans le respect des méthodes traditionnelles.</span></li><li><span><b>Tous les ouvrages</b> qui rendent votre toiture étanche.</span></li><li><span><b>Rénovation</b> ou construction neuve.</span></li></ul>
<div class="seals rv" style="position:static;margin-bottom:2rem"><img class="q" src="{A}qualibat.png" alt="Qualibat"><img class="q" src="{A}maitre-artisan.png" alt="Maître artisan"></div>{pill('Le savoir-faire', '#services', 'blue')}</div>{tile(PH + 'cheminee.webp', '', par=8, alt='Abergement de cheminée en zinc')}</div></section>

<section class="story"><span class="micro mute m3">Le métier</span>
<h2><span class="w">Votre</span> <span class="w">toit</span> <span class="w">mérite</span> <span class="w"><em>un</em></span> <span class="w"><em>spécialiste</em></span></h2>
<div class="stack">{tile(PH + 'cheneau.webp')}{tile(PH + 'noue.webp')}{tile(PH + 'pierre.webp')}</div>
<p class="micro mute m1">Chaque matériau a ses règles de l’art, en harmonie avec votre toiture.</p><span class="micro mute m2">Zinc · cuivre · plomb</span></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Zinguerie et couverture</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Qu’est-ce qu’on <em>pose ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Quelques chantiers</span><h2 class="sp" style="margin-bottom:clamp(2rem,4vw,3rem)">Du travail <em>bien soudé</em></h2>
{gal(GAL[:6])}<div class="row rv" style="margin-top:2rem">{pill('Toutes les réalisations', 'realisations.html', 'blue')}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Avis Google</span><h2 class="sp">Sérieux <em>et de confiance</em></h2>
<div class="cnt rv"><div><b data-to="4.6">0</b><span>sur 5, note moyenne sur Google</span></div><div><b data-to="5">0</b><span>avis publiés sur Google</span></div><div><b data-to="15">0</b><span>kilomètres de Bourg-en-Bresse</span></div></div>
<div style="margin-top:clamp(2rem,4vw,3rem)">{avis_cards(AVIS)}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">L’engagement</span><h2 class="sp">Les règles <em>de l’art</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    zin_more = sec('gouttieres', 'Eaux pluviales', 'Gouttières <em>et descentes</em>', 'Gouttières et chéneaux en zinc, en cuivre ou en tôle laquée, tuyaux de descente : l’eau du toit part là où il faut, sans abîmer vos murs.', 'maison.webp', 'Gouttière zinc sur couverture tuiles canales') + \
        sec('habillages', 'Habillages', 'Bandeaux <em>et frisettes</em>', 'Bandeaux en aluminium laqué, tôle laquée, zinc ou cuivre, frisettes en débord de toiture, habillage de cheminées et de façades.', 'bandeau.webp', 'Habillage de bandeau')
    P['zinguerie.html'] = service('zinguerie.html', 'Zinguerie à Condeissiat, près de Bourg-en-Bresse — Jaillot Zinguerie', 'Gouttières, chéneaux, descentes, abergements de cheminée, noues, solins, habillages de bandeaux. Soudures à l’étain et au plomb. Jaillot Zinguerie, Condeissiat (Ain).',
        'Zinguerie', 'La <em>zinguerie</em>', 'Tous les ouvrages réalisés par soudures à l’étain et au plomb. Le zinc, le cuivre et la tôle, travaillés à la main.', PH + 'cheminee.webp', PH + 'gouttiere.webp',
        'Les raccords <em>de toiture</em>', 'Ce sont eux qui font l’étanchéité de votre toit. Ils se confient à un spécialiste qui respecte les règles de l’art propres à chaque matériau.',
        [('Abergement', 'de cheminée.'), ('Noue', ', couloir et solin contre mur.'), ('Sorties', 'de ventilation (VMC).'), ('Lucarnes', 'habillées et étanches.')],
        [('Quels matériaux utilisez-vous ?', 'Zinc, cuivre, plomb, aluminium laqué et tôle laquée, selon votre toiture.'), FAQ_NEUF, FAQ_ZONE, FAQ_CONTACT], zin_more)

    cou_more = sec('service', 'Service +', 'Entretien <em>et Velux</em>', 'Entretien de toiture, traitement et démoussage, pose de fenêtres de toit Velux.', 'veranda2.webp', 'Véranda couverte en zinc')
    P['couverture.html'] = service('couverture.html', 'Couvreur à Condeissiat, près de Bourg-en-Bresse — Jaillot Zinguerie', 'Couverture ardoise, tuiles plates et canales, couvertures métalliques à joint debout, bacs acier, entretien et démoussage, pose de Velux. Jaillot Zinguerie, Condeissiat (Ain).',
        'Couverture', 'La <em>couverture</em>', 'Ardoise, tuiles, zinc ou acier : le bon toit pour votre maison, posé dans les règles.', PH + 'canales.webp', PH + 'veranda.webp',
        'Toutes les <em>techniques</em>', 'Ardoise en noue ronde, arêtier ou renvers, tuiles plates type Bourgogne et Alsace, tuiles canales, couvertures métalliques à joint debout ou à tasseaux.',
        [('Ardoise', ': noue ronde, arêtier, renvers.'), ('Tuiles', 'plates (Bourgogne, Alsace) et canales.'), ('Métal', ': joint debout en zinc, cuivre, inox ; à tasseaux.'), ('Bacs acier', 'en tôles laquées.')],
        [('Faites-vous l’entretien des toitures ?', 'Oui : entretien de toiture, traitement et démoussage.'), ('Posez-vous des fenêtres de toit ?', 'Oui, la pose de Velux fait partie du service.'), FAQ_NEUF, FAQ_CONTACT], cou_more)

    P['realisations.html'] = head('Réalisations — Jaillot Zinguerie, Condeissiat', 'Galerie de chantiers de Jaillot Zinguerie : gouttières, chéneaux, abergements, couvertures zinc, ardoise et tuiles.', 'realisations.html') + pagehead('Réalisations', 'Mon <em>savoir-faire</em>', 'Quelques chantiers en photos : zinguerie, couverture, habillages.', PH + 'veranda.webp') + f'''
<section class="sec"><div class="wrap">{gal(GAL)}</div></section>''' + cta() + foot()

    P['contact.html'] = head('Contact — Jaillot Zinguerie, Condeissiat', f'Contactez Jaillot Zinguerie, {ADR[0]}, {ADR[1]}. {TEL}.', 'contact.html') + pagehead('Contact', 'Je suis <em>à votre écoute</em>', 'Un appel, ou quelques mots sur votre projet et son lieu.', PH + 'gouttiere.webp') + f'''
<section class="sec" id="devis"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Par téléphone</span><h2 class="sp">Un appel, <em>un doigt</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a><a href="{TEL2H}">{TEL2}</a></div>
<p class="lead rv" style="margin-top:1.6rem">SARL Jaillot Zinguerie<br>{ADR[0]}<br>{ADR[1]}</p>
<div class="hor rv"><span><b>Horaires</b> · à confirmer</span><span class="micro">Non publiés sur l’ancien site ni sur Google</span></div></div>
<form class="f calc rv" id="resa"><div class="fld"><label for="pr">Projet</label><select id="pr"><option>Gouttières, descentes</option><option>Raccords de toiture</option><option>Habillage de bandeaux</option><option>Couverture</option><option>Entretien, démoussage</option><option>Pose de Velux</option><option>Autre</option></select></div>
<div class="fld"><label for="pl">Lieu du projet</label><input id="pl" placeholder="Commune"></div>
<div class="fld"><label for="pc">Description de votre projet</label><textarea id="pc" rows="4"></textarea></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune demande n’est envoyée.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
