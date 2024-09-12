# USSD App
This USSD (Unstructured Supplementary Service Data) App is a Flask-based application designed to interact with Africa's Talking servers. It provides a simple interface for users to check their account information and phone number through a USSD menu system.

# Features

- Interactive USSD menu system
- Account information retrieval
- Phone number display
- Integration with Africa's Talking API

## Getting started

Create an Africa's Talking account or sign into your account. Head over to the Sandbox section and get your API key to make sure that your app can be authenticated by the servers.

### Initializing the app

1. Clone the repository (if you haven't already):
`git clone https://github.com/bryokn/USSD.git`
`cd USSD`

2. Create and activate a virtual environment:
`python3 -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`


<!-- While in the project directory,activate python virtual environment by -->

<!-- ```
source ./venv/bin/activate
``` -->

Download the python file to your project folder. 
Install flask making sure all the dependencies are fulfilled

```
pip install flask
```
OR (depending on how your Python installation works)
```
pip3 install flask
```

## Usage

Once done, run the file with

(Ensure your virtual environment is activated.)

```python3 app.py```

OR (depending on your python installation)

```python app.py```
The server should be up and running after that.

### Exposing the app to the internet

Download and install  [ngrok](https://ngrok.com/)

Head over to where you have installed ngrok and run: 

```./ngrok http 5000```

Ngrok will provide a public URL (e.g., https://abcd1234.ngrok.io) that you can use to access your app.

NOTE: The free version of ngrok will generate a new URL each time you restart it. For a consistent URL, consider upgrading to a paid plan.

This is the workflow for Unix based systems (Linux and MacOS) I'll add something for Windows later. Or check ngrok docs. 
That maps the localhost to a live link hosted by ngrok.

### Linking to Africa's Talking

1. Log in to your Africa's Talking account.
2. Navigate to the Sandbox section.
3. Create a new USSD channel:
    - Set the channel name
    - Enter the ngrok URL as the callback URL
    - Choose POST as the HTTP method

4. Once created, you'll receive a USSD code for testing.
5. Use the Africa's Talking simulator or a real device to test your USSD application.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Verify that the ngrok URL is correctly set as the callback URL in your Africa's Talking USSD channel.
3. Check the Flask server logs for any error messages.

## It should be running!! 

If you have any problems, raise and issue here and I will be sure to help out!


### Contributions are welcome!! HAPPY CODING!