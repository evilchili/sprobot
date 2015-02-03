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

    # make sure the virtual env was in place. If it had to
    # be created or updated, we can skip the call to the
    # update_python_requirements() task, since it will be
    # carried out automatically by install().
    if not cotton.install():
        cotton.update_python_requirements()
    cotton.git_push()
