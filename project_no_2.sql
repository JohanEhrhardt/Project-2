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

-- Join tables on company_code
SELECT a200.company_code, a200.company_name, a200.price_29jul22, a200.percent_change, a200.one_year_percent_change, a.sector , a.market_cap
FROM asx_200 a200
LEFT JOIN asx_companies a
ON a200.company_code = a.company_code;

-- create view
CREATE VIEW asx_200_data AS
SELECT a200.company_code, a200.company_name, a200.price_29jul22, a200.percent_change, a200.one_year_percent_change, a.sector , a.market_cap
FROM asx_200 a200
LEFT JOIN asx_companies a
ON a200.company_code = a.company_code;