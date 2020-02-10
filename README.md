# Text Summarization:
  This is a POC project developed for showing text summarization on wikipedia web link in 10 lines. 
  
## Skill used: 

1. NPL to build model
2. Python as a programming medium
3. Flask as web framework for making application
4. Heroku to deploy the web application on the internet.

### Algorithm used: 

1. TF-IDF 
2. Bag of Word 

### Working model:

https://rajeevranjan-summarizetext.herokuapp.com/

### How to use the project:

1. Download the repository.
2. open anaconda command prompt and go to the stored folder and run python app.py
3. After running app.py, the flask framework will get created on to your system locally and it will produce you a url by which you can access the application home page.
4. For deployment of the app on the web i.e., Heroku you need to connect you git by heroku. You can create new app there and store this repo there. All the further steps will be there which is very easy to tackle in order to deploy the model on web. This is user friendlt framework so anyone can easily follow each steps.

### About the files:

1. In the create.py file I created two files for future uses one data.csv and other a numpy matrix.
2. The application is run from the main.py file.
3. In the template folder, there are home.html page from which you will ask your query and the result will be directed on recommend.html page.
4. You need to have procfile where we initialize the app.
5. You need to import all the libraries which are necessary for running the application that needs to be installed in heroku. All the necessary libraries are kept in requirement.txt file.
