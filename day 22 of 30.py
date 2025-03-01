from bs4 import BeautifulSoup
import requests
import json
#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
"""
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

#-- get data 
response= requests.get(url)
content= response.content
soup = BeautifulSoup(content, 'html.parser')

try:
    # Obtener datos con cabeceras
    print("Obteniendo la página web...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    print(f"Estado de la respuesta: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    bu_data = {
        "universidad": "Boston University",
        "url": url,
        "secciones": []
    }
    
    # Buscar el contenido
    main_content = soup.find('main')
    if main_content:
        print("Contenido principal encontrado")
        
        # Encontrar las secciones
        sections = main_content.find_all(['section', 'div'])
        print(f"Número de secciones encontradas: {len(sections)}")
        
        for section in sections:
            section_data = {}
            
            # Buscar titulos
            title_elem = section.find(['h1', 'h2', 'h3'])
            if title_elem:
                title_text = title_elem.text.strip()
                print(f"Título encontrado: {title_text}")
                section_data["titulo"] = title_text
                
                # Buscar parrafos o elementos
                facts = []
                for elem in section.find_all(['p', 'li', 'div']):
                    text = elem.text.strip()
                    if text and text != title_text:
                        facts.append({"descripcion": text})
                
                if facts:
                    section_data["hechos"] = facts
                    bu_data["secciones"].append(section_data)
    else:
        print("No se encontró el contenido principal")
        print("Primeros 500 caracteres del HTML:")
        print(soup.prettify()[:500])
    #--convert to json
    bu_json = json.dumps(bu_data, indent=4, ensure_ascii=False)
    
    print("\nDatos extraídos:")
    print(bu_json)
    
    # Guardar
    with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
        f.write(bu_json)
    
    print("\nLos datos han sido guardados en 'bu_facts_stats.json'")
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página web: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    import traceback
    print(traceback.format_exc())
"""

#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets) and change it to a json file
"""
#-- get data 
url='https://archive.ics.uci.edu/ml/datasets'
response= requests.get(url)
content= response.content
soup = BeautifulSoup(content, 'html.parser')

datasets = []

dataset_elements = soup.find_all('div', role='row')

for element in dataset_elements:
    dataset = {}
    
    # Obtener título
    title_elem = element.find('a', class_='link-hover')
    if title_elem:
        dataset['titulo'] = title_elem.text.strip()
        dataset['url'] = title_elem['href']
    
    # Obtener descripción
    desc_elem = element.find('p', class_='truncate')
    if desc_elem:
        dataset['descripcion'] = desc_elem.text.strip()
    
    # Obtener imagen
    img_elem = element.find('img')
    if img_elem:
        dataset['imagen'] = img_elem['src']
    
    # Obtener metadatos
    metadata_div = element.find('div', class_='grid-cols-12')
    if metadata_div:
        metadata = []
        for meta_item in metadata_div.find_all('div', class_='col-span-3'):
            text = meta_item.find('span')
            if text:
                metadata.append(text.text.strip())
        
        # Asignar metadatos
        if len(metadata) >= 4:
            dataset['tipo_tarea'] = metadata[0]
            dataset['tipo_datos'] = metadata[1]
            dataset['instancias'] = metadata[2]
            dataset['caracteristicas'] = metadata[3]
    
    if dataset:
        datasets.append(dataset)

json_output = json.dumps(datasets, indent=4, ensure_ascii=False)
print(json_output)

# Guardar
with open('uci_datasets.json', 'w', encoding='utf-8') as f:
    f.write(json_output)

print("\nLos datos han sido guardados en 'uci_datasets.json'")
"""

#Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# The table is not very structured and the scrapping may take very long time.#
import pandas as pd
"""
def obtener_presidentes():
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    print("Obteniendo datos de Wikipedia...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar tabla principal
        table = soup.find('table', class_='wikitable')
        
        if not table:
            print("No se pudo encontrar la tabla de presidentes")
            return

        presidentes = []
        for row in table.find_all('tr')[1:]:
            # Obtener celdas
            cells = row.find_all(['td', 'th'])
            
            if len(cells) >= 6:
                # Extraer los datos
                presidente = {
                    'numero': cells[0].text.strip(),
                    'nombre': cells[3].text.strip(),
                    'partido': cells[6].text.strip() if len(cells) > 6 else "No disponible",
                    'periodo': cells[1].text.strip(),
                }
                
                #obtener imagen
                img = cells[3].find('img')
                if img and 'src' in img.attrs:
                    presidente['imagen'] = 'https:' + img['src']
                
                # Limpiar datos
                presidente = {k: v.replace('\n', ' ').strip() for k, v in presidente.items()}
                
                presidentes.append(presidente)
        
        print(f"Se encontraron {len(presidentes)} presidentes")
        
        # Convertir JSON
        json_data = json.dumps(presidentes, indent=4, ensure_ascii=False)
        with open('presidentes_usa.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        
        print("\nDatos guardados en 'presidentes_usa.json'")
        
        #DataFrame mejor visualización
        df = pd.DataFrame(presidentes)
        
        # Guardar CSV
        df.to_csv('presidentes_usa.csv', index=False, encoding='utf-8')
        print("Datos guardados en 'presidentes_usa.csv'")
        
        print("\nPrimeros 5 presidentes:")
        print(df.head().to_string())
        
        return presidentes
        
    except requests.RequestException as e:
        print(f"Error al obtener los datos: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    presidentes = obtener_presidentes()
"""
