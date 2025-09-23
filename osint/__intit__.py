
"""
OSINT modules for company and people search.

"""

from .company_searcher import CompanySearcher
from .people_finder import PeopleFinder
from .salary_researcher import SalaryReasearcher

__all__ = ['CompanySearcher',
           'PeopleFinder',
           'SalarySearcher']
