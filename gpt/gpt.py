import os
# import config   
import openai   
import conn
import json
import time
import utils
from timeit import default_timer as timer



class GPT:

    def __init__(self, text) -> None:
        
        self.text = text 

    # Generation function to create JSON outputs and store them
    def generation(self, iterations, code_text, prompt_name, prompt_command):
        # Initialize lists to store responses, response times, and token counts
        response_list = []
        time_list = []
        tokens_list = []

        # Iterating over the specified number of iterations
        for i in range(iterations):
            # Start timing the response generation
            start = timer()
            
            # Get response from OpenAI using a custom connection module
            openai_response = conn.connect_to_openai(prompt_command, code_text)
         
            # Append the response text and token count to their respective lists
            response_list.append(openai_response["choices"][0]["message"]["content"])
            tokens_list.append(openai_response['usage']['total_tokens'])

            # Stop timing and calculate elapsed time
            end = timer()
            time = end - start

            # Append elapsed time to the list
            time_list.append(time)

        # Extract the first response from the list
        res = response_list[0]

        # Convert the first response from string to JSON
        final_response = utils.string_to_json(res)
        return final_response

    # Main function to run the generation process and handle the output
    def value_gen(self, prompt_name):
        # Set the number of iterations for generation to 1
        iterations = 1

        # Retrieve the command associated with the given prompt name
        prompt_command = utils.grab_prompt_command(prompt_name)

        # Retrieve text to be processed
        code_text = self.text

        # Generate response for the given text and prompt
        response = self.generation(iterations, code_text, prompt_name, prompt_command)

        # Return appropriate response based on the prompt name
        if prompt_name == "judge":
            return response[0]
        else:
            return response[0][prompt_name]

# Main execution block of the script
if __name__ == "__main__":
    # Directory containing OCR text files
    codes_path = "codes"

    # Iterate through each file in the OCR text files directory
    for code_file in os.listdir(codes_path):
        # Construct full path to the file
        full_path = os.path.join("codes", code_file)

        # Read the content of the file
        code_text = open(full_path).read()

        # Instantiate a GPT3 object with the text
        object = GPT(code_text)

        # Set the prompt name
        prompt_name = "judge"

        # Generate response for the given prompt
        gpt_response = object.value_gen(prompt_name)

        # Output the generated response
        print(gpt_response)