import pandas as pd
import pytrends

# Set the start and end dates for the tracking period
start_date = "2023-01-01"
end_date = "2023-12-31"

# Create a list of the terms to track
terms = ["Woodford Reserve", "Russell's Reserve", "Blanton's Bourbon",
"Eagle Rare", "Heaven's Door", "Jefferson's", "Old Rip Van Winkle", 
"Distillery", "Brothers Bond", "Johnnie Walker", "The Sassenach",
"Whiskey JYPSI"]

# Create a PyTrends object
pytrends = pytrends.InterestOverTime()

# Build the payload
pytrends.build_payload(terms, start_date, end_date)

# Get the daily Google Trend Scores for the terms
daily_trend_scores = pytrends.interest_over_time()

# Save the daily trend scores to a Google Sheet
daily_trend_scores.to_gsheet("daily_google_trend_scores.csv")