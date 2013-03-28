Welcome to Greendizer Boilerplate

#Contents
This is a Django starter project using OAuth for authentication.
This boilerplate enables you to start your first django-powered Greendizer application.
The provided code enables you (as a buyer) to display the user settings along with all the related invoices.

Greendizer is a new kind of invoicing system.
It turns the invoices sent with it to an extremely rich source of data for business intelligence and process automation.
Check out [the Greendizer website](https://www.greendizer.com/) for more information.

#Requirements
In order to use this boilerplate the following is needed:
* [Greendizer Python Library](https://github.com/Greendizer/Greendizer-Python-Library) which includes OAuth
* [PyXMLi](https://github.com/Greendizer/PyXMLi)

#Account Setup
To setup your Greendizer account go to the Account Settings on greendizer.com.
Then create a new application: Developer > Register Application
* Name: you application's name
* Website: the URL of you main application page
* Description: a brief description of your application
* Redirect URL: the URL of you main application page or part of the URL
* Application type: select "Client"

Then in Developer > My Applications slect your newly created app
* client id: your user ID in greendizer.com
* client secret: a secret key used for OAuth 2.0 authentication


#About authentication
The OAuth flow used is the "Authorization Code Grant" for client/server applications
In order to perform authentication, please modify the credentials by the ones provided to you upon registration of your application; namely:
* client_id
* client_secret
* email
