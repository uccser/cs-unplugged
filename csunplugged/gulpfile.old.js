// gulp build : for a one off development build
// gulp build --production : for a minified production build

'use strict';

const js_files_skip_optimisation = [
  // Optimise all files
  '**',
  // But skip the following files
  // For example: '!static/js/vendor/**/*.js'
];

var gulp = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var gulpif = require('gulp-if');
var exec = require('child_process').exec;
var runSequence = require('run-sequence')
var notify = require('gulp-notify');
var buffer = require('vinyl-buffer');
var argv = require('yargs').argv;
const filter = require('gulp-filter');
const errorHandler = require('gulp-error-handle');

// sass
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var postcssFlexbugFixes = require('postcss-flexbugs-fixes');
var autoprefixer = require('autoprefixer');
var sourcemaps = require('gulp-sourcemaps');

// Scratch image rendering
var scratchblocks = require('scratchblocks');
var rename = require("gulp-rename");
var through = require('through2');
var PluginError = require('gulp-util').PluginError;

// gulp build --production
var production = !!argv.production;

// js
const tap = require('gulp-tap');
const terser = require('gulp-terser');
const browserify = require('browserify');

// ----------------------------
// Error notification methods
// ----------------------------
var handleError = function handle_error_func(task) {
    return function (err) {
        notify.onError({
            message: task + ' failed, check the logs..',
            sound: false
        })(err);

        gutil.log(gutil.colors.bgRed(task + ' error:'), gutil.colors.red(err));
    };
};

function catchError(error) {
    gutil.log(
        gutil.colors.bgRed('Error:'),
        gutil.colors.red(error)
    );
    this.emit('end');
}

// --------------------------
// Delete build folder
// --------------------------
function clean() {
    return del(['build/']);
}
// --------------------------
// Copy static images
// --------------------------
function images() {
    return gulp.src('static/img/**/*')
        .pipe(gulp.dest('build/img'));
}
// --------------------------
// CSS
// --------------------------
function css() {
    return gulp.src('static/css/**/*.css')
        .pipe(gulp.dest('build/css'));
}

// --------------------------
// Scratch
// --------------------------
function scratchSVG() {
    var PLUGIN_NAME = 'scratchSVG';
    return through.obj(function (file, encoding, callback) {
        if (file.isNull()) {
            // nothing to do
            return callback(null, file);
        }

        if (file.isStream()) {
            // file.contents is a Stream - https://nodejs.org/api/stream.html
            this.emit('error', new PluginError(PLUGIN_NAME, 'Streams not supported!'));
        } else if (file.isBuffer()) {
            // file.contents is a Buffer - https://nodejs.org/api/buffer.html
            var doc = scratchblocks.parse(file.contents.toString())
            doc.render(svg => {
                var string = doc.exportSVGString();
                // Remove invalid xmlns attribute due to issue https://github.com/scratchblocks/scratchblocks/issues/219
                string = string.replace(
                    /<use xmlns="http:\/\/www\.w3\.org\/1999\/xlink"/g,
                    '<use'
                );
                file.contents = new Buffer(string);
            })
            return callback(null, file);
        }
    });
};
function scratch() {
    return gulp.src('temp/scratch-blocks-*.txt')
        .pipe(scratchSVG())
        .pipe(rename(function (path) {
            path.extname = ".svg"
        }))
        // give it a file and save
        .pipe(gulp.dest('build/img'));
}

// --------------------------
// scss (libsass)
// --------------------------
function scss() {
    return gulp.src('static/scss/**/*.scss')
        .pipe(errorHandler(catchError))
        // sourcemaps + scss + error handling
        .pipe(gulpif(!production, sourcemaps.init()))
        .pipe(sass({
            sourceComments: !production,
            outputStyle: production ? 'compressed' : 'nested'
        }))
        .on('error', handleError('SASS'))
        // generate .maps
        .pipe(gulpif(!production, sourcemaps.write({
            'includeContent': false,
            'sourceRoot': '.'
        })))
        // autoprefixer
        .pipe(gulpif(!production, sourcemaps.init({
            'loadMaps': true
        })))
        .pipe(postcss([autoprefixer({ browsers: ['last 2 versions'] }), postcssFlexbugFixes]))
        // we don't serve the source files
        // so include scss content inside the sourcemaps
        .pipe(sourcemaps.write({
            'includeContent': true
        }))
        .pipe(rename(function (path) {
            path.dirname = path.dirname.replace("scss", "css");
        }))
        .pipe(gulp.dest('build/css'));
}
// --------------------------
// JavaScript
// --------------------------
function js() {
    const f = filter(js_files_skip_optimisation, { restore: true });
    return gulp.src(['static/**/*.js', '!static/js/modules/**/*.js'])
        .pipe(f)
        .pipe(errorHandler(catchError))
        .pipe(tap(function (file) {
            file.contents = browserify(file.path, { debug: true }).bundle().on('error', catchError);
        }))
        .pipe(buffer())
        .pipe(errorHandler(catchError))
        .pipe(gulpif(production, sourcemaps.init({ loadMaps: true })))
        .pipe(gulpif(production, terser({ keep_fnames: true })))
        .pipe(gulpif(production, sourcemaps.write('./')))
        .pipe(f.restore)
        .pipe(gulp.dest('build'));
}

// // --------------------------
// // CUSTOMS TASKS
// // --------------------------
// define complex tasks
const build = gulp.series(clean, gulp.parallel(images, css, scss, scratch, js));

// export tasks
exports.clean = clean;
exports.images = images;
exports.css = css;
exports.scss = scss;
exports.js = js;
exports.scratch = scratch;

exports.build = build;
exports.default = build;
