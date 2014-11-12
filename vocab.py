#  -*- coding: UTF-8 -*-
#
# vocab.py
#   -- vocabulary for the SproBot

import random

TASTE = [
    'citrus', 'lemon', 'lemonade', 'lime', 'grapefruit', 'clementine', 'tangerine',
    'mandarin orange', 'orange', 'pear', 'green apple', 'red apple', 'melon', 'watermelon',
    'honeydew', 'cantaloupe', 'grape', 'white grape', 'green grape', 'red grape', 'concord grape',
    'tropical fruit', 'lychee', 'star fruit', 'tamarind', 'passion fruit', 'pineapple', 'mango',
    'papaya', 'kiwi', 'banana', 'coconut', 'stone fruit', 'peach', 'nectarine', 'apricot', 'plum',
    'cherry', 'black cherry', 'berry', 'cranberry', 'raspberry', 'strawberry', 'blueberry',
    'red currant', 'black currant', 'dried fruit', 'golden raisin', 'raisin', 'dried fig',
    'dried dates', 'prune', 'chocolate', 'cacao nibs', 'dark chocolate', "baker's chocolate",
    'bittersweet chocolate', 'cocoa powder', 'milk chocolate', 'sugar', 'vanilla', 'nougat',
    'honey', 'butter', 'cream', 'marshmallow', 'sugar cane', 'brown sugar', 'caramel',
    'maple syrup', 'molasses', 'cola', 'nut', 'almond', 'hazlenut', 'pecan', 'cashew', 'peanut',
    'walnut', 'grains', 'fresh bread', 'barley', 'wheat', 'rye', 'graham cracker', 'granola',
    'sweet bread pastry', 'carbon', 'smokey', 'burnt sugar', 'toast', 'spice', 'cloves',
    'licorice-anise', 'curry', 'nutmeg', 'ginger', 'coriander', 'cinnamon', 'white pepper',
    'black pepper', 'tomato', 'sundried tomato', 'soy sauce', 'meat', 'leather', 'soil', 'earth',
    'bergamot', 'hops', 'black tea', 'green tea', 'mint', 'sage', 'dill', 'grass', 'snow pea',
    'sweet pea', 'mushroom', 'squash', 'green pepper', 'olive', 'greens', 'straw', 'tobacco',
    'cedar', 'fresh wood', 'flowers', 'lemongrass', 'orange blossom', 'jasmine', 'honeysuckle',
    'magnolia', 'lavender', 'rose hips', 'hibiscus', 'mold', 'phenolic', 'iodine', 'band-aid',
    'rubber', 'medicinal', 'chlorine', 'musty', 'mildew', 'potato', 'raw potato', 'paper',
    'dried wood', 'stale bread', 'cardboard', 'wood smoke', 'diesel', 'turpentine', 'baggy',
    'ash', 'fishy', 'unsweet peas', 'unsweet grain', 'stale grain', 'raw nut', 'decomposing fruit',
    'sour', 'old wine', 'funk', 'garbage', 'animal hide', 'compost', 'vinegar', 'gamey', 'rot',
    'terror', 'love', 'ennui', 'death', 'privilege', 'freedom', 'rainbow', 'unicorn', 'starfield',
    'sunbeam', 'daylight', 'night', 'moonbeam', 'beach at midnight', 'hidden forest glade',
    'way forward', 'the past', 'springtime', 'summer', 'late summer', 'winter', 'winter snow',
    'ice on the windows', 'dust',
]

BODY = [
    'watery', 'tea-like', 'silky', 'slick', 'juicy', 'smooth', '2%', 'syrupy', 'round', 'creamy',
    'full', 'velvety', 'big', 'chewy', 'coating', 'thick', 'sticky', 'fat', 'skinny', 'crunchy',
    'chewy', 'furry', 'fuzzy', 'bald', 'rough', 'chalky',
]

OBJ = [
    'bean', 'coffee', 'selection', 'roast', 'cup'
]


