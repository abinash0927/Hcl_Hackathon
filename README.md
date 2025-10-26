🏦 Smart Banking — Web Application 📖 Overview

Smart banking is a full-featured banking & managing transaction application built using Django & Rest-framework as back-end. It allows to create users & bank account with preferred account type and user can make transactions,apply for loan & view statements.The admins are able to manage requested loans and transactions. The goal of the project is to create a user-friendly and seamless Banking app.

🚀 Features

🧾 User authentication (signup, login, logout)
  > Create customer table and fields [ 'name,'contact','email','password','phone','address','kyc(pan , aaddhar etc.)','kyc_verified_status]. 
  > Submitted Kyc details will be viewed and verified by admin.
  > if failure: notify customer failure of kyc uploads like image not clear or invalid kyc.
  > After Validating details if success: User will be redirected for account creation.
    Flow:
      User Creation ➜ Kyc Verification ➜ Notifying Customer ➜ Account Creation

  > Testing and validating user credentials like password length,unique email id.
  > Testing Api end-points with swagger-ui 


🧠 Tech Stack

Backend: Django,Rest_framework,Swagger,Python 3.11.8
Database: MySQL Version Control: Git & GitHub

⚙️ Installation & Setup 
1️⃣ Create and Activate Virtual Environment python -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows

2️⃣ Clone the Repository git clone [Hcl_Hackathon](https://github.com/abinash0927/Hcl_Hackathon.git) cd Hcl_Hackathon

3️⃣ Install Dependencies pip install -r requirements.txt

4️⃣ Apply Migrations python manage.py migrate

5️⃣ Run the Server python manage.py runserver

6️⃣ Configure settings.py Change database for Mysql with your details

Now open your browser and go to http://127.0.0.1:8000/customers/
