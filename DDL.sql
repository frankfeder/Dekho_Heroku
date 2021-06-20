CREATE TABLE CarEngineInfo (
	name VARCHAR(150) NOT NULL,
	selling_price INT,
	km_driven INT,
	fuel VARCHAR(50),
	mileage VARCHAR(100),
	engine VARCHAR(50),
	max_power VARCHAR(100),
	torque VARCHAR (200),
	seats int,
	CONSTRAINT pk_CarEngineInfo PRIMARY KEY (name)

);


CREATE TABLE CarYear (
	name VARCHAR(150) NOT NULL,
	year INT NOT NULL,
	CONSTRAINT pk_CarYear PRIMARY KEY (name)
);


CREATE TABLE UserInfo (
	name VARCHAR(150) NOT NULL,
	seller_type VARCHAR(100),
	transmission VARCHAR(100),
	owner VARCHAR(100),
	CONSTRAINT pk_UserInfo PRIMARY KEY (name)
);

CREATE TABLE CarDetails (
	name VARCHAR(150) NOT NULL,
	year INT NOT NULL,
	selling_price INT,
	km_driven INT,
	fuel VARCHAR(50),
	seller_type VARCHAR(100),
	transmission VARCHAR(100),
	owner VARCHAR(100),
	CONSTRAINT pk_CarDetails PRIMARY KEY (name)
);



ALTER TABLE CarYear ADD CONSTRAINT fk_CarYear_car_name FOREIGN KEY(name)
REFERENCES CarEngineInfo (name);

ALTER TABLE UserInfo ADD CONSTRAINT fk_UserInfo_car_name FOREIGN KEY(name)
REFERENCES CarEngineInfo (name);

ALTER TABLE CarDetails ADD CONSTRAINT fk_CarDetails_car_name FOREIGN KEY(name)
REFERENCES CarEngineInfo (name);
