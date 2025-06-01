import sys
import os
import configparser
from jinja2 import Environment, FileSystemLoader

# Check for correct usage
if len(sys.argv) != 2:
    print("Usage: python code_generator.py <config.ini>")
    sys.exit(1)

# Get the ini file from argument
ini_file = sys.argv[1]

# Verify the ini file exists
if not os.path.isfile(ini_file):
    print(f"Error: {ini_file} does not exist.")
    sys.exit(1)

# Load configuration from ini file
config = configparser.ConfigParser()
config.read(ini_file)

# Required keys for template replacement
required_keys = ["print_msg", 
		        "func_name", 
		        "func_desc", 
		        "func_int"]
                
if not all(key in config['OVERWRITE_INFO'] for key in required_keys):
    print("Error: Missing required keys in ini file.")
    sys.exit(1)

# Define the directory containing the template file
template_dir = '.'  # Change this to the actual template directory if needed
template_file = 'template.c'

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load the template
template = env.get_template(template_file)

# Define values to be replaced in the template
context = {key: value for key, value in config['OVERWRITE_INFO'].items()}

# Render the template with the provided values
output = template.render(context)

# Save the generated output to a new .c file
output_file = f"axis_{context['print_msg']}.c"
with open(output_file, "w") as f:
    f.write(output)

print(f"Generated C file: {output_file}")
