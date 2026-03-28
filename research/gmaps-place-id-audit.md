# Google Maps Place ID Audit Report

**Date**: 2026-03-28
**Total stations**: 389

## Summary

| Status | Count | Lines will show? |
|--------|-------|-----------------|
| `subway_station` | 230 | Yes |
| `train_station` | 78 | Yes |
| `transit_station` (not subway) | 80 | Probably not |
| `bus_station` | 0 | No (WRONG) |
| Other / No Place ID | 1 | No |
| **Total will show lines** | **308** | |
| **Total won't show lines** | **81** | |

## Stations that WILL show metro lines (308)

These have `subway_station` or `train_station` type -- Google Maps will show the metro/rail line preview.

| ID | Our Name | Google Maps Name | Type |
|----|----------|-----------------|------|
| cercanias_001 | Recoletos | Recoletos | TRAIN_STATION |
| cercanias_002 | Sol | Sol | SUBWAY_STATION |
| cercanias_003 | Atocha | Estación Madrid - Puerta de Atocha | TRAIN_STATION |
| cercanias_004 | Chamartín-Clara Campoamor | Chamartín-Clara Campoamor | TRAIN_STATION |
| cercanias_008 | Príncipe Pío | Príncipe Pío | SUBWAY_STATION |
| cercanias_009 | Méndez Álvaro | Méndez Álvaro | SUBWAY_STATION |
| cercanias_010 | Delicias | Delicias | TRAIN_STATION |
| cercanias_011 | Pirámides | Pirámides | SUBWAY_STATION |
| cercanias_012 | Embajadores | Embajadores | SUBWAY_STATION |
| cercanias_013 | Doce de Octubre | Doce de Octubre | TRAIN_STATION |
| cercanias_014 | Orcasitas | Orcasitas | TRAIN_STATION |
| cercanias_015 | Puente Alcocer | Puente Alcocer | TRAIN_STATION |
| cercanias_016 | San Cristóbal de los Ángeles | San Cristóbal de los Ángeles | TRAIN_STATION |
| cercanias_017 | San Cristóbal Industrial | San Cristóbal Industrial | TRAIN_STATION |
| cercanias_018 | Getafe Industrial | Getafe Industrial | TRAIN_STATION |
| cercanias_019 | Getafe Centro | Getafe Central | SUBWAY_STATION |
| cercanias_020 | Getafe Sector 3 | Getafe Sector 3 | TRAIN_STATION |
| cercanias_021 | Las Margaritas Universidad | Las Margaritas-Universidad | TRAIN_STATION |
| cercanias_022 | El Casar | El Casar | TRAIN_STATION |
| cercanias_023 | Pinto | Pinto | TRAIN_STATION |
| cercanias_024 | Valdemoro | Valdemoro | TRAIN_STATION |
| cercanias_025 | Ciempozuelos | Ciempozuelos | TRAIN_STATION |
| cercanias_026 | Aranjuez | Aranjuez | TRAIN_STATION |
| cercanias_027 | Parla | Parla | TRAIN_STATION |
| cercanias_028 | Fuencarral | Fuencarral | TRAIN_STATION |
| cercanias_029 | Cantoblanco Universidad | Cantoblanco Universidad | TRAIN_STATION |
| cercanias_030 | Alcobendas-San Sebastián de los Reyes | Alcobendas-San Sebastián de los Reyes | TRAIN_STATION |
| cercanias_031 | El Goloso | El Goloso | TRAIN_STATION |
| cercanias_032 | Colmenar Viejo | Colmenar Viejo | TRAIN_STATION |
| cercanias_033 | Asamblea de Madrid-Entrevías | Asamblea de Madrid-Entrevías | TRAIN_STATION |
| cercanias_034 | El Pozo | El Pozo | TRAIN_STATION |
| cercanias_035 | Santa Eugenia | Santa Eugenia | TRAIN_STATION |
| cercanias_036 | Coslada | Coslada Central | TRAIN_STATION |
| cercanias_037 | San Fernando | San Fernando | TRAIN_STATION |
| cercanias_038 | Torrejón de Ardoz | Torrejón de Ardoz | TRAIN_STATION |
| cercanias_039 | Soto del Henares | Soto del Henares | TRAIN_STATION |
| cercanias_040 | La Garena | La Garena | TRAIN_STATION |
| cercanias_041 | Alcalá de Henares | Alcalá de Henares | TRAIN_STATION |
| cercanias_042 | Alcalá de Henares Universidad | Alcalá de Henares-Universidad | TRAIN_STATION |
| cercanias_043 | Meco | Meco | TRAIN_STATION |
| cercanias_044 | Azuqueca | Azuqueca | TRAIN_STATION |
| cercanias_045 | Guadalajara | Guadalajara | TRAIN_STATION |
| cercanias_046 | Aluche | Aluche | SUBWAY_STATION |
| cercanias_047 | Maestra Justa Freire-Polideportivo Aluche | Maestra Justa Freire-Polideportivo Aluche | TRAIN_STATION |
| cercanias_048 | Las Águilas | Las Águilas | TRAIN_STATION |
| cercanias_049 | Cuatro Vientos | Cuatro Vientos | SUBWAY_STATION |
| cercanias_050 | Laguna | Laguna | SUBWAY_STATION |
| cercanias_051 | Alcorcón | Alcorcon Central | SUBWAY_STATION |
| cercanias_052 | San José de Valderas | San José de Valderas | TRAIN_STATION |
| cercanias_053 | Las Retamas | Las Retamas | TRAIN_STATION |
| cercanias_054 | Móstoles | Móstoles-El Soto | TRAIN_STATION |
| cercanias_055 | Móstoles-El Soto | Móstoles-El Soto | TRAIN_STATION |
| cercanias_056 | Leganés | Leganés Central | SUBWAY_STATION |
| cercanias_057 | Parque Polvoranca | Parque Polvoranca | TRAIN_STATION |
| cercanias_058 | Fuenlabrada | Fuenlabrada Central | SUBWAY_STATION |
| cercanias_059 | La Serna-Fuenlabrada | La Serna | TRAIN_STATION |
| cercanias_060 | Humanes | Humanes | TRAIN_STATION |
| cercanias_061 | Aravaca | Aravaca | TRAIN_STATION |
| cercanias_062 | El Barrial-Centro Comercial Pozuelo | El Barrial-Centro Comercial-Pozuelo | TRAIN_STATION |
| cercanias_063 | Pozuelo | Pozuelo | TRAIN_STATION |
| cercanias_064 | Majadahonda | Majadahonda | TRAIN_STATION |
| cercanias_065 | Las Rozas | Las Rozas | TRAIN_STATION |
| cercanias_066 | Pinar | Pinar de Las Rozas | TRAIN_STATION |
| cercanias_067 | Las Matas | Las Matas | TRAIN_STATION |
| cercanias_068 | Torrelodones | Torrelodones | TRAIN_STATION |
| cercanias_069 | Galapagar-La Navata | Galapagar-La Navata | TRAIN_STATION |
| cercanias_070 | San Yago | San Yago | TRAIN_STATION |
| cercanias_071 | El Escorial | El Escorial | TRAIN_STATION |
| cercanias_072 | Robledo de Chavela | Robledo de Chavela | TRAIN_STATION |
| cercanias_073 | Santa María de la Alameda-Peguerinos | Santa María de la Alameda Peguerinos | TRAIN_STATION |
| cercanias_074 | Los Negrales | Los Negrales | TRAIN_STATION |
| cercanias_075 | Alpedrete | Alpedrete | TRAIN_STATION |
| cercanias_076 | Collado Mediano | Collado Mediano | TRAIN_STATION |
| cercanias_077 | Los Molinos | Los Molinos-Guadarrama | TRAIN_STATION |
| cercanias_078 | Cercedilla | Cercedilla | TRAIN_STATION |
| cercanias_081 | Mirasierra-Paco de Lucía | Mirasierra-Paco de Lucía | TRAIN_STATION |
| cercanias_082 | Ramón y Cajal | Ramón y Cajal | TRAIN_STATION |
| cercanias_084 | Tres Cantos | Tres Cantos | TRAIN_STATION |
| cercanias_085 | Valdebebas | Valdebebas | TRAIN_STATION |
| cercanias_086 | Vallecas | Vallecas | TRAIN_STATION |
| cercanias_087 | Vicálvaro | Vicálvaro | TRAIN_STATION |
| cercanias_088 | Villaverde Bajo | Villaverde Bajo | TRAIN_STATION |
| cercanias_089 | Villaverde Alto | Villaverde Alto | SUBWAY_STATION |
| cercanias_090 | Universidad P. Comillas | Universidad Pontificia de Comillas | TRAIN_STATION |
| cercanias_091 | Valdelasfuentes | Valdelasfuentes | TRAIN_STATION |
| cercanias_092 | Zarzaquemada | Zarzaquemada | TRAIN_STATION |
| cercanias_093 | Villalba | Villalba de Guadarrama | TRAIN_STATION |
| cercanias_094 | Las Zorreras | Las Zorreras | TRAIN_STATION |
| cercanias_095 | Zarzalejo | Zarzalejo | TRAIN_STATION |
| metro_001 | Sol | Sol | SUBWAY_STATION |
| metro_004 | La Latina | La Latina | SUBWAY_STATION |
| metro_005 | Goya | Goya | SUBWAY_STATION |
| metro_006 | Argüelles | Argüelles | SUBWAY_STATION |
| metro_007 | Chueca | Chueca | SUBWAY_STATION |
| metro_008 | Embajadores | Embajadores | SUBWAY_STATION |
| metro_009 | Lavapiés | Lavapiés | SUBWAY_STATION |
| metro_011 | Callao | Callao | SUBWAY_STATION |
| metro_012 | Ópera | Ópera | SUBWAY_STATION |
| metro_016 | Paco de Lucía | Paco de Lucía | SUBWAY_STATION |
| metro_017 | Manuela Malasaña | Manuela Malasaña | SUBWAY_STATION |
| metro_018 | Príncipe Pío | Príncipe Pío | SUBWAY_STATION |
| metro_019 | Eugenia de Montijo | Eugenia de Montijo | SUBWAY_STATION |
| metro_020 | Guzmán el Bueno | Guzmán el Bueno | SUBWAY_STATION |
| metro_021 | Alonso Martínez | Alonso Martínez | SUBWAY_STATION |
| metro_023 | Vicente Aleixandre | Vicente Aleixandre | SUBWAY_STATION |
| metro_024 | Concha Espina | Concha Espina | SUBWAY_STATION |
| metro_025 | Santiago Bernabeu | Santiago Bernabeu | SUBWAY_STATION |
| metro_027 | Feria de Madrid | Feria de Madrid | SUBWAY_STATION |
| metro_028 | Estadio Metropolitano | Estadio Metropolitano | SUBWAY_STATION |
| metro_029 | Atocha | Atocha | SUBWAY_STATION |
| metro_030 | Pirámides | Pirámides | SUBWAY_STATION |
| metro_032 | Noviciado | Noviciado | SUBWAY_STATION |
| metro_033 | Bilbao | Bilbao | SUBWAY_STATION |
| metro_034 | Quevedo | Quevedo | SUBWAY_STATION |
| metro_035 | Islas Filipinas | Islas Filipinas | SUBWAY_STATION |
| metro_036 | Moncloa | Moncloa | SUBWAY_STATION |
| metro_037 | Ventas | Ventas | SUBWAY_STATION |
| metro_038 | Manuel Becerra | Manuel Becerra | SUBWAY_STATION |
| metro_040 | Ibiza | Ibiza | SUBWAY_STATION |
| metro_041 | Pacífico | Pacífico | SUBWAY_STATION |
| metro_042 | Menéndez Pelayo | Menéndez Pelayo | SUBWAY_STATION |
| metro_043 | Ríos Rosas | Ríos Rosas | SUBWAY_STATION |
| metro_044 | Iglesia | Iglesia | SUBWAY_STATION |
| metro_045 | Cruz del Rayo | Cruz del Rayo | SUBWAY_STATION |
| metro_046 | Prosperidad | Prosperidad | SUBWAY_STATION |
| metro_047 | Cuatro Caminos | Cuatro Caminos | SUBWAY_STATION |
| metro_048 | Tetuán | Tetuán | SUBWAY_STATION |
| metro_049 | Estrecho | Estrecho | SUBWAY_STATION |
| metro_050 | Valdeacederas | Valdeacederas | SUBWAY_STATION |
| metro_051 | Francos Rodríguez | Francos Rodríguez | SUBWAY_STATION |
| metro_052 | Carpetana | Carpetana | SUBWAY_STATION |
| metro_053 | Oporto | Oporto | SUBWAY_STATION |
| metro_054 | Vista Alegre | Vista Alegre | SUBWAY_STATION |
| metro_055 | Carabanchel | Carabanchel | SUBWAY_STATION |
| metro_056 | Arturo Soria | Arturo Soria | SUBWAY_STATION |
| metro_057 | Esperanza | Esperanza | SUBWAY_STATION |
| metro_058 | Canillas | Canillas | SUBWAY_STATION |
| metro_059 | Mar de Cristal | Mar de Cristal | SUBWAY_STATION |
| metro_061 | Colombia | Colombia | SUBWAY_STATION |
| metro_063 | Rubén Darío | Rubén Darío | SUBWAY_STATION |
| metro_064 | Núñez de Balboa | Núñez de Balboa | SUBWAY_STATION |
| metro_065 | Barajas | Barajas | SUBWAY_STATION |
| metro_066 | Canillejas | Canillejas | SUBWAY_STATION |
| metro_067 | Torre Arias | Torre Arias | SUBWAY_STATION |
| metro_068 | Legazpi | Legazpi | SUBWAY_STATION |
| metro_069 | Delicias | Delicias | SUBWAY_STATION |
| metro_070 | Méndez Álvaro | Méndez Álvaro | SUBWAY_STATION |
| metro_071 | Palos de la Frontera | Palos de La Frontera | SUBWAY_STATION |
| metro_072 | Pavones | Pavones | SUBWAY_STATION |
| metro_073 | Valdebernardo | Valdebernardo | SUBWAY_STATION |
| metro_074 | Vicálvaro | Vicálvaro | SUBWAY_STATION |
| metro_075 | San Cipriano | San Cipriano | SUBWAY_STATION |
| metro_077 | Almendrales | Almendrales | SUBWAY_STATION |
| metro_078 | Usera | Usera | SUBWAY_STATION |
| metro_079 | Plaza Elíptica | Plaza Elíptica | SUBWAY_STATION |
| metro_080 | Puerta de Arganda | Puerta de Arganda | SUBWAY_STATION |
| metro_081 | Arganda del Rey | Arganda del Rey | SUBWAY_STATION |
| metro_082 | La Poveda | La Poveda | SUBWAY_STATION |
| metro_083 | Tres Olivos | Tres Olivos | SUBWAY_STATION |
| metro_084 | Montecarmelo | Montecarmelo | SUBWAY_STATION |
| metro_085 | Las Tablas | Las Tablas | SUBWAY_STATION |
| metro_086 | Pinar de Chamartín | Pinar de Chamartín | SUBWAY_STATION |
| metro_087 | Antón Martín | Antón Martín | SUBWAY_STATION |
| metro_088 | Retiro | Retiro | SUBWAY_STATION |
| metro_089 | Banco de España | Banco de España | SUBWAY_STATION |
| metro_090 | Sevilla | Sevilla | SUBWAY_STATION |
| metro_091 | Santo Domingo | Santo Domingo | SUBWAY_STATION |
| metro_092 | San Bernardo | San Bernardo | SUBWAY_STATION |
| metro_093 | Canal | Canal | SUBWAY_STATION |
| metro_094 | Ventura Rodríguez | Ventura Rodríguez | SUBWAY_STATION |
| metro_096 | Acacias | Acacias | SUBWAY_STATION |
| metro_097 | Marqués de Vadillo | Marqués de Vadillo | SUBWAY_STATION |
| metro_098 | Conde de Casal | Conde de Casal | SUBWAY_STATION |
| metro_099 | Sáinz de Baranda | Sainz de Baranda | SUBWAY_STATION |
| metro_101 | Velázquez | Velázquez | SUBWAY_STATION |
| metro_102 | Lista | Lista | SUBWAY_STATION |
| metro_104 | República Argentina | República Argentina | SUBWAY_STATION |
| metro_105 | Alonso Cano | Alonso Cano | SUBWAY_STATION |
| metro_106 | Cuzco | Cuzco | SUBWAY_STATION |
| metro_108 | Alvarado | Alvarado | SUBWAY_STATION |
| metro_110 | Nueva Numancia | Nueva Numancia | SUBWAY_STATION |
| metro_111 | Portazgo | Portazgo | SUBWAY_STATION |
| metro_112 | Puerta del Ángel | Puerta del Ángel | SUBWAY_STATION |
| metro_113 | Alto de Extremadura | Alto de Extremadura | SUBWAY_STATION |
| metro_114 | Lucero | Lucero | SUBWAY_STATION |
| metro_115 | Laguna | Laguna | SUBWAY_STATION |
| metro_116 | Aluche | Aluche | SUBWAY_STATION |
| metro_117 | Campamento | Campamento | SUBWAY_STATION |
| metro_119 | Lago | Lago | SUBWAY_STATION |
| metro_120 | Casa de Campo | Casa de Campo | SUBWAY_STATION |
| metro_121 | Plaza de España | Plaza de España | SUBWAY_STATION |
| metro_122 | Ciudad Universitaria | Ciudad Universitaria | SUBWAY_STATION |
| metro_123 | Pío XII | Pío XII | SUBWAY_STATION |
| metro_124 | Duque de Pastrana | Duque de Pastrana | SUBWAY_STATION |
| metro_125 | Herrera Oria | Herrera Oria | SUBWAY_STATION |
| metro_126 | Barrio del Pilar | Barrio del Pilar | SUBWAY_STATION |
| metro_127 | Ventilla | Ventilla | SUBWAY_STATION |
| metro_128 | Mirasierra | Mirasierra | SUBWAY_STATION |
| metro_129 | Arganzuela-Planetario | Arganzuela-Planetario | SUBWAY_STATION |
| metro_130 | Suanzes | Suanzes | SUBWAY_STATION |
| metro_131 | Ciudad Lineal | Ciudad Lineal | SUBWAY_STATION |
| metro_132 | Quintana | Quintana | SUBWAY_STATION |
| metro_133 | El Carmen | El Carmen | SUBWAY_STATION |
| metro_134 | García Noblejas | García Noblejas | SUBWAY_STATION |
| metro_135 | Simancas | Simancas | SUBWAY_STATION |
| metro_136 | Las Musas | Las Musas | SUBWAY_STATION |
| metro_137 | San Blas | San Blas | SUBWAY_STATION |
| metro_138 | Pueblo Nuevo | Pueblo Nuevo | SUBWAY_STATION |
| metro_139 | Pinar del Rey | Pinar del Rey | SUBWAY_STATION |
| metro_140 | Bambú | Bambú | SUBWAY_STATION |
| metro_141 | Estrella | Estrella | SUBWAY_STATION |
| metro_142 | Vinateros | Vinateros | SUBWAY_STATION |
| metro_143 | Artilleros | Artilleros | SUBWAY_STATION |
| metro_145 | Cartagena | Cartagena | SUBWAY_STATION |
| metro_146 | Antonio Machado | Antonio Machado | SUBWAY_STATION |
| metro_147 | Valdezarza | Valdezarza | SUBWAY_STATION |
| metro_148 | Colonia Jardín | Colonia Jardín | SUBWAY_STATION |
| metro_149 | Opañel | Opañel | SUBWAY_STATION |
| metro_150 | Rivas Vaciamadrid | Rivas Vaciamadrid | SUBWAY_STATION |
| metro_151 | Julián Besteiro | Julián Besteiro | SUBWAY_STATION |
| metro_152 | Juan de la Cierva | Juan de La Cierva | SUBWAY_STATION |
| metro_153 | Alonso de Mendoza | Alonso de Mendoza | SUBWAY_STATION |
| metro_154 | Hospital Severo Ochoa | Hospital Severo Ochoa | SUBWAY_STATION |
| metro_155 | Reyes Católicos | Reyes Católicos | SUBWAY_STATION |
| metro_156 | Manuel de Falla | Manuel de Falla | SUBWAY_STATION |
| metro_157 | Marqués de la Valdavia | Marqués de la Valdavia | SUBWAY_STATION |
| metro_158 | Avenida de la Paz | Avenida de La Paz | SUBWAY_STATION |
| metro_159 | Alto del Arenal | Alto del Arenal | SUBWAY_STATION |
| metro_160 | Parque de Santa María | Parque de Sta. María | SUBWAY_STATION |
| metro_161 | Hortaleza | Hortaleza | SUBWAY_STATION |
| metro_162 | Manoteras | Manoteras | SUBWAY_STATION |
| metro_163 | Empalme | Empalme | SUBWAY_STATION |
| metro_164 | La Gavia | La Gavia | SUBWAY_STATION |
| metro_165 | El Capricho | El Capricho | SUBWAY_STATION |
| metro_166 | Alameda de Osuna | Alameda de Osuna | SUBWAY_STATION |
| metro_168 | Arroyofresno | Arroyofresno | SUBWAY_STATION |
| metro_169 | Lacoma | Lacoma | SUBWAY_STATION |
| metro_170 | La Elipa | La Elipa | SUBWAY_STATION |
| metro_171 | Peñagrande | Peñagrande | SUBWAY_STATION |
| metro_172 | Parque de las Avenidas | Parque de Las Avenidas | SUBWAY_STATION |
| metro_173 | Barrio de la Concepción | Barrio de la Concepción | SUBWAY_STATION |
| metro_174 | Ascao | Ascao | SUBWAY_STATION |
| metro_175 | Barrio del Puerto | Barrio del Puerto | SUBWAY_STATION |
| metro_176 | Coslada Central | Coslada Central | TRAIN_STATION |
| metro_177 | San Lorenzo | San Lorenzo | SUBWAY_STATION |
| metro_178 | San Fernando | San Fernando | SUBWAY_STATION |
| metro_179 | Jarama | Jarama | SUBWAY_STATION |
| metro_180 | Henares | Henares | SUBWAY_STATION |
| metro_181 | Hospital del Henares | Hospital del Henares | SUBWAY_STATION |
| metro_182 | Urgel | Urgel | SUBWAY_STATION |
| metro_188 | Avenida de la Ilustración | Avenida de la Ilustración | SUBWAY_STATION |
| metro_195 | La Rambla | La Rambla | SUBWAY_STATION |
| metro_200 | Aeropuerto T1-T2-T3 | Aeropuerto T1-T2-T3 | SUBWAY_STATION |
| metro_202 | Rivas-Urbanizaciones | Rivas Urbanizaciones | SUBWAY_STATION |
| metro_203 | Rivas Futura | Rivas Futura | SUBWAY_STATION |
| metro_204 | Puerta del Sur | Puerta del Sur | SUBWAY_STATION |
| metro_205 | Joaquín Vilumbrales | Joaquín Vilumbrales | SUBWAY_STATION |
| metro_206 | Cuatro Vientos | Cuatro Vientos | SUBWAY_STATION |
| metro_207 | Aviación Española | Aviación Española | SUBWAY_STATION |
| metro_209 | Fuencarral | Fuencarral | SUBWAY_STATION |
| metro_210 | Ronda de la Comunicación | Ronda de la Comunicación | SUBWAY_STATION |
| metro_212 | La Moraleja | La Moraleja | SUBWAY_STATION |
| metro_213 | Baunatal | Baunatal | SUBWAY_STATION |
| metro_214 | Hospital Infanta Sofía | Hospital Infanta Sofía | SUBWAY_STATION |
| metro_215 | La Fortuna | La Fortuna | SUBWAY_STATION |
| metro_216 | La Peseta | La Peseta | SUBWAY_STATION |
| metro_217 | Carabanchel Alto | Carabanchel Alto | SUBWAY_STATION |
| metro_218 | San Francisco | San Francisco | SUBWAY_STATION |
| metro_219 | Pan Bendito | Pan Bendito | SUBWAY_STATION |
| metro_220 | Abrantes | Abrantes | SUBWAY_STATION |
| metro_221 | Parque Lisboa | Parque Lisboa | SUBWAY_STATION |
| metro_222 | Alcorcón Central | Alcorcon Central | SUBWAY_STATION |
| metro_223 | Parque Oeste | Parque Oeste | SUBWAY_STATION |
| metro_224 | Universidad Rey Juan Carlos | Universidad Rey Juan Carlos | SUBWAY_STATION |
| metro_225 | Móstoles Central | Móstoles Central | SUBWAY_STATION |
| metro_226 | Pradillo | Pradillo | SUBWAY_STATION |
| metro_227 | Hospital de Móstoles | Hospital de Móstoles | SUBWAY_STATION |
| metro_228 | Loranca | Loranca | SUBWAY_STATION |
| metro_229 | Hospital de Fuenlabrada | Hospital de Fuenlabrada | SUBWAY_STATION |
| metro_230 | Parque Europa | Parque Europa | SUBWAY_STATION |
| metro_232 | Parque de los Estados | Parque de los Estados | SUBWAY_STATION |
| metro_233 | Arroyo Culebro | Arroyo Culebro | SUBWAY_STATION |
| metro_234 | Conservatorio | Conservatorio | SUBWAY_STATION |
| metro_235 | Getafe Central | Getafe Central | SUBWAY_STATION |
| metro_236 | El Casar | El Casar | TRAIN_STATION |
| metro_237 | Los Espartales | Los Espartales | SUBWAY_STATION |
| metro_238 | El Bercial | El Bercial | SUBWAY_STATION |
| metro_239 | El Carrascal | El Carrascal | SUBWAY_STATION |
| metro_240 | Casa del Reloj | Casa del Reloj | SUBWAY_STATION |
| metro_241 | Leganés Central | Leganés Central | SUBWAY_STATION |
| metro_242 | San Nicasio | San Nicasio | SUBWAY_STATION |
| metro_243 | Buenos Aires | Buenos Aires | SUBWAY_STATION |
| metro_244 | Miguel Hernández | Miguel Hernández | SUBWAY_STATION |
| metro_245 | Sierra de Guadalupe | Sierra de Guadalupe | SUBWAY_STATION |
| metro_246 | Villa de Vallecas | Villa de Vallecas | SUBWAY_STATION |
| metro_247 | Congosto | Congosto | SUBWAY_STATION |
| metro_248 | Valdecarros | Valdecarros | SUBWAY_STATION |
| metro_250 | Avenida de Guadalajara | Avenida de Guadalajara | SUBWAY_STATION |
| metro_251 | Alsacia | Alsacia | SUBWAY_STATION |
| metro_252 | La Almudena | La Almudena | SUBWAY_STATION |
| metro_253 | San Fermín-Orcasur | San Fermín-Orcasur | SUBWAY_STATION |
| metro_254 | Ciudad de los Ángeles | Ciudad de los Ángeles | SUBWAY_STATION |
| metro_255 | Villaverde Bajo-Cruce | Villaverde Bajo-Cruce | SUBWAY_STATION |
| metro_256 | San Cristóbal | San Cristóbal | SUBWAY_STATION |
| metro_257 | Villaverde Alto | Villaverde Alto | SUBWAY_STATION |
| ml_001 | Pinar de Chamartín | Pinar de Chamartín | SUBWAY_STATION |
| ml_010 | Colonia Jardín | Colonia Jardín | SUBWAY_STATION |
| ml_044 | Reyes Católicos | Reyes Católicos | SUBWAY_STATION |

