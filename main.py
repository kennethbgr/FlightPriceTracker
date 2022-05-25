import data_manager
import flight_search
import flight_data
import notification_manager

datamanager = data_manager.DataManager()
sheet_data = datamanager.read_data()
flight_data = flight_data.FlightData()
notification_manager = notification_manager.NotificationManager()

# -------------------------Populate the iata codes for cities ---------------------
# for index in range(len(sheet_data)):
#     if sheet_data[index]["iataCode"] == "":
#         fix_iata = flight_search.FlightSearch()
#         new_iata = fix_iata.replace_iata(sheet_data[index])
#         sheet_data[index].update({"iataCode": new_iata})
#         datamanager.update_data(sheet_data[index], index+2)

for index in range(len(sheet_data)):
    try:
        flight_data.search_flight_data(sheet_data[index])[0]
    except TypeError:
        flight_info = None
        print(f"No flights found for {sheet_data[index]['iataCode']}")
    else:
        flight_info = flight_data.search_flight_data(sheet_data[index])[0]
        flight_price = flight_data.search_flight_data(sheet_data[index])[1]
        link = flight_data.search_flight_data(sheet_data[index])[2]
        is_price_lower = notification_manager.compare_prices(flight_price, sheet_data[index])
        if is_price_lower:
            # notification_manager.send_txt(flight_info, link) ----> enable texting of information
            emails = datamanager.read_email()
            notification_manager.send_email(flight_info, emails, link)





