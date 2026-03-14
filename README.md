AI Persona Sandbox
This project is a sandbox environment designed to enable autonomous interaction between AI-configured characters. It uses the Gemini API to process responses and generate coherent dialogues based on user-provided descriptions.

Prerequisites
To run this project locally, you will need the following:

 -Visual Studio Code: The recommended text editor.

 -Live Server extension: To serve the application and handle requests correctly.

 -Gemini API Key: You must have a valid Google AI Studio API key.

Environment Setup
The project uses environment variables to protect sensitive information. Follow these steps to configure your access:

 1- Locate the file named .env in the project root (create it if it doesn't exist).

 2- Inside the file, add your API key as follows:
 GEMINI_API_KEY=your_key_here

 3- Be sure not to upload this file to public repositories if you decide to make personal modifications.

Installation and Execution
To test the project on your local machine:

 1- Clone this repository or download the files.

 2- Open the project's root folder with Visual Studio Code.

 3- Make sure you have the Live Server extension installed.

 4- Right-click on the index.html file and select the "Open with Live Server" option.

 5- The application will automatically open in your default browser (usually at http://127.0.0.1:5500).

How the Application Works
The main feature of this sandbox is the ability to generate conversations between two AI entities. To initiate an interaction, the user must follow these steps:

 1- Create the first character: Enter a name and a detailed description that defines its personality, tone, and knowledge.

 2- Create the second character: Enter a name and a description that establishes the context for this second individual.

 3- Start Conversation: Once both profiles are defined, the system will use the descriptions to automatically establish the dialogue flow between the two characters.
