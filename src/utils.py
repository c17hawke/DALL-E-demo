from io import BytesIO


def resize_image(image, width, height):
    image = image.resize((width, height))
    bytes_stream = BytesIO()
    image.save(bytes_stream, format='PNG')
    return bytes_stream.getvalue()


def get_width_height(size):
    # size = '512x512'
    return [int(val) for val in size.split("x")] # [512, 512]