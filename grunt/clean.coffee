module.exports =

  # Clear files and folders
  # https://github.com/gruntjs/grunt-contrib-clean

  stylesheets: ['<%= paths.css %>/build']

  scripts: [
    '<%= paths.js %>/build'
    '<%= paths.js %>/tests/build'
  ]

  images: ['<%= paths.img %>/compressed']

  logs: [
    'logs/*.log'
    'logs/*.log.*'
  ]
