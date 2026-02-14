# Logging

# Every system produce a lot of messages and a lot of states, information, and errors.
# The system will store the kinds conditions into "logging"
# It's like a report of the system that keep update you about system's condition and activities

# 5 security levels
# DEBUG: When you're testing around your troubleshooting, what happens at a certain the value of the code
# INFO: Informational messages. Just announcing and printing the information
# *WARNING: Indicates that something might happen if you don't do something. Warns you to consider the actions.
# ERROR: Do something wrong in the code but not that harsh. Couldn't do the calculations so do something about it.
# CRITICAL: Essentials part of the system breaks down! NEED TO FIX RIGHT NOW.

# *Python have the default security level of warning and security's higher levels works!

import logging

logging.basicConfig(level=logging.DEBUG) # Set your level of security

logging.info("You've got 30 mails in your inbox.")
logging.warning("You can't open an emails in your inbox.")
logging.critical("All components failed!")

logger = logging.getLogger("Fluke's Logger")
logger.info("My best logger just made created!")
logger.critical("You haven't answered the client emails yet!")
logger.log(logging.ERROR, msg="Error. Those files are not founded.")

logger.setLevel(logging.DEBUG) # Set this is fine

handler = logging.FileHandler("mylog.log") # Create log files
handler.setLevel(logging.DEBUG)

# Ask for what happens at that time. what the system gonna say at that exact time.
formatter = logging.Formatter("%(levelname)s: - %(asctime)s: %(message)s))")
handler.setFormatter(formatter)
# Check out the mylog.log will have a timestamp

logger.addHandler(handler) # just print the message there

logger.debug("You haven't attached the files on the email.")
logger.info("Your email have been sent successfully!")

