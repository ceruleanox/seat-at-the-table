CREATE TABLE IF NOT EXISTS guilds (
    GuildID Integer PRIMARY KEY,
    Prefix text DEFAULT +
);

CREATE TABLE IF NOT EXISTS leader (
    UserID Integer PRIMARY KEY,
    TeamsLed Integer DEFAULT 0,
    BeginnersMentored Integer DEFAULT 0,
    XPLock text DEFAULT CURRENT_TIMESTAMP
);