# WEBAPPSTORE CI/CD Pipeline

A Python Flask web application that retrieves data from a clients database table and packages it as a Docker container.

## Key Features

    Docker containerization

    Database connectivity (supports multiple database backends)

    Configurable via environment variables

    Python 3 with Flask framework

## Prerequisites

    Docker installed

    Python 3.x

    Database with a clients table

## Recommandation 
optimaziation reason use the image python:3.9-slim 
for security reason create user **webapp** than can be used as default user in the container 


## Installation
Building the Docker Image

    Upgrade pip (required before package installation):
      **pip install --upgrade pip**

    Install required Python packages:
      **pip3 install flask  mysql-connector-python** 

## Configuration

The application requires these environment variables:       
**these variable can be added to the Dockerfile or injected when running the container**
**For better flexibility inject them when running a container expet for  FLAS_APP**
 
 Requirement | Description               | default value      |
|------------|---------------------------|--------------------|
| FLAS_APP   | Path of the application   | /app               |
| DBUSER     | username used for DB      | admin              |
| DBPASSWORD | password used for DB      | admin              |
| DBHOST     | IP add or FQDN of DB host | inspect container  |
| DB         | Is the name of database   | webstore           | 

## Building the image 
** docker build -t name:tag .** 
### example 
** docker build -t webapp:latest .




