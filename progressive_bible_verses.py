
"""
Progressive & Inclusive Bible Verses API
Fetches affirming scripture about love, inclusion, and equality 🌈🏳️‍⚧️💖
"""

import requests
import random

# Collection of progressive/inclusive verses
PROGRESSIVE_VERSES = {
    "Galatians 3:28": "No male nor female - all are one",
    "Ruth 1:16": "Ruth & Naomi's covenant of devotion",
    "Acts 10:34": "God shows no partiality",
    "John 13:34": "Love one another",
    "1 Samuel 18:1": "David & Jonathan's love",
    "Matthew 25:40": "What you did for the least of these"
}
# Helper method to wrap text when verse is formatted to print
def wrap_text(text, width=50):
    if len(text) <= width:
        return [text]
    
    lines = []
    remaining = text
    
    while len(remaining) > width:
        # Try to break at a space
        if ' ' in remaining[:width]:
            # Find the last space within width
            break_point = remaining[:width].rfind(' ')
            lines.append(remaining[:break_point])
            remaining = remaining[break_point+1:].lstrip()
        else:
            # No space found, force break at width
            lines.append(remaining[:width])
            remaining = remaining[width:].lstrip()
    
    if remaining:
        lines.append(remaining)
    
    return lines

def fetch_verse(reference):
    """Fetch a Bible verse from the API"""
    # Format reference for URL (replace spaces with +)
    formatted_ref = reference.replace(" ", "+").replace(":", "%3A")
    url = f"https://bible-api.com/{formatted_ref}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "reference": data.get("reference"),
                "text": data.get("text"),
                "translation": data.get("translation_name")
            }
        else:
            return {
                "success": False,
                "error": f"Error {response.status_code}: Verse not found"
            }
    # except Exception as e:
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Connection error: {str(e)}"
        }

def display_verse(verse_data):
    """Display the verse in a nice format"""
    if verse_data["success"]:
        print("\n" + "="*60)
        print(f"📖 {verse_data['reference']}")
        print(f"   ({verse_data['translation']})")
        print("="*60 + "\n")
        
        # Wrap the verse text
        wrapped_lines = wrap_text(f'"{verse_data["text"]}..."', width=50)
        for line in wrapped_lines:
            print(line)
        
        print("\n" + "="*60 + "\n")
    else:
        print(f"\n❌ {verse_data['error']}\n")

def get_random_verse():
    """Get a random verse from our progressive collection"""
    reference = random.choice(list(PROGRESSIVE_VERSES.keys()))
    description = PROGRESSIVE_VERSES[reference]
    
    print(f"\n🌈 Fetching: {reference} - {description}")
    verse_data = fetch_verse(reference)
    display_verse(verse_data)

def search_specific_verse():
    """Let user search for a specific verse"""
    print("\n🔍 Enter a Bible reference (e.g., 'John 3:16'):")
    reference = input("Reference: ").strip()
    
    verse_data = fetch_verse(reference)
    display_verse(verse_data)

def main():
    """Main menu"""
    print("\n" + "="*60)
    print("🌈 PROGRESSIVE & INCLUSIVE BIBLE VERSES 🌈")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Get a random progressive verse 💖")
        print("2. Search for a specific verse 🕊️")
        print("3. Exit 🌥️")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == "1":
            get_random_verse()
        elif choice == "2":
            search_specific_verse()
        elif choice == "3":
            print("\n💜 Go in peace! 💜\n")
            print("And remember ...")
            print("\n" + "="*60)
            print("\n\"Do not judge, and you will not be judged.")
            print("Do not condemn, and you will not be condemned.")
            print("Forgive, and you will be forgiven.\" (Luke 6:37)")
            print("\n" + "="*60)
            print("\n🙌\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()  