# termux_git_push.py নামে একটি file তৈরি করুন
import os
import requests

# আপনার GitHub credentials
GITHUB_TOKEN = ""
USERNAME = "sheikhsadi12"
REPO_NAME = "New-copy-app"

# Create repository via API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

data = {
    "name": REPO_NAME,
    "description": "AI Teacher Notebook - Android App",
    "private": False,
    "auto_init": False
}

print("Creating repository...")
response = requests.post(
    "https://api.github.com/user/repos",
    headers=headers,
    json=data
)

if response.status_code == 201:
    print("✅ Repository created!")
    
    # Now push files
    print("\nPushing files to GitHub...")
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial commit"')
    os.system(f"git remote add origin https://{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git")
    os.system("git branch -M main")
    os.system("git push -u origin main")
    
    print("\n🎉 Success! Your repository is ready at:")
    print(f"https://github.com/{USERNAME}/{REPO_NAME}")
else:
    print("❌ Error creating repository")
    print(response.json())
