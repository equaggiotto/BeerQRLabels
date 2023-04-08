import qrcode
from qrcode.image.pure import PyPNGImage

beer_info = """
Name:Easy Going Ale\n
Date Brewed:17/03/2023\n
Date Bottled:03/4/2023\n
2.5G+60g Dextrose\n
OG:1.0300\n
FG:1.0000\n
Grain:[5.5lb 2-Row Malted Barley,\n
3lb Morris Otter Pale Ale Malt,\n
0.25lb Crystal 60L,\n
0.5lb Buiscuit Malt]
Boil Time: 60min\n
Hops[1.25oz East Kent Golding 60min,\n
1oz Sterling 5min,\n
Whirfloc tablet 15min]\n
"""

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=0,
    image_factory=PyPNGImage
)
qr.add_data(data=beer_info)
img = qr.make_image(fill_color="black", back_color="white")
img.save("easy_going_17_3_2023.png")