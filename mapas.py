import folium

# Cria o mapa
mapa = folium.Map(
    location=[-23.55, -46.63],
    tiles='Stamen Terrain',  # Estilo do mapa
    zoom_start=16
)

# Adiciona o marcador no mapa
folium.Marker(
    [-23.55, -46.63],
    popup='<i>Minha casa</i>',
    tooltip='Click aqui!'
).add_to(mapa)

# Salva html do mapa
mapa.save(r'.\mapa.html')
