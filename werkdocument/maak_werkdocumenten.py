#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor les 5 "Netiquette, phishing en de groepschat" (Onderzoekslabo Jongeren & Welzijn, 3MWWE):

  Groepschat-onderzoekslabo.docx   het werkdocument dat de leerling INLEVERT (wordt in Classroom een Google-document,
                                   een kopie voor elke leerling)

Gebruik:  python3 maak_werkdocumenten.py     (vereist python-docx; huisstijl.py en go-dalton-gent.png
          staan ernaast)

Geen zip en geen losse bestanden: de leerling werkt in dit werkdocument en in één nieuw Google-document dat hij zelf
maakt (de gedragscode met zijn duopartner). Dat gedeelde document zit in dit werkdocument als link (deel 3).

LET OP bij aanpassen:
 - Alle namen en adressen zijn verzonnen; de adressen eindigen op .example (RFC 2606). Geen telefoonnummers, geen
   e-mailadres van de leraar.
 - Rij a van deel 1 en de kolom a van deel 2 zijn al ingevuld (het uitgewerkte voorbeeld van de demo, in het grijs).
   Laat ze ingevuld.
 - Elk antwoord staat in een eigen vak, en elk vak hoort bij één criterium van lesvoorbereiding § 22
   (_afspraken/verbeteren.md, *Een les die je kan verbeteren*). Wijzig je de vakken, wijzig dan § 14 en § 22.
 - De punten in de controletabel van deel 4 (4 · 3 · 4 · 1 · 2 · 2,5 · 2,5 · 1 = 20) komen overeen met § 22.
 - Het codewoord (RUIS) staat bovenaan deel 4. De lespagina toont het pas als de zelftest juist is.
 - De tabel in deel 3 is bedoeld om te KOPIËREN naar het gedeelde document: de leerling vult ze hier niet in. De
   lichtblauwe vakken gaan mee bij het plakken, zodat het duo ziet waar het typt.
 - De berichten in deel 1 en de groepschat in deel 2 zijn tekeningen in tabellen (ontvangen() en chat()), naar het
   mailvenster van huisstijl.py; er is niets om op te klikken.
