use trippal
create table museums
(
Museum_ID char(10) not null primary key,
Museum_Name char(100),
Legal_Name char(100),
Alternate_Name char(100),
Museum_Type char(100),
Institution_Name char(100),
Street_Address_A char(100),
City_A char(100),
State_A char(100),
Zip_Code_A char(100),
Street_Address_P char(100),
City_P char(100),
State_P char(100),
Zip_Code_P char(100),
Phone char(100),
Latitude char(100),
Longitude char(100),
Locale_Code char(100),
County_Code char(100),
State_Code char(100),
Region_Code char(100),
Employer_ID char(100),
Tax_Period char(100),
Income char(100),
Revenue char(100)
);
/*
mysqlimport --ignore-lines=1 --fields-terminated-by=, --columns='Museum_ID,Museum_Name,Legal_Name,Alternate_Name,Museum_Type,Institution_Name,Street_Address_A,City_A,State_A,Zip_Code_A,Street_Address_P,City_P,State_P,Zip_Code_P,Phone,Latitude,Longitude,Locale_Code,County_Code,State_Code,Region_Code,Employer_ID,Tax_Period,Income,Revenue' --local -u root -p trippal museums.csv
*/
