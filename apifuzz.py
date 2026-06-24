import requests
import sys
from termcolor import colored, cprint
try:
	url = sys.argv[1]
	wordlist = sys.argv[2]

	cprint(f"[*] checking for endpoints...","red") 
	
	with open(wordlist,'r') as f:
		for line in f:
			word = line.strip()
			res = requests.get(f"{url}{word}")
			if (res.status_code != 404):
				cprint(f"[+] Endpoint: /{word} Status Code: {res.status_code}","green")
				cprint(res.json(),"white")

except IndexError:
	print("Usage: " + sys.argv[0] + " [Url] [wordlist]")
	
except (FileNotFoundError, ValueError) as error:
        print(f"System failed to process the file data: {error}")

except Exception as e:
	print(f"Unexpected error has occured {e}")
