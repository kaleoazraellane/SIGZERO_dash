import requests
import datetime

def check_domain(url):
    try:
        response = requests.get(url, timeout=10)
        status = "✅ Active" if response.status_code == 200 else f"⚠️ Code: {response.status_code}"
    except:
        status = "❌ Down/Unreachable"
    return status
    def fetch_data():
    # ... (existing domain check code) ...
    
    stack = """
### 🛠️ System Architecture (The Stack)
| Layer | Technology |
| :--- | :--- |
| **Frontend** | React / Next.js |
| **Backend** | Python (FastAPI) |
| **Database** | PostgreSQL |
| **Infrastructure** | GitHub Actions / Vercel |
"""
    # ... (combine this with your domain report) ...
    return stack + report

def fetch_data():
    domains = {
        "KaleoAzraelLane.com": "https://kaleoazraellane.com",
    }
    
    report = "### 🌐 Domain Status\n\n"
    report += "| Domain | Status |\n| :--- | :--- |\n"
    
    for name, url in domains.items():
        status = check_domain(url)
        report += f"| {name} | {status} |\n"
    
    return report

if __name__ == "__main__":
    content = fetch_data()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("data_output.txt", "w") as f:
        f.write(f"## SIGZERO Intelligence Dashboard\n\n")
        f.write(f"**Last Pulse:** `{timestamp} CST`\n\n---\n\n")
        f.write(content)
