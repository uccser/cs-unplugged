'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
var fs = require('fs');
var del = require('del');
var uglify = require('gulp-uglify');
var gulpif = require('gulp-if');
var exec = require('child_process').exec;
var runSequence = require('run-sequence')
var notify = require('gulp-notify');
var buffer = require('vinyl-buffer');
var argv = require('yargs').argv;
// sass
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var postcssFlexbugFixes = require('postcss-flexbugs-fixes');
var autoprefixer = require('autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
// BrowserSync
var browserSync = require('browser-sync');
// js
var watchify = require('watchify');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
// linting
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
// Scratch image rendering
var scratchblocks = require('scratchblocks');
var rename = require("gulp-rename");
var through = require('through2');
var PluginError = require('gulp-util').PluginError;

// gulp build --production
var production = !!argv.production;
// determine if we're doing a build
// and if so, bypass the livereload
var build = argv._.length ? argv._[0] === 'build' : false;
var watch = argv._.length ? argv._[0] === 'watch' : true;

// ----------------------------
// Error notification methods
// ----------------------------
var beep = function() {
  var os = require('os');
  var file = 'gulp/error.wav';
  if (os.platform() === 'linux') {
    // linux
    exec("aplay " + file);
  } else {
    // mac
    console.log("afplay " + file);
    exec("afplay " + file);
  }
};
var handleError = function(task) {
  return function(err) {
    beep();

      notify.onError({
        message: task + ' failed, check the logs..',
        sound: false
      })(err);

    gutil.log(gutil.colors.bgRed(task + ' error:'), gutil.colors.red(err));
  };
};
var scratchSVG = function() {
  var PLUGIN_NAME = 'scratchSVG';
  return through.obj(function(file, encoding, callback) {
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
          file.contents = new Buffer(doc.exportSVGString());
        })
        return callback(null, file);
    }
  });
};
// --------------------------
// CUSTOM TASK METHODS
// --------------------------
var tasks = {
  // --------------------------
  // Delete build folder
  // --------------------------
  clean: function() {
    return del(['build/']);
  },
  // --------------------------
  // Copy static images
  // --------------------------
  images: function() {
    return gulp.src('static/img/**/*')
      .pipe(gulp.dest('build/img'));
  },
  // --------------------------
  // CSS
  // --------------------------
  css: function() {
    return gulp.src('static/css/**/*.css')
      .pipe(gulp.dest('build/css'));
  },
  // --------------------------
  // JS
  // --------------------------
  js: function() {
    return gulp.src('static/js/**/*.js')
      .pipe(gulp.dest('build/js'));
  },
  // --------------------------
  // Scratch
  // --------------------------
  scratch: function() {
    return gulp.src('temp/scratch-blocks-*.txt')
      .pipe(scratchSVG())
      .pipe(rename(function (path) {
        path.extname = ".svg"
      }))
      // give it a file and save
      .pipe(gulp.dest('build/img'));
  },
  // --------------------------
  // SASS (libsass)
  // --------------------------
  sass: function() {
    return gulp.src('static/scss/*.scss')
      // sourcemaps + sass + error handling
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
      .pipe(postcss([autoprefixer({browsers: ['last 2 versions']}), postcssFlexbugFixes]))
      // we don't serve the source files
      // so include scss content inside the sourcemaps
      .pipe(sourcemaps.write({
        'includeContent': true
      }))
      // write sourcemaps to a specific directory
      // give it a file and save
      .pipe(gulp.dest('build/css'));
  },

  // --------------------------
  // linting
  // --------------------------
  lintjs: function() {
    return gulp.src([
        'gulpfile.js',
        'static/js/index.js',
        'static/js/**/*.js'
      ]).pipe(jshint())
      .pipe(jshint.reporter(stylish))
      .on('error', function() {
        beep();
      });
  },
};

gulp.task('browser-sync', function() {
    browserSync.init({
        proxy: "localhost:8000",
        port: process.env.PORT || 3000
    });
});

gulp.task('reload-sass', ['sass'], function(){
  browserSync.reload();
});
gulp.task('reload-scratch', ['scratch'], function(){
  browserSync.reload();
});
gulp.task('reload-js', ['js'], function(){
  browserSync.reload();
});
gulp.task('reload-css', ['css'], function(){
  browserSync.reload();
});
gulp.task('reload-templates', [], function(){
  browserSync.reload();
});

// // --------------------------
// // CUSTOMS TASKS
// // --------------------------
gulp.task('clean', tasks.clean);
// // for production we require the clean method on every individual task
var req = [];
// // individual tasks
gulp.task('images', req, tasks.images);
gulp.task('js', req, tasks.js);
gulp.task('css', req, tasks.css);
gulp.task('sass', req, tasks.sass);
gulp.task('scratch', req, tasks.scratch);
gulp.task('lint:js', tasks.lintjs);
gulp.task('optimize', tasks.optimize);
gulp.task('test', tasks.test);

// --------------------------
// DEV/WATCH TASK
// --------------------------
gulp.task('watch', ['scratch', 'images', 'css', 'js', 'sass', 'browser-sync'], function() {
  // --------------------------
  // watch:scratch
  // --------------------------
  gulp.watch('temp/scratch-blocks-*.txt', ['reload-scratch']);

  // --------------------------
  // watch:sass
  // --------------------------
  gulp.watch('static/scss/**/*.scss', ['reload-sass']);

  // --------------------------
  // watch:js
  // --------------------------
  gulp.watch('static/js/**/*.js', ['lint:js', 'reload-js']);

  // --------------------------
  // watch:css
  // --------------------------
  gulp.watch('static/css/**/*.css', ['reload-css']);

  // --------------------------
  // watch:templates
  // --------------------------
  gulp.watch('templates/**/*.html', ['reload-templates']);

  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});

// build task
gulp.task('build', function(callback) {
  runSequence('clean', ['images', 'css', 'js', 'sass', 'scratch'], callback);
});

gulp.task('default', ['watch']);

// gulp (watch) : for development and livereload
// gulp build : for a one off development build
// gulp build --production : for a minified production build