MODIFIER = [
    'crisp', 'bright', 'vibrant', 'tart', 'wild', 'unbalanced', 'sharp', 'pointed', 'dense',
    'deep', 'complex', 'juicy', 'lingering', 'dirty', 'muted', 'dull', 'mild', 'structured',
    'balanced', 'rounded', 'soft', 'faint', 'delicate', 'dry', 'astringent', 'quick', 'clean',
    'lively', 'funky', 'jazzy', 'classic', 'traditional', 'modern', 'surprising', 'daring',
    'explosive', 'massive', 'epic', 'really pretty good', 'pretty good', 'satisfying',
    'fine', 'great', 'the best', 'new', 'nice', 'important', 'wonderous', 'superlative',
    'lovely', 'epic', 'hardcore', 'dreamy', 'awesome', 'delicious', 'transcendent', 'killer',
    'suggestive', 'coy', 'lying', 'tricky', 'simple', 'clear', 'transparent', 'ironic',
    'self-aware'
]

PHRASE = [
    "this {obj} brings promise of a {modifier} {taste}",
    "{modifier} {taste} and {body} body",
    "{body}, {body} {taste} highlights this {modifier} {obj}",
    "the attentive will find pleasure in the {taste} aroma",
    "{taste} upfront and {modifier} {taste} on the back end",
    "a favourite {obj} this year",
    "{body} body, {modifier} taste",
    "the most {modifier} example of a {modifier} {obj} SproBot experienced this season",
    "a {modifier} {obj} full of {modifier} {taste}",
    "{taste} and {taste} mingled with {taste}",
    "{modifier}, {modifier} {taste} notes",
    "{modifier} {taste} abounds in this {modifier} {obj}",
    "{taste} all day",
    "{modifier}",
    "{taste}",
    "{taste} vs {taste}",
    "{taste} yields to {taste}",
    "{taste} yields to {modifier} {taste}",
    "{modifier} {taste} yields to {modifier} {taste}",
    "{body} body cools to {body}",
    "notes of {taste} and {taste}",
    "{taste} on top of {taste}",
    "{modifier} {taste} on the tongue",
    "{modifier} mouthfeel",
    "{taste} in the nose and {taste} on the tongue",
    "{taste} aromas",
    "aromas of {taste}, {taste} and {taste}"
    "{modifier} {taste} nose",
    "{taste} in the streets, {taste} in the sheets",
    "SproBot loves this {obj}",
    "SproBot wants more",
    "SproBot recommends this",
    "SproBot cannot compute this {obj}",
    "SproBot drinks this so you don't have to",
    "SproBot doesn't even"
]

EXCLAMATION = [
    'wow', 'wowza', 'yeeow', 'woo', 'woohoo', 'oh my', 'my goodness', 'sweet', 'sweeeet', 'super',
    'superb', 'remarkable', 'stunning', 'oh yes', 'could you not',
]

PUNCTUATION = ['!', '.']

