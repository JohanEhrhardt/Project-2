-- create asx_company table
CREATE TABLE asx_companies (
company_code VARCHAR(10) NOT NULL,
company_name VARCHAR(100) NOT NULL,
market_cap DEC,
price_28jul22 DEC,
change_28jul22 DEC,
percent_change_28jul22 DEC,
sector VARCHAR(100) NOT NULL,
PRIMARY KEY (company_code)
);

-- create asx_200 table
CREATE TABLE asx_200 (
company_code VARCHAR(10) NOT NULL,
percent_change_one_year TEXT,
PRIMARY KEY (company_Code)
);

-- Join tables on county_id
SELECT a200.company_code, a.sector , a.company_name, a.market_cap, a.price_28jul22, a.change_28jul22, a.percent_change_28jul22, a200.percent_change_one_year
FROM asx_company a
INNER JOIN asx_200 a200
ON a.company_code = a200.company_code;
