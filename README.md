# Handleiding voor de leraar — Les 5: Netiquette, phishing en de groepschat

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWWE — 2de graad Maatschappij- en welzijnswetenschappen, doorstroomfinaliteit
**Lesduur:** 1 × 50 minuten: **10 minuten instructie + 40 minuten keuzewerktijd**
**Context:** het Onderzoekslabo Jongeren & Welzijn (fictief), begeleider Ines Coppens; de groepschat *Onderzoek slaap 📱*
**Waar:** lokaal 18 (Windows 11)
**Lesdag:** donderdag 19 november 2026, 8ste uur (14.35–15.25), met les 4 erbij (lessenplan § 7)
**Kernleerplandoelen:** `BV2_04.04` (ethische, sociale en legale regels bij digitale technologie) en `BV2_05.01` (respectvol en constructief met anderen in interactie); ondersteunend `WD2_15.02.04` (het communicatieproces) en `BV2_04.01`; contextueel `WD2_14.01.02` (sociaal gedrag, groepsdruk)
**Opdracht in Classroom:** *Les 5 — Netiquette, phishing en de groepschat*, deadline vrijdag 20 november 2026, 20.00 uur

<!-- Beginvragen (stap 1 van CONTEXT.md), beantwoord door Jonas op 16-11-2026 (telkens het voorstel gekozen):
     klas 3MWWE · les 5 van het lessenplan MWW, met les 4 erbij (communicatiemodel; lessenplan § 7) · do 19-11-2026,
     8ste uur (14.35–15.25) · vorige les uit het lessenplan: les 3 (De formele e-mail, 15-10); daarna drie projectlessen
     → lesstart = ophalen uit les 3 · lokaal 18, Windows 11 · korte phishing-quiz, dan een fictieve escalerende
     groepschat ontleden met het communicatiemodel van les 4 (toon, emoji, ruis), en in duo een gedragscode opstellen in
     een gedeeld Google-document met opmerkingen · elke leerling levert een eigen werkdocument in met de link naar het
     gedeelde document · 20 punten, deadline vr 20-11-2026 20.00 · context Onderzoekslabo Jongeren & Welzijn. -->

## 1. Inhoud van het pakket

```text
W11 - Les 05 - MWW - Netiquette phishing en de groepschat/
├── index.html              de lespagina: startpagina in beelden · route · één stap · checklist (6 stappen, 21 taken)
├── presentatie.html        9 dia's voor het bord; dia 1 is de vaste startdia, dia 8 heeft kloktijden uit de planning
├── css/style.css           opmaak van de lespagina
├── css/slides.css          opmaak van de dia's
├── js/script.js, js/slides.js   interactie (zelftest + codewoord RUIS in stap 6, kloktijden)
├── assets/                 logo's Onderzoekslabo en GO! Dalton Gent, lettertypes (OFL), mascotte, video/inleveren.mp4
├── werkdocument/
│   ├── Groepschat-onderzoekslabo.docx   het werkdocument dat de leerling INLEVERT (een kopie per leerling)
│   ├── maak_werkdocumenten.py           genereert Groepschat-onderzoekslabo.docx (python-docx)
│   └── huisstijl.py, go-dalton-gent.png   de huisstijl van het werkdocument
├── lesvoorbereiding.md     de lesvoorbereiding (28 punten + bronnenonderzoek)
├── dalton-lesfiche.html    de Dalton-lesfiche (instructie 10 + KWT 40): openen, Kopieer de fiche, plakken
├── lesdoelen.json          de doelen voor je jaaroverzicht
├── classroom.json          de opdracht voor de Classroom-koppeling
└── README.md               deze handleiding
```

Geen zip en geen losse bestanden: de leerlingen werken in hun werkdocument en in één nieuw Google-document dat ze zelf maken.

### 1b. Hoe de lespagina werkt

- **Startpagina**: *Wat heb je nodig?* in drie beelden (de opdracht in Classroom, deze lespagina, je werkdocument
  *Groepschat-onderzoekslabo*), *Dit maak je vandaag* (de gedragscode in het gedeelde document: tabel met Nr, Regel, letter en
  Geschreven door, en een reactie met @, als tekening), *Na deze les kan je* en *Vast?* (*1. Toon stapjes · 2. Je duopartner · 3. Je
  leraar*).
- **Handelingen met stapjes, start in *Kort***: de vette regels volstaan om alles te maken; *Toon stapjes* toont een tekening van
  het scherm met een rood kader. Alle beelden zijn tekeningen in HTML en CSS (geen schermafbeeldingen): ook de mail van
  deel 1 (stap 1) en de groepschat van deel 2 (stap 3).
