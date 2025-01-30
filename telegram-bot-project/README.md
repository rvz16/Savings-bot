# Telegram Bot Project

This project is a Telegram bot designed to save and distribute topics with links to articles and YouTube videos. Users can create topics, set importance levels for saved videos, and receive daily reminders to watch specific videos.

## Intentions

The intention behind this bot is to help users manage and organize their saved messages and videos from YouTube efficiently. The bot can automatically categorize videos based on their descriptions and assign them to relevant topics. Users can also manually create topics and set the importance of each video, ranging from "super important" to "not very important." Additionally, the bot sends daily reminders to watch specific videos, ensuring that important content is not forgotten.

## Features

- Create and manage topics with associated links to articles and videos.
- Set importance levels for saved videos.
- Receive daily reminders for specific videos.
- Utilize machine learning for topic classification and retrieval-augmented generation.

## Project Structure

```
telegram-bot-project
├── src
│   ├── bot
│   │   ├── handlers
│   │   ├── __init__.py
│   │   └── main.py
│   ├── database
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   ├── ml
│   │   ├── knn.py
│   │   ├── rag.py
│   │   └── __init__.py
│   ├── api
│   │   ├── main.py
│   │   └── __init__.py
│   ├── utils
│   │   ├── embeddings.py
│   │   └── __init__.py
│   └── __init__.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-bot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in the `.env` file.

## Usage

1. Start the bot by running:
   ```
   python src/bot/main.py
   ```

2. Access the API endpoints defined in `src/api/main.py` to interact with the bot.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.