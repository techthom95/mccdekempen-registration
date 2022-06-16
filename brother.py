#!/usr/bin/env python3
# brother.py>
from configparser import *
from PIL import Image, ImageDraw, ImageFont
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

# Define configuration
def config():
    try:
        config = ConfigParser()
        config.read("config.ini")
        var1 = config.get("BROTHER", "backend")
        var2 = config.get("BROTHER", "model")
        var3 = config.get("BROTHER", "printer")
        var4 = config.get("DEFAULT", "year")
        return var1, var2, var3, var4
    except Exception as e:
        print("[+] BROTHER ERROR,", e)
        return -1

def create_label(year, **var):
    try:
        image = Image.new("RGB", (300,200), "white")
        draw = ImageDraw.Draw(image)
        font1 = ImageFont.truetype("arial", 30)
        font2 = ImageFont.truetype("arial", 16)
        spacing = 15
        text1 = "Trainingskaart " + year
        text2 =var.get('firstname') + """
""" + var.get('insertion') + """ """ + var.get('lastname') + """
""" + var.get('place') + """
""" + var.get('date-of-birth')

        draw.text((5,5), text1, fill="black", font=font1, spacing=spacing)
        draw.text((10,50), text2, fill="black", font=font2, spacing=spacing)
        return image
    except Exception as e:
        print("[+] BROTHER ERROR,", e)
        return -1

def main(**var):
    # Read configuration
    backend = config()[0] # 'pyusb', 'linux_kernal', 'network'
    model = config()[1]   # your printer model
    printer = config()[2] # Get these values from the Windows usb driver filter.  Linux/Raspberry Pi uses '/dev/usb/lp0'
    year = config()[3]
    if backend == -1 or model == -1 or printer == -1:
        return -1

    # Create label
    label = create_label(year, **var)
    #label.show()
    #label.save('sample-out.png')

    # Print label
    qlr = BrotherQLRaster(model)
    qlr.exception_on_warning = True

    instructions = convert(
        qlr=qlr, 
        images=[label],    #  Takes a list of file names or PIL objects.
        label='62', 
        rotate='90',    # 'Auto', '0', '90', '270'
        threshold=70.0,    # Black and white threshold in percent.
        dither=False, 
        compress=False, 
        red=False,    # Only True if using Red/Black 62 mm label tape.
        dpi_600=False, 
        hq=True,    # False for low quality.
        cut=True
    )

    send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)

# DEBUG TEST
if __name__ == "__main__":
    list = { "firstname":"test-fname",
                "insertion":"test-insert",
                "lastname":"test-lname",
                "place":"test-place",
                "date-of-birth":"test-date"
                }
    main(**list)