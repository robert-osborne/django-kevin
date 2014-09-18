module.exports =

  # Run grunt tasks concurrently
  # https://github.com/sindresorhus/grunt-concurrent
  lint: [
    'lint_stylesheets'
  ]
  build: [
    'build_stylesheets'
    'compress_images'
  ]
  test: []
