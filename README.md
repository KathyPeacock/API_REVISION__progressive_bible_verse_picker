 # ===========================================================================
🌈 PROGRESSIVE & INCLUSIVE BIBLE VERSES API Testing & Integrating Project🌈
===========================================================================

*A quick revision project completed during my Makers software testing bootcamp to practice API testing fundamentals through both manual and automated approaches. I'm a career-switcher into tech, with experience spanning the acting world and academic Theology - so utilising Bible API felt like a fun approach!*

This project uses the free Bible API: https://bible-api.com/

This was a focused revision exercise (completed in ~3 hours) to reinforce API testing concepts after our bootcamp's rapid introduction to the topic. I wanted a practical, portfolio-ready mini-project that demonstrated:

**Manual API Testing (Postman):**
- Creating and organizing API test collections
- Testing successful GET requests and validating responses
- Negative testing with invalid inputs (404 scenarios)
- Examining response structure (JSON parsing)
- Validating status codes and response times
- Testing query parameters (different Bible translations)

**Automated API Testing (Python):**
- Making HTTP GET requests programmatically
- Parsing JSON responses
- Implementing error handling for connection issues and invalid data
- Building a user-friendly CLI application
- Clean code structure with helper functions
- Playful & creative formatting of printed responses

## Technologies Used

- **Postman** - Manual API testing and request organization
- **Python 3** - Automation scripting (using VS Code)
- **requests library** - HTTP client for Python
- **Bible API** (https://bible-api.com) - Free, no-auth API for practice
- **Git/GitHub** - Version control and portfolio documentation

## Installation & Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Quick Start

1. **Clone the repository:**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install requests
```

3. **Run the application:**
```bash
python progressive_bible_verses.py
```

**Example endpoints tested:**
- `GET https://bible-api.com/john+3:16` - Fetch specific verse
- `GET https://bible-api.com/galatians+3:28?translation=kjv` - Fetch with translation parameter

*Created as a revision exercise during Makers Software Testing Bootcamp - November 2025*
