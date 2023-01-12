import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/AUS/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_hundred_years = response.json()[1][:100]

for year in last_hundred_years:
    display_width = year["value"] // 10_000_000
    value_fmt = "{:,}".format(year["value"])
    print(f'{year["date"]}: {value_fmt}', "=" * display_width)
