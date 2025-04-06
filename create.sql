create TABLE IncomeGroup(
  incomegroup varchar(50) primary key
);

create TABLE Region(
  region varchar(50) primary key
);

create TABLE Country(
    country varchar(50) unique,
    country_code varchar(3) primary key,
    region varchar(50),
    incomegroup varchar(50),
    foreign key(region) references Region(region),
    foreign key (incomegroup) references IncomeGroup(incomegroup)
);

create table Year(
    year integer check (year > 0) primary key
);

create table University(
    iau_id1 varchar(50) primary key,
    eng_name varchar not null,
    orig_name varchar not null,
    private01 bit not null,
    latitude float,
    longitude float,
    specialized bit not null,
    divisions integer,
    phd_granting bit not null,
    country_code varchar(3) not null,
    foreign key (country_code) references Country(country_code),
    foundedyr integer not null,
    foreign key (foundedyr) references Year(year),
    yrclosed integer,
    foreign key (yrclosed) references Year(year)
);

create table GotIn(
    year integer,
    foreign key (year) references Year(year),
    iau_id1 varchar(50),
    foreign key (iau_id1) references University(iau_id1),
    student5_est integer
);

