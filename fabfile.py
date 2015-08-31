from fabric.api import local, put, sudo

def upload():
    local('jekyll build')
    put('_site', '/tmp')
    sudo("cp -R /tmp/_site/* /usr/share/nginx/www/")
