# Import the relevant library
import win32com.client
# Set up a function from the library, which we will use as a voice
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# Define a piece of text we want read
websiteText = """
Biological research involves lots of data, typically stored on a computer.
Extracting the maximum amount of information from biological data is a task for bioinformaticians.
However, all biological researchers should have some computational tools at their disposal to help with data handling, processing and analysis.
Solely relying on Microsoft Excel for analysis is highly restrictive and expensive, and simply doesn't help with time-consuming tasks such as file formatting,
image manipulation or text manipulation.
"""
# Print the text to screen
print(websiteText)
# Read the text aloud
#speaker.Speak(websiteText)
