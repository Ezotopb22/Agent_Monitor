from flask import Flask, request
import json
app = Flask(__name__)





#route to /register_agent page and listen to POST request.
@app.route("/register_agent", methods=['POST'])
#Define register_agent() function in this page
def register_agent():
    #reg_data will be at json format
    req_data = json.loads(request.data)
    lk = req_data['license_key']
    # validate license key
    #Open the file "license" file and input to f
    with open('licenses') as f:
        #Read all line in f.
        for line in f:
          # check if lk is present in line
            if lk in line:
                #If yes, POST 200.
                return "Agent is registerd", 200
        #If not POST 500
        return "Agent is not registerd", 500

if __name__ == "__main__":
    app.run(port=5000)          #Flask port

