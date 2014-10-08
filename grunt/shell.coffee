module.exports =

  # Run shell commands
  # https://github.com/sindresorhus/grunt-shell

  flake8:
    command: 'flake8 <%= name %>'

  django:
    command: 'coverage run $(which django-admin.py) test && coverage combine && coverage report && coverage html'

  tdaemon:
    command: 'python <%= paths.config %>/lib/tdaemon.py <%= name %> -t django-nose-coverage --ignore-dirs=static,templates'
