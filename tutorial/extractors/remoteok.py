import requests

header = {
  "user-agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
from bs4 import BeautifulSoup


def extract_rmt_jobs(keyword):
  base_url = f"https://remoteok.com/remote-{keyword}-jobs"
  response = requests.get(base_url, headers=header)
  if response.status_code != 200:
    print("This URL has no response")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("td", class_="company position company_and_position")
    jobs.pop(0)
    for job in jobs:
      span = job.select_one("a h2")
      job_title = span.string
      anchor = job.find("a")
      link = anchor['href']
      company = job.select_one("span h3")
      company_etc_data = job.find_all("div", class_="location")
      location_lens = len(company_etc_data)
      etc_infos = []
      if location_lens == 2:
        location, payment = company_etc_data
        location_final = location.string
        payment_final = payment.string
      else:
        location_final, payment_final = "", ""
        company_etc_list = job.find_all("div", class_="location")
        for location_len in range(location_lens):

          etc_infos.append(company_etc_list[location_len].string)
      job_list = {
        'title': job_title.string.replace("\n", ""),
        'link': f"https://remoteok.com{link}",
        'companyName': company.string.replace("\n", ""),
        'location': location_final,
        'payment': payment_final,
        'etc_info': etc_infos,
      }

      results.append(job_list)
    return results


keyword = input("What kind of job are you finding?")
