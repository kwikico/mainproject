from app import app
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask application')
    parser.add_argument('--port', type=int, default=5002, help='Port to run the application on')
    args = parser.parse_args()
    
    # Use this configuration for local development
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, port=args.port)
    else:
        # Production configuration for Heroku
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=False, host="0.0.0.0", port=port) 