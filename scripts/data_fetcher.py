import requests
import datetime

def fetch_data():
    # Example: Fetching a daily quote to show 'Living' data
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()[0]
        return f"> \"{data['q']}\" \n> — **{data['a']}**"
    return "System Online: Intelligence feed pending."

if __name__ == "__main__":
    content = fetch_data()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # This writes the output to a temporary file for the next step
    with open("data_output.txt", "w") as f:
        f.write(f"### Last System Pulse: {timestamp}\n\n{content}")
