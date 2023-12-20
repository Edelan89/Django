# Django E-commerce Website

This is a full-fledged e-commerce website built using Django, a Python web framework. It provides features for managing products, user authentication, cart functionality, and order processing.

## Installation

1. Clone this repository to your local machine:

git clone <repository_url>


2. Navigate to the project directory:

cd django-ecommerce

3. Install dependencies:

pip install -r requirements.txt


4. Run migrations to set up the database:

python manage.py makemigrations
python manage.py migrate



5. Create a superuser for admin access:

python manage.py createsuperuser


6. Start the Django development server:

python manage.py runserver


The website will be accessible at `http://localhost:8000`.

## Features

### Product Management

- **Add/Edit/Delete Products:** Admins can add, edit, and delete products through the Django admin interface.

### User Authentication

- **Registration/Login:** Users can register an account and log in to access features like viewing orders and managing their cart.

### Cart Functionality

- **Add/Remove Items:** Users can add items to their cart and remove them as needed.
- **Adjust Quantity:** Users can adjust the quantity of items in their cart before checkout.

### Order Processing

- **Checkout:** Users can proceed to checkout, review their order, and complete the purchase.
- **Order History:** Users can view their order history and check the status of previous orders.

## Technologies Used

- **Django:** Backend web framework for building the website.
- **SQLite/PostgreSQL:** Database management system for storing product and user data.
- **HTML/CSS/JavaScript:** Frontend technologies for the website's user interface.
- **Bootstrap:** Frontend framework for responsive and mobile-first design.

## Contributing

Contributions are welcome! If you find any bugs or want to contribute new features, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE), allowing for both personal and commercial use.
This README file provides an overview of how to set up, run, and use your Django-
