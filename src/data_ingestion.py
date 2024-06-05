import requests

def get_carpark_dict(api_key: str):
    """Fetches the mapping between carpark id and name"""
    url = "https://api.transport.nsw.gov.au/v1/carpark"
    headers = {"Authorization": f"apikey {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_real_time_carpark_data(api_key: str, facility_id: str):
    """Fetches real-time car park occupancy data from TfNSW API"""
    url = "https://api.transport.nsw.gov.au/v1/carpark"
    headers = {"Authorization": f"apikey {api_key}"}
    params = {"facility": facility_id}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_historical_carpark_data(api_key: str, facility_id: str, event_date: str):
    """Fetches real-time car park occupancy data from TfNSW API"""
    url = "https://api.transport.nsw.gov.au/v1/carpark/history"
    headers = {"Authorization": f"apikey {api_key}"}
    params = {"facility": facility_id, "eventdate": event_date}
    response = requests.get(url, headers=headers, params=params)
    return response.json()