FIRST_NAME = {
    'latin': [
        'Santiago', 'Sebastián', 'Matías', 'Mateo', 'Nicolás', 'Alejandro', 'Diego', 'Samuel',
        'Benjamín', 'Daniel', 'Joaquín', 'Lucas', 'Tomas', 'Gabriel', 'Martín', 'David', 'Emiliano',
        'Jerónimo', 'Emmanuel', 'Agustín', 'Juan Pablo', 'Juan José', 'Andrés', 'Thiago', 'Leonardo',
        'Felipe', 'Ángel', 'Maximiliano', 'Christopher', 'Juan Diego', 'Adrián', 'Pablo',
        'Miguel Ángel', 'Rodrigo', 'Alexander', 'Ignacio', 'Emilio', 'Dylan', 'Bruno', 'Carlos',
        'Vicente', 'Valentino', 'Santino', 'Julián', 'Juan Sebastián', 'Aarón', 'Lautaro', 'Axel',
        'Fernando', 'Ian', 'Christian', 'Javier', 'Manuel', 'Luciano', 'Francisco', 'Juan David',
        'Iker', 'Facundo', 'Rafael', 'Alex', 'Franco', 'Antonio', 'Luis', 'Isaac', 'Máximo', 'Pedro',
        'Ricardo', 'Sergio', 'Eduardo', 'Bautista', 'Miguel', 'Cristóbal', 'Kevin', 'Jorge', 'Alonso',
        'Anthony', 'Simón', 'Juan', 'Joshua', 'Diego Alejandro', 'Juan Manuel', 'Mario', 'Alan',
        'Josué', 'Gael', 'Hugo', 'Matthew', 'Ivan', 'Damián', 'Lorenzo', 'Juan Martín', 'Esteban',
        'Álvaro', 'Valentín', 'Dante', 'Jacobo', 'Jesús', 'Camilo', 'Juan Esteban', 'Elías',
    ],
    'ethiopian': [
        'Abebe', 'Abeba', 'Addisu', 'Adanech', 'Abel', 'Alemnesh', 'Adunga', 'Adia', 'Aman',
        'Ayana', 'Afewerek', 'Aster', 'Bayissa', 'Beimnet', 'Beca', 'Beshadu', 'Biniam', 'Biftu',
        'Berhanu', 'Bisrat', 'Bruk', 'Brukawit', 'Caleb', 'Candace', 'Dagim', 'Dagamawit',
        'Daniel', 'Deborah', 'Desta', 'Dinha', 'Dawit', 'Dorcas', 'Dula', 'Eddel', 'Ejigu',
        'Eden', 'Eleazar', 'Edna', 'Elias', 'Elene', 'Emanuel', 'Elshaday', 'Etefu', 'Emebet',
        'Eyasu', 'Emnet', 'Ezana', 'Enku', 'Ezera', 'Eskedare', 'Fassil', 'Feker', 'Fasika',
        'Filagot', 'Frew', 'Freaulai', 'Fisha', 'Frezer', 'Fikre', 'Gadise', 'Gabra', 'Gelila',
        'Gedeyon', 'Genet', 'Getachew', 'Gete', 'Girma', 'Giftee', 'Gulema', 'Hanna', 'Habtamu',
        'Haimanot', 'Hakim', 'Hosanna', 'Hassan', 'Ibsituu', 'Iskinder', 'Jalene', 'Jember',
        'Kalkidan', 'Kabede', 'Kidist', 'Ketema', 'Konjit', 'Legesse', 'Layla', 'Lemma', 'Lielit',
        'Lire', 'Makda', 'Mamo', 'Mare', 'Mebrete', 'Martha', 'Mekonnen', 'Mehret', 'Meles', 'Mimi',
        'Mulu', 'Naomi', 'Nebiyou', 'Nigat', 'Neguse', 'Persinna', 'Palus', 'Rachel', 'Rada',
        'Rekik', 'Ruphael', 'Rediet', 'Samuel', 'Saba', 'Sebhat', 'Sebele', 'Selassie', 'Selam',
        'Shale', 'Semira', 'Solomon', 'Tadelech', 'Taddese', 'Tarik', 'Tamrat', 'Teru', 'Temesgen',
        'Tigist', 'Temesgen', 'Tsigereda', 'Tesfaye', 'Wubit', 'Workneh', 'Yehudit', 'Yeakob',
        'Yohanna', 'Yohannes', 'Zahra', 'Zere', 'Zenaye', 'Zewedu'
    ],
    'kenyan': [
        'Abasi', 'Abbo', 'Abdalla', 'Abdu', 'Adhama', 'Adia', 'Afiya', 'Aisha', 'Aishia', 'Akina',
        'Aleela', 'Aluna', 'Amana', 'Amani', 'Amanika', 'Anasa', 'Andaiye', 'Angalia', 'Arusi',
        'Ashante', 'Ashanti', 'Ashon', 'Ashonti', 'Ashura', 'Asya', 'Atiena', 'Atieno', 'Ayah',
        'Ayo', 'Ayubu', 'Azima', 'Azizi', 'Badru', 'Bahati', 'Bakari', 'Baraka', 'Barasa', 'Barika',
        'Bavana', 'Bayana', 'Bayinika', 'Beno', 'Budhya', 'Busar', 'Busara', 'Bwana Mkubwa',
        'Chagina', 'Chane', 'Chanua', 'Chiku', 'Chilemba', 'Chinira', 'Chitundu', 'Chriki',
        'Dafina', 'Dalia', 'Dalila', 'Darweshi', 'Daudi', 'Dhamiria', 'Dinka', 'Duma', 'Elea',
        'Elewa', 'Elim', 'Elimisha', 'Endana', 'Endelea', 'Fanaka', 'Fanaka', 'Faraji', 'Farijika',
        'Fatuma', 'Fikira', 'Gethera', 'Goma', 'Habib', 'Hadiya', 'Hali', 'Halina', 'Halisi',
        'Hamidi', 'Hamisi', 'Hanif', 'Haoniyao', 'Haoniyao', 'Hasana', 'Hasanati', 'Hasina', 'Hawa',
        'Heshima', 'Himaya', 'Hodari', 'Huseina', 'Ikeno', 'Imani', 'Imara', 'Imarisha', 'Inira',
        'Inithia', 'Issa', 'Issa', 'Itanya', 'Jafari', 'Jaha', 'Jahaira', 'Jama', 'Jamaa', 'Jamal',
        'Jamani', 'Jamba', 'Jamba', 'Jata', 'Jehlani', 'Jela', 'Jina', 'Jina', 'Jiona', 'Julisha',
        'Juma', 'Jumaane', 'Kakena', 'Kalere', 'Kaluwa', 'Kamara', 'Kamari', 'Kamaria', 'Kanene',
        'Kanika', 'Kanisa', 'Karama', 'Keambiroiro', 'Keanjaho', 'Kenithia', 'Kenura', 'Kereenyaga',
        'Kesi', 'Khadija', 'Khalfani', 'Kiama', 'Kiania', 'Kibibi', 'Kichea', 'Kifeda', 'Kiira',
        'Kiira', 'Kijakazi', 'Kilinda', 'Kinaya', 'Kinjia', 'Kito', 'Kito', 'Kitwana', 'Kobe',
        'Koffi', 'Koman', 'Kudio', 'Kuende', 'Kuende', 'Kwanzaa', 'Kwashi', 'Lindana', 'Lindia',
        'Lisha', 'Madaadi', 'Madini', 'Mahiri', 'Majda', 'Maji', 'Majida', 'Malika', 'Maliza',
        'Malkia', 'Maridhia', 'Marijani', 'Marini', 'Mashika', 'Masika', 'Maskini', 'Maulidi',
        'Maulidi', 'Mbita', 'Mhina', 'Milima', 'Mkiwa', 'Mosi', 'Moyo', 'Mpenda', 'Mshindi',
    ],
    'indonesia': [
        'Ade', 'Adi', 'Agus', 'Ari', 'Bambang', 'Benny', 'Budi', 'Deddy', 'Djaja', 'Doddy', 'Hadi',
        'Hadian', 'Hamdani', 'Handoko', 'Hartono', 'Hendra', 'Hendri', 'Hengki', 'Herman', 'Indra',
        'Irwan', 'Ivan', 'Iwan', 'Johan', 'Ridwan', 'Sonny', 'Sudirman', 'Sudomo', 'Sugiarto',
        'Suharto', 'Suhendra', 'Sukarno', 'Suparman', 'Surya', 'Suryadi', 'Susanto', 'Teguh',
        'Yandi', 'Yohanes', 'Ade', 'Devi', 'Dewi', 'Erlin', 'Fanny', 'Farida', 'Glenna', 'Harjanti',
        'Hartanti', 'Ida', 'Inge', 'Lanny', 'Leony', 'Liana', 'Liani', 'Ratna', 'Shinta', 'Siska',
        'Sri', 'Sucianty', 'Susanti', 'Utami', 'Vera', 'Verawati', 'Veronika', 'Widya', 'Widyawati',
        'Yanti', 'Yenny', 'Yulia', 'Yuliana', 'Yuliani',
    ],
    'tanzania': [
        'Aadila', 'Aailyah', 'Abasi', 'Abiria', 'Adhra', 'Adika', 'Adila', 'Adimu', 'Adin', 'Adla',
        'Adli', 'Afaafa', 'Afifa', 'Afifah', 'Afiya', 'Afrika', 'Afua', 'Afya', 'Ahadi', 'Aida',
        'Ainra', 'Ajabu', 'Ajali', 'Ajia', 'Akida', 'Akila', 'Akilah', 'Akili', 'Akuji', 'Alama',
        'Alamisi', 'Alasiri', 'Alfajiri', 'Aliya', 'Almasi', 'Amali', 'Amana', 'Amaziah', 'Ambakisye',
        'Ambata', 'Ambidwile', 'Ambilikile', 'Ambokile', 'Ambonisye', 'Amina', 'Aminah', 'Aminali',
        'Aminifu', 'Amira', 'Amiri', 'Amri', 'Andalwisye', 'Andengwisye', 'Andongwisye', 'Andwele',
        'Aneesa', 'Anga', 'Angaza', 'Angolwisye', 'Angosisye', 'Anisa', 'Anisun', 'Anyabwile',
        'Anyelwiswe', 'Anza', 'Aoko', 'Arafa', 'Arifa', 'Asani', 'Asante', 'Asatira', 'Asha',
        'Ashura', 'Asili', 'Asilia', 'Asiya', 'Asma', 'Asmahani', 'Asubuhi', 'Asukile',
        'Asumini', 'Asya', 'Atiya', 'Auni', 'Awena', 'Aza', 'Azima', 'Aziza', 'Azize', 'Azizi',
        'Babu', 'Badriya', 'Bahari', 'Bahati', 'Bahiya', 'Bali', 'Balozi', 'Bamba', 'Banji',
        'Baraka', 'Barke', 'Basha', 'Bashira', 'Basma', 'Baya', 'Bia', 'Bibi', 'Binti', 'Bishara',
        'Bonde', 'Bora', 'Bupe', 'Buruji', 'Busara', 'Bushira', 'Busu', 'Buyu', 'Chausiku', 'Chiku',
        'Chuki', 'Dabiku', 'Dafina', 'Dalila', 'Dalili', 'Darweshi', 'Dhakiya', 'Ducha', 'Duni',
        'Durah', 'Durra', 'Eidi', 'Elimu', 'Endesha', 'Enzi', 'Erevu', 'Eshe', 'Etana', 'Fadhila',
        'Fadhili', 'Fadiya', 'Fahamu', 'Fahari', 'Fahima', 'Fahimah', 'Faida', 'Faika', 'Faiza',
        'Faizah', 'Fanaka', 'Fanana', 'Faraja', 'Faraji', 'Farashuu', 'Farasi', 'Farida', 'Fathiya',
        'Fatima', 'Fatimah', 'Feruzi', 'Fila', 'Firyali', 'Furaha', 'Gasira', 'Gheche', 'Ghubari',
        'Habeebah', 'Habiba', 'Habibah', 'Hadhi', 'Hadithi', 'Hadiya', 'Hafidha', 'Hafsa', 'Hafsah',
        'Haiba', 'Haji', 'Haki', 'Hakima', 'Hala', 'Halili', 'Halima', 'Halisi', 'Hamida', 'Hanaa',
        'Hanifa', 'Hanuni', 'Hasa', 'Hashiki', 'Hasnaa', 'Hawa', 'Hawla', 'Haya', 'Hazina', 'Hiari',
        'Hiba', 'Hidaya', 'Ibada', 'Ibtisam', 'Idi', 'Idili',
    ],
    'rwanda': [
        'Akaliza', 'Amahoro', 'Garuka', 'Iragena', 'Iribagiza', 'Isaro', 'Ingabire', 'Kampire',
        'Keza', 'Mitaako', 'Mugwaneza', 'Mujjawimana', 'Mukobwajana', 'Mulekatete', 'Mushikiwabo',
        'Mutesi', 'Mutoni', 'Neza', 'Niyonyugura', 'Nkurunziza', 'Uwamahoro', 'Uwimbabazi', 'Uwase',
        'Gahigi', 'Gasimba', 'Gasore', 'Gatete', 'Habimana', 'Hakizimana', 'Mazimpaka', 'Mihigo',
        'Mugabo', 'Mugisha', 'Mugwaneza', 'Munezero', 'Munyentwali', 'Mutanguha', 'Ngabo',
        'Ndengeyingoma', 'Nsengiyumva', 'Nshimiye', 'Ntwali', 'Rusanganwa', 'Siboyintore',
    ],

}
FIRST_NAME['papua new guinea'] = FIRST_NAME['indonesia']
FIRST_NAME['sumatra'] = FIRST_NAME['indonesia']


