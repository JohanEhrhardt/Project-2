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