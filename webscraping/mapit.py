# mapit.py - open a browser and search for a place

import webbrowser, sys

if len(sys.argv) > 1:
   arguments = " ".join(sys.argv[1:])
   print(arguments)

if len(sys.argv) > 1:
   address= " ".join(sys.argv[1:])
   prefix = "https://www.google.ca/maps/place/"

   webbrowser.open(prefix + address)

# TODO: Get the address form the clipbroad.

