from requests import get, post
from typing import BinaryIO, Callable, TypedDict
from typing_extensions import NotRequired, Required


class CreateBookRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/create-a-book
    """

    name: Required[str]
    """
    The name of the Book that will be created.
    """

    book_class: NotRequired[str]
    """
    The processing type of the book. Can be either 'COMPLETE' or 'INSTANT'.
    By default this value will be set to COMPLETE unless your organization is configured to have INSTANT as the default.
    """

    book_type: NotRequired[str]
    """
    Describes how the Book was created. This feature is in beta. See our guides on OPTIMA and WIDGET for additional information.
    """

    is_public: NotRequired[bool]
    """
    `true` allows all users in your organization to see and upload Documents into this Book.
    """

    xid: NotRequired[str]
    """
    A free form field that can be used to associate a Book with some identity outside of Ocrolus.
    """


class DeleteBookRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/delete-a-book
    """

    book_id: NotRequired[int]
    """
    The PK of the Book you'd like to delete. Mutually exclusive with `book_uuid`.
    """

    book_uuid: NotRequired[str]
    """
    The unique identifier of the Book you'd like to delete. Mutually exclusive with `book_id`.
    """


class UpdateBookRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/update-book
    """

    book_uuid: NotRequired[str]
    """
    The unique identifier of the Book you want to configure. Mutually exclusive with `pk`.
    """

    pk: NotRequired[int]
    """
    The PK of the Book you want to configure. Mutually exclusive with `book_uuid`.
    """

    book_class: NotRequired[str]
    """
    Determines what type of processing the Book will go through. By default this value will be set to COMPLETE unless your organization is configured to have INSTANT as the default.
    """

    book_type: NotRequired[str]
    """
    Describes how the Book was created. This feature is in beta. See our guides on OPTIMA and WIDGET for additional information.
    """

    is_public: NotRequired[bool]
    """
    `true` allows all users in your organization to see and upload Documents into this Book.
    """

    name: NotRequired[str]
    """
    The Book's new name. If not given, the name will be unchanged.
    """

    xid: NotRequired[str]
    """
    A free form field that can be used to associate a Book with some identity outside of Ocrolus.
    """


class BookInfoRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/book-info
    """

    book_uuid: NotRequired[str]
    """
    The unique identifier of the Book whose information you want to retrieve. Mutually exclusive with `book_pk`.
    """

    pk: NotRequired[int]
    """
    Unique primary key (pk) of the Book whose information you want to retrieve. Mutually exclusive with `book_uuid`.
    """


class BookListRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/book-list
    """

    limit: NotRequired[int]
    """
    Sets the number of results to return.
    """

    offset: NotRequired[int]
    """
    Sets the starting point of the results list. The list is index-based and starts at integer 0.
    """

    order: NotRequired[str]
    """
    By default, results are returned in descending order, which is newest to oldest.
    """

    order_by: NotRequired[str]
    """
    Determines what field to order the results by.
    """

    search: NotRequired[str]
    """
    Limits the results based on a keyword search using book_name
    """


class BookStatusRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/book-status
    """

    book_uuid: NotRequired[str]
    """
    The unique identifier of the Book whose status you want to retrieve. Mutually exclusive with book_pk.
    """

    pk: NotRequired[int]
    """
    Unique primary key (pk) of the Book whose status you want to retrieve. Mutually exclusive with book_uuid.
    """


class UploadDocumentRequest(TypedDict):
    book_uuid: NotRequired[str]
    """
    The unique identifier of the Book that the uploaded Document will be saved to. Mutually exclusive with pk.
    """

    pk: NotRequired[int]
    """
    The PK of the Book that the uploaded Document will be saved to. Mutually exclusive with book_uuid.
    """

    form_type: NotRequired[str]
    """
    The code identifying the type of Document that you're uploading.
    """

    doc_name: NotRequired[str]
    """
    The name of the Document that will be created from the imported file. Defaults to the name of the file if not given.
    """


class Client:
    """
    A client for the Ocrolus API.

    https://docs.ocrolus.com/reference/ocrolus-api-intro
    """

    def __init__(
        self,
        bearer_token_provider: Callable[[], str],
        base_url: str = "https://api.ocrolus.com",
    ):
        self.bearer_token_provider = bearer_token_provider
        self.base_url = base_url

    def _headers(self):
        return {"Authorization": f"Bearer {self.bearer_token_provider()}"}

    def create_book(self, req: CreateBookRequest):
        """
        Create a Book that you can use to group related Documents.

        https://docs.ocrolus.com/reference/create-a-book
        """

        res = post(f"{self.base_url}/v1/book/add", headers=self._headers(), json=req)
        return res.json()

    def delete_book(self, req: DeleteBookRequest):
        """
        Delete a Book that you no longer need.

        https://docs.ocrolus.com/reference/delete-a-book
        """

        res = post(f"{self.base_url}/v1/book/remove", headers=self._headers(), json=req)
        return res.json()

    def update_book(self, req: UpdateBookRequest):
        """
        Configure various properties of a Book.

        https://docs.ocrolus.com/reference/update-book
        """

        res = post(f"{self.base_url}/v1/book/update", headers=self._headers(), json=req)
        return res.json()

    def book_info(self, req: BookInfoRequest):
        """
        Retrieve details of a Book, including uploaded Documents, bank account information, and transaction periods.

        https://docs.ocrolus.com/reference/book-info
        """

        res = get(f"{self.base_url}/v1/book/info", headers=self._headers(), json=req)
        return res.json()

    def book_list(self, req: BookListRequest = {}):
        """
        Retrieve a list of all Books available to the current user.

        https://docs.ocrolus.com/reference/book-list
        """

        res = get(f"{self.base_url}/v1/books", headers=self._headers(), json=req)
        return res.json()

    def book_status(self, req: BookStatusRequest):
        """
        Retrieve the status of a Book.

        https://docs.ocrolus.com/reference/book-status
        """

        res = get(f"{self.base_url}/v1/books", headers=self._headers(), json=req)
        return res.json()

    def upload_document(self, req: UploadDocumentRequest, upload: BinaryIO):
        """
        Upload a PDF file to a Book for processing.

        https://docs.ocrolus.com/reference/upload-document
        """

        res = post(
            f"{self.base_url}/v1/book/upload",
            headers=self._headers(),
            data=req,
            files={"upload": upload},
        )
        return res.json()
