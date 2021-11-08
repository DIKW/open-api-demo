# open-api-demo
open api demo to be used in workshop on micro service architectures

We make a template to build an api based on open api stanndards to craft a REST api efficiently.

## Refence documentation

Overview of available design , test and development tools are [here](https://openapi.tools/#gui-editors)

Minimum viable blog post is [here](https://anthony-f-tannous.medium.com/working-with-openapi-swagger-tools-python-1c0c22f7a629)

Crafting effective microservices in python [connexion](https://engineering.zalando.com/posts/2016/12/crafting-effective-microservices-in-python.html) by Zalando seems like a good package for this.

## Requirements

We need to add swagger-ui-bundle to requirements.txt to make the swagger-ui work

## Howto

Generate server python flask

Extract folder

Open visual studio

Goto extracted folder

Create virtual environment with 

    python3 -m venv env

Source this environemnt

    source /home/hugo/git/open-api-demo/server/python-flask-server-generated-v03/env/bin/activate
    
Add pyjwt to the requirements.txt 

    pyjwt == 2.3.0

Install requirements

    pip3 install -r requirements.txt
    
Add the requirements for the swagger-ui

    pip3 install connexion[swagger-ui]
    
Run flask app, goto folder and run 

    python3 -m swagger_server
    
    

