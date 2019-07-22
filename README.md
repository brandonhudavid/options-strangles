# Options Scrape

Gets data regarding stocks and their past quarters' earnings reports.

## Setup

1. Clone this repo
2. [Claim a free API key from Alpha Vantage](https://www.alphavantage.co/support/#api-key)
3. Within the cloned repo, create a file `config.py` with content `APIKEY="YOUR_API_KEY"`
   
## Usage

Open `options.py` in a Python interactive interpreter. To get data about a stock's past earnings reports, call `get("STOCK_TICKER")`

i.e. `get("MSFT")`

## To-do

- Format better via [tabulate](https://pypi.org/project/tabulate/)
- Scrape P/E ratio from [Yahoo Finance API](https://rapidapi.com/apidojo/api/yahoo-finance1/pricing)
- Perform function call for all companies reporting earnings today/on a certain day