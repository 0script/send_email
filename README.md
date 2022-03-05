# send_email

## Table of content

- [About the project](#about-the-project)<!-- - [Technologies](#technologies) -->
- [Setup](#setup)

## About the project

This python3 script allow you to send email from the terminal using a json file as configuration file and a .txt file as the subject for the mail.

## Setup

Install required packages

```shell
cd send_email
$ pip install -r requirements.txt
```

Create the config.json file with your credentials . This configuration file is for gmail
Change port and server for others smtp providers.

```json
{
  "email": "xxx@gmail.com",
  "password": "xxxxxx",
  "port": 587,
  "server": "smtp.gmail.com"
}

Remove reading write to the config file for other user to protect your credential
```shell
$chmod 600 config.json
```

```

Create a text file with the subject:

```shell
echo "The message to be send" > subject.txt
```

Send the mail:

```shell
python3 sending.py receiver@gmail.com -c config.json -s subject.txt -a 'Attachement Of The Mail : SENDED USING PYTHON3'
```
