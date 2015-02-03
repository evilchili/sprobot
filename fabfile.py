from fabric.api import task
#from fabric.contrib.files import exists

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
    cotton.install()
