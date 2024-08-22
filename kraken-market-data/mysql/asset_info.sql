-- Script to create required database and table
CREATE DATABASE kraken_market_data;
USE kraken_market_data;
CREATE TABLE asset_info (
    name VARCHAR(255) NOT NULL,
    aclass VARCHAR(255) NOT NULL,
    altname VARCHAR(255) NOT NULL,
    decimals INT NOT NULL,
    display_decimals INT NOT NULL,
    collateral_value FLOAT,
    status VARCHAR(255) NOT NULL,
    PRIMARY KEY (name)
);