SURNAME = {
    'latin': [
        'GARCIA', 'RODRIGUEZ', 'MARTINEZ', 'HERNANDEZ', 'LOPEZ', 'GONZALEZ', 'PEREZ', 'SANCHEZ',
        'RAMIREZ', 'TORRES', 'FLORES', 'RIVERA', 'GOMEZ', 'DIAZ', 'REYES', 'MORALES', 'CRUZ',
        'ORTIZ', 'GUTIERREZ', 'CHAVEZ', 'RAMOS', 'GONZALES', 'RUIZ', 'ALVAREZ', 'MENDOZA',
        'VASQUEZ', 'CASTILLO', 'JIMENEZ', 'MORENO', 'ROMERO', 'HERRERA', 'MEDINA', 'AGUILAR',
        'GARZA', 'CASTRO', 'VARGAS', 'FERNANDEZ', 'GUZMAN', 'MUNOZ', 'MENDEZ', 'SALAZAR', 'SOTO',
        'DELGADO', 'PENA', 'RIOS', 'ALVARADO', 'SANDOVAL', 'CONTRERAS', 'VALDEZ', 'GUERRERO',
        'ORTEGA', 'ESTRADA', 'NUNEZ', 'MALDONADO', 'VEGA', 'VAZQUEZ', 'SANTIAGO', 'DOMINGUEZ',
        'ESPINOZA', 'SILVA', 'PADILLA', 'MARQUEZ', 'CORTEZ', 'ROJAS', 'ACOSTA', 'FIGUEROA', 'LUNA',
        'JUAREZ', 'NAVARRO', 'CAMPOS', 'MOLINA', 'AVILA', 'AYALA', 'MEJIA', 'CARRILLO', 'DURAN',
        'SANTOS', 'SALINAS', 'ROBLES', 'SOLIS', 'LARA', 'CERVANTES', 'AGUIRRE', 'DELEON', 'OCHOA',
        'MIRANDA', 'CARDENAS', 'TRUJILLO', 'VELASQUEZ', 'FUENTES', 'CABRERA', 'LEON', 'RIVAS',
        'MONTOYA', 'CALDERON', 'COLON', 'SERRANO', 'GALLEGOS', 'ROSALES', 'CASTANEDA',
    ],
    'ethiopian': FIRST_NAME['ethiopian'],
    'kenyan': [
        "Agina", "Adida", "Obong'o", "Abong'o", "Ahenda", "Obama", "Obiero", "Abiero", "Obonyo",
        "Abonyo", "Obura", "Abura", "Oburu", "Aburu", "Obuo", "Abuo", "Ochanda", "Ochieng’",
        "Achieng’", "Ochola", "Achola", "Ochuka", "Achuka", "Odede", "Adede", "Odero", "Adero",
        "Odhiambo", "Adhiambo", "Odhon’g", "Adhon’g", "Odek", "Odika", "Adika", "Odinga", "Odiwuor",
        "Adiwuor", "Odondi", "Adondi", "Odongo", "Adongo", "Odoyo", "Adoyo", "Oduol", "Aduol",
        "Oero", "Aero", "Ogola", "Ogol", "Ogolo", "Ogot", "Agot", "Ogutu", "Agutu", "Oigo", "Aigo",
        "Ojuok", "Okelo", "Akelo", "Okech", "Akech", "Okeyo", "Akeyo", "Okinyi", "Akinyi", "Okombo",
        "Akombo", "Okomo", "Akomo", "Okongo", "Akongo", "Okoth", "Akoth", "Okumu", "Akumu",
        "Okungu", "Akungu", "Oloo", "Aloo", "Oludhe", "Aludhe", "Oluoch", "Aluoch", "Omolo",
        "Amolo", "Omole", "Omondi", "Aondi", "Okoka", "Anoka", "Ondiek", "Oneko", "Aneko",
        "Ong’ina", "Ang’ina", "Ongonga", "Angonga", "Onyango", "Anyango", "Ooko", "Aoko",
        "Ooro", "Aoro", "Opiyo", "Apiyo", "Opolo", "Apolo", "Opondo", "Apondo", "Osano", "Otieno",
        "Atieno", "Otiende", "Atiende", "Ouma", "Auma", "Owino", "Awino", "Ounda", "Owiti", "Awiti",
        "Owuor", "Awuo",
    ],
    'tanzania': [
        'Nyondo', 'Muyila', 'Kalagho', 'Malokotela', 'Sibale', 'Chizimu', 'Kayuni', 'Simengwa',
        'Kapesa', 'Munkhodya', 'Panja'
    ],
}

