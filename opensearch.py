import json
from opensearchpy import OpenSearch, helpers

# Connect to OpenSearch (update the host if needed)
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'StrongPassword123!'),
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)

INDEX_NAME = "recipes"

def load_data():
    with open('recipes.json', 'r') as f:
        data = json.load(f)
        for recipe in data:
            yield {
                "_index": INDEX_NAME,
                "_source": recipe
            }
helpers.bulk(client, load_data())
print("Data ingestion complete!")
