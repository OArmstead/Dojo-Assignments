
#Delete the 3 dojos you just created

#Delete From dojos WHERE condition(s)

#Query: Create 3 more dojos

#insert INTO dojos (name)
#Values ('South'),('East')

#Select * from dojos

#INSERT INTO ninjas (first_name, last_name, age, dojos_id)
#VALUES ('James', 'Bond', 43,1 ),('Michael', 'Jackson', 51,1 ),('Franklin', 'Davis', 43,1 )

# Create 3 ninjas that belong to the second dojo

#INSERT INTO ninjas (first_name, last_name, age, dojos_id)
#VALUES ('Bruce', 'Lee', 33,2 ),('Chuck', 'Norris', 50,2 ),('Jet', 'Li', 52,2 )

# Create 3 ninjas that belong to the third dojo
#INSERT INTO ninjas (first_name, last_name, age, dojos_id)
#VALUES ('Randy', 'Savage', 37,3 ),('Brett', 'Hartt', 40,3 ),('Shawn', 'Michaels', 30,3 )

#Select * from ninjas

# Retrieve all the ninjas from the first dojo
#Select * FROM ninjas where dojos_id = 1;

#Retrieve all the ninjas from the last dojo
#Select * From ninjas where dojos_id = 3;

#Retrieve the last ninja's dojo

Select * From dojos
Where dojo.id = (Select dojo_id FROM ninjas Order BY dojo_id DESC Limit 1);
