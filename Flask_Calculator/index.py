from flask import Flask, render_template, url_for,request
app = Flask(__name__)
# route == link == url

# main route
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate", methods = ["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    if operation == "plus":
        result = first_number + second_number
        return render_template("simple.html", result=result)
    elif operation == "minus":
        result = first_number - second_number
        return render_template("simple.html", result=result)
    elif operation == "multiply":
        result = first_number * second_number
        return render_template("simple.html", result=result)
    elif operation == "divide":
        result = first_number / second_number
        return render_template("simple.html", result=result)
    else:
        return "There is an Error!"


if __name__ == "__main__":
    app.run(debug=True)