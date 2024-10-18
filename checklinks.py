# The purpsoe of this file is to check external links in markdown files
import os
import requests

# Load all markdown files recursively in the docs folder
def load_markdown_filenames():
    markdown_files = []
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

# Load a markdown file and return the content
def load_markdown_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Check all links in a markdown file
def check_links_in_markdown_file(filename):
    content = load_markdown_file(filename)
    lines = content.split("\n")
    for line in lines:
        if "](http" in line:
            start = line.index("](http") + 2
            end = line.index(")", start)
            url = line[start:end]
            check_link(url, filename)

# Check a link
def check_link(url, filename):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {url} - {filename}")
        else:
            #print(f"OK: {url} - {filename}")
            pass # Ignore OK for now
    except Exception as e:
        print(f"Error: {e} - {url} - {filename}")


# Main function
def main():
    markdown_files = load_markdown_filenames()
    for filename in markdown_files:
        check_links_in_markdown_file(filename)

# Run the main function
if __name__ == "__main__":
    print("Note: some sites will give 403 errors because cloudflate doesn't like the Python requests library.")
    main()