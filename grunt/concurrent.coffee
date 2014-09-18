module.exports =

  # Run grunt tasks concurrently
  # https://github.com/sindresorhus/grunt-concurrent

  lint: [
    'lint_stylesheets'
    'lint_scripts'
  ]

  build: [
    'build_stylesheets'
    'build_scripts'
    'build_images'
  ]
