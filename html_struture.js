const cheerio = require("cheerio");
const fs = require("fs");

// Read the custom HTML file
fs.readFile("custom_file.html", "utf8", (err, htmlContent) => {
    if (err) throw err;

    // Use cheerio to parse the HTML
    const $ = cheerio.load(htmlContent);

    // Find all the heading tags (h1, h2, h3...)
    const headings = $("h1, h2, h3, h4, h5, h6");

    // Initialize a variable to keep track of the previous heading tag
    let prevHeading = null;

    // Iterate through each heading tag
    headings.each((index, heading) => {
        // Create a new "section" element
        const section = $("<section>");
        // Set the class attribute to the heading level (e.g. "h1", "h2", "h3")
        section.attr("class", heading.name);

        if (prevHeading === null) {
            // If this is the first heading, insert the section element before the heading
            $(heading).before(section);
        } else {
            // If this is not the first heading, insert the section element after the previous heading
           
