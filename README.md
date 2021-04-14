<a href="https://www.czechitas.cz/"><img align="right" src="https://cdn.myshoptet.com/usr/www.shop-czechitas.cz/user/logos/logo.png" alt="Czechitas logo" width="180"/></a> 

# Python pro web

Django aplikace tvořená během výuky posledních 4 lekcí [dlouhodobého kurzu jazyka Python](https://www.czechitas.cz/cs/kalendar-akci/akce/24752/2021/02/16), který je organizovaný [Czechitas](https://www.czechitas.cz/en/).
Oficiální materiály [zde](https://kodim.cz/czechitas/progr2-python/python-pro-web).

### 1. Úkol
Czechitas potřebují spravovat nejen kurzy, ale i tradiční firemní agendu, mezi kterou patří kontakty se sponzory, partnery a dalšími důležitými osobami. Vytvořme si základ jednoduchého CRM systému (Customer Relationship Management), který by takovou agendu dokázal obstarat.

1. Uvnitř svého projektu `czechitas` založ novou aplikaci `crm`.
2. Vytvoř pohled, který přivítá uživatele na úvodní straně textem `"Vítej v CRM systému Czechitas!"`
3. Vytvoř model `Kontakt`, který bude reprezentovat kontakt na nějakou osobu. 
   - U kontaktu eviduj jméno, příjmení, e-mail a datum posledního kontaktu.
   - Vyber pro každý údaj vhodný typ pole.
4. Přidej aplikaci do souboru `settings.py` a proveď migraci databáze.
5. Zaregistruj model do administrátorského rozhraní a vytvoř testovací záznam.