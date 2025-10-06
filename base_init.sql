CREATE TABLE currency (
	num_code INTEGER,
	word_code VARCHAR(3),
	units INTEGER,
	cur_name VARCHAR(37),
	rub_cost DECIMAL(3, 4),
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (num_code, rec_date)
);

CREATE TABLE crypto (
	word_code VARCHAR(10),
	cru_name VARCHAR(50),
	dol_cost DECIMAL(6,8),
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (word_code, rec_date)
);