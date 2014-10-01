module.exports =

  # Copy files and folders
  # https://github.com/gruntjs/grunt-contrib-copy

  jasmine:
    expand: true
    flatten: true
    src: '<%= paths.js %>/tests/lib/*.js'
    dest: '<%= paths.js %>/tests/build/'
