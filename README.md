#send_email

##Table of content
* [About the project](#about-the-project)
* [Technologies](#technologies)
* [Setup](#setup)

##About the project

    This python3 script allow you to send email from the terminal using a ...json file as configuration file and a .txt file as the subject for the mail.

##Setup
    
    * Install required paskage
    ```
    $cd send_email
    $pip install -r requirements.txt
    ```
    
    
    * create the .json file with your credential (example if .json file)
    ```→ cat config.json 
        {
          "email":"xxx@gmail.com",
          "password":"xxxxxx",
          "port":587,
          "server":"smtp.gmail.com"
        }
    ```

    * Create a text file with the subject:
    ```
    $echo "The mail to be send " > subject.txt
    ```

    * Send the mail :
    ```
      python3 sending.py receiver@gmail.com -c config.json -s subject.txt
    ```
