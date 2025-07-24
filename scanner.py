import requests
from bs4 import BeautifulSoup

def crawl(url):
    visited = set()
    to_visit = [url]
    links = []

    while to_visit:
        current = to_visit.pop()
        if current in visited:
            continue
        try:
            res = requests.get(current)
            soup = BeautifulSoup(res.text, 'html.parser')
            for tag in soup.find_all('a', href=True):
                full_link = requests.compat.urljoin(url, tag['href'])
                if full_link not in visited and url in full_link:
                    to_visit.append(full_link)
                    links.append(full_link)
            visited.add(current)
        except:
            continue
    return links
def get_forms(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('form')
payloads = {
    'XSS': "<script>alert('XSS')</script>",
    'SQLi': "' OR '1'='1"
}

def scan(url):
    pages = crawl(url)
    results = []
    for page in pages:
        res = requests.get(page)
        forms = get_forms(res.text)
        for form in forms:
            form_data = {}
            inputs = form.find_all('input')
            for payload_type, payload in payloads.items():
                for input_tag in inputs:
                    name = input_tag.get('name')
                    if name:
                        form_data[name] = payload
                action = form.get('action')
                method = form.get('method', 'get').lower()
                action_url = requests.compat.urljoin(page, action)
                if method == 'post':
                    response = requests.post(action_url, data=form_data)
                else:
                    response = requests.get(action_url, params=form_data)
                if payload in response.text:
                    results.append({"url": page, "vulnerability": payload_type, "payload": payload})
    return results
