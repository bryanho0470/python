from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
from datetime import date

search_term = input("What kind of job do you want to search?")

wwr_jobs = extract_wwr_jobs(search_term)
indeed_jobs = extract_indeed_jobs(search_term)

total_jobs = wwr_jobs + indeed_jobs

save_to_file(search_term, total_jobs)



