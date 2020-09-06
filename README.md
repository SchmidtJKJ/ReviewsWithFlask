# ReviewsWithFlask
A simple movie review web application using Flask and SQLite <br>
This web app shows off Flask route skills, there is no verification or sanitiztion<br>
To test it out one need to have python3 installed and the flask module and clone the repository as it is (or have the same structure in the copy, for the template with the html files is crucial for flask render_template module)<br>
Create a new SQLite database (.db extension) file with the same name as in the setup.py (reviewData.db)<br>
Run the setup.py file which sets the stage for our app<br>
Run the Flask webserver locally:<br>
within the directory of the project assign the global FLASK_APP to the file to run (export FLASK_APP=app.py, which is the name of the main file in the project)<br>
You should be good to go and run flask with *flask run* command<br>
then go to http://127.0.0.1:5000/ which is the default localhost/port for flask<br>
