# APIFuzz 🚀

A lightweight Python-based API endpoint fuzzing tool that discovers valid API endpoints and displays their response content directly in the terminal.

## 📌 Motivation

While using tools like **ffuf** for endpoint enumeration, I noticed that although they efficiently identify valid endpoints, I still had to manually visit each endpoint in a browser or use additional tools to inspect the response.

To streamline this process, I created **APIFuzz**.

APIFuzz not only identifies valid endpoints but also displays:

* Endpoint path
* HTTP status code
* Response content

All directly inside the terminal.

---

## ✨ Features

* Endpoint enumeration using custom wordlists
* Displays valid endpoints
* Shows HTTP status codes
* Prints API response content
* Colorized terminal output
* Simple and lightweight

---

## 🛠 Requirements

* Python 3.x
* requests
* termcolor

Install dependencies:

```bash
pip install requests termcolor
```

---

## 📂 Usage

```bash
python3 apifuzz.py <API_URL> <WORDLIST>
```

### Example

```bash
python3 apifuzz.py http://target-api.com/ wordlist.txt
```

---

## 📸 Example Output

```text
[*] checking for endpoints...

[+] Endpoint: /users Status Code: 200
{'id': 1, 'name': 'admin'}

[+] Endpoint: /products Status Code: 200
{'items': ['item1', 'item2']}
```

---

## ⚙️ How It Works

1. Accepts a target API URL.
2. Reads endpoints from a wordlist.
3. Sends GET requests to each endpoint.
4. Ignores 404 responses.
5. Prints valid endpoints and their response content.

---

## 📁 Project Structure

```text
APIFuzz/
│
├── apifuzz.py
├── wordlist.txt
└── README.md
```

---

## 🚀 Future Improvements

* Multithreading support
* Custom headers
* Authentication support
* Rate limiting
* JSON/CSV output
* POST request support
* Response filtering

---

## 👨‍💻 Author

**Aniruddh Kumar Yadav**

GitHub: https://github.com/annithehunter

LinkedIn: https://linkedin.com/in/annithehunter

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain proper permission before testing any target.

