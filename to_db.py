import psycopg2
import requests
import ipaddress
import psycopg2.errors

URLS = ["https://openphish.com/feed.txt",
        "https://www.badips.com/get/list/any/2",
        "http://reputation.alienvault.com/reputation.data"]


def get_data(url):
    r = requests.get(url)
    data = r.content.decode('utf8').strip()
    data = data.split('\n')
    return data


def process_reputation(data):
    processed_data = list()
    for d in data:
        processed_data.append(d.split("#")[0])
    return processed_data


def is_ip_address(address):
    if ":" in address:
        address = address.split(':')[0]
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


def insert_source(source, conn):
    """
    Inserts source into DB
    :return: Returns ID of inserted source
    """
    try:
        with conn:
            with conn.cursor() as cur:
                insert_sql = "INSERT INTO source (source_url) VALUES (%s) RETURNING id"
                cur.execute(insert_sql, (source,))
                source_id = cur.fetchone()[0]
    except psycopg2.errors.UniqueViolation:
        with conn:
            with conn.cursor() as cur:
                select = "SELECT id FROM source WHERE source_url = (%s)"
                cur.execute(select, (source,))
                source_id = cur.fetchone()[0]

    return source_id


def insert_url(url, source_id, conn):
    """
    :param url: URL to store in DB
    :param curs: DB cursor
    :return: None
    """
    try:
        with conn:
            with conn.cursor() as cur:
                insert_sql = "INSERT INTO urls (url_adress, source_id) VALUES (%s, %s)"
                cur.execute(insert_sql, (url, source_id))
    except psycopg2.errors.UniqueViolation:
        print(f"{url} already in DB, skipping.")


def insert_IP(ip_address, source_id, conn):
    """
    :param ip_address: IP to store in DB
    :param source_id: Foreign key for source_id
    :param curs: DB cursor
    :return: None
    """
    try:
        with conn:
            with conn.cursor() as cur:
                insert_sql = "INSERT INTO ips (ip_adress, source_id) VALUES (%s, %s)"
                cur.execute(insert_sql, (ip_address, source_id))
    except psycopg2.errors.UniqueViolation:
        print(f"{ip_address} already in DB, skipping.")


if __name__ == "__main__":

    conn = psycopg2.connect(
        user='postgres',
        password='*******',
        host="127.0.0.1",
        port="5432",
        database='nova'

    )

    for url in URLS:
        data = get_data(url)
        if url == "http://reputation.alienvault.com/reputation.data":
            data = process_reputation(data)
        _len = len(data)
        source_id = insert_source(url, conn)

        for index, i in enumerate(data):
            if is_ip_address(i):
                print(f"{index+1}/{_len}: INSERTING {i}")
                insert_IP(i, source_id, conn)
            else:
                print(f"{index + 1}/{_len}: INSERTING {i}")
                insert_url(i, source_id, conn)
    conn.close()
