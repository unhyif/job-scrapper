import requests
from bs4 import BeautifulSoup

based_url = "https://stackoverflow.com/jobs"
def get_last_page(search=""):
  url = based_url + f"?q={search}&r=true"
  soup = BeautifulSoup(requests.get(url).text, "html.parser")
  last_page = int(soup.find("div", class_ = "s-pagination").find_all("a")[-2].find("span").string)
  return last_page

def get_jobs(search=""):
  try:
    jobs = []
    for page in range(get_last_page(search)):
      url = based_url + f"?q={search}&r=true&pg={page+1}"
      soup = BeautifulSoup(requests.get(url).text, "html.parser")
      divs = soup.find("div", class_ = "listResults").find_all("div", class_ = "-job")
      for div in divs:
        if extract_info(div):
          jobs.append(extract_info(div))
    return jobs
  except:
    return []
  
def extract_info(soup):
  company = soup.find("h3").find("span").string
  if company:
    title = soup.find("h2").text.strip()
    link = based_url + "/" + soup["data-jobid"]
    result = {"Title":title, "Company":company.strip(), "Link":link}
    return result
  return None