from linkedin_jobs import get_linkedin_jobs
from mploy_jobs import get_mploy_jobs
import json

save_as = 'sample.json'

if __name__ == '__main__':
    key = input("Please input your search keyword: > ")
    limit = int(input("The limit for each website: > "))
    data = []
    for job in get_linkedin_jobs(key, limit):
        data.append(job)
    for job in get_mploy_jobs(key, limit):
        data.append(job)
    with open(save_as, 'w', encoding='utf8') as jsonFile:
        json.dump(data, jsonFile, indent=4, ensure_ascii=False)
    print(f'Data saved as {save_as}')

    for opportunity in data:
        print(f"\n-----====|||   {opportunity['title']}   |||=====-----")
        print(f"{opportunity['url']}")
        print(f"{opportunity['source']} | {opportunity['date']}")
    print(f'Total results:{len(data)}')
