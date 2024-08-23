-- Script to create required database and table
CREATE DATABASE kraken_market_data;
USE kraken_market_data;
CREATE TABLE tradable_asset_pairs (
    name VARCHAR(255) NOT NULL,
    altname VARCHAR(255) NOT NULL,
    wsname VARCHAR(255) NOT NULL,
    aclass_base VARCHAR(255) NOT NULL,
    base VARCHAR(255) NOT NULL,
    aclass_quote VARCHAR(255) NOT NULL,
    quote VARCHAR(255) NOT NULL,
    pair_decimals INT NOT NULL,
    cost_decimals INT NOT NULL,
    lot_decimals INT NOT NULL,
    lot_multiplier INT NOT NULL,
    -- leverage_buy [INT] NOT NULL,
    -- leverage_sell [INT] NOT NULL,
    -- fees [] NOT NULL,
    -- fees_maker [] NOT NULL,
    fee_volume_currency VARCHAR(255) NOT NULL,
    margin_call INT NOT NULL,
    margin_stop INT NOT NULL,
    ordermin VARCHAR(255) NOT NULL,
    costmin VARCHAR(255) NOT NULL,
    tick_size VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    long_position_limit INT NOT NULL,
    short_position_limit INT NOT NULL,
    PRIMARY KEY (name)
);