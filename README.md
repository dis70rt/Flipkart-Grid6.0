# Flipkart GRiD Hackathons Level 1 MCQ Round Helper

This Python script fetches and processes the latest tweets from Flipkart's Twitter account to assist with the Flipkart GRiD Hackathons Level 1 MCQ Round. It also generates a `prompt.txt` file that can be used with ChatGPT to create a comprehensive summary document for the tweets data, aiding in preparation for the E-commerce MCQ Round.

## Features

- Retrieves tweets from Flipkart's Twitter account using the `FlipkartClient`.
- Saves tweet data in JSON format to `data/flipkart_twitter.json`.
- Generates a `prompt.txt` file for detailed analysis and summary generation using ChatGPT.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/saikat-iit/Flipkart-Grid6.0.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Use `prompt.txt` with ChatGPT to generate a detailed summary document for the tweets data.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
