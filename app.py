from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('Ayurveda.csv')


symptoms = df['Symptoms'].unique().tolist()
herbs = df['Herbs_ID'].unique().tolist()


herb_names = {
    1: "Agastya",
    2: "Amalaki",
    3: "Amruta-phalam",
    4: "Apamarga",
    5: "Aparajita",
    6: "Aragavadha",
    7: "Ardraka",
    8: "Arishtaka",
    9: "Arjuna",
    10: "Ashoka",
    11: "Asthisamharaka",
    12: "Asvagandha",
    13: "Asvattha",
    14: "Atasi",
    15: "Atmagupta",
    16: "Avartani",
    17: "Bhringaraja",
    18: "Bhumyamlaki",
    19: "Bibhitaka",
    20: "Bilva",
    21: "Bimbi",
    22: "Brahmi",
    23: "Changeri",
    24: "Chitraka",
    25: "Dadima",
    26: "Dhanyaka",
    27: "Dronapushpi",
    28: "Dugdhika",
    29: "Durva",
    30: "Edagaja",
    31: "Eranda",
    32: "Erandakarkati",
    33: "Gokshura",
    34: "Guduchi",
    35: "Gunja",
    36: "Haridra",
    37: "Haritaki",
    38: "Harita manjari",
    39: "Hingu",
    40: "Indravalli",
    41: "Indravaruni",
    42: "Isvari",
    43: "Jalapippali",
    44: "Jambu",
    45: "Japa",
    46: "Jatiphala",
    47: "Jiraka",
    48: "Kadali",
    49: "Kalamegha",
    50: "Kamala",
    51: "Kanchanara",
    52: "Karanja",
    53: "Karavellaka",
    54: "Karpura",
    55: "Katuka",
    56: "Kharjura",
    57: "Khaskhasa",
    58: "Krishna musali (talamuli)",
    59: "Kulanjana (rasna variety)",
    60: "Kuluttha",
    61: "Kumari",
    62: "Kumkuma",
    63: "Kutaja",
    64: "Lajjalu",
    65: "Lashuna",
    66: "Lavanga",
    67: "Madayanti",
    68: "Manjishta",
    69: "Maricha",
    70: "Masha",
    71: "Meshashringi",
    72: "Methi",
    73: "Mishreya",
    74: "Mulaka",
    75: "Mundi",
    76: "Musta",
    77: "Nagakesara",
    78: "Nagavalli",
    79: "Narikela",
    80: "Nimba",
    81: "Nirgundi",
    82: "Palandu",
    83: "Palasha",
    84: "Parisha (kapitana)",
    85: "Parnabija",
    86: "Parnayavani",
    87: "Pippali",
    88: "Punarnava",
    89: "Rajaudumbara",
    90: "Sadapushpa",
    91: "Sariva",
    92: "Sarshapa",
    93: "Satavari",
    94: "Satyanashi",
    95: "Saurabhanimba",
    96: "Shigru",
    97: "Sukshmaila",
    98: "Svetachandana",
    99: "Thakkolam",
    100: "Tila",
    101: "Tulasi",
    102: "Tvak",
    103: "Tvakpatra",
    104: "Vacha",
    105: "Vasa",
    106: "Vatama",
    107: "Yashtimadhu",
    108: "Yavani"
}


@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms, herb_ids=herbs)

@app.route('/get_medicine', methods=['POST'])
def get_medicine():
    data = request.get_json()
    symptom = data['symptom']
    herb_id = int(data['herb_id'])
    
    result = df[(df['Symptoms'] == symptom) & (df['Herbs_ID'] == herb_id)]
    
    if not result.empty:
        formulation = result['Formulation'].values[0]
        herb_name = herb_names.get(herb_id, 'Unknown Herb')
        return jsonify({'formulation': formulation, 'herb_name': herb_name})
    
    return jsonify({'formulation': 'No match found', 'herb_name': ''})

if __name__ == '__main__':
    app.run(debug=True)
