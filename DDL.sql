CREATE TABLE CarEngineInfo (
	car_name VARCHAR(150) NOT NULL,
	selling_price INT,
	km_driven INT,
	fuel VARCHAR(50),
	mileage VARCHAR(100),
	engine VARCHAR(50),
	max_power VARCHAR(100),
	torque VARCHAR (200),
	seat int
	CONSTRAINT "pk_CarEngineInfo" PRIMARY KEY (
        "car_name"

)


CREATE TABLE CarYear (
	car_name VARCHAR(150) NOT NULL,
	car_year INT NOT NULL
	CONSTRAINT "pk_CarYear" PRIMARY KEY (
        "car_name"
)


CREATE TABLE UserInfo (
	car_name VARCHAR(150) NOT NULL,
	seller_type VARCHAR(100),
	transmission VARCHAR(100),
	car_owner VARCHAR(100)
	CONSTRAINT "pk_UserInfo" PRIMARY KEY (
        "car_name"
)

ALTER TABLE "CarYear" ADD CONSTRAINT "fk_CarYear_car_name" FOREIGN KEY("car_name")
REFERENCES "CarEngineInfo" ("car_name");

ALTER TABLE "UserInfo" ADD CONSTRAINT "fk_UserInfo_car_name" FOREIGN KEY("car_name")
REFERENCES "CarEngineInfo" ("car_name");
