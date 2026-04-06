# Role-Based Financial Backend System (Django REST Framework)

## Overview

This is a backend system I built for managing personal finances. It's designed for people who want to track their income and expenses, but with different access levels for different users. I created it to learn about Django and APIs, and it turned out to be a good way to understand role-based permissions and data isolation.

The main idea is that users can log in and manage their own transactions, but depending on their role (admin, analyst, or viewer), they have different permissions. Admins can do everything, analysts can add new transactions but can't edit old ones, and viewers can only look at the data.

## Features

I implemented a custom user system where each user has a role that controls what they can do. For transactions, you can create, read, update, and delete entries with details like amount, type (income or expense), category, date, and description. There's validation to make sure amounts aren't zero or negative, which I added after testing and realizing it was needed.

Filtering is built in, so you can search transactions by type or category using query parameters. The dashboard gives you a quick summary of total income, expenses, and net balance, calculated from all your transactions.

Everything requires login, and users can only see their own data – no peeking at someone else's finances.

## Tech Stack

I used Django for the main framework because it's powerful and has good documentation. Django REST Framework made building the APIs straightforward. For the database, I went with SQLite since it's simple and doesn't need a separate server setup.

## Project Structure

The project is organized into a few Django apps:

- **main**: This is the core settings and URLs for the whole project.
- **users**: Handles the custom user model and authentication. I extended AbstractUser to add roles.
- **transactions**: All the transaction-related stuff – models, views, serializers, and permissions.
- **dashboard**: A simple app for the summary calculations.

Each app has its own models, views, and tests, which helped keep things organized as I built it.

## Setup Instructions

Getting this running locally was pretty straightforward once I figured out the virtual environment part. Here's what you need to do:

1. Clone the repository:
   ```
   git clone <repo-url>
   cd finance_backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (this will be an admin):
   ```
   python manage.py createsuperuser
   ```

6. Run the server:
   ```
   python manage.py runserver
   ```

The API will be available at http://localhost:8000/api/

## API Endpoints

The main endpoints are:

- **POST /api/auth/login/**: Login with username and password
- **GET /api/transactions/**: List all your transactions
- **POST /api/transactions/**: Create a new transaction
- **GET /api/transactions/{id}/**: Get a specific transaction
- **PUT /api/transactions/{id}/**: Update a transaction (if you have permission)
- **DELETE /api/transactions/{id}/**: Delete a transaction (if you're admin)
- **GET /api/dashboard/**: Get your financial summary

All transaction endpoints require authentication, and the dashboard aggregates your data.

## Role Behavior Explanation

The roles work like this:

- **Admin**: Can do everything – create, read, update, delete transactions. I made the superuser an admin.
- **Analyst**: Can read all transactions and create new ones, but can't edit or delete existing ones. Good for someone who analyzes data but shouldn't change history.
- **Viewer**: Can only read transactions. No creating, editing, or deleting.

For example, if you're a viewer, trying to POST to /api/transactions/ will give you a permission denied error. As an analyst, you can POST but not PUT or DELETE.

## Filtering Usage

To filter transactions, add query parameters to the GET request:

- `?type=income` – shows only income transactions
- `?category=salary` – shows only transactions in the salary category
- `?type=expense&category=food` – combines filters

I implemented this using Django's queryset filtering, which was easier than I expected once I got the syntax right.

## Dashboard Logic

The dashboard takes all your transactions and adds up the amounts based on type. Income gets added to total income, expenses to total expenses. Net balance is income minus expenses. It's simple aggregation using Django's Sum function on the queryset.

## Testing Process

I tested this mostly through the browser using Django REST Framework's built-in UI. I'd log in as different users, switch their roles in the admin panel, and try the endpoints. For validation, I'd try posting invalid data like negative amounts and check the error messages.

Permissions were trickier – I'd create test users with different roles and verify they could only do what they should. The DRF UI made it easy to test without writing full test scripts.

## Challenges Faced

This project had some frustrating moments. At first, I couldn't get authentication working – kept getting 401 errors even after logging in. Turned out I forgot to add the authentication classes to the viewsets.

Permissions were confusing too. I mixed up the logic for analysts vs viewers, and for a while analysts could delete things they shouldn't. Had to debug the permission classes carefully.

Filtering gave me trouble with the query params – I was trying to filter on fields that didn't exist, and it took me a while to realize I needed to use the right field names.

The dashboard aggregation was the hardest. I kept getting wrong totals because I wasn't filtering by user properly. Spent a whole evening debugging queryset logic.

## What I Learned

Building this taught me a lot about backend development. Authentication in Django is straightforward once you understand tokens vs sessions. Permissions showed me how to control access at the object level, not just views.

Serializers are powerful for validation and data transformation – I learned to use them for more than just API responses. API design principles like RESTful URLs and proper status codes became clearer.

Most importantly, I learned a debugging mindset. When something doesn't work, check the basics first – is the user authenticated? Does the permission allow it? Are the field names correct? Small mistakes can cause big issues.

## Conclusion

This was a solid project for learning Django and REST APIs. It covers the essentials of a real backend system with authentication, permissions, and data management. I made plenty of mistakes along the way, but that's how you learn. If you're new to Django like I was, this kind of hands-on building is the best way to understand it.
