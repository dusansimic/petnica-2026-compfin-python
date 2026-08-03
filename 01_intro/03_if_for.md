# `if` i `for`

Prvi korak u uvođenju ozbiljnije logike u naš program je grananje toka izvšavanja i ponovno izvršavanje određenog dela koda. Ovo se omogućava kroz `if` grananja i `for` petlje.

## `if` grananja

Osnovni princip grananja je da se određenim logičkim uslovom određuje koji deo koda će se izvršiti.

```mermaid
flowchart TD
    A[Kod pre grananja] --> B{Logički uslov}
    B --> C[Uslov je tačan]
    B --> D[Uslov je netačan]
    C & D --> E[Nastavak koda]
```

## `for` petlje

Princip petlje je da se dok se ne obradi svaki element neke sekvence izvršava neko određeno parče koda.

```mermaid
flowchart TD
    A[Kod pre grananja] --> B@{ shape: hex, label: "Svaki element neke sekvence" }
    B --> C[Obrada elementa]
    C --> B
    C --> E[Nastavak koda]
```

Python dokumentacija: [link](https://docs.python.org/3.13/tutorial/controlflow.html)

Primer koda: [03_if_for.py](./03_if_for.py)
