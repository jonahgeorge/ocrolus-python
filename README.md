# ocrolus-python

A Python client library for the [Ocrolus REST API](https://docs.ocrolus.com).

## Installing

TODO

<!--
```sh
pip install ocrolus-python
```
-->

## Usage

```py
from ocrolus.client import ApiClient, AuthClient

token_response = AuthClient().grant_auth_token({
    "grant_type": "client_credentials",
    "client_id": "...",
    "client_secret": "..."
})

api_client = ApiClient(token_response["access_token"])

res = api_client.create_book({ "name": "Test Book" })
print(res)

book_pk = res.get('response').get('id')

res = api_client.upload_document(
    {
        "pk": book_pk,
        "doc_name": "Test Doc",
        "form_type": "W2",
    },
    upload=open("/Users/jonahgeorge/Downloads/download.pdf", "rb")
)
print(res)
```
