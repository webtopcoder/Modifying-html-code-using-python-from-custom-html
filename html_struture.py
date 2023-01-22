from bs4 import BeautifulSoup

# Read the custom HTML file
with open("custom_file.html", "r") as file:
    html_content = file.read()

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all the heading tags (h1, h2, h3...)
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

# Initialize a variable to keep track of the previous heading tag
prev_heading = None


soup = BeautifulSoup("", "html.parser")
# Iterate through each heading tag
for heading in headings:
    # Create a new "section" element
    section = soup.new_tag("section")
    # Set the class attribute to the heading level (e.g. "h1", "h2", "h3")
    section["class"] = heading.name

    if prev_heading is None:
        # If this is the first heading, insert the section element before the heading
        heading.insert_before(section)
    else:
        # If this is not the first heading, insert the section element after the previous heading
        prev_heading.insert_after(section)

    # Move all the elements between the current heading and the previous heading into the new section element
    for element in heading.next_siblings:
        if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            break
        section.append(element)

    prev_heading = heading

print("--------------", str(section))
# Write the modified HTML file
with open("modified_file.html", "w") as file:
    file.write(str(section))
