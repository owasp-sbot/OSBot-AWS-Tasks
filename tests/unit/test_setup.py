import os
import osbot_aws_tasks
from unittest                       import TestCase
from unittest.mock                  import patch
from osbot_utils.utils.Files        import parent_folder

from osbot_aws_tasks.utils.Version import Version

EXPECTED_PACKAGES = ['osbot_aws_tasks']

class test_setup(TestCase):


    @patch('setuptools.setup')                                                      # this prevents the sys.exit() from being called
    def test_setup(self, mock_setup):
        parent_path = parent_folder(osbot_aws_tasks.path)                            # get the root of the repo
        os.chdir(parent_path)                                                       # change current directory to root so that the README.me file can be resolved
        import setup                                                                # do the import
        args, kwargs = mock_setup.call_args                                         # capture the params used on the setup call

        if kwargs.get('name') == 'osbot_aws_tasks':                                  # make sure we imported the correct setup (submodules will imapct this)
            assert kwargs.get('description'     ) == 'OWASP Security Bot - AWS Tasks'
            assert kwargs.get('long_description') == setup.long_description
            assert kwargs.get('version'         ) == Version().value()
            assert kwargs.get('packages'        ) == EXPECTED_PACKAGES