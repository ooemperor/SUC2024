TRUNCATE TABLE immoscout_mieten;
TRUNCATE TABLE immoscout_kaufen;
TRUNCATE TABLE immoscout_keywords;

INSERT INTO public.immoscout_mieten
SELECT NOW() AS Load_DTS,
       id,
       fullid,
       CONCAT('https://immoscout24.ch', fullid) as uri,
       street,
       title,
       type,
       LEFT(city, 4) AS plz,
       city,
       country,
       anzahl_badezimmer,
       anzahl_etagen,
       anzahl_wohnungen,
       anzahl_zimmer,
       baujahr,
       etage,
       grundstueckflaeche,
       inseratenummer,
       kubatur,
       CAST(letztes_renovationsjahr AS BIGINT),
       CASE WHEN miete = 'auf Anfrage' THEN NULL ELSE CAST(miete AS BIGINT) END AS miete,
       mindestnutzflaeche,
       CASE WHEN nebenkosten = 'auf Anfrage' THEN NULL ELSE CAST(nebenkosten AS BIGINT) END AS nebenkosten,
       CASE WHEN nettomiete = 'auf Anfrage' THEN NULL ELSE CAST(nettomiete AS BIGINT) END AS nettomiete,
       nutzflaeche,
       objekt_ref,
       objekttyp,
       raumhoehe,
       verfuegbarkeit,
       CAST(replace(wohnflaeche, ' m2', '') AS BIGINT),
       description
FROM stage.immoscout_mieten;

INSERT INTO public.immoscout_kaufen
SELECT NOW() AS Load_DTS,
       id,
       fullid,
       CONCAT('https://immoscout24.ch', fullid) as uri,
       street,
       LEFT(city, 4) AS plz,
       city,
       country,
       title,
       type,
       anzahl_badezimmer,
       anzahl_etagen,
       anzahl_wohnungen,
       anzahl_zimmer,
       baujahr,
       bruttorendite,
       etage,
       grundstueckflaeche,
       inseratenummer,
       CASE WHEN kaufpreis = 'auf Anfrage' THEN NULL ELSE CAST(kaufpreis AS BIGINT) END AS kaufpreis,
       kubatur,
       CAST(letztes_renovationsjahr AS BIGINT),
       mindestnutzflaeche,
       nutzflaeche,
       objekt_ref,
       objekttyp,
       raumhoehe,
       verfuegbarkeit,
       CAST(replace(wohnflaeche, ' m2', '') AS BIGINT),
       description
FROM stage.immoscout_kaufen;


INSERT INTO public.immoscout_keywords
SELECT fullid, keyword from stage.immoscout_keywords;