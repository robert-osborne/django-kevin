module.exports =

  # General purpose text replacement for grunt
  # https://github.com/yoniholmes/grunt-text-replace

  stylesheets:
    src: ['<%= paths.css %>/build/*.css.map']
    overwrite: true
    replacements: [
      from: '<%= name %>/static'
      to: '/static'
    ]

  specRunner:
    src: ['<%= paths.tests %>/jasmine.html']
    overwrite: true
    replacements: [
      {
        from: '.grunt'
        to: '../.grunt'
      }
      {
        from: '<%= name %>'
        to: '../<%= name %>'
      }
      {
        from: '</body>'
        to: '
            <h1 style="font-family: Helvetica Neue; font-weight: 300;">
              <a href="/tests/coverage" style="color: #007069;">
                Click here for JS Test Coverage
              </a>
            </h1></body>
            '
      }
    ]
