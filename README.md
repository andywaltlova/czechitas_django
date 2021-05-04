<a href="https://www.czechitas.cz/"><img align="right" src="https://cdn.myshoptet.com/usr/www.shop-czechitas.cz/user/logos/logo.png" alt="Czechitas logo" width="180"/></a> 

# Python pro web

Django aplikace tvořená během výuky posledních 4 lekcí [dlouhodobého kurzu jazyka Python](https://www.czechitas.cz/cs/kalendar-akci/akce/24752/2021/02/16), který je organizovaný [Czechitas](https://www.czechitas.cz/en/).
Oficiální materiály [zde](https://kodim.cz/czechitas/progr2-python/python-pro-web).

## Week 8 + 9 (6.4.2021 + 13.4.2021)
Czechitas potřebují spravovat nejen kurzy, ale i tradiční firemní agendu, mezi kterou patří kontakty se sponzory, partnery a dalšími důležitými osobami. Vytvořme si základ jednoduchého CRM systému (Customer Relationship Management), který by takovou agendu dokázal obstarat.

1. Uvnitř svého projektu `czechitas` založ novou aplikaci `crm`.
2. Vytvoř pohled, který přivítá uživatele na úvodní straně textem `"Vítej v CRM systému Czechitas!"`
3. Vytvoř model `Kontakt`, který bude reprezentovat kontakt na nějakou osobu. 
   - U kontaktu eviduj jméno, příjmení, e-mail a datum posledního kontaktu.
   - Vyber pro každý údaj vhodný typ pole.
4. Přidej aplikaci do souboru `settings.py` a proveď migraci databáze.
5. Zaregistruj model do administrátorského rozhraní a vytvoř testovací záznam.

## Week 10 (20.4.2021)

Vrať se nyní k práci na aplikaci crm.

1. Vytvoř pohled `KontakyView`, který bude obsahovat seznam všech kontaktů, které jsou uložené v databázi. Pohledu vytvoř šablonu. U kontaktu zobrazuj jméno, přijímení a email. Pohledu přiřaď URL a otestuj ho.
2. Přidej do své aplikace model `Organizace`, který bude obsahovat informace o organizacích. Každá organizace bude mít jméno, identifikační číslo a adresu. Zamysli se nad tím, jestli by adresu bylo dobré uložit jako jedno pole, nebo jestli např. uložit ulici, město a PSČ zvlášť.
3. Proveď migraci databáze, zaregistruj model do administrátorského rozhraní a vytvoř nějakou testovací organizaci (např. svoji firmu nebo školu).
4. Vytvoř pohled `OrganizaceView`, která zobrazí všechny organizace v databázi. Pohledu vytvoř šablonu. Pohledu přiřaď URL a otestuj ho.

Uprav své modely tak, aby bylo možné propojit organizaci a konkrétního člověka.

5. Uvažuj, že chceš propojit jeden kontakt vždy s maximálně jednou organizací. Zamysli se nad tím, kde by mělo být umístěno pole ForeignKey. Pole umísti, proveď migraci databáze a zkus propojit některé ze svých záznamů.

## Week 11 (27.4.2021)

Umožni uživatelům prohlédnout si detaily organizace.

- Vytvoř pohledy pro zobrazení detailu organizace.
- Pohledu vytvoř šablonu a provázej je pomocí odkazů s pohledy na seznam organizací. Na stránce zobrazuj všechny informace, které máš uložené v databázi.

### Bonus
Obdobným způsobem umožni uživatelům prohlédnout si detaily kontaktu.

## Week 12 (4.5.2021)

### ČÁST 1
Vrať se ke své aplikaci crm pro správu kontaktů.

- Pokud máš zájem, použij ve cvičení Bootstrap a vytvoř si šablonu base.html a používej tagy pro Bootstrap v dalších bodech.
- Přidej do aplikace formulář na přidání kontaktu. Vytvoř šablonu, která bude obsahovat tag pro vložení formuláře. Dále přidej pohled a nastav potřebné atributy. Počítej, že chceme zobrazit ve formuláři všechna pole, které má model Kontakt.
- Pohledu přidej URL adresu.
- Ověř, že vše funguje tím, že si otevřeš cílovou stránku, na které je daný formulář. Zkus pro některou organizaci vytvořit nový kontakt.

### ČÁST 2
- Vytvoř nový pohled pohled pro vytvoření kontaktu, který nebude mít pole organizace, ale bude organizaci číst z URL adresy. Pohled může používat stejnou šablonu jako ten, který jsi použil(a) v předchozím cvičení.
- Nastav URL adresu pohledu, aby s ID orgaizace počítala, tj. aby obsahovala část <int:pk>.
- Na stránku orgaizace přidej tlačítko s textem “Přidej kontakt”, které tě přesměruje na stránku s formulářem na přidání kontaktu. Nezapomeň, že výsledná adresa musí obsahovat ID organzace.
- Ověř, že vše funguje tím, že pomocí nového formuláře vytvoříš kontakt.