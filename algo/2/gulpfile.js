var gulp = require('gulp');
var pug  = require('gulp-pug');
var scss = require('gulp-sass');
var dart = require("gulp-dart");

var PATHS = {
    "scss": [
        'dev/style/*.scss',
        // 'dev/style/student/*.scss',
    ],
    "pug":  [
        'dev/template/*.pug',
        // 'dev/template/student/*.pug',
    ],
    "dart": [
        "dev/script/index.dart",
        // "dev/script/**/*.dart",
    ],
};


gulp.task('compile-pug', function () {
    return gulp.src(PATHS.pug)
               .pipe(pug({ pretty: true }))
               .pipe(gulp.dest(function (file) {
                   return file.base.replace(/\/dev\//, '/build/');
                }));
});


gulp.task('compile-scss', function () {
    return gulp.src(PATHS.scss)
               .pipe(scss({ outputStyle: 'nested' }))
               .pipe(gulp.dest(function (file) {
                   return file.base.replace(/\/dev\//, '/build/');
                }));
});


gulp.task('compile-dart', function () {
    return gulp.src(PATHS.dart)
               .pipe(dart({
                   "dest": "build/script",
                   "no-source-maps": true,
                   "enable-diagnostic-colors": true,
               }))
               .pipe(gulp.dest(function (file) {
                   return file.base.replace(/\/dev\//, '/build/');
               }));
});


gulp.task('compile', function () {
    gulp.watch(PATHS.pug,  gulp.series('compile-pug'));
    gulp.watch(PATHS.scss, gulp.series('compile-scss'));
    gulp.watch(PATHS.dart, gulp.series('compile-dart'));
});
