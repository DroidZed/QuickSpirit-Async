from typing import Any, Callable, Dict, Optional

from httpx import AsyncClient, HTTPStatusError, Response

from .http_errors import RequestError
from .models import Result


class HttpAsyncClient:
    """## Asynchronous HTTP client for making requests.

    ### Attributes:
        - client: The underlying AsyncClient instance for making requests.
    """

    async def send_request(
        self,
        method: str,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP request using the specified method.

        Args:
            method: The HTTP method to use (e.g., "get", "post").
            url: The URL to send the request to.
            body: The request body as a dictionary.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            A Result instance representing either the RAW response body
            or a RequestError if there was an error.

        Raises:
            RequestError: If there was an error in the request.
        """
        try:
            async with AsyncClient() as client:
                request_method: Callable = getattr(client, method)

                if method in {"get", "delete"}:
                    response: Response = await request_method(
                        url,
                        headers=headers,
                        params=url_params,
                    )

                else:
                    response = await request_method(
                        url,
                        data=data,
                        json=json,
                        headers=headers,
                        params=url_params,
                        files=files,
                    )

                response.raise_for_status()

                return Result(Data=response.read(), Error=None)

        except HTTPStatusError as exec:
            error_message = f"Endpoint returned: {exec.response.text}\n"

            return Result(Error=RequestError(error_message), Data=None)

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP GET request.

        Args:
            url: The URL to send the request to.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "get",
            url,
            headers=headers,
            url_params=url_params,
        )

    async def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP POST request.

        Args:
            url: The URL to send the request to.
            body: The request body as a dictionary.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "post",
            url,
            data=data,
            json=json,
            headers=headers,
            url_params=url_params,
            files=files,
        )

    async def put(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP PUT request.

        Args:
            url: The URL to send the request to.
            body: The request body as a dictionary.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "put",
            url,
            data=data,
            json=json,
            headers=headers,
            url_params=url_params,
            files=files,
        )

    async def patch(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP PATCH request.

        Args:
            url: The URL to send the request to.
            body: The request body as a dictionary.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "patch",
            url,
            data=data,
            json=json,
            headers=headers,
            url_params=url_params,
            files=files,
        )

    async def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
    ) -> Result:
        """Make an HTTP DELETE request.

        Args:
            url: The URL to send the request to.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "delete",
            url,
            headers=headers,
            url_params=url_params,
        )
