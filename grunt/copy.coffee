module.exports =

  # Copy files and folders
  # https://github.com/gruntjs/grunt-contrib-copy

  tests:
    expand: true
    flatten: true
    src: '<%= paths.js %>/tests/lib/*.js'
    dest: '<%= paths.js %>/tests/build/'

  specRunner:
    src: '_SpecRunner.html'
    dest: '<%= paths.tests %>/jasmine.html'
