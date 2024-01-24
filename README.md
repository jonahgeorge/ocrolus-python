# ocrolus-python

A Python client library for the [Ocrolus REST API](https://docs.ocrolus.com).

## Installing

```sh
pip install 'ocrolus @ git+https://github.com/jonahgeorge/ocrolus-python.git'
```

## Usage

```py
from ocrolus.client import Client
from ocrolus.token_provider import BearerTokenProvider

bearer_token_provider = BearerTokenProvider(client_id="...", client_secret="...")
client = Client(bearer_token_provider)

create_book_response = client.create_book({ "name": "Test Book" })
print(create_book_response)

book_id = create_book_response.get('response').get('id')
upload_document_response = client.upload_document(
    {
        "pk": book_id,
        "doc_name": "Test Doc",
        "form_type": "W2",
    },
    upload=open("/Users/jonahgeorge/Downloads/download.pdf", "rb")
)
print(upload_document_response)
```
