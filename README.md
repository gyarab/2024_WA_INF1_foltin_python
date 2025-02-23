# Redakční systém v Django

Tato aplikace vytvořená k demonstraci možností frameworku Django v hodinách Webové aplikace.

## Struktura datového modelu

Projekt obsahuje tři hlavní modely: `Category`, `Author` a `Article`. Tyto modely tvoří základní strukturu redakčního systému a jejich vztahy jsou následující:

### **`Category`** (Kategorie)
- Reprezentuje tematickou oblast článků.
- Obsahuje atributy `name` (název) a `description` (popis).
- Vztah M:N s modelem `Article` (jeden článek může patřit do více kategorií).

### **`Author`** (Autor)
- Reprezentuje autora článku.
- Obsahuje atributy `first_name`, `last_name`, `bio` (stručný popis) a `email`.
- Vztah 1:N s modelem `Article` (jeden autor může napsat více článků).

### **`Article`** (Článek)
- Reprezentuje jednotlivý článek publikovaný v systému.
- Obsahuje atributy `title` (název), `perex` (krátký úvodní text), `text` (plný obsah článku) a `published` (datum a čas publikace).
- Vztah M:N s modelem `Category`.
- Vztah 1:N s modelem `Author`.

Projekt byl vyvíjen s asistencí GitHub Copilot.

## Zdroj obsahu

Veškerý textový a obrázkový obsah byl vygenerován pomocí ChatGPT jako ukázka možností generování obsahu pro testovací účely. 

Úvodní prompt:
```
Ahoj, vytvářím jednoduchý redakční systém a potřebuji ukázková data. Chci udělat vtipný surealistický, až dadaistický web, s několika rubrikami, autory a vygenerovat několik článků. Nejprve mi vygeneruj seznam šesti rubrik. Každá rubrika má název, max 30 znaků a krátký popisek (cca 200 znaků).
```

Zajímavý poznatek:

![ChatGPT](chatgpt.png)
