# On a CircuitPython microcontroller:
import board
import busio
uart = busio.UART(board.TX, board.RX, baudrate=19200)
import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
from digitalio import DigitalInOut, Direction, Pull
import time


printer = ThermalPrinter(uart)

btn = DigitalInOut(board.D5)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    if not btn.value:
        print("BTN is down")
        time.sleep(.2)
        printer.bold = True   # Turn on bold
        printer.print('Hello, [NAME OF NEW HIRE #1]!')
        printer.bold = False  # Turn off bold
        # Feed lines to make visible:
        printer.feed(2)
        printer.print('Welcome aboard! We are so excited to have you working with us at the Department of Transdimensional Musicology and New Religious Practices; Workers’ Union. I say we, but, so far it has really just been me. Or, I guess now, it’s us! Wow. I think we are going to get along great.')
        printer.feed(1)
        printer.print('As we discussed during your interview the department of late is not particularly well funded, which takes me away from our programming more than I’d like. You’ll see me around in the off hours when I’m not courting donations for the capital campaign (don’t forget to contribute if you haven’t already!) but for the most part, it’ll be up to you to keep up with the equipment and the day-to-day research we do here at DTMNRPWU. What we lack in supervision we make up for in hands-on experience and letters of recommendation!')
        printer.feed(1)
        printer.print('Until we can get you formally trained, why don’t you start by just having a look around? A lot has happened since we opened our doors a few weeks ago when the transdimensional portal first appeared (it’s the freaky glowing one that sometimes makes weird sounds). Every couple of days a new object falls out of it. We’ve been calling them “instruments,” but who knows what (or who) they really are for. We have been trying our best to communicate with the other side…and I think we are close to a big breakthrough. While you are around, feel free to answer the cord phone or to make calls. There’s usually someone on the other end but they don’t talk much.')
        printer.feed(1)
        printer.print('From here, use the attached link to access the email client for the department. There’s a lot of helpful information there and it’ll be what I use to communicate with you from here. Oh also, If you see a little robot running around, don’t mind them, that’s just Pete. We can check in on how things are going during your mid-year review but, otherwise, good luck!')
        printer.feed(2)
        printer.print('L Autumn Gnadinger')
        printer.print('(they/them/theirs)')
        printer.print('Temporary Administrative Appointment')
        printer.print('Department of Transdimensional Musicology')
        printer.print('& New Religious Practices; Workers’ Union.')
        printer.feed(2)
        printer.bold = True   # Turn on bold
        printer.print('-tear off and take with you-')
        printer.bold = False  # Turn off bold
    else:
        #print("BTN is up")
        pass

    time.sleep(.2) # sleep for debounce
