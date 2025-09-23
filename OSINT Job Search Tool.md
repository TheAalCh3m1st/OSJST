# OSINT Job Search Tool

# Project Structure

# osint_job_search/
# ├── main.py              # Entry point with TUI
# ├── config/
# │   ├── roles_config.py  # Job role definitions & variants
# │   └── search_config.py # Search parameters & limits
# ├── engines/
# │   ├── base_searcher.py # Abstract base class
# │   ├── indeed_searcher.py
# │   ├── linkedin_searcher.py
# │   └── glassdoor_searcher.py
# ├── osint/
# │   ├── company_research.py
# │   ├── people_finder.py
# │   └── salary_research.py
# ├── output/
# │   └── report_generator.py
# └── utils/
#    ├── rate_limiter.py
#    └── error_handler.py