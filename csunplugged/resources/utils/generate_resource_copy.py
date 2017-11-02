"""Retrieve data for one copy of resource from resource generator."""

from utils.errors.ThumbnailPageNotFound import ThumbnailPageNotFound
from utils.errors.MoreThanOneThumbnailPageFound import MoreThanOneThumbnailPageFound
from PIL import Image
from io import BytesIO
import base64

MM_TO_PIXEL_RATIO = 6


def generate_resource_copy(generator, thumbnail=False):
    """Retrieve data for one copy of resource from resource generator.

    Images are resized to paper size.

    Args:
        generator: Instance of specific resource generator class.
        thumbnail: True if only the thumbnail page should be returned (bool).

    Raises:
        ThumbnailPageNotFound: If resource with more than one page does not
                               provide a thumbnail page.
        MoreThanOneThumbnailPageFound: If resource provides more than one page
                                       as the thumbnail.

    Returns:
        List of lists containing data for one copy.
        Each inner list contains:
        - String of type ("image", "html")
        - Data of type:
            - String for HTML.
            - Base64 string of image.
    """
    data = generator.data()
    if not isinstance(data, list):
        data = [data]

    paper_size = generator.requested_options["paper_size"]
    if paper_size == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif paper_size == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO

    if thumbnail and len(data) > 1:
        data = list(filter(lambda data: data.get("thumbnail"), data))
        if len(data) == 0:
            raise ThumbnailPageNotFound(generator)
        elif len(data) > 1:
            raise MoreThanOneThumbnailPageFound(generator)

    # Resize images to reduce file size
    for index in range(len(data)):
        if data[index]["type"] == "image":
            image = data[index]["data"]
            (width, height) = image.size
            if height > max_pixel_height:
                ratio = max_pixel_height / height
                width *= ratio
                height *= ratio
                image = image.resize((int(width), int(height)), Image.ANTIALIAS)
            # Convert from Image object to base64 string
            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")
            data[index]["data"] = base64.b64encode(image_buffer.getvalue())
    return data
