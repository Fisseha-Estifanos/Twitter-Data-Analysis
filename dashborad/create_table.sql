CREATE TABLE IF NOT EXISTS TweetInformation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statuses_count INTEGER  NULL,
    created_at TEXT NOT NULL,
    source TEXT NULL,
    original_text TEXT DEFAULT NULL,
    polarity FLOAT DEFAULT NULL,
    subjectivity FLOAT DEFAULT NULL,
    favorite_count INTEGEREGER DEFAULT NULL,
    retweet_count INTEGER DEFAULT NULL,
    screen_name TEXT DEFAULT NULL,
    followers_count INTEGER DEFAULT NULL,
    friends_count INTEGER DEFAULT NULL,
    possibly_sensitive TEXT DEFAULT NULL,
    hashtags TEXT DEFAULT NULL,
    user_mentions TEXT DEFAULT NULL,
    location TEXT  NULL,
    language TEXT DEFAULT NULL
);
