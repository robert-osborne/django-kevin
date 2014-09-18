module.exports =

  # Automatic desktop notifications for Grunt
  # https://github.com/dylang/grunt-notify

  lint:
    options:
      message: "Lint is complete"

  build:
    options:
      message: "Build is complete"

  default:
    options:
      message: "Compiling is complete, now watching..."
