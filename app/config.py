class Config:
    SECRET_KEY = 'bae5f8bb14e95a28a1d679fe833a7ba2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///nba.db'
    SQLALCHEMY_BINDS = {
        'favorite': 'sqlite:///favorite.db',
        'comment': 'sqlite:///comment.db'
    }
    CACHE_TYPE = 'simple'
