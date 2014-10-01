module.exports =

  # Run jasmine specs headlessly through PhantomJS
  # https://github.com/gruntjs/grunt-contrib-jasmine

  scripts:
    options:
      specs: '<%= paths.js %>/tests/build/*Spec.js'
      helpers: '<%= paths.js %>/tests/build/*Helper.js'
      vendor: [
        'http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
        '<%= paths.js %>/lib/*.js',
        ]
      outfile: 'tests/jasmine.html'
      keepRunner: true
    src: '<%= paths.js %>/build/*.js'
