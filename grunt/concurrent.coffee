module.exports =

  # Run grunt tasks concurrently
  # https://github.com/sindresorhus/grunt-concurrent

  # Concurrently run two continuous tasks during development
  # - Static server at localhost:9000 to watch jasmine test spec runner
  # - Watch when files change and re-compile
  dev:
    options:
      logConcurrentOutput: true
    tasks: [
      'connect:jasmine'
      'watch'
    ]
