# Patent Information Scraper / Extractor de Información de Patentes

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english) [![Español](https://img.shields.io/badge/lang-Espa%C3%B1ol-red.svg)](#español)

## English

### Description
This project is a web scraping tool designed to extract patent summaries from OEPM (Spanish Patent and Trademark Office) and Patentscope websites. It automatically processes URLs, extracts relevant information, and stores it in a MongoDB database.

### Features
- Automated web scraping of patent information
- Support for multiple patent websites (OEPM and Patentscope)
- MongoDB database integration
- Robust error handling
- URL cleaning and processing
- Progress tracking and statistics

### Technologies
- Python
- Selenium WebDriver
- BeautifulSoup4
- MongoDB
- Chrome/Chromium browser

### Requirements
- Python 3.x
- Chrome/Chromium browser
- ChromeDriver
- MongoDB server
- Python packages:
  - selenium
  - beautifulsoup4
  - pymongo

### Installation
1. Clone the repository
2. Install required Python packages:
```bash
pip install selenium beautifulsoup4 pymongo
```
3. Install and configure MongoDB
4. Ensure Chrome/Chromium and ChromeDriver are installed

### Usage
1. Configure MongoDB connection in the script
2. Prepare your patent URLs in the MongoDB collection
3. Run the script:
```bash
python patent_scraper.py
```

---

## Español

### Descripción
Este proyecto es una herramienta de web scraping diseñada para extraer resúmenes de patentes de los sitios web de la OEPM (Oficina Española de Patentes y Marcas) y Patentscope. Procesa automáticamente URLs, extrae información relevante y la almacena en una base de datos MongoDB.

### Características
- Web scraping automatizado de información de patentes
- Soporte para múltiples sitios web de patentes (OEPM y Patentscope)
- Integración con base de datos MongoDB
- Manejo robusto de errores
- Limpieza y procesamiento de URLs
- Seguimiento de progreso y estadísticas

### Tecnologías
- Python
- Selenium WebDriver
- BeautifulSoup4
- MongoDB
- Navegador Chrome/Chromium

### Requisitos
- Python 3.x
- Navegador Chrome/Chromium
- ChromeDriver
- Servidor MongoDB
- Paquetes Python:
  - selenium
  - beautifulsoup4
  - pymongo

### Instalación
1. Clonar el repositorio
2. Instalar paquetes Python requeridos:
```bash
pip install selenium beautifulsoup4 pymongo
```
3. Instalar y configurar MongoDB
4. Asegurar que Chrome/Chromium y ChromeDriver están instalados

### Uso
1. Configurar la conexión MongoDB en el script
2. Preparar las URLs de patentes en la colección MongoDB
3. Ejecutar el script:
```bash
python patent_scraper.py
```
