from PIL import Image, ImageDraw, ImageFont
from random import sample


def resource_image(get_request, resource):
    """Creates a image for Treasure Hunt resource.

    Returns:
        A Pillow image object.
    """
    image_path = 'static/img/resource-treasure-hunt.png'
    font_path = 'static/fonts/PatrickHand-Regular.ttf'
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    prefilled_values = get_request['prefilled_values']
    range_min = 0
    if prefilled_values == 'easy':
        range_max = 100
        font_size = 97
    elif prefilled_values == 'medium':
        range_max = 1000
        font_size = 80
    elif prefilled_values == 'hard':
        range_max = 10000
        font_size = 70

    # Add numbers to image if required
    if prefilled_values != 'blank':
        font = ImageFont.truetype(font_path, font_size)

        total_numbers = 26
        numbers = sample(range(range_min, range_max), total_numbers)
        if get_request['number_order'] == 'sorted':
            numbers.sort()

        starting_coord_y = 494
        base_coord_y = starting_coord_y
        coord_y_increment = 286
        base_coords_x = [257, 692]
        for i in range(0, total_numbers):
            text = str(numbers[i])
            text_width, text_height = draw.textsize(text, font=font)

            coord_x = base_coords_x[i % 2] - (text_width / 2)
            coord_y = base_coord_y - (text_height / 2)
            if i % 2 == 1:
                coord_y -= 10
                base_coord_y += coord_y_increment
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill='#000'
            )

    return image
