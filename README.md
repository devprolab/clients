# 🐳 WEBAPPSTORE – CI/CD Pipeline Exercise  

This project is a **Python Flask web application** that retrieves data from a `clients` database table and packages it as a **Docker container**.  

Your task is to **write a Dockerfile from scratch**, build the image, and run the container connected to a database.  

---

## 🎯 Learning Objectives  

By the end of this exercise, you will be able to:  
- Create a functional **Dockerfile** for a Python Flask app  
- Install dependencies inside an image  
- Configure environment variables for database connectivity  
- Build and run a container successfully  

---

## ✅ Prerequisites  

- Docker installed and running  
- A MariaDB container up and running  
  - Database created with a `clients` table  
- Basic Dockerfile knowledge  

---

## 📝 Build Docker image 

1. Create a new project directory:  
   ```bash
   mkdir project && cd project
2. Create Dockerfile
   ```bash 
   touch Dockerfile
3. clone this repository:
   ```bash
   git clone https://github.com/devprolab/clients.git

4. check the structure
   ```bash
   tree .
   ├── clients
   │   ├── clients.html
   │   ├── index.html
   │   ├── README.md
   │   ├── requirements.txt
   │   └── webapp.py
   └── Dockerfile

   
5. Write the Dockerfile
   - Using the image **python:3.9-slim**
   - Update and install pip  using this two commands :  **pip install --upgrade pip**  and **pip install flask mysql-connector-python**
   - The Working directory has to be **/app**
   - Create a non-root user to run the application in the future containers named **webappuser**
   - The image has to expose the port **5000** in **tcp** 
   - Copy all the content of **client** directory into **/app**
   - The application uses by default the folowing environment variables
     
     --------------------------------------------------------------------------------------------
     |Requirement | Description               | default value      |Required in Dockerfile      |
     |------------|---------------------------|--------------------|-----------------------------
     | FLAS_APP   | Path of the application   | /app               | yes                        |
     | DBUSER     | username used for DB      | admin              | no                         |
     | DBPASSWORD | password used for DB      | admin              | no                         |
     | DBHOST     | IP add or FQDN of DB host | inspect container  | no                         |
     | DB         | Is the name of database   | webstore           | no                         |
     --------------------------------------------------------------------------------------------
     
   - use the entrypoint as entry for the image **ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "-p", "5000"]**
  
6. build the image named **webapplication:latest**
   
8. once the image has been build test it using the following command:
   ```bash
   docker run --name webapp -p 80:5000 \
    -e DBUSER=root \
    -e DBPASSWORD=root \
    -e DBHOST=172.16.0.2 \
    -e DB=clientdb \
    webapp:latest
   
9. using your web browser try to access to your application using **http://localhost:80**  or **http://<dock-host-ip>:80** 
