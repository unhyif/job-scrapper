import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

based_url = "https://remoteok.com/"

def get_jobs(search=""):
  try:
    jobs = []
    url = based_url + f"remote-dev+{search}-jobs"
    soup = BeautifulSoup(requests.get(url, headers = headers).text, "html.parser")
    trs = soup.find("table", id = "jobsboard").find_all("tr", class_ = "job")
    for tr in trs:
      jobs.append(extract_info(tr))
    return jobs
  except:
    return []
  
def extract_info(soup):
  title = soup.find("h2", itemprop = "title").string
  company = soup.find("h3", itemprop = "name").string
  link = based_url + soup["data-id"]
  result = {"Title":title, "Company":company, "Link":link}
  return result