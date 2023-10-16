from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url_A = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
  base_url_B = "&vjk=192f4184990521d4"

  response = get(f"{base_url_A}{keyword}")
  if response.status_code != 200:
    print("the request not response")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs: #task for list to data
      job_posts = job_section.find_all('li') 
      job_posts.pop(-1) # this is List still.
      
      # if we use find_all, the result is gonna be A LIST([]or()). so we cant use soup command directly, we need to convert to text data, by using FOR loop.
      for post in job_posts: #task for list to data again.
        anchors = post.find_all('a')
        anchor = anchors[1]
        print(anchor)
        link = anchor['href']
        company, type, region = anchor.find_all('span', class_='company') # this is not a LIST. result.
        job_title = anchor.find('span', class_="title")
        job_data = {
          'title' : job_title.string.replace(",", "/"),
          'company' : company.string.replace(",", "/"),
          'type' : type.string.replace(",", "/"),
          'location' : region.string.replace(",", "/"),
          'link' : f"https://weworkremotely.com{link}",
        }
        results.append(job_data)
    return results