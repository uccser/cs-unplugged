from PIL import Image, ImageDraw, ImageFont
from random import sample
from django.utils.translation import ugettext as _

def resource_image(get_request, resource):
    """Creates a image for Sorting Network resource.

    Returns:
        A Pillow image object.
    """
    image_path = 'resources/content/{}/sorting-network-colour.png'.format(resource.folder)
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    prefilled_values = get_request['prefilled_values']
    if prefilled_values == 'easy':
        range_min = 1
        range_max = 10
        font_size = 150
    elif prefilled_values == 'medium':
        range_min = 10
        range_max = 100
        font_size = 120
    elif prefilled_values == 'hard':
        range_min = 100
        range_max = 1000
        font_size = 90

    font_path = 'resources/content/fonts/PatrickHand-Regular.ttf'

    # Add numbers to text if needed
    if prefilled_values != 'blank':
        font = ImageFont.truetype(font_path, font_size)
        numbers = sample(range(range_min, range_max), 6)
        base_coord_x = 70
        base_coord_y = 2560
        coord_x_increment = 204
        for number in numbers:
            text = str(number)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = base_coord_x - (text_width / 2)
            coord_y = base_coord_y - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill='#000'
            )
            base_coord_x += coord_x_increment

    return image
