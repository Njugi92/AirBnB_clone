0x00. AirBnB clone - The console

/tmp/65f4a1dd9c51265f49d0.png

/tmp/815046647d23428a14ca-1.png

Description:
irBnB is a complete web application complising of database storage, a back-end API and a front-end interface. The project currently impliments the back-end console.

<<<<<<< HEAD
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.
=======
Classes:
HolbertonBnB uses the following classes:
	-> BaseModel - It is the base class which entails all common attributes/	   methods for other classes.
	-> FileStorage - It is an implimentation of JSON file which act as a dat	   abase for the entire AirBnB project.
	-> Other classes that inherit from BaseModel class are, User, State, Cit	   y, Amenity and Place.
Console: This is command line interplater that allows management of back-end of AirBnB.

Using the console:
To run console in non-interactive mode, pipe any command into an excecution of the file console.py at command line
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$

Other way is to run AirBnB interactively through running the file console.py itself.

$ ./console.py

When running in interactive mode, console display prompt for input:

$ ./console.py
(hbnb)

To exit the console enter command quit, or input EOF signal (ctrl-D)

$ ./console.py
(hbnb) quit
$

$ ./console.py
(hbnb) EOF
$

The AirBnB console supports the following commands:
-> create
	- Usage: create <class>
This creates a new instance of a given class. Class ID is printed and instance saved to file.json

$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}

-> Show
	- Usage: show <class> <id> or <class>.show(<id>)
It prints the string representation of a class instance based on a given ID

$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)

-> Destroy
	- Usage: destroy <class> <id> or <class>.destroy(<id>)
Deletes a class instance based on a given id. The storage file.json is updated

$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) create Place
3e-8329-4f47-9947-dca80c03d3ed
(hbnb)
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
(hbnb) quit
$ cat file.json ; echo ""
{}

-> all
	- Usage: all or all <class> or <class>.all()
Prints the string representation of all instances of a given class. If no class name provided the command prints all instances of every class.

$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User]
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb)
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)

-> count
	- Usage:update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).

It updates a class instance based on given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only 'simple ' attributes can be updated but not: id, created_at, updated_at. However any attribute can be updated by providing a dictionary.

$ ./console.py
(hbnb) create User
6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
t")
(hbnb) User.show(6f348019-0499-420f-8eec-ef0fdc863c02)
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'address': '98 Mission St', 'first_name': 'Ho
lberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id
': '6f348019-0499-420f-8eec-ef0fdc863c02'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, {'email': 'holberton@h
olberton.com', 'last_name': 'School'})
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'email': 'holberton@holberton.co
m', 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21,
54, 39, 234382), 'address': '98 Mission St', 'last_name': 'School', 'id': '6f34
8019-0499-420f-8eec-ef0fdc863c02', 'created_at': datetime.datetime(2019, 2, 17,
21, 54, 39, 234382)}
(hbnb)

Testing:
Unittest for AirBnB project are defined in the tests directory. To run the entire tests excecute the following commands:

$ python3 unittest -m discover tests
>>>>>>> 9554aefc83322426ca9857d8ce06c9a4ef60d145
