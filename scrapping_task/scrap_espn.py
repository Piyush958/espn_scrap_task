import requests
from bs4 import BeautifulSoup

url = "https://www.espn.in/cricket/scores/series/8048/season/2024/indian-premier-league"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    main_divs = soup.find_all("div", class_="cscore_link cscore_link--button")

    allMatches = []

    for main_div in main_divs:
        match_no = main_div.find_all("div", class_="cscore_info-overview")
        team1 = main_div.find_all('li', class_='cscore_item cscore_item--away')
        team2 = main_div.find_all('li', class_='cscore_item cscore_item--home')
        resultDiv = main_div.find_all("span", class_="cscore_notes_game")

        allMatches.append({
            "match_no": match_no,
            "between": {
                'team1': team1,
                'team2': team2,
            },
            "resultDiv": resultDiv
        })

    finalResult = []

    for match in allMatches:
        match_no = match["match_no"]
        result_divs = match["resultDiv"]

        team1_name = match["between"]["team1"][0].find_all("span", class_="cscore_name cscore_name--abbrev")[0].get_text(strip=True)
        team2_name = match["between"]["team2"][0].find_all("span", class_="cscore_name cscore_name--abbrev")[0].get_text(strip=True)

        match_details = f" ({team1_name} vs {team2_name}) "

        finalResult.append({
            "M_no": str(match_no[0].get_text(strip=True)),
            "vs": match_details,
            "result": str(result_divs[0].get_text(strip=True))
        })

    print(finalResult)

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
