create table producer
    (
    producer_id varchar(10) primary key,
    companyname varchar(255),
    country varchar(255)
    );

create table movie
    (
    movie_id varchar(10) primary key,
    title varchar(255),
    duration varchar(255),
    rating char(5),
    awardwon varchar(255),
    releasedate varchar(255)
    );

create table customer_movie
    (
    date_rented varchar(255),
    due_date varchar(255),
    rentalID varchar(255) primary key,
    late varchar(255),
    damage varchar(3),
    date_returned varchar(255)
    );
    
create table customer
    (
    customer_id varchar(255) primary key,
    first_name varchar(255),
    last_name varchar(255),
    address varchar(255),
    phone_number varchar(20),
    birthdate varchar(255)
    );

create table distributor
    (
    distributor_id varchar(10) primary key,
    distributor_name varchar(255),
    price decimal,
    stock int
    );
    
create table format
    (
    format_id varchar(255) primary key,
    format_type varchar(255)
    );
    
create table actor
    (
    actor_id varchar(255) primary key,
    actor_firstname varchar(255),
    actor_lastname varchar(255)
    );

create table award
    (
    award_id varchar(255) primary key,
    award_name varchar(255)
    );

