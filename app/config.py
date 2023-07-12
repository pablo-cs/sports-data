class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///nba.db'
    SQLALCHEMY_BINDS = {
        'favorite': 'sqlite:///favorite.db',
        'comment': 'sqlite:///comment.db'
    }
    CACHE_TYPE = 'simple'
