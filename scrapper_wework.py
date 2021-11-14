import requests
from bs4 import BeautifulSoup

based_url = "https://weworkremotely.com"

def get_jobs(search=""):
  try:
    jobs = []
    url = based_url + f"/remote-jobs/search?term={search}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    lis = soup.find("div", class_ = "jobs-container").find_all("li", class_ = lambda x: x != "view-all")
    for li in lis:
      jobs.append(extract_info(li))
    return jobs
  except:
    return []
  
def extract_info(soup):
  title = soup.find("span", class_ = "title").string
  company = soup.find("span", class_ = "company").string
  link = based_url + soup.find_all("a")[1]["href"]
  result = {"Title":title, "Company":company, "Link":link}
  return result