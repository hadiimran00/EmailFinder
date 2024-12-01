### Buyers Email Scraper

**Buyers Email Scraper** is a Python-based desktop application built with **Tkinter** that allows users to scrape email addresses from Google search results based on user-defined criteria. The tool is designed to help businesses or researchers collect contact information efficiently while maintaining flexibility and simplicity.

#### **Features:**
- **Customizable Input Fields**:
  - Specify a **topic** (e.g., towel, bedsheet) to refine your search.
  - Define the **email domain** (e.g., Gmail, Hotmail) to target specific providers.
  - Limit the search to a particular **site** (e.g., LinkedIn, Google).
- **Smart Validation**:
  - Ensures inputs contain only valid characters for optimal search accuracy.
- **Efficient Email Extraction**:
  - Scrapes unique email addresses from the Google search results using **BeautifulSoup**.
  - Saves results to a local file (`emails.txt`) for easy access.
- **User-Friendly Interface**:
  - A clean and simple GUI built with **Tkinter** for non-technical users.

#### **Requirements:**
- Python 3.x
- Required libraries:
  - `BeautifulSoup`
  - `requests`
  - `tkinter`

#### **How to Use:**
1. Enter your search parameters (topic, email domain, site) in the respective fields.
2. Click the **Scrape Emails** button.
3. View the collected emails in the `emails.txt` file saved in the same directory.

#### **Disclaimer:**
This tool is for educational purposes only. Always respect website terms of service and avoid violating privacy regulations.

---

Feel free to customize this description further for your GitHub repository!
