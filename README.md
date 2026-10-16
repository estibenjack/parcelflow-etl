# 📦 ParcelFlow ETL Pipeline

## Overview

ParcelFlow is a fictional UK parcel delivery company operating across three depots: Belfast, Manchester and Birmingham. Each depot generates daily CSV exports containing shipment information and parcel tracking events.

This project involves designing and developing a Python-based ETL pipeline to consolidate these datasets into a centralised PostgreSQL database.

## Business Problem

Shipment and tracking data is currently stored in separate depot-level CSV files, making it difficult to analyse delivery performance across the business.

ParcelFlow needs a reliable process to extract, clean, validate and consolidate this data to support operational reporting, including shipment statuses, delivery times, delays and depot performance.

## Data Model

The relational model consists of three tables:


| Table name | Description |
|------------|-------------|
| `depots` | Depot information |
| `shipments` | Individual shipment details |
| `tracking_events` | Shipment tracking history |

![ParcelFlow Entity Relationship Diagram](docs/parcelflow-erd.drawio.png)