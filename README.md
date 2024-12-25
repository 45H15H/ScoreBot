# ScoreBot

## Description

**ScoreFetcher** is a Python-based automation tool that scrapes scorecards from an online portal and downloads them locally. Designed for efficiency and ease of use, this script leverages web scraping techniques to streamline the retrieval of results, saving users significant time and effort.

---

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/45H15H/ScoreBot.git
   cd ScoreBot
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Configure student details**:
   - Edit the `DOBs.txt` file to include the login credentials (e.g., roll number, date of birth) for each student.

### Running the Project

1. **Run the script**:

   ```bash
   python score_fetcher.py
   ```

2. **Retrieve results**:
   - The scorecards will be downloaded to the `output/` folder by default.

---

## Contributing

Feel free to contribute, report issues, or request features to make **ScoreBot** even better!
