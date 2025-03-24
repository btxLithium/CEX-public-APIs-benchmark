# Configuration file for API latency monitoring

# Exchanges information
EXCHANGES = {
    'okx': {
        'name': 'OKX',
        'description': 'OKX Cryptocurrency Exchange'
    },
    'bitget': {
        'name': 'Bitget',
        'description': 'Bitget Cryptocurrency Exchange'
    }
}

# API endpoints for different exchanges
ENDPOINTS = {
    'okx': {
        'market_data': {
            'url': 'https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        },
        'book': {
            'url': 'https://www.okx.com/api/v5/market/books?instId=BTC-USDT&sz=10',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        },
        'trades': {
            'url': 'https://www.okx.com/api/v5/market/trades?instId=BTC-USDT',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        }
    },
    'bitget': {
        'market_data': {
            'url': 'https://api.bitget.com/api/mix/v1/market/ticker?symbol=BTCUSDT_UMCBL',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        },
        'book': {
            'url': 'https://api.bitget.com/api/mix/v1/market/depth?symbol=BTCUSDT_UMCBL&limit=20',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        },
        'trades': {
            'url': 'https://api.bitget.com/api/mix/v1/market/trades?symbol=BTCUSDT_UMCBL&limit=20',
            'method': 'GET',
            'headers': {
                'Accept': 'application/json'
            }
        }
    }
}

# Settings for API requests
API_SETTINGS = {
    'timeout': 10,        # Request timeout in seconds
    'retry_count': 3,     # Number of retries for failed requests
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'use_api_key': False, # Whether to use API keys for requests
    'api_key_header': 'X-API-KEY', # Header name for API key
    'api_keys': {         # API keys for different exchanges
        # 'okx': 'your-api-key-here',
        # 'bitget': 'your-api-key-here'
    }
}

# Benchmark settings
BENCHMARK_SETTINGS = {
    'min_rounds': 5,      # Minimum number of rounds to run for each benchmark
    'max_time': 1.0,      # Maximum time (in seconds) to run each benchmark
    'warmup': True,       # Whether to perform a warmup round
    'latency_threshold': {  # Maximum acceptable latency in ms for each endpoint
        'market_data': 500,
        'book': 600,
        'trades': 550
    }
}

# Data storage settings
DATA_STORAGE = {
    'max_entries': 1000,  # Maximum number of data points to keep per exchange
    'output_dir': 'benchmark_results',  # Directory to store benchmark data
    'chart_width': 12,    # Width of charts in inches
    'chart_height': 7,    # Height of charts in inches
    'dpi': 300           # DPI for saved charts
}

# Reporting settings
REPORTING = {
    'chart_width': 12,
    'chart_height': 7,
    'dpi': 300,
} 