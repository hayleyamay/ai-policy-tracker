from govuk_scraper import get_govuk_ai_policy
from us_scraper import get_us_ai_policy
from eu_scraper import get_eu_ai_policy 

print("Starting AI Policy Tracker scrape...")

get_govuk_ai_policy()
get_us_ai_policy()
get_eu_ai_policy()

print("All done! Data saved to data/ folder.") 