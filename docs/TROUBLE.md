# General Feeling:
I'm handing in the project with mixed feelings. On one hand, I learned a lot and basically learned Docker and Travis from scratch and 
delivered the necessary result. On the other hand, I feel that it isn't good enough but it's the best I could achieve in the given time.
Due to two mistakes in the challenge instructions I received 12 additional hours. 

I feel that although we perform tests and build in my current job, there's a "missing link" when it comes to integrating with virtual 
server. Not something too hard to understand and learn but defiantly something that requires learning.

#Steps along the way:
## PythonApp:
Was pretty simple to build, didn't require anything special. Yet, due to lack of time, the app doesn't take care of possible 
exceptions and failures and doesn't include any validations.
## DynamoDB:
Still need to improve in using nosql DB's. I have to admit that I wasn’t familiar with the DB and the service and general and had to watch some 
tutorials to figure out how the DB is built and how to extract the data using Python lib, boto3. Had some struggles in the beginning that cost me 
many hours of frustration when I received a wrong key and didn't get the default region. 
## Docker:
My first "hands on" with Docker. I was familiar with the tool but never used it before. Same here, I had to watch tons of tutorials to get satisfying results
and I really hope that all of the requirements were achieved. Not having "Ubuntu" on my machine at home made it quite difficult and I had to
use Windows 10 "bash-on-Ubuntu". I believe things would have been much easier otherwise. I spent a lot of time figuring out how to publish the 
data received from the application to the local server...
## TravisCI:
First encounter with the tool, kind of similar to Jenkins only slightly different. At work we use Jenkins on local machines so debugging is so 
much easier. Again, watched some tutorials to understand the integration with Docker. Same here, not having "Ubuntu" was a bummer and as a result
integrating Travis with Docker required a lot of trail and error, hence the times I had to commit and run.

I believe that learning each part of the puzzle isn't easy but absolutely doable and not having the deadline for handing out the project 
will make the learning process easier and much more fun.

Avner
