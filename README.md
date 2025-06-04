Teacher Portal – Student Management System


This Django project provides a simple yet extensible Teacher Portal where teachers can log in, view students, edit marks, and manage student records. The architecture is scalable, secure, and easy to maintain.



->How to Run Locally

1.Clone the repository
git clone https://github.com/your-username/teacher-portal.git
cd teacher-portal

2.Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies
pip install django

4.Apply migrations
python manage.py makemigrations
python manage.py migrate

5.Create superuser (optional)
python manage.py createsuperuser

6.Run the server
python manage.py runserver

7.Access the app at:
http://127.0.0.1:8000


->Features Implemented

🔐 Teacher Login Authentication

🏠 Teacher Portal Home Dashboard

📋 Student Listing with Name, Subject, and Marks

✏️ Inline Student Edit and Update

🗑️ Student Delete with Confirmation

➕ Add New Student with Duplicate Check

👁️ Password Toggle (Show/Hide)

🔐 Forgot Password Flow via Email Reset

✅ CSRF Protection, Input Validation


->Additional Improvements

🎨 Clean Bootstrap 5 UI

🔍 AJAX support for inline updates (future-ready)

🧪 Django Unit Tests for views and forms

📦 Modular Code (views, forms, templates organized)


->Security Best Practices Followed

*CSRF tokens used in all forms

*Input validation on both frontend & backend

*Email reset secured with token-based URL

*App password used for SMTP to avoid plain text passwords


->Testing Strategy

*Unit Tests: form validation, view logic

*Integration Tests: Login flow, CRUD functionality

*Manual End-to-End: full user journeys


->Scalable & Maintainable Architecture

*Models are easily extendable

*Views follow Class-Based View (CBV) architecture

*Forms decoupled for reusability

*All templates extend a base layout
