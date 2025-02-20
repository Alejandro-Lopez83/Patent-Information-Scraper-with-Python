Patent Information Scraper / Extractor de Información de Patentes
Show Image Show Image
English
Description
This project is a web scraping tool designed to extract patent summaries from OEPM (Spanish Patent and Trademark Office) and Patentscope websites. It automatically processes URLs, extracts relevant information, and stores it in a MongoDB database.
Features

Automated web scraping of patent information
Support for multiple patent websites (OEPM and Patentscope)
MongoDB database integration
Robust error handling
URL cleaning and processing
Progress tracking and statistics

Technologies

Python
Selenium WebDriver
BeautifulSoup4
MongoDB
Chrome/Chromium browser

Requirements

Python 3.x
Chrome/Chromium browser
ChromeDriver
MongoDB server
Python packages:

selenium
beautifulsoup4
pymongo



Installation

Clone the repository
Install required Python packages:

bashCopypip install selenium beautifulsoup4 pymongo

Install and configure MongoDB
Ensure Chrome/Chromium and ChromeDriver are installed

Usage

Configure MongoDB connection in the script
Prepare your patent URLs in the MongoDB collection
Run the script:

bashCopypython patent_scraper.py

Español
Descripción
Este proyecto es una herramienta de web scraping diseñada para extraer resúmenes de patentes de los sitios web de la OEPM (Oficina Española de Patentes y Marcas) y Patentscope. Procesa automáticamente URLs, extrae información relevante y la almacena en una base de datos MongoDB.
Características

Web scraping automatizado de información de patentes
Soporte para múltiples sitios web de patentes (OEPM y Patentscope)
Integración con base de datos MongoDB
Manejo robusto de errores
Limpieza y procesamiento de URLs
Seguimiento de progreso y estadísticas

Tecnologías

Python
Selenium WebDriver
BeautifulSoup4
MongoDB
Navegador Chrome/Chromium

Requisitos

Python 3.x
Navegador Chrome/Chromium
ChromeDriver
Servidor MongoDB
Paquetes Python:

selenium
beautifulsoup4
pymongo



Instalación

Clonar el repositorio
Instalar paquetes Python requeridos:

bashCopypip install selenium beautifulsoup4 pymongo

Instalar y configurar MongoDB
Asegurar que Chrome/Chromium y ChromeDriver están instalados

Uso

Configurar la conexión MongoDB en el script
Preparar las URLs de patentes en la colección MongoDB
Ejecutar el script:

bashCopypython patent_scraper.py
