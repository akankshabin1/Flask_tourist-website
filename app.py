from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Data for famous places in and around Bangalore, categorized
categories = {
    "Fun Activity Places": [
        "Wonderla", 
        "Innovative Film City", 
        "Snow City", 
        "Fun World", 
        "Guhantara Resort",
        "Play Arena", 
        "The Mystery Rooms", 
        "Escape Hunt", 
        "Pondicherry Beach", 
        "Xtreme Zone"
    ],
    "Historical Places": [
        "Bangalore Palace", 
        "Tipu Sultan's Summer Palace", 
        "Nandi Hills", 
        "Devanahalli Fort", 
        "Someshwara Temple",
        "Ramanagara Fort", 
        "Chikkajala Fort", 
        "Hesaraghatta Lake", 
        "Bull Temple", 
        "Jama Masjid"
    ],
    "Gardens and Parks": [
        "Lalbagh Botanical Garden", 
        "Cubbon Park", 
        "Bannerghatta National Park", 
        "Jayaprakash Narayan Biodiversity Park", 
        "Lumbini Gardens",
        "Hesaraghatta Grasslands", 
        "Kanteerava Indoor Stadium Park", 
        "Botanical Garden", 
        "Bagmane Tech Park", 
        "Nehru Park"
    ],
    "Shopping Places": [
        "Commercial Street", 
        "Brigade Road", 
        "Chickpet Market", 
        "Avenue Road", 
        "MG Road",
        "Russell Market", 
        "Koramangala 5th Block", 
        "Koshy’s", 
        "Sankey Road", 
        "Hosur Road"
    ],
    "Famous Malls": [
        "Orion Mall", 
        "Phoenix Marketcity", 
        "UB City Mall", 
        "Forum Mall", 
        "Mantri Square",
        "Inorbit Mall", 
        "Garuda Mall", 
        "VR Bengaluru", 
        "Elements Mall", 
        "Brigade Gateway"
    ],
    "Restaurants": [
        "Mavalli Tiffin Rooms", 
        "Vidyaranya Bhavan", 
        "Shiro", 
        "Toit Brewpub", 
        "Brahmin's Coffee Bar",
        "The Only Place", 
        "Rim Naam", 
        "Smoke House Deli", 
        "Arbor Brewing Company", 
        "Shao"
    ],
    "Lakes": [
        "Ulsoor Lake", 
        "Hebbal Lake", 
        "Madiwala Lake", 
        "Sankey Tank", 
        "Yelahanka Lake",
        "Bellandur Lake", 
        "Hesaraghatta Lake", 
        "Puttenahalli Lake", 
        "Agara Lake", 
        "Kudlu Lake"
    ],
    "Sprots and Adventure": [
        "Meco Kartopia", 
        "Torq03", 
        "Play Arena", 
        "Red Riders Sports", 
        "Grips Go Karting",
        "Karting King", 
        "Extreme Karting", 
        "Karting Arena", 
        "Racer's Edge", 
        "Race Kart"
    ]
}

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/category/<category_name>')
def category(category_name):
    # Fetch places for the selected category
    places = categories.get(category_name, [])
    return jsonify(places=places)

if __name__ == '__main__':
    app.run(debug=True)
