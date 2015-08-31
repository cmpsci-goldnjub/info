from fabric.api import local, put, run, sudo

NGINX_DIR = "/usr/share/nginx/www"

def upload():
    # Build the site
    local('jekyll build')

    # Upload it to a temporary place
    temp_dir = run('mktemp -d')
    put('_site/*', temp_dir)

    # Overwrite the nginx directory with the new files
    sudo("rsync --delete -rvc {}/ {}/".format(temp_dir, NGINX_DIR))

    # Cleanup
    run('rm -rf {}'.format(temp_dir))
