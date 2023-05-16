# Sync-Net


This project demonstrates the integration of various third-party APIs with Django to add different functionalities to your application. It showcases the usage of popular APIs to enhance your application's features and provide additional services to your users.

## Features

This project demonstrates the integration of the following third-party APIs:

1. IP Address API: Retrieves IP address based on location if the request is not from a certain continent you're restricted from seeing contents in the next page.
2. Payment Gateway API: Enables secure online payments for your application with PayPal.
3. Social Media API: Integrates social media authentication features.
4. COVID19 API: Retrieves the highest deathrate at any point with covid19 data.


## Technologies Used

- Python and Django framework for the backend server.
- HTML for the frontend user interface.
- [IP Address API]: (http://api.ipstack.com/) for IP address.
- [Payment Gateway API]: (https://www.paypal.com) for online payments.
- [Social Media API]: (https://facebook.com/) for social media integration.
- [COVID19 API]: (https://coronavirus.m.pipedream.net) for COVID data

## Installation

 1. Clone the repository:
  
 2. Set up a virtual environment: Pipenv shell
 
 3. Install dependencies: pip install -r requirements.txt
 
 4. Set up the environment variables: 
- Create a .env file based on the .env.example file provided.
- Fill in the required API credentials and configuration values.

5. Apply database migrations: python manage.py migrate

6. Start the development server: python manage.py runserver

## Usage

Explore the different functionalities available through the integrated APIs.
- Test the IP address API by entering an IP address and if you do not live in a certain continent you're restricted from seeing contents in the next page.
- Perform test payments using the integrated payment gateway API.
- Authenticate on social media using the provided social media integration.
- Retrieve user location information using the geolocation API.



## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, please submit a pull request.



