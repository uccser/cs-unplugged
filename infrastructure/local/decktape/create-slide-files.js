const http = require('http');
const fs = require('fs');
const path = require('path');
const { execSync } = require("child_process");

// Top level directory is created by inherited Docker image and is mapped
// by Docker Compose to the csunplugged/build/ directory to set the correct
// permissions.
const ROOT_PATH = '/slides/'
// The second /slides/ directory to be created in
// the build directory with the correct permissions.
const FILES_BASE_PATH = path.join(ROOT_PATH, '/slides/');
const BASE_URL = 'http://django:8000';


function generateSlideFiles(data) {
    var resolution = data.resolution;

    // For each language
    for (const [language_code, lesson_slugs] of Object.entries(data.languages)) {
        // For each lesson
        lesson_slugs.forEach(lesson_slug => {

            let output_directory = path.join(FILES_BASE_PATH, language_code, lesson_slug);
            let slide_count = data.slide_counts[lesson_slug]

            // Create directory if it doesn't exist
            if (!fs.existsSync(output_directory)) {
                fs.mkdirSync(output_directory, {recursive: true});
            }

            // Create screenshots and PDF
            execSync(
                `/decktape/decktape.js reveal \
                --chrome-path chromium-browser \
                --chrome-arg=--no-sandbox \
                --slides 1-${slide_count} \
                --screenshots \
                --screenshots-size=${resolution} \
                --screenshots-directory=${output_directory} \
                ${BASE_URL}/${language_code}/at-a-distance/${lesson_slug}/slides-file-generation/?hide-debug-toolbar\\\&hide-controls-modal \
                ${lesson_slug}.pdf`,
                {
                    stdio: 'inherit',
                },
            );

            // Move and rename PDF file to correct directory
            fs.renameSync(
                path.join(ROOT_PATH, `${lesson_slug}.pdf`),
                path.join(output_directory, `${lesson_slug}-slides.pdf`),
            )

            console.log(`Created '${language_code}' slide files for ${lesson_slug}.`)
        });
    }
}


var args = process.argv.slice(2);


if (args[0] == '--production') {
    query_parameters = 'language=all';
    console.log('Generating slide files for all languages')
} else if (args[0] == '--language' && args[1]) {
    language_code = args[1];
    query_parameters = `language=${language_code}`;
    console.log(`Generating slide files for '${language_code}' only`)
} else {
    query_parameters = '';
    console.log("Generating slide files for 'en' only")
}

http.get(BASE_URL + `/en/at-a-distance/slides-file-generation-json/?${query_parameters}`, res => {
    let data = [];

    res.on('data', chunk => {
        data.push(chunk);
    });

    res.on('end', () => {
        json_data = Buffer.concat(data).toString();
        console.log("Received data:");
        console.log(json_data);
        generateSlideFiles(JSON.parse(json_data));
    });
}).on('error', err => {
    console.log('Error: ', err.message);
});
