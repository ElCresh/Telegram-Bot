# Telegram Bot
===============
_`Introduzione`
===============

Bot basato sulle `Telegram Bot API <https://core.telegram.org/bots/api>`_.

Sono richieste le seguenti librerie:
- sqlite3
- telepot

-------------------------
_`Versioni di Python supportate`
-------------------------

=============== =============
Versione Python *Supportato?*
=============== =============
2.6             Non testato
2.7             Si
3.3             Non testato
3.4             Si
3.6             Si
=============== =============

====================
_`Tipi di risposta`
====================
=============== =============
Tipo di dato    *Descrizione*
=============== =============
text            Messaggio di risposta testuale
img             Risposta con immagine (solo URL)
aud             Risposta con messaggio vocale (solo percorsi locali)
=============== =============
====================
_`Requisiti`
====================
- cat telegram_bot.sql | sqlite3 telegram_bot.db
- Creare una copia di setting_dist.py con il token con nome setting.py

====================
_`Ottieni il codice`
====================

Il codice lo trovate a https://github.com/CreshZmine/Telegram-Bot/

Per ottenere il codice::

    $ git clone https://github.com/CreshZmine/Telegram-Bot/
    $ cd Telegram-Bot
