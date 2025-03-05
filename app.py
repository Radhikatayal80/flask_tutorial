from flask import Flask, jsonify

app = Flask(__name__)

class ApiResponse:
    def __init__(self, message, status, data=None):
        self.message = message
        self.status = status
        self.data = data

    def to_dict(self):
        return {
            "message": self.message,
            "status": self.status,
            "data": self.data
        }

    def to_json(self):
        return jsonify(self.to_dict())

@app.route('/api/data')
def get_data():
    data = {"user": "Radhika Tayal", "age": 21, "address": "Greater Noida", "contact":878947488}
    response = ApiResponse("Data retrieved successfully", "success", data)
    return response.to_json()

@app.route('/api/error')
def get_error():
    response = ApiResponse("Something went wrong", "error", None)
    return response.to_json()

if __name__ == '__main__':
    app.run(debug=True)
