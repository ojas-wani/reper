# Research Literature Review Application

A Streamlit-based application for performing automated literature reviews using AI.

## Features

- Automated literature review generation
- Research topic analysis
- Novel research approach suggestions
- Interactive UI with real-time progress updates
- Concurrent request handling
- Caching for improved performance
- Comprehensive error handling and logging

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (optional)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Repo/ml
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_base_url_here  # Optional
DEBUG=False
LOG_LEVEL=INFO
```

## Running the Application

### Development

```bash
streamlit run streamlit_app.py
```

### Production Deployment

1. Set up a production server (e.g., AWS, Google Cloud, Heroku)

2. Configure environment variables on your deployment platform

3. Deploy using your preferred method:
   - Docker container
   - Cloud platform specific deployment
   - Traditional server deployment

4. For Docker deployment, use the provided Dockerfile:
```bash
docker build -t literature-review-app .
docker run -p 8501:8501 literature-review-app
```

## Configuration

The application can be configured through:
- Environment variables
- `config.py` file
- `.env` file

Key configuration options:
- `MAX_WORKERS`: Number of concurrent request handlers
- `REQUEST_TIMEOUT`: Maximum time for request processing
- `RATE_LIMIT_REQUESTS`: Maximum requests per time window
- `CACHE_TTL`: Cache time-to-live in seconds

## Monitoring and Logging

- Application logs are stored in `app.log`
- Log level can be configured in `.env` file
- Real-time monitoring available through Streamlit's built-in metrics

## Performance Optimization

The application includes several performance optimizations:
- Request caching
- Concurrent request handling
- Rate limiting
- Resource cleanup
- Memory management

## Security Considerations

- API keys are stored securely
- Rate limiting prevents abuse
- Input validation and sanitization
- Secure file handling
- Error message sanitization

## Troubleshooting

Common issues and solutions:
1. API connection errors
   - Check API key configuration
   - Verify network connectivity
   - Check rate limits

2. Performance issues
   - Adjust `MAX_WORKERS` in config
   - Monitor resource usage
   - Check cache settings

3. Memory issues
   - Adjust cache size
   - Monitor memory usage
   - Implement cleanup routines

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
