from io import BytesIO
from PIL.PngImagePlugin import PngImageFile
from PIL.JpegImagePlugin import JpegImageFile
from typing import Union, List

ImageLike = Union[PngImageFile, JpegImageFile]

def resize_image(image: ImageLike, width: int, height: int) -> bytes:
    """resize image to the given width and height

    Args:
        image (ImageLike): input image to resize of type PngImageFile or JpegImageFile
        width (int): expected width of the image
        height (int): expected height of the image

    Returns:
        bytes: a new image with the given width and height in PNG format
    """
    image = image.resize((width, height))
    bytes_stream = BytesIO()
    image.save(bytes_stream, format='PNG')
    return bytes_stream.getvalue()


def get_width_height(size: str) -> List:
    """get width and height of the image from the given size as a string, for example - 
        size = '512x512' 

    Args:
        size (str): size described as '_width_x_height_' example '512x512'

    Returns:
        List: returns a list of interger as [width, height] extracted from the 
        given size
    """
    # size = '512x512'
    return [int(val) for val in size.split("x")] # [512, 512]
