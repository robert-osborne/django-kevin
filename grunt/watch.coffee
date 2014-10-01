module.exports =

  # Run tasks whenever watched files change
  # https://github.com/gruntjs/grunt-contrib-watch

  options:
    spawn: false

  config:
    options:
      reload: true
    files: [
      'Gruntfile.coffee'
      'grunt/*.{coffee,yaml}'
    ]

  livereload:
    options:
      livereload: true
    files: [
      '<%= paths.templates %>/**/*.html'
      '<%= paths.css %>/**/*.{scss,css}'
      '<%= paths.js %>/**/*.{coffee,js}'
    ]

  stylesheets:
    files: ['<%= paths.css %>/scss/*.scss']
    tasks: [
      'newer:scsslint'
      'newer:sass'
      'newer:autoprefixer'
      'replace:stylesheets'
    ]

  scripts:
    files: [
      '<%= paths.js %>/coffee/*.coffee'
      '<%= paths.js %>/tests/coffee/*.coffee'
      '<%= paths.js %>/tests/lib/*.js'
    ]
    tasks: [
      'newer:coffeelint'
      'newer:coffee'
      'newer:copy:jasmine'
      'jasmine'
    ]

  images:
    files: ['<%= paths.img %>/**/*.{png,jpg,gif,svg}']
    tasks: ['newer:imagemin']
