module.exports = (grunt) ->

  # Initial variable configuration
  pkg = grunt.file.readJSON 'package.json'
  name = pkg.name.toLowerCase()
  paths =
    templates: name + "/templates"
    css: name + "/static/css"
    fonts: name + "/static/fonts"
    img: name + "/static/img"
    js: name + "/static/js"

  # Loads grunt config automatically via broken up tasks
  # https://github.com/firstandthird/load-grunt-config
  require('load-grunt-config') grunt,
    data:
      name: name
      paths: paths

  # Times how long tasks take
  # https://github.com/sindresorhus/time-grunt
  require('time-grunt') grunt
