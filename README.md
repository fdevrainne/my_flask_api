# Install the requirements

You might want to install the requirements inside a virtual environment <br>
```pip3 install -r requirements.txt```

# Load the data.csv

* Either: change ```DB_PATH``` variable in constant.py to your path to data.csv
* Or: ```mkdir data``` and move the file data.csv to the data folder

# Start the Flask API locally

Run: ```python3 main.py```

Make sure that ```BASE_URL``` variable in constant.py is the host the API is running on (with no final /). <br>

# Test the API

You can change the value of the variables ```method``` and ```column``` in test_api.py to test the API features. <br>
Then in a new terminal run: ```python3 test_api.py```

