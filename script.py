from bs4 import BeautifulSoup
import requests
import re
import tkinter as tk
from tkinter import messagebox


def is_valid_topic(topic):
    """Validate that the topic contains only letters, numbers, or spaces."""
    return bool(re.match(r'^[A-Za-z0-9 ]+$', topic))


def is_valid_email_domain(domain):
    """Validate that the email domain matches typical domain patterns."""
    return bool(re.match(r'^[A-Za-z0-9]+$', domain))


def is_valid_site(site):
    """Validate that the site is a valid domain name."""
    return bool(re.match(r'^[A-Za-z0-9.-]+$', site))


def scrape_and_save_emails():
    # Get the values for topic, emaildomain, and site from Entry widgets
    topic = topic_entry.get().strip()
    emaildomain = emaildomain_entry.get().strip()
    site = site_entry.get().strip()

    # Validate inputs
    if not topic:
        messagebox.showerror("Error", "Topic field cannot be empty.")
        return
    if not is_valid_topic(topic):
        messagebox.showerror("Error", "Invalid topic. Use only letters, numbers, and spaces.")
        return

    if not emaildomain:
        messagebox.showerror("Error", "Email domain field cannot be empty.")
        return
    if not is_valid_email_domain(emaildomain):
        messagebox.showerror("Error", "Invalid email domain. Use only letters and numbers (e.g., gmail).")
        return

    if not site:
        messagebox.showerror("Error", "Site field cannot be empty.")
        return
    if not is_valid_site(site):
        messagebox.showerror("Error", "Invalid site. Use a valid domain name (e.g., linkedin, google).")
        return

    # Construct the URL with the provided values
    url = f"https://www.google.com/search?hl=en&as_q={topic}+&as_epq={emaildomain}+com&as_oq=sales+purchasing+importer+buyer+marketing&as_eq=&as_nlo=&as_nhi=&lr=&cr=countryUS&as_qdr=all&as_sitesearch={site}.com&as_occt=any&as_filetype=&tbs=&&num=1000#ip=1"

    # Perform the request and parse the HTML
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch URL: {e}")
        return

    soup = BeautifulSoup(page.text, 'html.parser')

    # Find and collect unique email addresses
    unique_emails = set()
    for element in soup.find_all(string=True):
        for match in re.finditer(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', element):
            unique_emails.add(match.group())

    # Write unique emails to 'emails.txt' by overwriting its content
    with open('emails.txt', 'w') as file:
        for email in unique_emails:
            file.write(f"{email}\n")

    messagebox.showinfo("Success", "The unique email addresses have been successfully saved to 'emails.txt'. You can find the file in the same directory as this program.")


# Create the main window
root = tk.Tk()
root.title("Buyers Email Scraper")

# Create and place widgets
topic_label = tk.Label(root, text="Enter the topic: (such as: towel, bedsheet)")
topic_label.pack(pady=10)

topic_entry = tk.Entry(root, width=50)
topic_entry.pack(pady=10)

emaildomain_label = tk.Label(root, text="Enter the email domain: (such as: gmail, hotmail, etc.)")
emaildomain_label.pack(pady=10)

emaildomain_entry = tk.Entry(root, width=50)
emaildomain_entry.pack(pady=10)

site_label = tk.Label(root, text="Enter the site: (such as: linkedin, google, etc.)")
site_label.pack(pady=10)

site_entry = tk.Entry(root, width=50)
site_entry.pack(pady=10)

scrape_button = tk.Button(root, text="Scrape Emails", command=scrape_and_save_emails)
scrape_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
