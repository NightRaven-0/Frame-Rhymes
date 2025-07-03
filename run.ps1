# Start backend Flask app in a new terminal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Backend; python app.py"

Start-Sleep -Seconds 3

# Start frontend static server in a new terminal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Frontend\public; python -m http.server 5500"

Start-Sleep -Seconds 2

# Open default browser to frontend URL
Start-Process "http://127.0.0.1:5500/index.html"
