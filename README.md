# FlightPriceTracker

Application that I developed for personal use where the it communicates with different APIs to verify information of flight prices agaisnt information posted on a Google Sheet with what the user would consider low flight prices to any destination. 

The application will communicate with an API, ingest the data and corroborate if the price of a flight is below what the user wants to pay. If this is true, the application will trigger a message to send the flight information to the user via email or text. 

Application will search first for direct flights, if none is found, it will search for flights with multiple stops. 


See below for notifications sent to users: 

Text Notification: 
![42189](https://user-images.githubusercontent.com/101911504/169675237-f045f1fb-53d6-40c7-b463-6b8e570c17be.jpg)



Email Notification: 

![image](https://user-images.githubusercontent.com/101911504/169675282-4f4c6c2f-bbe8-4e8d-8de0-cf777dc8789e.png)



APIs/Libraries used in this project:
- smtplib (for sending email notifications)
- Twilio API (for sending text notifications)
- Tequila API (for getting information about flight prices)
- Sheety API (for communicating with Google Sheets)

