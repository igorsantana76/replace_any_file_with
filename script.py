import os
import re

input_folder = "input"
output_folder = "output"
pattern = r'\{(.*?)\}'

def read_all_file(file_name):
    text_content = ""
    if file_name.endswith(".txt"):
        f = open(os.path.join(input_folder, file_name), 'r')
        text_content += f.read()
    return text_content

def replace_strings_with_python(text):
    matches = set(re.findall(pattern, text))

    if not matches:
        return text

    replacements = {}
    for match in matches:
        replacement = input(f"Substituir '{match}' por: ")
        replacements[match] = replacement

    for match, replacement in replacements.items():
        text = text.replace(f'{{{match}}}', replacement)

    return text

def main():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        print(f"Substituindo arquivo '{file_name}':\n")
        text = read_all_file(file_name)
        output_text = replace_strings_with_python(text)
        output_file_name = os.path.join(output_folder, file_name)
        with open(output_file_name, 'w') as output_file:
            output_file.write(output_text)
        print('\n\n')
    
main()
print("Arquivos substituidos com sucesso, https://www.linkedin.com/in/igor-santana-5b8a49116/")