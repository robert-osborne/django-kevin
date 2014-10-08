module.exports =

  # Run shell commands
  # https://github.com/sindresorhus/grunt-shell

  django:
    command: 'echo "Running flake8..." && flake8 <%= name %>; echo && coverage run $(which django-admin.py) test && coverage combine && coverage report && coverage html'

  tdaemon:
    command: 'python <%= paths.config %>/lib/tdaemon.py <%= name %> -t django-nose-coverage --ignore-dirs=static,templates'
