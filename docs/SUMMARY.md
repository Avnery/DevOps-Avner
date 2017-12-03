# General:
This project allows you to build, test and deploy the DynamodbExtractor, which connect to the comapny's DB and extracrt the necessary secret code.
The secret code will allow us to extract important information from the DB and to minimize the potential damaged inflicted by the leak.

# Building Blocks:
## Python app
The DynamodbExtractor is the main Python app that connects to the DynamoDB and extract the secret code. 
Using the "boto3" python library, the application queries the DB using the table name and the relevant key. 
Once the data has been extracted, it is published over HTTP to local server. After launching the server, it will be 
listening for requests on port 5000 with path "secret". 

Except for publishing the qurey result, the app also publishes the link to the relevant Docker container and the 
link to this GitHub repository. This time the data is published over port 5000 with path "Health".

## Docker
Now, once the application is ready to undergo a build. The Docker performs the build using the .Dockerfile as a configuration file. 
The main configuration fields in this Docker file are the parent image, in this case, Python, the working directory, the relevant packages that need 
to be installed prior to running the app and in case we want to use a certain port, just like in our case, we use the EXPOSE option.
Once container is ready, the Docker runs the app.

As the app is running, both URL mentioned before are up and running on the local server.

## TravisCI
Once the container is ready, we use TravisCI to automate the process. The TravisCI uses the .Travis.yml that has the required configuration
fot this project. First it reads the relevant code language, Python and then it runs the Docker service. Once the Docker is up, it performs 
the build and runs the container. 

Once the container is running, the TracisCI performs simple testing using curl to make sure that the data was published properly to the local
host server. Once the test are passed, the TravisCI goes on pushing the new image to the Docker Hub repository.
