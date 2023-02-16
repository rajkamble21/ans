from bs4 import BeautifulSoup
import requests
import re

def is_wordpress(domain):
    try:
        response = requests.get(f"http://{domain}")
    except:
        return "Error: Invalid domain or connection issue"
    
    if response.status_code == 200:
        if re.search(r"wp-(content|admin|includes)", response.text):
            soup = BeautifulSoup(response.content, "html.parser")
            version_tag = soup.find("meta", attrs={"name": "generator"})
            if version_tag:
                version = version_tag["content"]
                return f"Yes, running WordPress {version}"
            else:
                return "Yes, running WordPress"
        else:
            return "No, not running WordPress"
    else:
        return "Error: Invalid domain or connection issue"


print(is_wordpress("shoutmeloud.com"))
print(is_wordpress("rvcj.com"))
print(is_wordpress("vcommission.com"))
print(is_wordpress("miniblog216.pythonanywhere.com"))
print(is_wordpress("nothing"))