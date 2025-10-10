CREATE TABLE currency (
	num_code INTEGER NOT NULL,
	word_code VARCHAR(3) NOT NULL,
	units INTEGER,
	cur_name VARCHAR(37),
	rub_cost NUMERIC,
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (num_code, rec_date)
);

CREATE TABLE crypto (
	word_code VARCHAR(10) NOT NULL,
	cru_name VARCHAR(50) NOT NULL,
	dol_cost NUMERIC,
	rec_date DATE DEFAULT NOW(),
	PRIMARY KEY (cru_name, rec_date)
);