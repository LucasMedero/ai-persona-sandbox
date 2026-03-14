AI Character Sandbox
This project is an interactive sandbox designed to simulate conversations between AI-driven characters. Users can define unique personalities and observe how they interact with one another in a controlled environment.

Features
The primary feature of this project is the ability to create and simulate a dialogue between two distinct AI characters. To initiate a conversation, the user must provide:

Name: A unique identifier for the character.

Description: A detailed background or personality profile that guides the AI's behavior and tone.

Once both characters are configured, the system utilizes the Gemini API to generate a dynamic interaction based on their respective traits.

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x

Visual Studio Code (recommended)

A valid Gemini API Key

Installation
Clone the Repository
Clone this repository to your local machine using terminal or the Git integration in Visual Studio Code.

Install Dependencies
Open the project folder in Visual Studio Code. Open the integrated terminal and run the following command to install the necessary libraries listed in the requirements.txt file:

Bash
pip install -r requirements.txt
Environment Configuration
Create a file named .env in the root directory of the project. This file is used to manage sensitive information. Add your Gemini API key to the file as follows:


GEMINI_API_KEY=your_api_key_here
How to Run
To test the project and start the sandbox, follow these steps:

Ensure your virtual environment is active (if applicable).

In the Visual Studio Code terminal, execute the main script:

Bash
python app.py
Follow the on-screen prompts to input the names and descriptions for your two characters.

The application will then generate the interaction between the defined AI personas.
