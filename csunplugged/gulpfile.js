////////////////////////////////
// Setup
////////////////////////////////

// Gulp and package
const { src, dest, parallel, series, watch, lastRun } = require('gulp')
const pjson = require('./package.json')

// Plugins
const autoprefixer = require('autoprefixer')
const browserify = require('browserify')
const browserSync = require('browser-sync').create()
const buffer = require('vinyl-buffer');
const c = require('ansi-colors')
const concat = require('gulp-concat')
const cssnano = require('cssnano')
const dependents = require('gulp-dependents')
const errorHandler = require('gulp-error-handle')
const filter = require('gulp-filter')
const gulpif = require('gulp-if');
const { hideBin } = require('yargs/helpers')
const imagemin = require('gulp-imagemin')
const log = require('fancy-log')
const pixrem = require('pixrem')
const postcss = require('gulp-postcss')
const postcssFlexbugFixes = require('postcss-flexbugs-fixes')
const reload = browserSync.reload
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps')
const spawn = require('child_process').spawn
const tap = require('gulp-tap')
const terser = require('gulp-terser')
const yargs = require('yargs/yargs')

// Arguments
const argv = yargs(hideBin(process.argv)).argv
const PRODUCTION = !!argv.production;

// Relative paths function
function pathsConfig(appName) {
    this.app = `./${pjson.name}`
    const vendorsRoot = 'node_modules'
    const staticSourceRoot = 'static'
    const staticOutputRoot = 'build'

    return {
        app: this.app,
        // Source files
        bootstrap_source: `${vendorsRoot}/bootstrap/scss`,
        css_source: `${staticSourceRoot}/css`,
        scss_source: `${staticSourceRoot}/scss`,
        js_source: `${staticSourceRoot}/js`,
        images_source: `${staticSourceRoot}/img`,
        files_source: `${staticSourceRoot}/files`,
        fonts_source: `${staticSourceRoot}/fonts`,
        vendor_js_source: [
            `${vendorsRoot}/jquery/dist/jquery.js`,
            `${vendorsRoot}/popper.js/dist/umd/popper.js`,
            `${vendorsRoot}/bootstrap/dist/js/bootstrap.js`,
            `${vendorsRoot}/details-element-polyfill/dist/details-element-polyfill.js`,
            `${vendorsRoot}/scratchblocks/build/scratchblocks.min.js`,
            `${vendorsRoot}/multiple-select/dist/multiple-select-es.js`,
        ],
        // Output files
        css_output: `${staticOutputRoot}/css`,
        images_output: `${staticOutputRoot}/img`,
        js_output: `${staticOutputRoot}/js`,
        files_output: `${staticOutputRoot}/files`,
        fonts_output: `${staticOutputRoot}/fonts`,
    }
}

var paths = pathsConfig()

function catchError(error) {
    log.error(
        c.bgRed('Error:'),
        c.red(error)
    );
    this.emit('end');
}

////////////////////////////////
// Config
////////////////////////////////

// CSS/SCSS
const processCss = [
    autoprefixer(),         // adds vendor prefixes
    pixrem(),               // add fallbacks for rem units
    postcssFlexbugFixes(),  // adds flexbox fixes
]
const printProcessCss = [
    pixrem(),               // add fallbacks for rem units
]
const minifyCss = [
    cssnano({ preset: 'default' })   // minify result
]

// JS

const js_files_skip_optimisation = [
    // Optimise all files
    '**',
    // But skip the following files
    // For example: '!static/js/vendor/**/*.js'
];

////////////////////////////////
// Tasks
////////////////////////////////

// Styles autoprefixing and minification
function css() {
    return src(`${paths.css_source}/**/*.css`)
        .pipe(errorHandler(catchError))
        .pipe(sourcemaps.init())
        .pipe(postcss(processCss))
        .pipe(sourcemaps.write())
        .pipe(gulpif(PRODUCTION, postcss(minifyCss))) // Minifies the result
        .pipe(dest(paths.css_output))
}

function scss() {
    function postcss_callback(file) {
        if (file.basename.endsWith('.print.css')) {
            return { plugins: printProcessCss }
        } else {
            return { plugins: processCss }
        }
    }
    return src(`${paths.scss_source}/**/*.scss`, { since: lastRun(scss) })
        .pipe(errorHandler(catchError))
        .pipe(dependents())
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: [
                paths.bootstrap_source,
                paths.scss_source
            ],
            sourceComments: !PRODUCTION,
        }).on('error', sass.logError))
        .pipe(postcss(postcss_callback))
        .pipe(sourcemaps.write())
        .pipe(gulpif(PRODUCTION, postcss(minifyCss))) // Minifies the result
        .pipe(dest(paths.css_output))
}

// Javascript
function js() {
    const js_filter = filter(js_files_skip_optimisation, { restore: true })
    return src([
            `${paths.js_source}/**/*.js`,
            `!${paths.js_source}/modules/**/*.js`
        ], { since: lastRun(js) })
        .pipe(errorHandler(catchError))
        .pipe(sourcemaps.init())
        .pipe(js_filter)
        .pipe(tap(function (file) {
            file.contents = browserify(file.path, { debug: true }).bundle().on('error', catchError);
        }))
        .pipe(buffer())
        .pipe(gulpif(PRODUCTION, terser({ keep_fnames: true })))
        .pipe(js_filter.restore)
        .pipe(sourcemaps.write())
        .pipe(dest(paths.js_output))
}

// Vendor Javascript (always minified)
function vendorJs() {
    return src(paths.vendor_js_source)
        .pipe(errorHandler(catchError))
        .pipe(concat('vendors.js'))
        .pipe(terser())
        .pipe(dest(paths.js_output))
}

// Image compression
function img() {
    return src(`${paths.images_source}/**/*`)
        .pipe(gulpif(PRODUCTION, imagemin())) // Compresses PNG, JPEG, GIF and SVG images
        .pipe(dest(paths.images_output))
}

// Downloadable files
function files() {
    return src(`${paths.files_source}/**/*`)
        .pipe(dest(paths.files_output))
}

// Custom fonts files
function fonts() {
    return src(`${paths.fonts_source}/**/*`)
        .pipe(dest(paths.fonts_output))
}

// Browser sync server for live reload
// TODO: Not yet working
// function initBrowserSync() {
//     browserSync.init({
//         // https://www.browsersync.io/docs/options/#option-proxy
//         proxy: {
//                 target: 'cs-unplugged.localhost:8000',
//                 proxyReq: [
//                     function (proxyReq, req) {
//                         // Assign proxy "host" header same as current request at Browsersync server
//                         proxyReq.setHeader('Host', req.headers.host)
//                     }
//                 ]
//             },
//             // https://www.browsersync.io/docs/options/#option-open
//             // Disable as it doesn't work from inside a container
//             open: false
//         }
//     )
// }

// Watch
function watchPaths() {
    watch([`${paths.js_source}/**/*.js`], js).on("change", reload)
    watch([`${paths.css_source}/**/*.css`], css).on("change", reload)
    watch([`${paths.scss_source}/**/*.scss`], scss).on("change", reload)
    watch([`${paths.images_source}/**/*`], img).on("change", reload)
}

// Generate all assets
const generateAssets = parallel(
    css,
    scss,
    js,
    vendorJs,
    img,
    files,
    fonts
)

// Set up dev environment
const dev = parallel(
    // initBrowserSync,
    watchPaths
)
// TODO: Look at cleaning build folder
exports["generate-assets"] = generateAssets
exports["dev"] = dev
exports.default = series(generateAssets, dev)
