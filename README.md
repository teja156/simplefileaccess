# simplefileaccess
A simple way to access files on your computer from any device on the Internet (NO CLOUD)

This is a simple python script using which you make your own computer as a server, and access files from it, from anywhere on the Internet.
This also includes a simple password protection mechanism. 

You may use this tool to remotely access your computer files through any web browser on the Internet. You will need to enter your username and password to access your files.

Please note that there is no encryption invloved in the password protection mechanism or  whatesoever. Hence, it is not secure cryptographically.

USE IT ON YOUR OWN RISK


HOW TO USE THIS TOOL?

DOWNLOAD AND INSTALL :
1. Download Python from www.python.org
2. Add python to Environment Variables Path (if you are using Windows)
3. Download ngrok from https://ngrok.com/ and create an account. (We use this to create a secure tunnel to the localhost)
4. Now download the script as a ZIP file
5. Unzip the script file, and you will find a folder named as simplefileaccess

CONFIGURE : 

6. Open simplefileaccess -> ftpserver.py

7. On the line 12, change the value to your username, and on line 13, change the value to your password

8. On line 15, change the path to the path on your computer which you want to make accessible for the server

9. On the line 17, change the path to the path where the 'simplefileaccess' folder is saved on your computer. 


RUN:

10. Now open the path where you downloaded ngrok and execute the command ./ngrok tcp 1560

11. This will open a ngrok prompt where you can see the status of your tunnel, wait until it says 'online'

12. Now go the folder simpleaccess and run the script with python from your terminal using the command python ftpserver.py

13. Now the server is up and running


ACCESS FILES:

To access your server, copy the ngrok address and the port from the ngrok tunnel (for example, 0.tcp.ngrok.io:19292) and paste
it in the search box of your browser and hit enter. You will then be taken to a messy web page (cuz its desgined by me) where you
will need to enter your username and password. If your credentials are correct, you will be provided access.

THAT'S THE END OF THE STORY!

 -------- with <3 by Teja Swaroop ---------
