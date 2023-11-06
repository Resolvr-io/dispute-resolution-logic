#This file contains all ultily functions that are needed for the gpt package


# Import necessary modules
import os
import json
import sys

# Function to write JSON data to a text file. It overwrites the file if it already exists.
def write_json_file(text, folder, name):
    # Open (or create) a file in write mode. The filename is a combination of folder, name, and a suffix.
    file = open(folder + name + "-json.txt", "w")
    # Write the text (assumed to be JSON data) to the file.
    file.write(text)
    # Close the file to ensure data is saved and file is properly closed.
    file.close()

# Function to write text data to a text file. It overwrites the file if it already exists.
def write_text_file(text, folder, name):
    # Open (or create) a file in write mode. The filename is a combination of folder and name.
    file = open(folder + name + ".txt", "w")
    # Write the text to the file.
    file.write(text)
    # Close the file to ensure data is saved and file is properly closed.
    file.close()

# Function to append text data to an existing text file. Creates a new file if it doesn't exist.
def append_text_file(text, folder, name):
    # Open (or create) a file in append mode. The filename is a combination of folder and name.
    file = open(folder + name + ".txt", "a")
    # Append the text to the file.
    file.write(text)
    # Close the file to ensure data is saved and file is properly closed.
    file.close()

# Function to convert a string to JSON. Returns a list containing the JSON object, or an error message.
def string_to_json(string):
    try:
        # Attempt to parse the string as JSON.
        jsoner = json.loads(string)
        # Return the JSON object inside a list.
        return [jsoner]
    except:
        # If parsing fails, return a list with an error message.
        return [{"error": "string_to_json broke"}]

# Function to extract and return the 'total_tokens' value from a JSON response.
def get_token(response):
    # Extract the 'total_tokens' value from the 'usage' dictionary in the response.
    token = response['usage']['total_tokens']
    return token

# Function to retrieve a prompt text file's content if it exists in the specified 'Prompts' folder.
def grab_prompt_command(prompt_name, prompt_path="Prompts/"):
    # Append "_prompt.txt" to the prompt name to form the filename.
    prompt_name = prompt_name + "_prompt.txt"
    # Check the current working directory and adjust the path accordingly.
    if "gpt_pkg" in os.getcwd():
        path = os.path.join(os.getcwd(), "Prompts/")
    else:
        path = os.path.join(os.getcwd(), prompt_path)
    # Check if the file exists in the specified directory.
    if prompt_name in os.listdir(path):
        # Open the file and read its content.
        with open(path + prompt_name, "r") as f:
            text = f.read()
            # Return the text content of the file.
            return text
