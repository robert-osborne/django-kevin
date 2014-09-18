module.exports =

  # Lint your SCSS
  # https://github.com/ahmednuaman/grunt-scss-lint
  options:
    colorizeOutput: true
    config: 'grunt/config/scsslint.yaml'
  stylesheets: ['<%= paths.css %>/src/*.scss']
