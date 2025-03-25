from app import app
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask application')
    parser.add_argument('--port', type=int, default=5002, help='Port to run the application on')
    args = parser.parse_args()
    
    # Set development environment
    os.environ['FLASK_ENV'] = 'development'
    
    # Development configuration that allows all hosts
    app.run(debug=True, host='0.0.0.0', port=args.port) 