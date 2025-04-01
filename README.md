# lexo

Language learning through spaced repetition with AI practice enabled

## Installation

1. Clone the repository:
```bash
git clone https://github.com/wastella/lexo.git
cd lexo
```

2. Install the package in development mode:
```bash
python3 -m pip install -e .
```

This will automatically install the required dependencies:
- fsrs (for spaced repetition)
- google-generativeai (for AI-powered practice sessions)

## Usage

You'll need a Google Gemini API key to use Lexo. Once you have it, you can start practicing:

```bash
# Start a new practice session (saves to stored_concepts.json)
python3 main.py -k YOUR_API_KEY

# Load/save progress from a custom file
python3 main.py -k YOUR_API_KEY -f my_progress.json

# Do more or fewer practice sessions
python3 main.py -k YOUR_API_KEY -n 5
```

The program will:
1. Present you with Spanish language concepts to practice
2. Generate English sentences for you to translate to Spanish
3. Grade your translations and track your progress
4. Use spaced repetition to optimize your learning schedule

Your progress is automatically saved after each session, and you can continue where you left off by using the same save file.


## TODO 
- Revise recommendation algorithm to include repeat questions
- Add support for other languages
- Add support for other exercises
