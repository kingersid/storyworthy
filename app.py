from app import create_app
import os

app = create_app()

@app.route('/debug')
def debug():
    return f"Template folder: {os.path.join(app.root_path, 'templates')}"

if __name__ == '__main__':
    app.run(debug=True)