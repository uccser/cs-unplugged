"""Tests deployments."""

import os
import re
from tests.BaseTest import BaseTest


class DeploymentTest(BaseTest):
    """Tests for deployments."""

    def test_dev_deploy_scripts_are_called(self):
        # Create list of script files
        FILES_TO_SKIP = (
            'decrypt-dev-secrets.sh',
            'load-dev-deploy-config-envs.sh',
        )

        filenames = set()
        path = "../infrastructure/dev-deploy/"
        for filename in sorted(os.listdir(path)):
            if filename.endswith('.sh') and filename not in FILES_TO_SKIP:
                filenames.add(filename)

        with open("../.travis.yml", "r") as f:
            deployment_contents = f.read()

        regex = re.compile(r'bash \./infrastructure/dev-deploy/(.*)$', flags=re.MULTILINE)
        results = re.findall(regex, deployment_contents)
        for called_filename in results:
            filenames.remove(called_filename)

        # Check if any files are missed
        error_text = ''
        for filename in filenames:
            error_text += f"\n'{filename}' is not called during dev deployment"

        if error_text:
            raise Exception(error_text)

    def test_prod_deploy_scripts_are_called(self):
        # Create list of script files
        FILES_TO_SKIP = (
            'decrypt-prod-secrets.sh',
            'load-prod-deploy-config-envs.sh',
        )

        filenames = set()
        path = "../infrastructure/prod-deploy/"
        for filename in sorted(os.listdir(path)):
            if filename.endswith('.sh') and filename not in FILES_TO_SKIP:
                filenames.add(filename)

        with open("../.travis.yml", "r") as f:
            deployment_contents = f.read()

        regex = re.compile(r'bash \./infrastructure/prod-deploy/(.*)$', flags=re.MULTILINE)
        results = re.findall(regex, deployment_contents)
        for called_filename in results:
            filenames.remove(called_filename)

        # Check if any files are missed
        error_text = ''
        for filename in filenames:
            error_text += f"\n'{filename}' is not called during prod deployment"

        if error_text:
            raise Exception(error_text)
