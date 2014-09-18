module.exports =

  # Minify PNG, JPEG, GIF, and SVG images
  # https://github.com/gruntjs/grunt-contrib-imagemin

  images:
    files: [
      expand: true
      cwd: '<%= paths.img %>/'
      src: ['**/*.{png,jpg,gif,svg}']
      dest: '<%= paths.img %>/compressed'
    ]
