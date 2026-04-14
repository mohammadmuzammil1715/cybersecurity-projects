# Advanced Fake Game Link Detector

url = input("Enter game link: ")

score = 0

# Rule 1: HTTPS check
if "https" in url:
    score += 1
else:
    score -= 2

# Rule 2: URL length
if len(url) > 30:
    score -= 1

# Rule 3: Special characters
if "@" in url or "-" in url:
    score -= 2

# Rule 4: Suspicious words
suspicious_words = ["free", "hack", "mod", "crack", "cheat"]

for word in suspicious_words:
    if word in url.lower():
        score -= 2

# Rule 5: Numbers in domain
if any(char.isdigit() for char in url):
    score -= 1

# Final Decision
print("Security Score:", score)

if score >= 1:
    print("Safe Link ✅")
elif score >= -2:
    print("Suspicious Link ⚠")
else:
    print("Phishing Link ❌")