from setuptools import setup, find_packages

with open("README.md", "r") as file_readme:
    long_description = file_readme.read().strip()

with open("osbot_aws_tasks/version", "r") as file_version:
    version = file_version.read().strip()

setup(
    version                       = version                                         ,
    name                          = "osbot_aws_tasks"                               ,
    author                        = "Dinis Cruz"                                    ,
    author_email                  = "dinis.cruz@owasp.org"                          ,
    description                   = "OWASP Security Bot - AWS Tasks"                ,
    long_description              = long_description                                ,
    long_description_content_type = " text/markdown"                                ,
    url                           = "https://github.com/owasp-sbot/OSBot-AWS-Tasks" ,
    packages                      = find_packages()                                 ,
    classifiers                   = [ "Programming Language :: Python :: 3"         ,
                                      "License :: OSI Approved :: MIT License"      ,
                                      "Operating System :: OS Independent"          ])
