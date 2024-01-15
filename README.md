<div align='center'>
  <h1>Text-to-Speech Search Engine 💬</h1>
</div>
<br>

<div align='center'>
  <br>
  <img src="https://github.com/altamsh04/Text-To-Speech-Search-Engine/assets/84860267/fd7ceb4b-00ba-4a6c-9273-a8ecf066809a" alt="TS Screenshot">
  <br>
</div>

The Text-to-Speech Search Engine is a Python-based application that utilizes the Wikipedia module to provide a user-friendly interface for searching and retrieving information. The graphical user interface (GUI) is built using the tkinter library, and text-to-speech functionality is implemented using the pyttsx3 module.

## Technologies Used
- Python

## Python Modules Used
1. **tkinter:** Used for creating the graphical user interface (GUI) to interact with the user.
2. **pyttsx3:** Employs text-to-speech synthesis to convert the retrieved information into audible speech.
3. **wikipedia:** Enables the application to fetch and summarize information from Wikipedia based on user queries.

## Features
1. **Search Functionality:**
   - Allows users to input queries and retrieves information from Wikipedia using the `wikipedia` module.
   - Displays a summary of the search results in the GUI.
2. **Text-to-Speech:**
   - Utilizes the `pyttsx3` module to convert the retrieved information into spoken words.
   - Enhances accessibility and provides an alternative way to consume information.
3. **Error Handling:**
   - Warns users if the query is too ambiguous or if no results are found on Wikipedia.
4. **Clear and Repeat:**
   - Clear button resets the search bar and result area.
   - Repeat button reads aloud the content present in the result area.

## How to Use
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/altamsh04/Text-To-Speech-Search-Engine.git
   ```
2. Ensure you have Python installed on your machine.
3. Run the Python script `search.py`.
4. Enter your query in the search bar and click the "Search" button.
5. View the search results in the GUI.
6. Use the "Repeat" button to listen to the retrieved information.
7. Clear the search bar and result area using the "Clear" button.

## Dependencies
- The application relies on external libraries such as `tkinter`, `pyttsx3`, and `wikipedia`. Make sure to install them using:
   ```bash
   pip install tk
   pip install pyttsx3
   pip install wikipedia
   ```
