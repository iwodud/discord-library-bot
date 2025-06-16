# Discord Library Bot

A Discord bot that manages a simple library system.  
Users can borrow and return books directly through Discord commands.  
The bot also reminds users about due dates.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/iwodud/discord-library-bot.git
cd discord-library-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the database

```bash
python3 init_db.py
```

### 4. (Optional) Add example data

```bash
python3 example_data.py
```

### 5. Run the bot

```bash
python3 bot/main.py
```

---

## Project Structure

```
discord-library-bot/
├── bot/                # Bot logic: commands, reminders, main entry point
├── database/           # Database schema and access logic
├── init_db.py          # Script to initialize SQLite database
├── example_data.py     # Optional: insert sample books, users, and loans
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (e.g., Discord bot token)
└── README.md           # This file
```

---

## Technologies Used

- Python 32
- discord.py
- SQLite (as a temporary local database)

---

## Features (in progress)

- [x] SQLite database structure
- [x] Database init script
- [ ] Command: borrow a book
- [ ] Command: return a book
- [ ] Command: list available books
- [ ] Reminder system for due dates
- [ ] User tracking via Discord ID

---

## Notes

- `library.db` is **not committed to the repository**. Each developer creates their own local version using `init_db.py`.
- In the future, the project may migrate to a production-grade database like MySQL or PostgreSQL.

---