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
    ]

  stylesheets:
    files: ['<%= paths.css %>/src/*.scss']
    tasks: [
      'newer:scsslint'
      'newer:sass'
      'newer:autoprefixer'
      'replace:stylesheets'
    ]

  images:
    files: ['<%= paths.img %>/src/**/*.{png,jpg,gif,svg}']
    tasks: [
      'newer:imagemin'
    ]
