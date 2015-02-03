from fabric.api import task, put, env
#from fabric.contrib.files import exists
import os

# import the fabric tasks and templates from cotton
import cotton.fabfile as cotton

# load application-specific settings from this module
cotton.set_fabric_env('cotton_settings')

# application-specific fabric tasks go here.


@task
def ship():
    """
    Deploy the current branch to production
    """
    cotton.git_push()
    cotton.update_python_requirements()

    # Deploy the secrets module to the remote project root
    spath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'secrets'))
    put(spath, env.project_root)

    cotton.upload_template_and_reload('cron')
