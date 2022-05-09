#!/usr/bin/env python3
# brother.py>
from configparser import *
from PIL import Image, ImageDraw, ImageFont
#from brother_ql.conversion import convert
#from brother_ql.backends.helpers import send
#from brother_ql.raster import BrotherQLRaster

# Define configuration
def config():
    try:
        config = ConfigParser()
        config.read("config.ini")
        var1 = config.get("BROTHER", "backend")
        var2 = config.get("BROTHER", "model")
        var2 = config.get("BROTHER", "printer")
        return var1, var2
    except Exception as e:
        print("[+] BROTHER ERROR,", e)
        return -1

def create_label(**var):
    try:
        image = Image.new("RGB", (400,200), "white")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial", 20)
        spacing = 0
        text = """

        """ + var.get('firstname') + """ """ + var.get('insertion') + """ """ + var.get('lastname') + """

        """ + var.get('place') + """

        """ + var.get('date-of-birth')

        draw.text((0,0), text, fill="black", font=font, spacing=spacing)
        return image
    except Exception as e:
        print("[+] BROTHER ERROR,", e)
        return -1

def main(**var):
    # Read configuration
    backend = config()[0] # 'pyusb', 'linux_kernal', 'network'
    model = config()[1]   # your printer model
    printer = config()[2] # Get these values from the Windows usb driver filter.  Linux/Raspberry Pi uses '/dev/usb/lp0'
    if backend == -1 or model == -1 or printer == -1:
        return -1

    # Create label
    label = create_label(**var)
    label.show()
    #label.save('sample-out.png')

    # Print label
    """
    qlr = BrotherQLRaster(model)
    qlr.exception_on_warning = True

    instructions = convert(
        qlr=qlr, 
        images=[label],    #  Takes a list of file names or PIL objects.
        label='29x90', 
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
    """

# DEBUG TEST
if __name__ == "__main__":
    list= { "firstname":"test-fname",
            "insertion":"",
            "lastname":"test-lname",
            "place":"test-place",
            "date-of-birth":"test-date"
        }
    main(**list)