import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=utf-8",
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36',
}


def format_job(opportunity):
    try:
        title = opportunity.find('div').find(class_='result-card__title job-result-card__title').text
    except:
        title = 'Unknown'
    try:
        company = opportunity.find(class_='result-card__subtitle-link job-result-card__subtitle-link').text
    except:
        company = 'Unknown'
    try:
        location = opportunity.find(class_='job-result-card__location').text
    except:
        location = 'Israel'
    try:
        date = opportunity.find(class_='job-result-card__listdate--new').text
    except:
        date = 'Not a long ago..'

    return {
        'title': title,
        'company': company,
        'url': opportunity.find('a')['href'],
        'date': date,
        'location': location,
        'description': "None",
        'source': 'www.linkedin.com'
    }


def get_linkedin_jobs(keyword,limit):
    counter = 0
    jobs = []
    keep_running = True
    while keep_running:
        search = requests.get(
            f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}'
            f'&location=Israel&trk=public_jobs_jobs-search-bar_search-submit&sortBy=DD&redirect=false&'
            f'position=1&pageNum=0&start={counter}', headers=headers)
        data = BeautifulSoup(search.text, 'lxml')
        jobs_list = data.find_all('li')
        if len(jobs_list) > 0 and counter < limit:
            for opportunity in jobs_list:
                jobs.append(format_job(opportunity))
            counter = counter + 25
        else:
            return jobs
    return jobs
