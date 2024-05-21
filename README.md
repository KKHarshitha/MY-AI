# MY-AI
-------> Introduction:

This Python script implements a voice-activated virtual assistant designed to assist users with a variety of tasks through spoken commands. Utilizing               libraries such as pyttsx3 for text-to-speech, speech_recognition for capturing voice input, wikipedia for information retrieval, and requests for AI                chatbot interactions, the assistant can provide time and date information, perform web searches, take screenshots, send messages via WhatsApp, play YouTube         videos, send emails, and control music playback. Additionally, it can execute system commands like shutting down or restarting the PC. This versatile               assistant enhances user productivity by automating routine tasks through voice interactions.

------->The provided code is a Python script for a voice-activated virtual assistant. It utilizes several libraries to perform various tasks:

pyttsx3 for text-to-speech functionality.
speech_recognition for capturing and recognizing spoken commands.
wikipedia for fetching summaries from Wikipedia.
pyscreeze for taking screenshots.
pywhatkit for YouTube and WhatsApp interactions.
smtplib for sending emails.
requests and json for making API calls to an AI chatbot service for more complex queries.
The assistant can:
        
Greet the user and provide the current time and date.
Recognize voice commands and respond appropriately.
Perform web searches, play YouTube videos, and send WhatsApp messages.
Send emails, take screenshots, and interact with Wikipedia.
Remember and recall notes.
Control playback of songs through a custom sample module.
Execute system commands like shutting down or restarting the PC.
The main loop continuously listens for user commands and executes corresponding functions until the user decides to exit.

--------> How to use the code?:

To use the provided code, follow these steps:
        
Install the required libraries:
Ensure you have all necessary Python packages installed. You can install them using pip:
        
bash
Copy code
pip install pyttsx3 speechrecognition wikipedia pyscreeze requests pywhatkit smtplib
Set up the required API keys and modules:
        
Ensure you have a valid API key for the AI chatbot and replace the placeholder Bearer <your_token_here> with your actual token in the headers dictionary.
Make sure the sample module is present and properly implemented with the playsong and control functions.
Run the script:
Execute the script in your Python environment:
        
bash
Copy code
python <your_script_name>.py
Interact with the assistant:
The assistant will greet you and wait for your commands. You can speak various commands such as:
        
"What is the time?"
"What is the date?"
"Search Wikipedia for [topic]"
"Take a screenshot"
"Open YouTube and search for [video]"
"Send WhatsApp message to [number]"
"Remember [note]"
"Say what you remember"
"Send email to [email]"
"Play song from [path]"
"Pause the song"
"Unpause the song"
        "Stop the song"
"Shut down my PC"
"Restart my PC"
Any other general query for the AI chatbot to handle.
The assistant will respond to your voice commands and perform the corresponding actions. If a command is not recognized or an error occurs, the assistant will ask you to repeat the command.
        
--------> Conclusion:

The provided code is a comprehensive script for a voice-activated virtual assistant that leverages various Python libraries to offer a wide range of                functionalities. These include responding to time and date queries, searching Wikipedia, taking screenshots, interacting with YouTube and WhatsApp, sending         emails, and controlling music playback. Additionally, it can remember user notes and execute system commands like shutting down or restarting the PC. The           integration with an AI chatbot API allows it to handle more complex queries. By following the setup instructions and running the script, users can interact         with the assistant through voice commands to automate and simplify numerous tasks.
