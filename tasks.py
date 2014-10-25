from invoke import task, run

from os.path import basename, dirname, realpath

# Create scripted tasks to run in command-line here
# http://docs.pyinvoke.org/en/latest/


@task
def clean():
    """Clean up static, compiled, test, and log files"""
    project_name = get_project_name()

    print("Deleting *.pyc files...")
    run('find . -name *.pyc -delete')

    print("Deleting collected static files...")
    run('rm -rf %s/public' % project_name)

    print("Deleting compiled stylesheets...")
    run('rm -rf %s/static/css/build' % project_name)

    print("Deleting compiled scripts...")
    run('rm -rf %s/static/js/build' % project_name)
    run('rm -rf %s/static/js/tests/build' % project_name)

    print('Deleting compressed images...')
    run('rm -rf %s/static/img/compressed' % project_name)

    print('Deleting test files...')
    run('rm -rf tests/*')
    run('rm -rf .coverage')
    run('rm -rf _SpecRunner.html')

    print('Deleting log files...')
    run('rm -rf logs/*')


def get_project_name():
    return basename(dirname(realpath(__file__)))
