module.exports =

  # Lint your SCSS
  # https://github.com/ahmednuaman/grunt-scss-lint
  options:
    colorizeOutput: true
    config: 'grunt/scss-lint.yaml'
  stylesheets: ['<%= paths.css %>/src/*.scss']
