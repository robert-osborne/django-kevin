module.exports =

  # Start a static web server
  # https://github.com/gruntjs/grunt-contrib-connect

  jasmine:
    options:
      port: 9000
      hostname: 'localhost'
      livereload: true
      keepalive: true
      open:
        target: 'http://localhost:9000/tests/jasmine.html'
