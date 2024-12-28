import psycopg2
from config import config


def execute_sql_immo_DB(sqlStatement: str) -> bool:
    """
    Executes a SQL Statement on the database
    :param sqlStatement: the Statement that shall be executed.
    :type sqlStatement: str
    :return: The output of the query
    """
    try:
        conn = psycopg2.connect(user=config.db_username, password=config.db_password, host=config.db_host, port=config.db_port,
                                dbname=config.db_name)
        cur = conn.cursor()
        cur.execute(sqlStatement)
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)
        print(sqlStatement)
    return True


def write_immoscout_kaufen_to_DB(values: dict) -> None:
    """
    Inserts the given values for a buy object into the database
    :param values: The values for the buy object
    :type values: dict
    :return: None
    """
    insert_sql = (f"INSERT INTO stage.immoscout_kaufen(	id, "
                  f"fullid, "
                  f"street, "
                  f"city, "
                  f"title, "
                  f"type, "
                  f"anzahl_badezimmer, "
                  f"anzahl_etagen, "
                  f"anzahl_wohnungen, "
                  f"anzahl_zimmer, "
                  f"baujahr, "
                  f"bruttorendite, "
                  f"etage, "
                  f"grundstueckflaeche, "
                  f"inseratenummer, "
                  f"kaufpreis, "
                  f"kubatur, "
                  f"letztes_renovationsjahr, "
                  f"mindestnutzflaeche, "
                  f"nutzflaeche, "
                  f"objekt_ref, "
                  f"objekttyp, "
                  f"raumhoehe, "
                  f"verfuegbarkeit, "
                  f"wohnflaeche, "
                  f"description) VALUES ("
                  f"NULLIF('{values.get('id', '''''')}', ''),"
                  f"NULLIF('{values.get('fullId', '''''')}', ''),"
                  f"NULLIF('{values.get('street', '''''')}', ''),"
                  f"NULLIF('{values.get('city', '''''')}', ''),"
                  f"NULLIF('{values.get('title', '''''')}', ''),"
                  f"NULLIF('{values.get('type', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Badezimmer', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Etagen', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Wohnungen', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Zimmer', '''''')}', ''),"
                  f"NULLIF('{values.get('Baujahr', '''''')}', ''),"
                  f"NULLIF('{values.get('Bruttorendite', '''''')}', ''),"
                  f"NULLIF('{values.get('Etage', '''''')}', ''),"
                  f"NULLIF('{values.get('Grundstückfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Inseratenummer', '''''')}', ''),"
                  f"NULLIF('{values.get('Kaufpreis', '''''')}', ''),"
                  f"NULLIF('{values.get('Kubatur', '''''')}', ''),"
                  f"NULLIF('{values.get('Letztes Renovationsjahr', '''''')}', ''),"
                  f"NULLIF('{values.get('Mindestnutzfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Nutzfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Objekt-Ref.', '''''')}', ''),"
                  f"NULLIF('{values.get('Objekttyp', '''''')}', ''),"
                  f"NULLIF('{values.get('Raumhöhe', '''''')}', ''),"
                  f"NULLIF('{values.get('Verfügbarkeit', '''''')}', ''),"
                  f"NULLIF('{values.get('Wohnfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('description', '''''')}', ''));"
                  )
    execute_sql_immo_DB(insert_sql)


def write_immoscout_mieten_to_DB(values: dict) -> None:
    """
    Inserts the given values for a renting object into the database
    :param values: The values for the renting object
    :type values: dict
    :return: None
    """
    insert_sql = (f"INSERT INTO stage.immoscout_mieten(	id, "
                  f"fullid, "
                  f"street, "
                  f"city, "
                  f"title, "
                  f"type, "
                  f"anzahl_badezimmer, "
                  f"anzahl_etagen, "
                  f"anzahl_wohnungen, "
                  f"anzahl_zimmer, "
                  f"baujahr, "
                  f"etage, "
                  f"grundstueckflaeche, "
                  f"inseratenummer, "
                  f"kubatur, "
                  f"letztes_renovationsjahr, "
                  f"miete, "
                  f"mindestnutzflaeche, "
                  f"nebenkosten, "
                  f"nettomiete, "
                  f"nutzflaeche, "
                  f"objekt_ref, "
                  f"objekttyp, "
                  f"raumhoehe, "
                  f"verfuegbarkeit, "
                  f"wohnflaeche, "
                  f"description) VALUES ("
                  f"NULLIF('{values.get('id', '''''')}', ''),"
                  f"NULLIF('{values.get('fullId', '''''')}', ''),"
                  f"NULLIF('{values.get('street', '''''')}', ''),"
                  f"NULLIF('{values.get('city', '''''')}', ''),"
                  f"NULLIF('{values.get('title', '''''')}', ''),"
                  f"NULLIF('{values.get('type', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Badezimmer', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Etagen', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Wohnungen', '''''')}', ''),"
                  f"NULLIF('{values.get('Anzahl Zimmer', '''''')}', ''),"
                  f"NULLIF('{values.get('Baujahr', '''''')}', ''),"
                  f"NULLIF('{values.get('Etage', '''''')}', ''),"
                  f"NULLIF('{values.get('Grundstückfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Inseratenummer', '''''')}', ''),"
                  f"NULLIF('{values.get('Kubatur', '''''')}', ''),"
                  f"NULLIF('{values.get('Letztes Renovationsjahr', '''''')}', ''),"
                  f"NULLIF('{values.get('Miete', '''''')}', ''),"
                  f"NULLIF('{values.get('Mindestnutzfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Nebenkosten', '''''')}', ''),"
                  f"NULLIF('{values.get('Nettomiete', '''''')}', ''),"
                  f"NULLIF('{values.get('Nutzfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('Objekt-Ref.', '''''')}', ''),"
                  f"NULLIF('{values.get('Objekttyp', '''''')}', ''),"
                  f"NULLIF('{values.get('Raumhöhe', '''''')}', ''),"
                  f"NULLIF('{values.get('Verfügbarkeit', '''''')}', ''),"
                  f"NULLIF('{values.get('Wohnfläche', '''''')}', ''),"
                  f"NULLIF('{values.get('description', '''''')}', ''));"
                  )

    execute_sql_immo_DB(insert_sql)