REGION = {
    'latin': [
        'columbia', 'mexico', 'peru', 'guatemala', 'el salvador', 'honduras',
        'costa rica', 'nicaragua', 'bolivia', 'panama',
    ],
    'ethiopian': [
        'ethiopia', 'ethiopia harar', 'ethiopia yrgacheffe', 'ethiopia limu',
    ],
    'kenyan': [
        'kenya', 'kenya ruiri', 'kenya thika', 'kenya kirinyaga', 'mt. kenya west',
        'kenya nyeri', 'kenya kiambu', 'kenya muranga',
    ],
    'indonesia': ['flores', 'java', 'sumbawa', 'papua new guinea', 'sulawesi'],
    'papua new guinea': ['papua new guinea'],
    'rwanda': ['rwanda', 'rwanda maraba'],
    'tanzania': ['tanzania'],
    'sumatra': ['sumatra mandehling', 'sumatra lintong', 'sumatra gayo'],
}

VARIETY = [
    'arusha', 'bergendal', 'sidikalang', 'jamaican blue mountain', 'bourbon', 'catuai', 'caturra',
    'charrieriana', 'french mission', 'geisha', 'guadeloupe bonifieur', 'hawaiian kona', 'java',
    'kenya K7', 'maragogype', 'mayagüez', 'yemeni mocha', 'mundo novo', 'orange burbon',
    'yellow burbon', 'red burbon', 'pacamera', 'paca', 'pache collis', 'pache comum', 's795',
    'brazil santos', 'sarchimor', 'SL28', 'SL34', 'S795', 'timor', 'arabusta', 'typica',
    'monsoon malabar'
]

VARIETY_MODIFIER = [
    'AA', 'AAA', 'Microlot', 'Peaberry'
]

# return a random phrase template
template = lambda: random.choice(PHRASE)

# return a random exclamation
extra = lambda: random.choice(EXCLAMATION).capitalize()

# return random punctuation
punctuation = lambda: random.choice(PUNCTUATION)

# return a random variety
variety = lambda: random.choice(VARIETY).title()

# return a random variety modifier
variety_modifier = lambda: random.choice(VARIETY_MODIFIER)

# return a random region for a given key, if one exists
region = lambda x: random.choice(REGION[x]).title() if x in REGION else ''

# return a random first name for a given key, if one exists
first_name = lambda x: random.choice(FIRST_NAME[x]).title() if x in FIRST_NAME else ''

# return a random surname for a given key, if one exists
surname = lambda x: random.choice(SURNAME[x]).title() if x in SURNAME else ''

# return a random word of a given type; used to resolve phrase template format strings.
word = {
    'obj': lambda: random.choice(OBJ),
    'modifier': lambda: random.choice(MODIFIER),
    'taste': lambda: random.choice(TASTE),
    'body': lambda: random.choice(BODY),
}
