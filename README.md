# Item Catalog Project
#### Full Stack Web Developer Nano-Degree

### Overview
> This project is a web application that provides
  a list of items within a variety of categories and integrate third party
  user registration and authentication (Google Sign-in). Authenticated users have the
  ability to add, edit, and delete their own items.

### Requirements
* [Python2](https://www.python.org/)
* [Flask](https://pypi.org/project/Flask/)
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
* [Vagrant](https://www.vagrantup.com/downloads.html) 
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [FSND virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

### Setup
##### 1. Start with Software Installation
Once you get the above software installed, follow the following instructions:
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
```

\- For this project, all the work will be on your Linux machine, so always make sure you logged in by using the following commands:
`vagrant up`, then `vagrant ssh`, then `cd /vagrant`.
Note: Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not.

##### 2. Download and Move the files
  - Move the project files to the vagrant folder


#### How to run:
  1- Setup application database 
  ```
   $ python database_setup.py
  ```
  2- Insert fake data 
  
  ```
    $ python items.py
  ```
    
  3- Run application using
  ```
    $ python application.py
  ```
  4- Access the application locally using 
  ```
    http://localhost:8000
  ```