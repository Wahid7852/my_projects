### Admin
- Signup their account. Then Login (No approval Required).
- Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
- Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
- Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
- Can view/book/approve Appointment (approve those appointments which is requested by patient).

### Doctor
- Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can view their discharged(by admin) patient list.
- Can view their Appointments, booked by admin.
- Can delete their Appointment, when doctor attended their appointment.

### Patient
- Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
- Can view assigned doctor's details like ( specialization, mobile, address).
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments.(approval required by admin)
- Can view/download Invoice pdf (Only when that patient is discharged by admin).

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
 - To get these, follow the steps here
 To obtain the required client ID and client secret for Google OAuth 2.0, you'll need to create a project in the Google Cloud Console, set up the OAuth credentials, and generate these values. Here are the steps to get these credentials:
1. **Go to the Google Cloud Console**:
   Visit the Google Cloud Console at https://console.cloud.google.com/ and log in with your Google account.

2. **Create a New Project**:
   If you don't already have a project, create a new one by clicking the project drop-down and selecting "New Project." Give your project a name and select your organization if necessary.

3. **Enable the Gmail API**:
   In your project, navigate to the "APIs & Services" section and click on "Library" on the left sidebar. Search for "Gmail API" and click on it. Then, click the "Enable" button to enable the Gmail API for your project.

4. **Create OAuth 2.0 Credentials**:
   - In the Google Cloud Console, navigate to "APIs & Services" > "Credentials."
   - Click the "Create Credentials" button and select "OAuth client ID."
   - Choose "Web application" as the application type.

5. **Configure the OAuth Consent Screen**:
   - You might be prompted to configure the OAuth consent screen. Fill in the necessary information, such as the "App name" and "User support email." Save your changes.

6. **Set Authorized JavaScript Origins and Redirect URIs**:
   - In the OAuth 2.0 Client ID creation form, you need to set authorized JavaScript origins and redirect URIs.
   - For authorized JavaScript origins, add your development server's URL, e.g., `http://localhost:8000`.
   - For redirect URIs, add the callback URL for your Django application. It could be something like `http://localhost:8000/auth/callback/google/` if you are running a local development server.

7. **Get Your Client ID and Client Secret**:
   After completing the setup, Google will provide you with a client ID and client secret. These are the values you need to replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' in your Django settings.

8. **Generate an App Password for Gmail**:
   To securely use Gmail as your email provider, generate an "app password" for your Gmail account:
   - Go to your Google Account settings: https://myaccount.google.com/security.
   - Under "Security," find "App passwords" and generate a unique app password for your application. This is the password to replace 'your-app-password' in your Django settings.

Once you have these credentials, you can use them in your Django project as described in the previous code samples. Remember to keep these credentials secure, and do not share them publicly.