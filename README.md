# Project-4 Build an Item Catalog
An application that provides a list of items within a variety of categories. It also includes the registration and the authentication module. Registered users can also able to delete , edit , and post their own items.


# How to Run
Google plus Registration
1. Go to <a href="https://console.developers.google.com/project">Google Developer API</a> and login with your credentials.
2. Create a new project
3. Navigate to API & credentials in the dropdown menu and go to Credentials and Create a new OAuth client ID 
4. Now select web application and give the product name
5. Add `http://localhost:5000`  to the authorized JavaScript options and add  `http://localhost:5000` also `http://localhost:5000/gconnect` to the Authorized redirect URL
6. Copy and paste the client-id into the project file `signin.html` under the templates folder and replace `data-clientid` with your client id
7. Select and download JSON file and rename to client_secrets.json 
8. Replace the client_secrets.json actual file with your downloaded JSON file.


## Running the App

* <h4>Download and install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></h4>
* <h4>Download the project zip file and extract it </h4>
* <h4>Copy the extracted folder to the downloaded  vagrant directory </h4>
* <h4>Open a terminal inside the vagrant directory and type `vagrant up`</h4>
* <h4>Once the download and installation completes type `vagrant ssh` in terminal</h4>
* <h4>Load the database with values. Run `python lotsofmenu.py` in the terminal</h4>
* Type `python project.py` in the terminal
* Now navigate to  `http://localhost:5000` in the browser

### References and Source Code

- Authorization and Authentication: [Udacity](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/348776022975461/lessons/3960758610/concepts/39804189030923)
- Third party Sign In (Google) : [Udacity](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/348776022975461/lessons/3967218625/concepts/41458490190923)