"""Retrieve data for one copy of resource from resource generator."""

from resources.utils.resize_encode_resource_images import resize_encode_resource_images


def generate_resource_copy(generator):
    """Retrieve data for one copy of resource from resource generator.

    Images are resized to paper size.

    Args:
        generator: Instance of specific resource generator class.

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
    return resize_encode_resource_images(generator, data)
