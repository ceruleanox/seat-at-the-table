CREATE TABLE IF NOT EXISTS leader (
    UserID Integer PRIMARY KEY,
    TeamsLed Integer DEFAULT 0,
    BeginnersMentored Integer DEFAULT 0,
    XPLock text DEFAULT CURRENT_TIMESTAMP
);