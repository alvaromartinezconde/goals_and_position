import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
from paint_field import paint_field

# CARGA DE ARCHIVOS

ruta_jugadores = "inputs/eventos_2020_2021.csv"
df_jugadores = pd.read_csv(ruta_jugadores)

ruta_equipos = "inputs/opta_id_equipos.json"
with open(ruta_equipos, 'r') as fp:
    id_equipos  = json.load(fp)


# SELECCION DE VARIABLE EQUIPOS Y JUGADORES DE INTERÉS
 
df_jgd = df_jugadores['type_id']==16

clave = 't953'

equipo_id_name = {}
for id_e in id_equipos.keys():
    nuevo_id = id_e.replace("t","")
    equipo_id_name[nuevo_id] = id_equipos[id_e]

df_jugadores[df_jgd][df_jugadores['team']== 'Real Madrid']['player'].value_counts()

df_Karim_Benzema = df_jugadores[df_jgd][df_jugadores[df_jgd]['player']== 'Karim Benzema'].copy()

df_Lionel_Messi = df_jugadores[df_jgd][df_jugadores['player']== 'Lionel Messi'].copy()

color_campo = 'green'
paint_field.field_with_2_players(color_campo, df_Karim_Benzema, df_Lionel_Messi)
