from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChormeService
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
  options = Options()
  options.add_argument("--no--sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()) ,options=options)
  browser.get(f"https://jp.indeed.com/jobs?q={keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  
  pagination = soup.find('nav', class_="css-jbuxu0 ecydgvn0")
  pages = pagination.find_all('div', class_="css-tvvxwd ecydgvn1")
  
  count = len(pages)
  if count == 0:
    return 1
  elif count >= 5:
    return 5
  else:
    return count



def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  results = []
  print("Found", pages, "pages")
  for page in range(pages):
    options = Options()
    options.add_argument("--no--sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()) ,options=options)
    print("Requested", "page")
    browser.get(f"https://jp.indeed.com/jobs?q={keyword}&start={page*10}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)
    
    for job in jobs:
      zone = job.find('div', class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        print(anchor)
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_='companyLocation')
        job_data = {
          'title': title,
          'link': f"https://jp.indeed.com{link}",
          'company': company.string,
          'location': location.string,
        }
        for each in job_data:
          if job_data[each] != None:
            job_data[each] = job_data[each].replace(",","/")
        results.append(job_data)
  return results



