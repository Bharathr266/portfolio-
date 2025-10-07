-- SQL schema for the recipes table
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    cuisine VARCHAR(255),
    title VARCHAR(512) NOT NULL,
    rating FLOAT,
    prep_time INTEGER,
    cook_time INTEGER,
    total_time INTEGER,
    description TEXT,
    nutrients TEXT, -- JSON serialized
    serves VARCHAR(128)
);
CREATE INDEX IF NOT EXISTS idx_recipes_title ON recipes(title);
CREATE INDEX IF NOT EXISTS idx_recipes_cuisine ON recipes(cuisine);
CREATE INDEX IF NOT EXISTS idx_recipes_rating ON recipes(rating);
CREATE INDEX IF NOT EXISTS idx_recipes_total_time ON recipes(total_time);
