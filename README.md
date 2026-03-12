# E-Commerce ETL Pipeline

## Project Overview
This project is a step-by-step implementation of a real-world ETL pipeline for an e-commerce business.

The goal is to learn and build an end-to-end data pipeline using:
- MySQL as the source system
- PySpark for transformation
- Snowflake as the analytics warehouse
- Kafka in later versions for streaming ingestion

## Problem Statement
E-commerce businesses generate data from multiple systems such as customer records, product catalogs, and order events.

This project simulates how such data can be:
1. extracted from source systems,
2. transformed into analytics-ready datasets,
3. loaded into a warehouse for reporting.

## Tech Stack
- Python
- PySpark
- MySQL
- Snowflake
- Kafka (planned in later versions)
- Git / GitHub
- PyCharm Community Edition

## Project Roadmap

### Version 0
Project skeleton and architecture planning.

### Version 1
Batch ETL pipeline:
- Read `orders.csv`
- Read `customers` and `products` from MySQL
- Transform data using PySpark DataFrames
- Load analytics tables into Snowflake

### Version 2
Add JSON batch input support.

### Version 3
Replace batch order input with Kafka streaming events.

### Version 4
Add production-style improvements such as validation, logging, and better structuring.

## Learning Goals
- Understand the difference between Spark and PySpark
- Learn why DataFrames are preferred over RDDs in ETL pipelines
- Build a real ETL workflow using batch and later streaming data
- Practice version-controlled project evolution with Git

## Current Status
Version 0 completed: project initialized and roadmap defined.