- **Stap 2** (*Echt of phishing?*) heeft het infokader *Zo herken je een vals bericht*: de vijf vragen van Safeonweb en twee adressen
  met het woord dat telt. **Stap 3** (*De groepschat ontleden*) heeft de infokaders *Het communicatiemodel* (een schema) en
  *Netiquette en pesten*; wat een getuige doet (de laatste vraag van deel 2) staat bewust alleen op de theoriekaart. **Stap 4** heeft het
  infokader *Is je duopartner er niet?*; **stap 5** het infokader *Bouwstenen voor je regels* (vijf zinsbegin, *mag je overnemen*).
- **Stap 6 (*Inleveren*)**: de zelftest van drie meerkeuzevragen vergrendelt het tweede *Wat moet je doen?* (link en twee vragen in
  deel 3, codewoord, deel 4, inleveren). Zijn ze alle drie juist, dan toont de groene balk het codewoord **RUIS** (dat de leerling
  bovenaan deel 4 typt) en klapt het blok open, met onderaan het filmpje `assets/video/inleveren.mp4`.
- **Geen AI-hulp** (`data-ai-hulp="uit"`).

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages

Repository [`jonasdaltongent/Groepschat-Labo`](https://github.com/jonasdaltongent/Groepschat-Labo), Pages op branch `main`, map
`/ (root)`:
- **Lespagina:** <https://jonasdaltongent.github.io/Groepschat-Labo/>
- **Presentatie:** <https://jonasdaltongent.github.io/Groepschat-Labo/presentatie.html>

### Stap 2 — De opdracht in Classroom, met de koppeling

De opdracht staat als **concept** klaar in `3MWWE - Informatica`; inplannen voor **donderdag 19 november 2026 om 14.05 uur** (een
half uur vóór het 8ste lesuur van 14.35 uur) doet de hoofdsessie. Classroom publiceert dan zelf.

| | Opdracht: **Les 5 — Netiquette, phishing en de groepschat** |
|---|---|
| **Onderwerp** | Module 1 — Digitaal organiseren en communiceren |
| **Bijlage 1** | de link naar de lespagina (`Lespagina · Les 5 · Netiquette, phishing en de groepschat · Onderzoekslabo`) |
| **Bijlage 2** | `Groepschat-onderzoekslabo` (Google-document) — **Een kopie maken voor elke leerling** |
| **Punten** | 20 |
| **Deadline** | vrijdag 20 november 2026, 20.00 uur |

De instructietekst bevat `{email}` (het script vult je e-mailadres in, in de Classroom-opdracht en nooit in GitHub).

```bash
python3 "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/_tools/zet_opdracht_klaar.py" "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W11 - Les 05 - MWW - Netiquette phishing en de groepschat" --proef
```

### Stap 3 — Met de hand, als de koppeling niet werkt

Upload `werkdocument/Groepschat-onderzoekslabo.docx` in Drive zelf (**Nieuw** › **Bestand uploaden**; met de instelling *Uploads
converteren* wordt het een Google-document). Maak in Classroom een opdracht met **Bijvoegen** › **Link** (de lespagina) en
**Bijvoegen** › **Drive** (het werkdocument, **Een kopie maken voor elke leerling**), 20 punten, deadline vr 20-11 om 20.00 uur, en
zet je e-mailadres in de instructie.

### Afvinklijst vóór de les

- [ ] De lespagina en presentatie staan online (HTTP 200).
- [ ] De opdracht staat als **concept** klaar in `3MWWE - Informatica` en is ingepland voor do 19-11 om 14.05 uur.
- [ ] **Schrijf je e-mailadres op het bord** (staat nooit op een dia of de lespagina), en het wachtwoord van de klascomputers.
- [ ] Open `presentatie.html` op het bord op **dia 1 (*Zo start je*)** terwijl de leerlingen binnenkomen.
- [ ] Kopieer de Dalton-lesfiche uit `dalton-lesfiche.html` naar je planner.
- [ ] Duo's zijn buren: een leerling zonder partner? Zie het infokader in stap 4 (trio met een ander duo, of alleen).
- [ ] Kijk in de app *Na de les* of er al een antwoord over projectles 3 is.

### 2b. Nagelezen klikpaden

| Handeling | Klikpad / naam | Bron |
|---|---|---|
| Een nieuw leeg document | `docs.google.com` › onder *Een nieuw document starten* **Leeg** | [Docs 7068618](https://support.google.com/docs/answer/7068618?hl=nl), ruwe tekst 15-11-2026 |
| Het document delen | rechtsboven **Delen** › naam typen en aanklikken › rol **Kijker** · **Reageerder** · **Bewerker** › **Verzenden** | `_afspraken/klikpaden.md` (Jonas' scherm 09-10-2026; [Drive 2494822](https://support.google.com/drive/answer/2494822?hl=nl)) |
| De link kopiëren | **Delen** › **Link kopiëren** › **Klaar** | [Drive 2494822](https://support.google.com/drive/answer/2494822?hl=nl), ruwe tekst 15-11-2026 |
| Een reactie toevoegen | tekst markeren › **Reactie toevoegen** (werkbalk) › typen › **Invoegen** | [Docs 65129](https://support.google.com/docs/answer/65129?hl=nl), ruwe tekst 15-11-2026 |
| Een reactie met **@** | in de reactie **@** en de naam, de naam aanklikken, dan **Invoegen** | idem |
| Antwoorden en sluiten | klik op de reactie › **Reageren** › typen › **Reageren**; sluiten rechtsboven **Oplossen** (een gewone reactie, niet toegewezen) | idem |
| Het gedeelde document terugvinden | links **Gedeeld met mij** (Drive) | [Drive 2375057](https://support.google.com/drive/answer/2375057?hl=nl) |
| De naam van het document | de naam linksboven aanklikken, typen, **Enter**: beschreven, geen knopnaam | niet in de help gevonden; **nog na te kijken** |
| Kopiëren, plakken | **Ctrl + C** · **Ctrl + V** | [Microsoft](https://support.microsoft.com/nl-nl/windows/sneltoetsen-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) |
| De opdracht (leerling) en Inleveren | in het midden de bijlagen; rechts **Jouw werk** en **Inleveren** › venster **Je werk inleveren?** › **Inleveren** | demoleerling3 (15-10-2026), `_afspraken/klikpaden.md` |
| Computer vergrendelen | **Windows-toets + L** | [Microsoft](https://support.microsoft.com/nl-nl/windows/sneltoetsen-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) |

Een regel hoeft hier **niet** aan iemand toegewezen te worden: *Toewijzen aan* (alleen met een werk- of schoolaccount, nog niet
nagekeken met een leerlingaccount) komt in deze les niet voor.

## 3. Verloop van de les en de eerste rondgang

### Instructie en demo (10 minuten, dia 1–8)

- **Dia 1 (0–1'):** *Zo start je.* Wacht tot de meesten de lespagina open hebben. Schrijf je e-mailadres op het bord.
- **Dia 2 (1–3'):** *Weet je het nog?* Vingervraag (A, B of C), ophalen uit les 3: zou je een jongerenwerker “HALLO??? ANTWOORD AUB”
  mailen? → **B** (een formele e-mail is beleefd en rustig). Dan de brug: *in een groepschat met vrienden denken we daar minder
  over na; vandaag ontleden we wat er misloopt.*
- **Dia 3 (3–4'):** *Wat kan je straks?* en het eindproduct: het bericht van Ines en het voorbeeld van een gedragscode voor een
  voetbalclub (bewust een andere chat, niet de oplossing).
- **Dia 4–6 (4–8'):** de demo. Dia 4: het schema van het communicatiemodel (communicator › encodeert › boodschap in het medium ›
  decodeert › ontvanger, en ruis). Dia 5: **bericht a** van Lukas erin (wat bedoelde hij, wat las de groep, waar zit de ruis); dat is de
  ingevulde kolom a van deel 2. Dia 6: kort *delen als Bewerker* en *een reactie met @* (regel selecteren › **Reactie toevoegen** ›
  **@** + naam › **Invoegen**; de ander: **Reageren**, **Oplossen**). Deel 1 doe je niet voor: rij a staat ingevuld. Lees een nieuw
  soort tekening de eerste keer hardop voor (de notities zeggen hoe).
- **Dia 7 (8–9'):** *Controle · iedereen antwoordt.* Vingervraag: *Elif leest ‘typisch elif 🙄😂’ als uitlachen. Wat doet Elif dan?* →
  **2 (decoderen)**. Onthoud wie 1 of 3 toont.
- **Dia 8 (9–10'):** *Zo werk je verder.* Wie het dichtst bij het raam zit, maakt het document. Het adres van de leraar staat op het
  bord. Stap 1 (*Start*, 3') doen ze nu samen.

### Keuzewerktijd (40 minuten)

- **Eerste rondgang (stap 2 en 3):** typt iedereen in de lichtblauwe vakken? Kiezen ze bij deel 1 één signaal dat telt (bij b: een gekende
  afzender, verwacht, vraagt niets geheims; bij c: onbekend nummer, te mooi om waar te zijn, vraagt je schoolaccount)? Staat bij de ruis in
  deel 2 iets uit het bericht zelf (🙄😂 en *typisch elif*), en schrijven ze wat **Elif las**, niet alleen wat Wout bedoelde?
- **Tweede rondgang (stap 4 en 5):** staat de duopartner als **Bewerker** in het document en jij als **Reageerder**? Zijn de regels
  *concreet* (je kan zien of iemand ze breekt, niet *wees lief*), staat bij elke regel een letter a tot e, en schrijft ieder er
  minstens twee? Is er een reactie met @, beantwoord en opgelost? Een duo zonder partner: trio of alleen.
- **Dia 9 (laatste minuut):** exitvraag (*Welke ruis uit de groepschat was er in een gesprek in het echt niet geweest?*), en uitloggen
  of **Windows + L**. Zeg mondeling dat wie niet klaar is, toch inlevert.

## 4. Verbetersleutel

- **Codewoord** bovenaan deel 4: **RUIS** (ontbreekt of fout = −2; een tikfout zoals *RUUS* telt als juist).
- **Deel 1 (4 punten — voor bericht b en c elk 1 punt voor *echt* of *phishing* en 1 punt voor een signaal dat klopt):**
  - **b:** **echt** · gekende afzender (het adres eindigt op onderzoekslabo.example), verwacht, geen link, vraagt niets geheims.
  - **c:** **phishing** · onbekend nummer, te mooi om waar te zijn (win een gsm), vraagt je schoolaccount, link naar een vreemde site.
  - Geldt als juist signaal: de afzender, het domein van de link, onverwacht of te mooi, dringend, een vraag om je account. Niet:
    *je mag nooit op links klikken* zonder te zeggen wat er aan dit bericht niet klopt (0 voor het signaal); *phishing* bij b
    omdat er een vraag in staat (b is echt).
- **Deel 2, bericht b in het schema (3 punten):** communicator **Wout** (0,5) · bedoeling *een grapje* (of: Elif is altijd te laat) (0,5) ·
  wat Elif las *hij lacht mij uit* (1) · ruis: 🙄😂 en *typisch elif*, terwijl Elif net uitlegde waarom (ziekenhuis) (1). Een algemene zin over
  emoji's zonder dit bericht telt niet bij de ruis.
- **Deel 2, c, d, e en de slotvraag (4 punten, 1 per vraag):**
  - **c:** groepsdruk: je wil erbij horen, niet de enige zijn die niet lacht, je denkt dat de anderen het grappig vinden. Niet:
    *omdat ze gemeen zijn* (geen uitleg).
  - **d:** **niet oké**: Elif schreef het aan één persoon; doorsturen zonder toestemming kwetst en gaat over haar grenzen. Niet:
    *het is niet verboden* zonder meer. Wie schrijft dat Elif *geen zin had*, nam de lezing van Yasmine over: 0.
  - **e:** **uitsluiten** (een vorm van cyberpesten). Niet: *ruzie*.
  - **Slotvraag:** een rustig bericht overdag in de groep, of Elif zelf persoonlijk een bericht sturen of bellen (het medium past bij de
    boodschap). Niet: een medium zonder reden.
- **Deel 2, getuige (1 punt, 0,5 per ding):** niet meelachen · iets positiefs naar Elif sturen · een schermafbeelding als bewijs · praten met
  iemand die je vertrouwt (Ines, ouder, leerlingenbegeleiding). *De groep verlaten* alleen telt als één ding als er een tweede bij staat.
- **Deel 3, het gedeelde document (2 punten):** de link werkt en jij kan het openen als Reageerder (1); in de kolom *Geschreven door* staan
  beide namen (1). Is het niet met jou gedeeld, dan is de link niet te openen: 0 voor de link. Staat de partner als Kijker: essentiële fout (feedback).
- **Deel 3, de gedragscode (2,5 punten):** vijf regels, 0,5 per regel die **concreet** is (je kan zien of iemand ze breekt, bv. *geen berichten
  na 22 uur*, niet *wees lief*) en bij een letter a tot e past. Een regel met een letter die niet past, telt niet.
- **Deel 3, reactie met @ en de twee vragen (2,5 punten):** een reactie met @ en de naam van de partner (1); ze is beantwoord of opgelost
  (0,5); *Welke twee regels schreef jij?* (0,5) en *Welke reactie gaf jij, en wat antwoordde je partner?* (0,5). Een eigen bijdrage is nodig:
  dezelfde tekst als je partner mag, een leeg vak niet.
- **Deel 4, exitvraag (1 punt):** ruis die in een gesprek wegvalt: je hoort de toon of ziet het gezicht (hoofdletters of 🙄 lees je niet
  verkeerd), of Elif had meteen kunnen zeggen waarom.

### Essentiële fouten — geef hier altijd feedback op

- Een **privébericht doorsturen** of iemand **uitsluiten** oké vinden (deel 2 d, e).
- Bericht b van Ines als **phishing** zien (alles is vals: `phishing-en-oplichting.md`, *Typische fouten*).
- De partner als **Kijker** delen, of het document niet met de leraar delen.
- **Eén leerling schrijft alle regels.**

## 5. Schermafbeeldingen (optioneel)

Alle beelden op de lespagina en de dia's zijn tekeningen in HTML en CSS (de mail en de groepschat, het schema, het venster *Delen*, een
reactie met @, de tabel van het werkdocument, de opdracht in Classroom). Een echte schermafbeelding kan er later voor in de plaats komen
(`_afspraken/filmpjes-en-schermafbeeldingen.md`); `assets/screenshots/LEESMIJ.md` houdt dat bij.

## 6. Het materiaal opnieuw maken

```bash
cd "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W11 - Les 05 - MWW - Netiquette phishing en de groepschat/werkdocument" && python3 maak_werkdocumenten.py
```

## 7. Leerplandoelen in je jaaroverzicht

`lesdoelen.json` (klasgroep `3 MWW`): `BV2_04.04` en `BV2_05.01` (kern) · `WD2_15.02.04` en `BV2_04.01` (ondersteunend) · `WD2_14.01.02`
(contextueel). De pre-push hook werkt `Leerplandoelen 2026-2027.xlsx` bij.

## 8. Wat nog moet blijken in de klas

- **De knoppen met een leerlingaccount:** zien de leerlingen bij een reactie met @ de knop **Invoegen** (een gewone, niet toegewezen
  reactie) en daarna **Reageren** en **Oplossen**? Nog niet nagekeken met demoleerling3 (er is een tweede account nodig).
- **Het document een naam geven:** de help zegt niets over de naam bovenaan; de lespagina beschrijft het (*klik linksboven op de naam*).
- **De tabel kopiëren:** lukt het met de muis over de hele tabel te slepen en te plakken in een leeg Google-document, met de lichtblauwe
  vakken en de vijf lege rijen?
- **Het werkdocument in Google Documenten:** de berichten van deel 1 en de groepschat van deel 2 zijn tabellen met samengevoegde cellen;
  bekijk na het uploaden of niets verschuift en of deel 1 op één bladzijde past (de pdf van Google is nog niet bekeken; de lesbouwer kon
  het werkdocument alleen met Quick Look bekijken).
- **De tijd:** past stap 3 (deel 2: het schema bij bericht b, vier vragen en de getuigevraag) in 12 minuten, en stap 5 (vijf regels, een
  reactie, antwoorden en oplossen) in 11? Of blijft stap 6 te krap?
- **De regels:** schrijven ze echt concrete regels (*geen berichten na 22 uur*) of vage (*wees lief*), en helpen de bouwstenen met zinsbegin?
- **Duo's:** zijn er leerlingen zonder partner, en werkt het trio of alleen met de leraar als Bewerker?
- **Het communicatiemodel:** begrijpen ze het verschil tussen wat Wout bedoelde en wat Elif las (*encoderen* en *decoderen*)? De woorden volgen
  het leerplan (`WD2_15.02.04`); de uitleg ervan in `_vakinhoud/digitale-communicatie.md` is een voorstel van de AI.
- **Nog niet goedgekeurd:** `_vakinhoud/samenwerken-en-netiquette.md` en de nieuwe delen van `_vakinhoud/digitale-communicatie.md` (het
  communicatiemodel) zijn concepten; de netiquette-regels (hoofdletters, het uur) komen nog uit de algemene kennis van de AI en zijn op de
  lespagina niet als bron vermeld.
- **De zelftest met het codewoord RUIS en het filmpje Inleveren:** werkt het slot in lokaal 18 vlot en leveren alle leerlingen in?
