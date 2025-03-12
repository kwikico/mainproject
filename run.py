from app import app
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask application')
    parser.add_argument('--port', type=int, default=5002, help='Port to run the application on')
    args = parser.parse_args()
    
    app.run(debug=True, port=args.port) 