## Stations that probably WON'T show metro lines (80)

These have `transit_station` but NOT `subway_station` -- Google Maps will show the Place card but likely without the metro line overlay. This is Google's limitation, not a data error.

| ID | Our Name | Google Maps Name | Category | Our Line |
|----|----------|-----------------|----------|----------|
| cercanias_005 | Nuevos Ministerios | Nuevos Ministerios - Cercanías | cercanias | C-2;C-3;C-4;C-7;C-8;C-10 |
| cercanias_006 | Fuente de la Mora | Fuente de la Mora | cercanias | C-1;ML1 |
| cercanias_007 | Aeropuerto T4 | Aeropuerto T4 | cercanias | C-1 |
| cercanias_079 | Puerto de Navacerrada | Puerto de Navacerrada | cercanias | C-9 |
| cercanias_080 | Cotos | Cotos | cercanias | C-9 |
| cercanias_083 | Pitis | Estación de Pitis | cercanias | C-7;C-8 |
| metro_002 | Gran Vía | Metro Gran Vía | metro | 1;5 |
| metro_003 | Tirso de Molina | Estación de Tirso de Molina | metro | 1 |
| metro_013 | Príncipe de Vergara | Metro Príncipe de Vergara | metro | 2;9 |
| metro_014 | Alfonso XIII | Estación de Alfonso XIII | metro | 4 |
| metro_015 | Gregorio Marañón | Estación de Gregorio Marañón | metro | 7;10 |
| metro_022 | Diego de León | Estación de Diego de León | metro | 4;5;6 |
| metro_026 | Estación del Arte | Estación del Arte | metro | 1 |
| metro_031 | Tribunal | Estación de Tribunal | metro | 1;10 |
| metro_039 | O'Donnell | Metro O Donnell | metro | 6 |
| metro_060 | Chamartín | Estación de Madrid-Chamartín-Clara Campoamor | metro | 1;10 |
| metro_062 | Nuevos Ministerios | Estación de Nuevos Ministerios | metro | 6;8;10 |
| metro_076 | Hospital 12 de Octubre | Estación de Hospital 12 de Octubre | metro | 3 |
| metro_095 | Puerta de Toledo | Estación de Puerta de Toledo | metro | 5 |
| metro_100 | Serrano | Metro Serrano | metro | 4 |
| metro_103 | Colón | Metro Colón | metro | 4 |
| metro_107 | Plaza de Castilla | Estación de Plaza de Castilla | metro | 1;9;10 |
| metro_109 | Puente de Vallecas | Estación de Puente de Vallecas | metro | 1 |
| metro_118 | Batán | Batán | metro | 10 |
| metro_144 | Avenida de América | Estación de Avenida de América | metro | 4;6;7;9 |
| metro_167 | Pitis | Estación de Pitis | metro | 7 |
| metro_201 | Aeropuerto T4 | Estación de Aeropuerto T4 | metro | 8 |
| metro_208 | Begoña | Metro Begoña | metro | 10 |
| metro_211 | La Granja | Granja-Est.La Granja | metro | 10 |
| metro_231 | Fuenlabrada Central | Estación de Fuenlabrada Central | metro | 12 |
| metro_249 | Las Rosas | Metro Las Rosas | metro | 2 |
| ml_002 | Fuente de la Mora | Fuente de la Mora | metro_ligero | ML1 |
| ml_003 | Virgen del Cortijo | Virgen del Cortijo | metro_ligero | ML1 |
| ml_004 | Antonio Saura | Antonio Saura | metro_ligero | ML1 |
| ml_005 | Álvarez de Villaamil | Álvarez de Villaamil | metro_ligero | ML1 |
| ml_006 | Blasco Ibáñez | Blasco Ibáñez | metro_ligero | ML1 |
| ml_007 | María Tudor | María Tudor | metro_ligero | ML1 |
| ml_008 | Palas de Rey | Palas de Rey | metro_ligero | ML1 |
| ml_009 | Las Tablas | Estación de Las Tablas | metro_ligero | ML1 |
| ml_011 | Prado de la Vega | Prado de la Vega | metro_ligero | ML2 |
| ml_012 | Colonia de los Ángeles | Colonia de los Ángeles | metro_ligero | ML2 |
| ml_013 | Prado del Rey | Prado del Rey | metro_ligero | ML2 |
| ml_014 | Somosaguas Sur | Somosaguas Sur | metro_ligero | ML2 |
| ml_015 | Somosaguas Centro | Somosaguas Centro | metro_ligero | ML2 |
| ml_016 | Pozuelo Oeste | Pozuelo Oeste | metro_ligero | ML2 |
| ml_017 | Bélgica | Bélgica | metro_ligero | ML2 |
| ml_018 | Dos Castillas | Dos Castillas | metro_ligero | ML2 |
| ml_019 | Campus de Somosaguas | Campus de Somosaguas | metro_ligero | ML2 |
| ml_020 | Avenida de Europa | Avenida de Europa | metro_ligero | ML2 |
| ml_021 | Berna | Berna | metro_ligero | ML2 |
| ml_022 | Estación de Aravaca | Estación de Aravaca | metro_ligero | ML2 |
| ml_023 | Ciudad de la Imagen | Ciudad de la Imagen | metro_ligero | ML3 |
| ml_024 | José Isbert | José Isbert | metro_ligero | ML3 |
| ml_025 | Ciudad del Cine | Ciudad del Cine | metro_ligero | ML3 |
| ml_026 | Cocheras | Cocheras | metro_ligero | ML3 |
| ml_027 | Retamares | Retamares | metro_ligero | ML3 |
| ml_028 | Montepríncipe | Montepríncipe | metro_ligero | ML3 |
| ml_029 | Ventorro del Cano | Ventorro del Cano | metro_ligero | ML3 |
| ml_030 | Prado del Espino | Prado del Espino | metro_ligero | ML3 |
| ml_031 | Cantabria | Cantabria | metro_ligero | ML3 |
| ml_032 | Ferial de Boadilla | Ferial de Boadilla | metro_ligero | ML3 |
| ml_033 | Boadilla Centro | Boadilla Centro | metro_ligero | ML3 |
| ml_034 | Nuevo Mundo | Nuevo Mundo | metro_ligero | ML3 |
| ml_035 | Siglo XXI | Siglo XXI | metro_ligero | ML3 |
| ml_036 | Infante Don Luis | Infante Don Luis | metro_ligero | ML3 |
| ml_037 | Puerta de Boadilla | Puerta de Boadilla | metro_ligero | ML3 |
| ml_038 | Plaza de Toros | Plaza de Toros | metro_ligero | Tranvia Parla |
| ml_039 | Julio Romero de Torres | Julio Romero de Torres | metro_ligero | Tranvia Parla |
| ml_040 | La Ballena | La Ballena | metro_ligero | Tranvia Parla |
| ml_041 | Parla Centro-Bulevar Norte | Parla Centro - Bulevar Norte | metro_ligero | Tranvia Parla |
| ml_042 | Iglesia Centro | Iglesia Centro | metro_ligero | Tranvia Parla |
| ml_043 | Bulevar Sur-Miguel Ángel Blanco | Bulevar Sur | metro_ligero | Tranvia Parla |
| ml_045 | Isabel II | Isabel II | metro_ligero | Tranvia Parla |
| ml_046 | Parque Parla Este | Parque Parla Este | metro_ligero | Tranvia Parla |
| ml_047 | Avenida Sistema Solar | Avenida Sistema Solar | metro_ligero | Tranvia Parla |
| ml_048 | Tierra | Estrella Polar Sur | metro_ligero | Tranvia Parla |
| ml_049 | Venus | Venus Norte | metro_ligero | Tranvia Parla |
| ml_050 | Estrella Polar | Estrella Polar Norte | metro_ligero | Tranvia Parla |
| ml_051 | Jaime I | Jaime I Norte | metro_ligero | Tranvia Parla |
| ml_052 | Polígono Industrial Ciudad de Parla | Poligono Industrial Ciudad de Parla | metro_ligero | Tranvia Parla |

## Other issues (1)

| ID | Our Name | Issue |
|----|----------|-------|
| metro_010 | Chamberí | No Place ID (coordinate fallback) |

## Analysis

### Why some stations don't show metro lines

Google Maps only shows the metro line preview overlay for places tagged as `subway_station`. Many Madrid stations are tagged as `transit_station` instead -- particularly:

1. **All Metro Ligero / Tranvía stations** (52 entries) -- Google treats light rail as generic transit
2. **Some metro stations** that Google hasn't fully tagged (e.g., Gran Vía, Tirso de Molina, Príncipe de Vergara)
3. **Some cercanías stations** where Google uses the generic transit tag

### What can be done

- For `subway_station` entries: everything works perfectly
- For `transit_station` entries: the Place card opens correctly with reviews/photos, but without the line overlay. This is a Google Maps data limitation we cannot fix.
- The `transit_station` entries are still pointing to the CORRECT station -- they just don't have the enhanced subway UI

### Recommendation

Accept the `transit_station` entries as-is. The Place card still works correctly. The metro line overlay is a Google Maps feature that depends on their internal data classification, not something we can control through Place IDs.
