import requests


def download_data():
    response = requests.get("https://justjoin.it/api/offers")
    assert 200 == response.status_code
    data = response.json()

    return data


def award_points(data):
    dict_list = []


    for job in data:
        sum = 0
        if job['remote'] is True:
            sum += 10

        if job['remote'] is False:
            sum -= 10

        if job['marker_icon'] == 'data':
            sum += 1

        if job['experience_level'] == 'senior':
            sum -= 3

        if 'DevOps' in job['title']:
            sum -= 20

        for skill in job['skills']:
            if skill['name'] == 'Python':
                sum += 10

            if skill['name'] == 'GCP':
                sum += 20

            if skill['name'] == 'GCP or AWS':
                sum += 15

            if skill['name'] == 'SQL':
                sum += 10

            if skill['name'] == 'C#':
                sum -= 2

            if skill['name'] == 'Kubernetes':
                sum -= 3

            if skill['name'] == 'AWS':
                sum -= 2

        job_dict = {
            "id": 'https://justjoin.it/offers/' + job['id'],
            "points": sum,
            "full_json": job
        }
        dict_list.append(job_dict)

    sorted_list = sorted(dict_list, key=lambda d: d['full_json']['published_at'])
    return sorted_list

if __name__ == "__main__":
    data = download_data()
    sorted_list=award_points(data)

    for dict_job in sorted_list:
        if dict_job['points'] >=25:
            print(dict_job)
