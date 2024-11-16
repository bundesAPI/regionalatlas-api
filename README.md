# Regionalatlas API

API zum [Regionalatlas Deutschland](https://regionalatlas.statistikportal.de/#) der statistischen Ämter des Bundes und der Länder. 

Der Regionalatlas Deutschland der Statistischen Ämter des Bundes und der Länder visualisiert aktuell laut [statistischem Bundesamt](https://www.destatis.de/DE/Service/Statistik-Visualisiert/_inhalt.html) mehr als 160 Indikatoren aus 20 Themenbereichen für Bundesländer, Regierungsbezirke, Kreisfreie Städte und Landkreise. Grundlage des Regionalatlas ist die Regionaldatenbank Deutschland.

## query

**URL:** https://www.gis-idmz.nrw.de/arcgis/rest/services/stba/regionalatlas/MapServer/dynamicLayer/query

Die gewünschten Daten lassen sich über GET-Parameter im Query-String spezifizieren.


### Parameter

Die Werte aller Parameter müssen URL-codiert sein wie im Beispiel unten verdeutlicht (also z.B. "where=1%3D1" statt "where=1=1").


**Parameter** *layer* 

Komplexer Parameter, der im JSON-Format Details der Anfrage spezifiziert.
In der Regel enthält der layer-Parameter ein Objekt (in geschweiften Klammern), das seinerseits ein Objekt namens "source" enthält. Das source-Objekt wiederum enthält ein Objekt, das zum einen das Objekt "dataSource" und zum anderen ein Datum namens "type" mit dem Wert "dataLayer" enthält. In dataSource wird die gewünschte Tabelle spezifiziert (z.B. für Angaben zur Bevölkerungsdichte "ai002_1_5") - im Folgenden auch mit dem Platzhalter *tableName* gekennzeichnet.

Hier ein Beispiel für den Layer-Parameter:

```
layer={"source":{"dataSource":{"geometryType":"esriGeometryPolygon","workspaceId":"gdb","query":"SELECT * FROM verwaltungsgrenzen_gesamt LEFT OUTER JOIN ai002_1_5 ON ags = ags2 and jahr = jahr2 WHERE typ = 1 AND jahr = 2020 AND (jahr2 = 2020 OR jahr2 IS NULL)","oidFields":"id","spatialReference":{"wkid":25832},"type":"queryTable"},"type":"dataLayer"}}
```

dataSource kann unterschiedlich aufgebaut sein und enthält entweder (a) Daten namens "dataSourceName" (mit einem Wert wie z.B. "regionalatlas.*tableName*"), "workspaceId (z.B.  "gdb") und "type" (z.B. "table") oder (b) Daten namens "geometryType" (z.B. "esriGeometryPolygon"), "workspaceId" (z.B. "gdb"), "query" (mit einem SQL-Query, z.B. "SELECT * FROM verwaltungsgrenzen_gesamt LEFT OUTER JOIN *tableName* ON ags = ags2 and jahr = jahr2 WHERE typ = 3 AND jahr = 2020 AND (jahr2 = 2020 OR jahr2 IS NULL)"), "oidFields" (z.B. "id"), "spatialReference" (mit einem Objekt, das wiederum das Datum "wkid" mit einem Wert wie 25832 umfasst), und "type":"queryTable".

Der SQL-Query dürfte für Nutzer*innen des Regionalatlas Deutschland weitgehend selbsterklärend sein, wobei man wissen muss dass die Variable *typ* die gewünschte regionale Ebene spezifiziert: 
- 1=Bundesländer, 
- 2=Regierungsbezirke und Statistische Regionen, 
- 3=Kreise und kreisfreie Städte,
- 5=Gemeinden/Verbandsgemeinden 

Bzw. nach URL-Codierung:

```
layer=%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D
```

Gültige Einträge für die *tableName* finden sich unter [https://regionalatlas.statistikportal.de/taskrunner/services.json](https://regionalatlas.statistikportal.de/taskrunner/services.json) und werden im Folgenden tabellarisch dargestellt (*tableName* findet sich in der Spalte "table-code", die enthaltenen Variablen/fields - vgl. Parameter *outFields* - in der Spalte "attribute-code").

|attribute-title|attibute-code|attribute-unit|table-title|table-code|category|
|---|---|---|---|---|---|
|Anteil der Fläche für Siedlung an Gesamtfläche|AI0106|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil der Fläche für Verkehr an Gesamtfläche|AI0107|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil der Fläche für Landwirtschaft an Gesamtfläche|AI0108|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil der Fläche für Wald an Gesamtfläche|AI0109|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil Sport-, Freizeit-, Erholungsfläche an Gesamtfläche|AI0110|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil Siedlungs- und Verkehrsfläche an Gesamtfläche|AI0111|Prozent|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Siedlungs- und Verkehrsfläche je EW|AI0113|qm|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Freiraumfläche je EW|AI0114|qm|Flächennutzung nach ALKIS|AI001-2-5|Gebiet und Fläche|
|Anteil Siedlungs- und Verkehrsfläche an Gesamtfläche|AI0101|Prozent|Flächennutzung nach ALB|AI001-5|Gebiet und Fläche|
|Anteil Erholungsfläche an Gesamtfläche|AI0102|Prozent|Flächennutzung nach ALB|AI001-5|Gebiet und Fläche|
|Anteil Landwirtschaftsfläche an Gesamtfläche|AI0103|Prozent|Flächennutzung nach ALB|AI001-5|Gebiet und Fläche|
|Anteil Waldfläche an Gesamtfläche|AI0104|Prozent|Flächennutzung nach ALB|AI001-5|Gebiet und Fläche|
|Bevölkerungsdichte (EW je qkm)|AI0201|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Bevölkerungsentwicklung im Jahr je 10.000 EW|AI0202|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Anteil der ausländischen Bevölkerung  an der Gesamtbevölkerung|AI0208|Prozent|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Lebendgeborene je 1.000 EW|AI0209|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Gestorbene je 1.000 EW|AI0210|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Geburten-/Gestorbenenüberschuss je 10.000 EW|AI0211|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Wanderungssaldo je 10.000 EW|AI0212|Anzahl|Bevölkerungsstand - Geburten - Gestorbene - Wanderungen|AI002-1-5|Bevölkerung|
|Bevölkerung 0 bis 17 Jahre|AI0203|Prozent|Bevölkerung nach Alter|AI002-2-5|Bevölkerung|
|Bevölkerung 18 bis 24 Jahre|AI0204|Prozent|Bevölkerung nach Alter|AI002-2-5|Bevölkerung|
|Bevölkerung 25 bis 44 Jahre|AI0205|Prozent|Bevölkerung nach Alter|AI002-2-5|Bevölkerung|
|Bevölkerung 45 bis 64 Jahre|AI0206|Prozent|Bevölkerung nach Alter|AI002-2-5|Bevölkerung|
|Bevölkerung 65 Jahre und älter|AI0207|Prozent|Bevölkerung nach Alter|AI002-2-5|Bevölkerung|
|Wanderungssaldo je 10 000: Männer 18 bis 29 Jahre|AI0213|Anzahl|Wanderungen nach Geschlecht und- Alter|AI002-3|Bevölkerung|
|Wanderungssaldo je 10.000: Frauen 18 bis 29 Jahre|AI0214|Anzahl|Wanderungen nach Geschlecht und- Alter|AI002-3|Bevölkerung|
|Durchschnittsalter der Bevölkerung|AI0218|Anzahl|Bevölkerung - Durchschnittsalter|AI002-4-5|Bevölkerung|
|Durchschnittsalter der Mutter bei der Geburt des 1. Kindes|AI0219|Anzahl|Bevölkerung - Durchschnittsalter|AI002-4-5|Bevölkerung|
|Einbürgerungsquote|AI0220|Prozent|Einbürgerungen|AI002-5|Bevölkerung|
|Anteil betreute Kinder 0-2 Jahre in Tageseinrichtungen am 01.03.|AI0301|Prozent|Betreute Kinder in Tagespflege/Tageseinrichtungen|AI003-1|Bildung|
|Anteil betreute Kinder 0-2 Jahre in Tagespflege am 01.03.|AI0302|Prozent|Betreute Kinder in Tagespflege/Tageseinrichtungen|AI003-1|Bildung|
|Anteil betreute Kinder 3-5 Jahre in Tageseinrichtungen am 01.03.|AI0303|Prozent|Betreute Kinder in Tagespflege/Tageseinrichtungen|AI003-1|Bildung|
|Anteil Schulabgänger/-innen mit allgem. Hochschulreife|AI0304|Prozent|Schulabgänger/-innen|AI003-2|Bildung|
|Anteil Schulabgänger/-innen ohne Hauptschulabschluss|AI0305|Prozent|Schulabgänger/-innen|AI003-2|Bildung|
|Betreuungsquote 0 bis 2 Jahre am 01.03.|AI0306|Prozent|Betreuungsquote|AI003-3|Bildung|
|Betreuungsquote 3 bis 5 Jahre am 01.03.|AI0307|Prozent|Betreuungsquote|AI003-3|Bildung|
|Gewerbeanmeldungen je 10.000 EW|AI0401|Anzahl|Gewerbeanmeldungen|AI004-1|Unternehmen|
|Beantragte Unternehmensinsolvenzen je 10.000 steuerpfl. Unternehmen|AI0402|Anzahl|Unternehmensinsolvenzen|AI004-2|Unternehmen|
|AB insgesamt je 1.000 EW im erwerbsfähigen Alter|AI0403|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Bergbau je 1.000 EW im erwerbsfähigen Alter|AI0404|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Verarbeitenden Gewerbe je 1.000 EW im erwerbsfähigen Alter|AI0405|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in der Energieversorgung je 1.000 EW im erwerbsfähigen Alter|AI0406|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in der Wasserversorgung je 1.000 EW im erwerbsfähigen Alter|AI0407|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Baugewerbe je 1.000 EW im erwerbsfähigen Alter|AI0408|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Handel je 1.000 EW im erwerbsfähigen Alter|AI0409|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in Verkehr und Lagerei je 1.000 EW im erwerbsfähigen Alter|AI0410|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Gastgewerbe je 1.000 EW im erwerbsfähigen Alter|AI0411|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in der IKT je 1.000 EW im erwerbsfähigen Alter|AI0412|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in Finanz- und  Versich.dienstl. je 1.000 EW im erwerbsf. Alter|AI0413|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Grundst.- und Wohnungswesen je 1.000 EW im erwerbsf. Alter|AI0414|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in freib./ wissensch./ techn. DL je 1.000 EW im erwerbsf. Alter|AI0415|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in sonst. wirtschaftl. Dienstl. je 1.000 EW im erwerbsf. Alter|AI0416|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in Erziehung und Unterricht je 1.000 EW im erwerbsf. Alter|AI0417|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB im Gesundheits- und Sozialwesen je 1.000 EW im erwerbsf. Alter|AI0418|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in Kunst, Unterh. und Erholung je 1.000 EW im erwerbsf. Alter|AI0419|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|AB in sonstigen Dienstleistungen je 1.000 EW im erwerbsf. Alter|AI0420|Anzahl|Statistisches Unternehmensregister: Abhängig Beschäftigte (AB) je 1.000 EW|AI004-3|Unternehmen|
|Zweitstimmenanteil CDU/CSU, Bundestagswahl|AI0501|Prozent|Bundestagswahl|AI005|Wahlen|
|Zweitstimmenanteil SPD, Bundestagswahl|AI0502|Prozent|Bundestagswahl|AI005|Wahlen|
|Zweitstimmenanteil FDP, Bundestagswahl|AI0503|Prozent|Bundestagswahl|AI005|Wahlen|
|Zweitstimmenanteil GRÜNE, Bundestagswahl|AI0504|Prozent|Bundestagswahl|AI005|Wahlen|
|Zweitstimmenanteil DIE LINKE, Bundestagswahl|AI0505|Prozent|Bundestagswahl|AI005|Wahlen|
|Zweitstimmenanteil AfD, Bundestagswahl|AI0507|Prozent|Bundestagswahl|AI005|Wahlen|
|Wahlbeteiligung, Bundestagswahl|AI0506|Prozent|Bundestagswahl|AI005|Wahlen|
|Stimmenanteil CDU/CSU, Europawahl|AI0601|Prozent|Europawahl|AI006|Wahlen|
|Stimmenanteil SPD, Europawahl|AI0602|Prozent|Europawahl|AI006|Wahlen|
|Stimmenanteil FDP, Europawahl|AI0603|Prozent|Europawahl|AI006|Wahlen|
|Stimmenanteil GRÜNE, Europawahl|AI0604|Prozent|Europawahl|AI006|Wahlen|
|Stimmenanteil DIE LINKE, Europawahl|AI0605|Prozent|Europawahl|AI006|Wahlen|
|Stimmenanteil AfD, Europawahl|AI0607|Prozent|Europawahl|AI006|Wahlen|
|Wahlbeteiligung, Europawahl|AI0606|Prozent|Europawahl|AI006|Wahlen|
|Arbeitsplatzdichte|AI0701|Anzahl|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Land- u. Forstwirtschaft, Fischerei|AI0702|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Produzierendes Gewerbe|AI0703|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Verarbeitendes Gewerbe|AI0704|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Baugewerbe|AI0705|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Dienstleistungsbereiche|AI0706|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Handel, Verkehr, Gastgewerbe, Informat., Kommun.|AI0707|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Finanz-, Versich.-, Unt.-dl., Grundst.-, Wohnungsw.|AI0708|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil ET Öffentl. u. sonst. Dienstl., Erziehung, Gesundh.|AI0709|Prozent|Erwerbstätige (ET) nach Wirtschaftsbereichen|AI007-1|Erwerbstätigkeit und Arbeitslosigkeit|
|Beschäftigtenquote am 30.06.|AI0710|Prozent|Beschäftigtenquote|AI007-2|Erwerbstätigkeit und Arbeitslosigkeit|
|Arbeitslosenquote|AI0801|Prozent|Arbeitslosenquote, Anteil Arbeitslose|AI008-1-5|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil Arbeitslose 15-24 Jahre an Arbeitslosen insgesamt|AI0806|Prozent|Arbeitslosenquote, Anteil Arbeitslose|AI008-1-5|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil Arbeitslose 55-64 Jahre an Arbeitslosen insgesamt|AI0807|Prozent|Arbeitslosenquote, Anteil Arbeitslose|AI008-1-5|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil Langzeitarbeitslose an Arbeitslosen insgesamt|AI0808|Prozent|Arbeitslosenquote, Anteil Arbeitslose|AI008-1-5|Erwerbstätigkeit und Arbeitslosigkeit|
|Anteil der ausl. Arbeitslosen an Arbeitslosen insgesamt |AI0809|Prozent|Arbeitslosenquote, Anteil Arbeitslose|AI008-1-5|Erwerbstätigkeit und Arbeitslosigkeit|
|Arbeitslosenquote Männer|AI0802|Prozent|Arbeitslosenquote für ausgewählte Personengruppen|AI008-2|Erwerbstätigkeit und Arbeitslosigkeit|
|Arbeitslosenquote Frauen|AI0803|Prozent|Arbeitslosenquote für ausgewählte Personengruppen|AI008-2|Erwerbstätigkeit und Arbeitslosigkeit|
|Arbeitslosenquote 15 bis 24 Jahre|AI0804|Prozent|Arbeitslosenquote für ausgewählte Personengruppen|AI008-2|Erwerbstätigkeit und Arbeitslosigkeit|
|Arbeitslosenquote Ausländerinnen und Ausländer|AI0805|Prozent|Arbeitslosenquote für ausgewählte Personengruppen|AI008-2|Erwerbstätigkeit und Arbeitslosigkeit|
|Durchschnittliche Betriebsgröße|AI0901|ha|Landwirtschaftl. Betriebe - Viehhaltung|AI009|Landwirtschaft|
|Rinder je 100 ha landwirtschaftlich genutzter Fläche|AI0902|Anzahl|Landwirtschaftl. Betriebe - Viehhaltung|AI009|Landwirtschaft|
|Schweine je 100 ha landwirtschaftlich genutzter Fläche|AI0903|Anzahl|Landwirtschaftl. Betriebe - Viehhaltung|AI009|Landwirtschaft|
|Investitionen je Beschäftigten|AI1001|Tsd. EUR|Investitionen|AI010-1|Industrie|
|Bruttoentgelte je Beschäftigten|AI1002|Tsd. EUR|Bruttoentgelte|AI010-2-5|Industrie|
|Anteil neue Wohngebäude mit 1 oder 2 Wohnungen|AI1101|Prozent|Bautätigkeit und Wohnen|AI011-5|Bauen und Wohnen|
|Fertiggestellte Wohnungen je 1.000 EW|AI1102|Anzahl|Bautätigkeit und Wohnen|AI011-5|Bauen und Wohnen|
|Durchschnittliche Aufenthaltsdauer|AI1201|Tage|Beherbergung|AI012-5|Tourismus|
|Übernachtungen je EW|AI1202|Anzahl|Beherbergung|AI012-5|Tourismus|
|Pkw-Bestand je 1.000 EW am 01.01.|AI1301|Anzahl|Pkw-Dichte|AI013-1|Verkehr|
|Straßenverkehrsunfälle je 10.000 EW|AI1302|Anzahl|Straßenverkehrsunfälle bezogen auf EW|AI013-2|Verkehr|
|Getötete bei Straßenverkehrsunfällen je 100.000 EW|AI1304|Anzahl|Straßenverkehrsunfälle bezogen auf EW|AI013-2|Verkehr|
|Verletzte bei Straßenverkehrsunfällen je 100.000 EW|AI1305|Anzahl|Straßenverkehrsunfälle bezogen auf EW|AI013-2|Verkehr|
|Straßenverkehrsunfälle je 10.000 Kfz|AI1303|Anzahl|Straßenverkehrsunfälle bezogen auf Kfz|AI013-3|Verkehr|
|Krankenhausbettendichte (Betten je 1.000 EW)|AI1401|Anzahl|Krankenhäuser|AI014-1|Gesundheits- und Sozialwesen|
|Pflegebedürftige je 1.000 EW ab 65 Jahre|AI1402|Anzahl|Pflege und Personal|AI014-2|Gesundheits- und Sozialwesen|
|Personal je 100 Pflegebedürftige in vollstationären Pflege|AI1403|Anzahl|Pflege und Personal|AI014-2|Gesundheits- und Sozialwesen|
|Personal je 100 Pflegebedürftige in ambulanter Pflege|AI1404|Anzahl|Pflege und Personal|AI014-2|Gesundheits- und Sozialwesen|
|Plätze in Pflegeheimen je 1.000 EW ab 65 Jahre|AI1405|Anzahl|Pflege und Personal|AI014-2|Gesundheits- und Sozialwesen|
|Beschäftigte Bund, Länder, Gemeinden/-verbände je 1.000 EW|AI1501|Anzahl|Beschäftigte im öffentlichen Bereich|AI015|Öffentliche Haushalte|
|Verfügbares Einkommen je EW|AI1601|EUR|Verfügbares Einkommen|AI016-1|Verdienste und Einkommen|
|Gesamtbetrag der Einkünfte je Steuerpflichtigen|AI1602|Tsd. EUR|Einkünfte|AI016-2-5|Verdienste und Einkommen|
|BIP je Erwerbstätigen|AI1701|EUR|Bruttoinlandsprodukt (BIP)|AI017-1|Bruttoinlandsprodukt und Bruttowertschöpfung|
|Veränderung des BIP zum Vorjahr|AI1702|Prozent|Bruttoinlandsprodukt (BIP)|AI017-1|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BIP je EW|AI1703|EUR|Bruttoinlandsprodukt (BIP)|AI017-1|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Land- und Forstwirtschaft, Fischerei|AI1705|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Produzierendes Gewerbe|AI1706|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Verarbeitendes Gewerbe|AI1707|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Baugewerbe|AI1708|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Dienstleistungsbereiche|AI1709|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Handel, Verkehr, Gastgewerbe, Information, Kommunikation|AI1710|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Finanz-, Versicherg., Untern.-dl., Grundst.-,Wohnungsw.|AI1711|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|BWS Öffentl. u. sonst. Dienstleister, Erziehung, Gesundheit|AI1712|Prozent|Bruttowertschöpfung (BWS)|AI017-2|Bruttoinlandsprodukt und Bruttowertschöpfung|
|Haushaltsabfälle je EW|AI1901|kg|Haushaltsabfälle|AI019|Umwelt|
|Haus- und Sperrmüll je EW|AI1902|kg|Haushaltsabfälle|AI019|Umwelt|
|Getrennt erfasste Wertstoffe je EW|AI1903|kg|Haushaltsabfälle|AI019|Umwelt|
|Abfälle aus der Biotonne je EW|AI1904|kg|Haushaltsabfälle|AI019|Umwelt|
|Biologisch abbaubare Garten- und Parkabfälle je EW|AI1905|kg|Haushaltsabfälle|AI019|Umwelt|
|verbrauchsabhängig. Entgelt Trinkwasserversorgung pro m³|AI1906|EUR|Wasserentgelt|AI019-1-5|Umwelt|
|verbrauchsunabhängig. Entgelt für Trinkwasserversorgung|AI1907|EUR|Wasserentgelt|AI019-1-5|Umwelt|
|Wasserabgabe je EW und Tag (in Liter)|AI1908|l|Wasserversorgung, Wasserabgabe|AI019-2|Umwelt|
|Väteranteil Elterngeldbezug|AI1801|Prozent|Elterngeldbezug|AIG-018|Gender|
|Anteil betreute Kinder 0-2 Jahre in Tageseinrichtungen am 01.03.|AI0301|Prozent|Kinderbetreuung|AIG-03-1|Gender|
|Anteil betreute Kinder 0-2 Jahre in Tagespflege am 01.03.|AI0302|Prozent|Kinderbetreuung|AIG-03-1|Gender|
|Anteil männl. Schulabgänger mit allgemeiner Hochschulreife|AI0310|Prozent|Bildung|AIG-03-2|Gender|
|Anteil männlicher Schulabgänger ohne Hauptschulabschluss|AI0308|Prozent|Bildung|AIG-03-2|Gender|
|Anteil männlicher Schulabgänger mit Hauptschulabschluss|AI0309|Prozent|Bildung|AIG-03-2|Gender|
|Beschäftigtenquote Männer am 30.06.|AI0711|Prozent|Erwerbstätigkeit|AIG-07-2|Gender|
|Beschäftigtenquote Frauen am 30.06.|AI0712|Prozent|Erwerbstätigkeit|AIG-07-2|Gender|
|Index Beschäftigtenquote am 30.06.|AI0713|Prozent|Erwerbstätigkeit|AIG-07-2|Gender|
|Arbeitslosenquote Männer|AI0802|Prozent|Arbeitslosigkeit|AIG-08-2|Gender|
|Arbeitslosenquote Frauen|AI0803|Prozent|Arbeitslosigkeit|AIG-08-2|Gender|
|Grundsicherungsquote Männer ab Altersgrenze|AI2203|Prozent|Grundsicherung|AIG-22|Gender|
|Grundsicherungsquote Frauen ab Altersgrenze|AI2204|Prozent|Grundsicherung|AIG-22|Gender|
|Index Grundsicherungsquote|AI2205|Prozent|Grundsicherung|AIG-22|Gender|
|Anteil Männer am pädag. Personal in Kindertageseinrichtungen am 01.03.|AI2401|Prozent|Männliches pädagogisches Personal|AIG-24|Gender|
|Gesundheitsausgaben je Einwohner/-in|GSAUS201|EUR|Gesundheitsausgaben|AIGG-01|Gesundheitsökonomische Gesamtrechnungen|
|Anteil der Ausgaben der Gesetzlichen Krankenversicherung (GKV) an den gesamten Gesundheitsausgaben|GSAAI22|Prozent|Gesundheitsausgaben|AIGG-01|Gesundheitsökonomische Gesamtrechnungen|
|Anteil der Ausgaben der Privaten Krankenversicherung (PKV) an den gesamten Gesundheitsausgaben|GSAAI26|Prozent|Gesundheitsausgaben|AIGG-01|Gesundheitsökonomische Gesamtrechnungen|
|Anteil der Ausgaben der Sozialen Pflegeversicherung (SPV) an den gesamten Gesundheitsausgaben|GSAAI23|Prozent|Gesundheitsausgaben|AIGG-01|Gesundheitsökonomische Gesamtrechnungen|
|Ant. d. Ausgaben der Priv. Haush. u. Organisationen o. Erwerbszweck a. d. ges. Gesundheitsausgaben|GSAAI28|Prozent|Gesundheitsausgaben|AIGG-01|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000 Einwohner/-innen am 31.12.|GSP102|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000 Einwohner/-innen in Arztpraxen|GSPAI121|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000 Einwohner/-innen in Zahnarztpraxen|GSPAI122|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000 Einwohner/-innen in Apotheken|GSPAI124|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000Einwohner/-innen in der ambulanten Pflege|GSPAI126|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Gesundheitspersonal je 1.000 Einwohner/-innen in der stationären und teilstationären Pflege|GSPAI133|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Vollzeitäquivalente (VZÄ) im Gesundheitswesen je 100 Beschäftigte am 31.12.|GSP131|Anzahl|Gesundheitspersonal|AIGG-02|Gesundheitsökonomische Gesamtrechnungen|
|Bruttowertschöpfung (in jew. Preisen) je Erwerbstätige/-n i. d. Gesundheitswirtschaft|GSBWS405|EUR|Gesundheitswirtschaft|AIGG-03|Gesundheitsökonomische Gesamtrechnungen|
|Anteil an der Bruttowertschöpfung der Gesamtwirtschaft im Land|GSBWS404|Prozent|Gesundheitswirtschaft|AIGG-03|Gesundheitsökonomische Gesamtrechnungen|
|Erwerbstätige in der Gesundheitswirtschaft je 1.000 Einwohner/-innen|GSERW507|Anzahl|Gesundheitswirtschaft|AIGG-03|Gesundheitsökonomische Gesamtrechnungen|
|Anteil an den Erwerbstätigen der Gesamtwirtschaft im Land|GSERW504|Prozent|Gesundheitswirtschaft|AIGG-03|Gesundheitsökonomische Gesamtrechnungen|
|Anteil Siedlungs- und Verkehrsfläche an Gesamtfläche|AI0111|Prozent|Flächennutzung nach ALKIS|AI-N-01-2-5|Nachhaltigkeit|
|Veränderung der Siedlungs- und Verkehrsfläche|AI0112|Prozent|Flächennutzung nach ALKIS|AI-N-01-2-5|Nachhaltigkeit|
|4-jährige Veränderung der Siedlungs- und Verkehrsfläche je EW|AI0115|qm|Flächennutzung nach ALKIS (4-jährige Veränderung)|AI-N-01-3-5|Nachhaltigkeit|
|4-jährige Veränderung der Siedlungsfläche|AI0116|ha|Flächennutzung nach ALKIS (4-jährige Veränderung)|AI-N-01-3-5|Nachhaltigkeit|
|4-jährige Veränderung der Verkehrsfläche|AI0117|ha|Flächennutzung nach ALKIS (4-jährige Veränderung)|AI-N-01-3-5|Nachhaltigkeit|
|4-jährige Veränderung der Freiraumfläche je EW|AI0118|qm|Flächennutzung nach ALKIS (4-jährige Veränderung)|AI-N-01-3-5|Nachhaltigkeit|
|Anteil Siedlungs- und Verkehrsfläche an Gesamtfläche|AI0101|Prozent|Flächennutzung nach ALB|AI-N-01-5|Nachhaltigkeit|
|Veränderung der Siedlungs- und Verkehrsfläche|AI0105|Prozent|Flächennutzung nach ALB|AI-N-01-5|Nachhaltigkeit|
|Ökologischer Landbau|AI0904|Prozent|Landbewirtschaftung|AI-N-02|Nachhaltigkeit|
|Wanderungssaldo je 10.000 EW|AI0212|Anzahl|Bevölkerung - Wanderung|AI-N-03|Nachhaltigkeit|
|Altenquotient|AI0215|Anzahl|Bevölkerung - Alterung|AI-N-04|Nachhaltigkeit|
|Jugendquotient|AI0216|Anzahl|Bevölkerung - Alterung|AI-N-04|Nachhaltigkeit|
|Gesamtquotient|AI0217|Anzahl|Bevölkerung - Alterung|AI-N-04|Nachhaltigkeit|
|Ganztagsbetreuung 0 bis 2 Jahre am 01.03.|AI0311|Prozent|Ganztagsbetreuung von Kindern|AI-N-05|Nachhaltigkeit|
|Ganztagsbetreuung 3 bis 5 Jahre am 01.03.|AI0312|Prozent|Ganztagsbetreuung von Kindern|AI-N-05|Nachhaltigkeit|
|Anteil Schulabgänger/-innen mit allgem. Hochschulreife|AI0304|Prozent|Bildung|AI-N-06|Nachhaltigkeit|
|Anteil Schulabgänger/-innen ohne Hauptschulabschluss|AI0305|Prozent|Bildung|AI-N-06|Nachhaltigkeit|
|Arbeitslosenquote 15 bis 24 Jahre|AI0804|Prozent|Arbeitslosigkeit junger Menschen|AI-N-07|Nachhaltigkeit|
|Pkw-Bestand je 1.000 EW am 01.01.|AI1301|Anzahl|Pkw-Dichte|AI-N-08-01|Nachhaltigkeit|
|Getötete bei Straßenverkehrsunfällen je 100.000 EW|AI1304|Anzahl|Straßenverkehr|AI-N-08-02|Nachhaltigkeit|
|Armutsgefährdungsquote (Bundesmedian)|AI2301|Prozent|Armutsgefährdung|AI-N-09|Nachhaltigkeit|
|BIP je EW|AI1703|EUR|Wirtschaftliche Leistungsfähigkeit - BIP je EW|AI-N-10|Nachhaltigkeit|
|BIP je Arbeitsstunde|AI1704|EUR|Wirtschaftliche Leistungsfähigkeit - BIP je Arbeitsst.|AI-N-11|Nachhaltigkeit|
|Haushaltsabfälle je EW|AI1901|kg|Umwelt|AI-N-12|Nachhaltigkeit|
|Verfügbares Einkommen je EW|AI1601|EUR|Verfügbares Einkommen je EW|AI-S-01|Soziales|
|Armutsgefährdungsquote (Bundesmedian)|AI2301|Prozent|Armutsgefährdung|AI-S-02|Soziales|
|Armutsgefährdungsquote (regionaler Median)|AI2302|Prozent|Armutsgefährdung|AI-S-02|Soziales|
|Mindestsicherungsquote|AI2001|Prozent|Mindestsicherungsleistungen|AI-S-03|Soziales|
|SGB II-Quote bis Altersgrenze|AI2102|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Quote erwerbsfähige SGB II-Leistungsberechtigte|AI2108|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Quote erwerbsfähige SGB II-Leistungsberechtigte Frauen|AI2109|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Quote erwerbsfähige SGB II-Leistungsberechtigte Männer|AI2110|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Anteil Empfänger/-innen Arbeitslosengeld II bis 24 Jahre|AI2105|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Anteil Empfänger/-innen Arbeitslosengeld II ab 55 Jahre|AI2106|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Anteil Kinder mit Bezug von Sozialgeld|AI2107|Prozent|Grundsicherung für Arbeitssuchende (SGB II)|AI-S-04|Soziales|
|Grundsicherungsquote ab Altersgrenze|AI2201|Prozent|Grundsicherung im Alter und bei Erwerbsminderung|AI-S-05|Soziales|
|Grundsicherungsquote wegen Erwerbsminderung|AI2202|Prozent|Grundsicherung im Alter und bei Erwerbsminderung|AI-S-05|Soziales|
|Grundsicherungsquote Männer ab Altersgrenze|AI2203|Prozent|Grundsicherung im Alter und bei Erwerbsminderung|AI-S-05|Soziales|
|Grundsicherungsquote Frauen ab Altersgrenze|AI2204|Prozent|Grundsicherung im Alter und bei Erwerbsminderung|AI-S-05|Soziales|
|Durchschnittsalter Gesamtbevölkerung|AI-Z01|Anzahl|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Durchschnittsalter weibliche Bevölkerung|AI-Z02|Anzahl|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Durchschnittsalter männliche Bevölkerung|AI-Z03|Anzahl|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Anteil Personen mit MHG an der Gesamtbevölkerung|AI-Z04|Prozent|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Anteil Personen mit MHG 0 bis 19 Jahre|AI-Z05|Prozent|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Anteil Personen mit MHG 20 bis 59 Jahre|AI-Z06|Prozent|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Anteil Personen mit MHG 60 Jahre und älter|AI-Z07|Prozent|Bevölkerung - Durchschnittsalter - Migrationshintergrund|AI-Z1-2011|Zensus|
|Erwerbslosenquote|AI-Z08|Prozent|Erwerbstätigkeit|AI-Z2-2011|Zensus|
|Erwerbstätigenquote|AI-Z09|Prozent|Erwerbstätigkeit|AI-Z2-2011|Zensus|
|Erwerbstätigenquote Frauen|AI-Z10|Prozent|Erwerbstätigkeit|AI-Z2-2011|Zensus|
|Erwerbstätigenquote Männer|AI-Z11|Prozent|Erwerbstätigkeit|AI-Z2-2011|Zensus|
|Durchschnittliche Haushaltsgröße|AI-Z12|Anzahl|Haushalte|AI-Z3-2011|Zensus|
|Anteil Einpersonenhaushalte|AI-Z13|Prozent|Haushalte|AI-Z3-2011|Zensus|
|Haushalte mit Kindern|AI-Z14|Prozent|Haushalte|AI-Z3-2011|Zensus|
|Wohnungen je Wohngebäude|AI-Z15|Anzahl|Wohn- und Gebäudezählung|AI-Z4-2011|Zensus|
|Eigentümerquote|AI-Z16|Prozent|Wohn- und Gebäudezählung|AI-Z4-2011|Zensus|
|Leerstandsquote|AI-Z17|Prozent|Wohn- und Gebäudezählung|AI-Z4-2011|Zensus|
|Durchschnittliche Wohnfläche je EW|AI-Z18|m²|Wohn- und Gebäudezählung|AI-Z4-2011|Zensus|
|Durchschnittliche Wohnfläche je Wohnung|AI-Z19|m²|Wohn- und Gebäudezählung|AI-Z4-2011|Zensus|





**Parameter** *f*

Output-Format (z.B. "json" oder "html").


**Parameter** *outFields*

Auszugebende Variablen/fields (z.B. "*").


**Parameter** *returnGeometry*
Boolsche Angabe, ob Angaben zur Geometrie gesendet werden sollen (z.B. "false").


**Parameter** *spatialRel*

spational relation (z.B. "esriSpatialRelIntersects").


**Parameter** *where*

Spezifikation einer gewünschten Teilmenge der Daten (z.B."1=1"" für alle Daten oder "ags2 = 'DG' and jahr2 =  2020")


### Beispiel

```bash
bevoelkerungsdichteJeBundesland=$(curl https://www.gis-idmz.nrw.de/arcgis/rest/services/stba/regionalatlas/MapServer/dynamicLayer/query?layer=%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D&f=json&outFields=*&returnGeometry=false&spatialRel=esriSpatialRelIntersects&where=1%3D1)
```
