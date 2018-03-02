var gulp = require('gulp');
var pug  = require('gulp-pug');
var scss = require('gulp-sass');

var PATHS = {
    scss: [
        'dev/style/*.scss',
        'dev/style/student/*.scss',
    ],
    pug:  [
        'dev/template/*.pug',
        'dev/template/student/*.pug',
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


gulp.task('compile', function () {
    gulp.watch(PATHS.pug,  gulp.series('compile-pug'));
    gulp.watch(PATHS.scss, gulp.series('compile-scss'));
});
