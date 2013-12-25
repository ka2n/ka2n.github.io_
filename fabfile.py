from fabric.api import env, local
from fabric.contrib.console import confirm
from fabric.contrib.console import prompt
import os
import datetime

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.template_path = './template.rst'
DEPLOY_PATH = env.deploy_path
TEMPLTE_PATH = env.template_path


def new(filename=None):
    """Create new post"""
    now = datetime.datetime.now().replace(microsecond=0, tzinfo=None)
    payload = {
        "date": "{0:%Y-%m-%d}".format(now),
        "title": "{0:%Y-%m-%d}".format(now),
        "author": "ka2n"
    }
    if not filename:
        filename = "{0:%Y-%m-%d}.rst".format(now)
    new_file_path = os.path.join('./content', filename)
    if os.path.exists(new_file_path):
        if confirm("File already exists, edit?"):
            local('vim {0}'.format(new_file_path))
            return
        else:
            filename = prompt("Please input new filename", default=filename)
            return new(filename)

    template = open(TEMPLTE_PATH).read()
    new_file_body = template.format(**payload)
    local('echo "{0}" | vim - -c "file {1} |filetype detect"'.format(
        new_file_body, new_file_path))


def clean():
    """remove the generated files"""
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def build():
    """generate the web site"""
    local('pelican -s pelicanconf.py')


def rebuild():
    """clean & build"""
    clean()
    build()


def preview():
    """serve site at http://localhost:8000'"""
    local('pelican -r -s pelicanconf.py')
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))


def github():
    """upload the web site via gh-pages"""
    rebuild()
    if os.path.isdir(DEPLOY_PATH):
        local('ghp-import -p -b master {deploy_path}'.format(**env))
