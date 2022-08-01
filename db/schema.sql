-- create asx_200 table
CREATE TABLE asx_200 (
company_code VARCHAR(10) NOT NULL,
company_name VARCHAR(100) NOT NULL,
price_29jul22 DEC,
change DEC,
percent_change DEC,
one_year_percent_change DEC,
PRIMARY KEY (company_Code)
);

-- create asx_companies table
CREATE TABLE asx_companies (
company_code VARCHAR(10) NOT NULL,
company_name VARCHAR(100) NOT NULL,
market_cap DEC,
sector VARCHAR(100) NOT NULL,
PRIMARY KEY (company_code)
);
