from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def visitors():
	counter_read_file = open("count.txt", "r")
	count_visitors = int(counter_read_file.read())
	counter_read_file.close()

	count_visitors = count_visitors + 1

	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(count_visitors))
	counter_write_file.close()
	
	return render_template("index.html", count = count_visitors)

@app.route("/", methods = ["POST"])
def covid_stats():
	counter_read_file = open("count.txt", "r")
	count_visitors = int(counter_read_file.read())
	counter_read_file.close()

	country_code = request.form['text']



	country_stats = "https://covidstats-sdbd.onrender.com/?country=" + country_code
	print(country_stats)

	return render_template("index.html", count = count_visitors, image = country_stats)

if __name__ == "__main__": 
	app.run()