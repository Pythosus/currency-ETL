CREATE TABLE currency (
	num_code INTEGER,
	word_code VARCHAR(3),
	units INTEGER,
	cur_name VARCHAR(37),
	rub_cost DECIMAL(3, 4),
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (num_code)
);

CREATE TABLE crypto (
	word_code VARCHAR(3),
	cru_name VARCHAR(25),
	dol_cost DECIMAL(6,2),
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (word_code)
);