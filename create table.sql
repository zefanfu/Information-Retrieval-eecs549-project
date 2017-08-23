create table restaurant
(
    neighborhood char(255),
    business_id char(255) not null primary key,
    hours text,
    is_open int,
    address text,
    attributes text,
    categories text,
    city char(255),
    review_count int,
    name char(255),
    longitude double,
    state char(5),
    stars double,
    latitude double,
    postal_code char(30),
    type char(30)
);

neighborhood,business_id,hours,is_open,address,attributes,categories,city,review_count,name,longitude,state,stars double,latitude,postal_code,type

mysqlimport --fields-terminated-by=, --columns='neighborhood,business_id,hours,is_open,address,attributes,categories,city,review_count,name,longitude,state,stars,latitude,postal_code,type' --local -u root -p trippal /home/fuzzy/650/project/restaurant.csv

