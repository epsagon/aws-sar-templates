"""
Deploy all our serverless application repository templates
"""
import subprocess
import os.path


APPLICATIONS_BUCKET_NAME = 'epsagon-sar-templates'
TEMPLATES_FOLDER = 'templates'
APPLICATIONS = {
    'nodejs_hello_world': 'XXX'
}

def pack_application(application_name, application_arn):
    """ deploys a single application """
    app_dir = os.path.join('.', TEMPLATES_FOLDER, application_name)
    subprocess.check_call(['npm', 'install'], cwd=app_dir)
    subprocess.check_call([
        'sam',
        'package',
        '--template-file',
        os.path.join(app_dir, 'template.yaml'),
        '--s3-bucket',
        APPLICATIONS_BUCKET_NAME,
        '--output-template-file',
        os.path.join(app_dir, 'packed.yaml'),
    ])


def main():
    """ main """
    for application_name, application_arn in APPLICATIONS.items():
        deploy_application(application_name, application_arn)


if __name__ == '__main__':
    main()