"""
import os

import huisstijl as hs

HERE = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HERE, "Groepschat-onderzoekslabo.docx")

B = hs.BREEDTE
GRIJS_VLAK = "F1F3F4"
GRIJS_RAND = "9AA0A6"


def samen(rij, van, tot, cm):
    """Voegt de cellen van..tot van een rij samen en geeft de samengevoegde cel zijn volle breedte (anders raden
    Quick Look en Google Documenten die zelf)."""
    cel = rij.cells[van].merge(rij.cells[tot])
    cel.width = hs.Cm(cm)
    return cel


def nieuwe_pagina(doc):
    """Een kleine lege alinea die zelf op een nieuwe bladzijde begint (page_break_before in een tabelcel
    negeert Google Documenten; zo werkt het ook voor een deel met puntenvak)."""
    p = doc.add_paragraph()
    p.paragraph_format.page_break_before = True
    hs.zonder_ruimte(p)
    p.paragraph_format.line_spacing = hs.Pt(2)
    r = p.add_run("")
    r.font.size = hs.Pt(1)
    return p


def ontvangen(doc, titel, velden, tekst, knop=None, adres=None):
    """Een ontvangen bericht (mail of chat) als tekening: geen vakken, er valt niets in te typen.
    velden: [(label, tekst)] zoals Van en Onderwerp. tekst: lijst van alinea's. knop: tekst van een knop in het bericht.
    adres: het adres waar die knop naartoe gaat (zoals onderaan een browser als je de muis erop zet)."""
    aantal = 1 + len(velden) + 1 + (1 if adres else 0)
    t = doc.add_table(rows=aantal, cols=2)
    t.alignment = hs.WD_TABLE_ALIGNMENT.CENTER
    hs.randen(t, buiten=GRIJS_RAND)
    hs.breedtes(t, [2.6, B - 2.6])
    kop = samen(t.rows[0], 0, 1, B)
    hs.schaduw(kop, "F2F6FC")
    hs.celtekst(kop, titel, vet=True, kleur=hs.RGBColor(0x20, 0x21, 0x24), grootte=11)
    kop.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
    hs.hoogte(t.rows[0], 0.7)
    for i, (label, waarde) in enumerate(velden, start=1):
        links, rechts = t.rows[i].cells
        hs.celtekst(links, label, kleur=hs.GRIJS, grootte=10)
        hs.celtekst(rechts, waarde)
        for c in (links, rechts):
            c.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
            hs.cel_randen(c, "DADCE0", dikte=6, kanten=("bottom",))
        hs.hoogte(t.rows[i], 0.75)
    r = 1 + len(velden)
    cel = samen(t.rows[r], 0, 1, B)
    hs.marges(cel, boven=0.15, onder=0.15, links=0.3, rechts=0.3)
    cel.text = ""
    for j, alinea in enumerate(tekst):
        p = cel.paragraphs[0] if j == 0 else cel.add_paragraph()
        p.paragraph_format.space_after = hs.Pt(3)
        p.add_run(alinea)
    if knop:
        p = cel.add_paragraph()
        p.paragraph_format.space_before = hs.Pt(2)
        p.paragraph_format.space_after = hs.Pt(2)
        hs.stijl(p.add_run("  " + knop + "  "), None, 11, vet=True, kleur=hs.RGBColor(0x0B, 0x57, 0xD0))
    if adres:
        balk = samen(t.rows[r + 1], 0, 1, B)
        hs.schaduw(balk, GRIJS_VLAK)
        hs.celtekst(balk, "Het adres van de knop:  " + adres, kleur=hs.GRIJS, grootte=10)
        balk.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
        hs.hoogte(t.rows[r + 1], 0.65)
    hs.niet_splitsen(t)
    hs.ruimte(doc, 6)
    return t


def chat(doc, titel, berichten):
    """De groepschat als tekening. berichten: [(letter, [(naam en tijd, tekst), …], noot)]. Een bericht zonder letter
    heeft een lege eerste kolom. Een tekst met *sterretjes* wordt cursief. Geen vakken."""
    t = doc.add_table(rows=1 + len(berichten), cols=2)
    t.alignment = hs.WD_TABLE_ALIGNMENT.CENTER
    hs.randen(t, buiten=GRIJS_RAND, binnen="E3E3E3")
    hs.breedtes(t, [1.0, B - 1.0])
    kop = samen(t.rows[0], 0, 1, B)
    hs.schaduw(kop, "E8EAED")
    hs.celtekst(kop, titel, vet=True, grootte=11)
    hs.hoogte(t.rows[0], 0.7)
    for i, (letter, regels, noot) in enumerate(berichten, start=1):
        links, rechts = t.rows[i].cells
        hs.celtekst(links, letter, vet=True, kleur=hs.NAVY_DIEP)
        links.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
        links.paragraphs[0].alignment = hs.WD_ALIGN_PARAGRAPH.CENTER
        hs.marges(rechts, boven=0.12, onder=0.12)
        eerste = True
        for wie, tekst in regels:
            p = rechts.paragraphs[0] if eerste else rechts.add_paragraph()
            hs.zonder_ruimte(p)
            if not eerste:
                p.paragraph_format.space_before = hs.Pt(4)
            hs.stijl(p.add_run(wie), None, 10, kleur=hs.GRIJS)
            for tekstregel in tekst:
                p = rechts.add_paragraph()
                hs.zonder_ruimte(p)
                for k, stuk in enumerate(tekstregel.split("*")):
                    if stuk:
                        hs.stijl(p.add_run(stuk), None, None, cursief=(k % 2 == 1))
            eerste = False
        if noot:
            p = rechts.add_paragraph()
            hs.zonder_ruimte(p)
            hs.stijl(p.add_run(noot), None, 10, kleur=hs.GRIJS, cursief=True)
    hs.niet_splitsen(t)
    hs.ruimte(doc, 6)
    return t


def model(doc):
    """Het communicatiemodel bij twee berichten: kolom a is het voorbeeld (grijs), kolom b vult de leerling in.
    Eén vak per element, want elk element is een deel van een criterium (§ 22)."""
    rijen = [
        ("Communicator: wie stuurt het bericht?", "Lukas"),
        ("Wat bedoelde die persoon?", "Dat de enquête snel gedeeld moet worden."),
        ("Wat las de ontvanger? (decoderen)", "De groep: ‘hij roept, hij is boos’."),
        ("Ruis: wat in het bericht zelf?", "Hoofdletters, ??? en vier berichten na elkaar om 22.47 uur."),
    ]
    cm = [4.6, 6.2, B - 4.6 - 6.2]
    t = doc.add_table(rows=1 + len(rijen), cols=3)
    t.alignment = hs.WD_TABLE_ALIGNMENT.CENTER
    hs.randen(t, buiten=hs.HEX_PERI, binnen=hs.HEX_LIJN)
    hs.breedtes(t, cm)
    for i, h in enumerate(["", "Bericht a · Lukas (voorbeeld)", "Bericht b · Wout"]):
        c = t.rows[0].cells[i]
        hs.schaduw(c, hs.HEX_KOP)
        hs.celtekst(c, h, vet=True, kleur=hs.NAVY_DIEP, grootte=11)
    for r, (vraag, voorbeeld) in enumerate(rijen, start=1):
        rij = t.rows[r]
        for c in rij.cells:
            c.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
        hs.celtekst(rij.cells[0], vraag, vet=True, grootte=11)
        hs.celtekst(rij.cells[1], voorbeeld, kleur=hs.GRIJS, cursief=True)
        hs.vak(rij.cells[2])
        hs.hoogte(rij, 1.3)
    hs.niet_splitsen(t)
    hs.ruimte(doc, 6)
    return t


def gedragscode(doc):
    """De tabel die het duo kopieert naar het gedeelde document: Nr · Regel · Welk bericht uit de chat voorkomt ze? ·
    Geschreven door, met vijf lege rijen. Eén tabel, zodat één keer kopiëren volstaat."""
    cm = [1.2, 8.8, 4.0, B - 1.2 - 8.8 - 4.0]
    t = doc.add_table(rows=1 + 5, cols=4)
    t.alignment = hs.WD_TABLE_ALIGNMENT.CENTER
    hs.randen(t, buiten=hs.HEX_PERI, binnen=hs.HEX_LIJN)
    hs.breedtes(t, cm)
    for i, h in enumerate(["Nr", "Regel", "Welk bericht uit de chat voorkomt ze? (a tot e)", "Geschreven door"]):
        c = t.rows[0].cells[i]
        hs.schaduw(c, hs.HEX_KOP)
        hs.celtekst(c, h, vet=True, kleur=hs.NAVY_DIEP, grootte=11)
    for r in range(1, 6):
        rij = t.rows[r]
        for c in rij.cells:
            c.vertical_alignment = hs.WD_CELL_VERTICAL_ALIGNMENT.CENTER
        hs.celtekst(rij.cells[0], str(r), vet=True, kleur=hs.NAVY_DIEP)
        rij.cells[0].paragraphs[0].alignment = hs.WD_ALIGN_PARAGRAPH.CENTER
        for k in (1, 2, 3):
            hs.vak(rij.cells[k])
        hs.hoogte(rij, 1.2)
    hs.niet_splitsen(t)
    hs.ruimte(doc, 6)
    return t


# De criteria van lesvoorbereiding § 22 (samen 20): 4 · 3 · 4 · 1 · 2 · 2,5 · 2,5 · 1
CRITERIA = [
    ("Deel 1: bij bericht b en c staat *echt* of *phishing*, met een signaal dat bij dit bericht past.", 4),
    ("Deel 2: bij bericht b zijn de vier vakken van het communicatiemodel ingevuld.", 3),
    ("Deel 2: c, d, e en de slotvraag zijn elk beantwoord.", 4),
    ("Deel 2: bij de getuigevraag staan twee dingen.", 1),
    ("Deel 3: de link naar ons gedeelde document werkt en bij *Geschreven door* staan onze twee namen.", 2),
    ("Deel 3: er staan vijf concrete regels, elk met een letter van a tot e.", "2,5"),
    ("Deel 3: er is een reactie met @ voor mijn duopartner, ze is beantwoord of opgelost, en ik beantwoordde de twee vragen.", "2,5"),
    ("Deel 4: de exitvraag is beantwoord.", 1),
]


def werkdocument():
    """In de huisstijl van 12-10-2026 (huisstijl.py): alleen wat de leerling invult, en de feiten die hij
    daarvoor nodig heeft. Hoe hij werkt, staat op de lespagina."""
    doc = hs.nieuw_document()
    doc.core_properties.title = "Groepschat onderzoekslabo - werkdocument"
    doc.core_properties.author = "Toegepaste Informatica"
    hs.kopblok(doc, "GROEPSCHAT", punten=20)

    hs.kader(doc, "Het Onderzoekslabo Jongeren & Welzijn", [
        ("Jouw rol:", "je bent met een duopartner lid van het Onderzoekslabo. Je begeleider is mevrouw Ines Coppens. "
                      "Elke onderzoeksgroep van het labo heeft een groepschat."),
        ("Adressen van het labo:", "e-mails komen van een adres dat eindigt op @onderzoekslabo.example, "
                                   "en de website is www.onderzoekslabo.example."),
    ])

    # ---- Deel 1: drie berichten (bladzijde 1)
    hs.deel(doc, 1, "Echt of phishing?")
    ontvangen(doc, "Bericht a · een mail in je mailbox", [
        ("Van", "EnqueteSnel <support@enquetesnel-login.example>"),
        ("Onderwerp", "Uw enquête wordt verwijderd"),
    ], ["Uw enquête ‘Schermgebruik en slaap’ wordt binnen 24 uur verwijderd. Meld u aan om ze te bewaren."],
        knop="Aanmelden", adres="enquetesnel.account-herstel.example/login")
    ontvangen(doc, "Bericht b · een mail in je mailbox", [
        ("Van", "Ines Coppens <ines.coppens@onderzoekslabo.example>"),
        ("Onderwerp", "Jullie groepschat"),
    ], ["Dag, de onderzoeksgroep ‘Schermgebruik en slaap’ heeft een probleem. In hun groepschat liep het gisteravond mis, "
        "en nu wil Elif niet meer meedoen. Jullie zijn een duo van het labo: zoek uit wat er misging, en schrijf een "
        "gedragscode voor al onze groepschats. Deel ze met mij vóór vrijdag. Groetjes, Ines"])
    ontvangen(doc, "Bericht c · een bericht in de groepschat Onderzoek slaap 📱", [
        ("Van", "een onbekend nummer"),
    ], ["Vul onze enquête in en win een gsm! Log in met je schoolaccount: win-gsm.example"])
    hs.tabel(doc, ["Bericht", "Echt of phishing?", "Welk signaal geeft de doorslag?"], [
        ("a.  Enquête verwijderd", "Phishing", "Het woord vóór .example is niet enquetesnel."),
        ("b.  Jullie groepschat", "", ""),
        ("c.  Win een gsm", "", ""),
    ], [4.0, 3.2, B - 4.0 - 3.2], invul=(1, 2), rijhoogte=1.1, voorbeeld_rij=1)

    # ---- Deel 2: de groepschat ontleden (bladzijde 2)
    hs.deel(doc, 2, "Wat ging er mis in de groepschat?", nieuwe_pagina=True)
    chat(doc, "Onderzoek slaap 📱 · Lukas, Elif, Wout, Yasmine", [
        ("a", [("Lukas · 22.47 uur", ["WIE HEEFT DE ENQUÊTE NOG NIET GEDEELD???", "???", "hallo", "iemand?"])],
         "Lukas stuurt dit als vier berichten na elkaar."),
        ("", [("Elif · 22.55 uur", ["ik zit bij mijn oma in het ziekenhuis, morgen doe ik het"])], None),
        ("b", [("Wout · 22.56 uur", ["typisch elif 🙄😂"])], None),
        ("c", [("Lukas · 22.56 uur", ["😂"]), ("Yasmine · 22.56 uur", ["😂"])], None),
        ("d", [("Yasmine · 23.10 uur", ["[een schermafbeelding van een privébericht van Elif aan Yasmine: "
                                         "‘ik ben zo moe, ik kan dit niet meer’]",
                                         "zie je, ze heeft gewoon geen zin"])], None),
        ("e", [("23.24 uur", ["*Lukas heeft de groep ‘slaap zonder elif’ gemaakt*"])], None),
    ])
    model(doc)
    hs.vraag(doc, "c.  Lukas en Yasmine sturen ook 😂. Waarom doen mensen in een groep mee? Eén zin.")
    hs.antwoordvak(doc, 1.3)
    hs.vraag(doc, "d.  Yasmine zet een privébericht van Elif in de groep. Is dat oké? Waarom (niet)? Eén zin.")
    hs.antwoordvak(doc, 1.3)
    hs.vraag(doc, "e.  Lukas maakt de groep ‘slaap zonder elif’. Hoe heet dat?")
    hs.antwoordvak(doc, 0.9)
    hs.vraag(doc, "Lukas stuurde zijn vraag om 22.47 uur in de groep. Welk medium was beter geweest? Eén zin.")
    hs.antwoordvak(doc, 1.3)
    hs.vraag(doc, "Jij zit ook in de groep. Wat kan jij doen? Noem twee dingen.")
    hs.antwoordvak(doc, 1.6)

    # ---- Deel 3: de kern (bladzijde 3)
    hs.deel(doc, 3, "Onze gedragscode", nieuwe_pagina=True)
    hs.vraag(doc, "De tabel voor jullie gedeelde document:")
    gedragscode(doc)
    hs.vraag(doc, "De link naar ons gedeelde document:")
    hs.antwoordvak(doc, 1.0)
    hs.vraag(doc, "Welke twee regels schreef jij? Typ ze over.")
    hs.antwoordvak(doc, 1.5)
    hs.vraag(doc, "Welke reactie gaf jij aan je partner, en wat antwoordde die?")
    hs.antwoordvak(doc, 1.9)

    # ---- Deel 4: klaar (bladzijde 4)
    hs.deel(doc, 4, "Klaar?", nieuwe_pagina=True)
    hs.vraag(doc, "Het codewoord van de zelftest (stap 6 op de lespagina):")
    hs.antwoordvak(doc, 0.9)
    hs.controletabel(doc, CRITERIA)
    hs.vraag(doc, "Welke ruis uit deze chat was er in een gesprek in het echt niet geweest? Eén zin.")
    hs.antwoordvak(doc, 1.6)

    doc.save(UIT)


if __name__ == "__main__":
    werkdocument()
    print("Gemaakt: Groepschat-onderzoekslabo.docx")
