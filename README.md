# Minecraft Server Finder
Checks random IP addresses for Minecraft servers using the official API and outputs them to a spreadsheet. The vast majority of checks will fail, but I found a couple after a few days of running it in the background. It's pretty cool to find hidden servers, but please don't use this for malicious purposes like griefing (I'm not legally liable if you do).

# Requirements
- Python 3
- mcstatus module (can be installed with pip)

# How to use (Windows)
Just double click `MC_Servers.py` or run it from the command line using `python MC_Servers.py` (make sure you `cd` into the right directory). When you're done, just X out the window, because I didn't implement an actual exit function.

You can check random ports with `python MC_Servers.py -p`, but I recommend leaving that off. Most servers use the default port so checking random ones will decrease your odds of finding a sever, but it does technically expand the number of servers you can find.
