import requests
from bs4 import BeautifulSoup

class XSSScanner:
    def __init__(self, target_urls):
        self.target_urls = target_urls
        self.detected_vulnerabilities = []

    def scan(self):
        for url in self.target_urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                script_tags = soup.find_all('script')
                for script_tag in script_tags:
                    script_content = script_tag.get_text()
                    if self.is_suspicious_script(script_content):
                        vulnerability = {
                            "url": url,
                            "payload": script_content,
                            "context": "Script tag",
                            "severity": "Low"  # For demonstration purposes
                        }
                        self.detected_vulnerabilities.append(vulnerability)
            else:
                print(f"Failed to retrieve {url}. Status code: {response.status_code}")

    def is_suspicious_script(self, script_content):
        # Implement your logic to determine if the script content is suspicious
        # You should use a more robust method for XSS detection
        return False  # You need to implement a better check

    def generate_report(self):
        print("XSS Vulnerability Scanning Report")
        print("=" * 50)
        if not self.detected_vulnerabilities:
            print("No vulnerabilities detected.")
        else:
            for index, vulnerability in enumerate(self.detected_vulnerabilities, start=1):
                print(f"Vulnerability {index}:")
                print(f"URL: {vulnerability['url']}")
                print(f"Payload: {vulnerability['payload']}")
                print(f"Context: {vulnerability['context']}")
                print(f"Severity: {vulnerability['severity']}")
                print("-" * 50)

if __name__ == "__main__":
    target_urls = ["http://128.198.49.198:8102/mutillidae/index.php?page=login.php"]
    scanner = XSSScanner(target_urls)
    scanner.scan()
    scanner.generate_report()