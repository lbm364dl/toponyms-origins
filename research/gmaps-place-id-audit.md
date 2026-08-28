# Google Maps Place ID Audit Report

**Date**: 2026-03-28
**Method**: Nearby Search API for all subway_station/train_station/transit_station in Madrid area, then matched to our 389 stations by name + proximity (<1km)

## Summary

| Type | Count | Metro lines show? |
|------|-------|--------------------|
| `subway_station` | 213 | **Yes** |
| `train_station` | 41 | **Yes** (rail lines) |
| `transit_station` only | 3 | No |
| Not found in nearby search | 132 | Unknown (using previous Place ID) |
| **Total showing lines** | **254** | |

---

## subway_station (213) -- will show metro lines

| ID | Our Name | Google Maps Name | Dist | URL |
|----|----------|-----------------|------|-----|
| cercanias_002 | Sol | Sol | 75m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJf-YYGX4oQg0RRvnJ0KBzhDM) |
| cercanias_003 | Atocha | Atocha | 98m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJA-pTRiQmQg0RSaADkNa57tI) |
| cercanias_004 | Chamartín-Clara Campoamor | Chamartín | 80m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0ZiXfxUpQg0RAW0xyx-572s) |
| cercanias_008 | Príncipe Pío | Príncipe Pío | 67m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJn_Hd820oQg0RgOhjR0WLNbk) |
| cercanias_010 | Delicias | Delicias | 47m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJf0tZ8jAmQg0RCNfaRO_UW5E) |
| cercanias_011 | Pirámides | Pirámides | 82m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD3LgJtAnQg0REkusFhF3_Ew) |
| cercanias_012 | Embajadores | Embajadores | 41m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6eQxKi0mQg0RpzPMa8LPjJc) |
| cercanias_028 | Fuencarral | Fuencarral | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ8xNn-NcrQg0R-2x5h1TOjDk) |
| cercanias_036 | Coslada | Coslada Central | 20m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFVxiygwwQg0R4B6Obpc2090) |
| cercanias_046 | Aluche | Aluche | 64m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD1Y70z6IQQ0Rod6ykz1wisc) |
| cercanias_047 | Maestra Justa Freire-Polideportivo Aluche | Aluche | 844m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD1Y70z6IQQ0Rod6ykz1wisc) |
| cercanias_049 | Cuatro Vientos | Cuatro Vientos | 63m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0WiZWfqIQQ0R_69vfZNhrNg) |
| cercanias_050 | Laguna | Laguna | 54m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ2Rq2cB2IQQ0RuoWf41dcqRU) |
| cercanias_051 | Alcorcón | Alcorcon Central | 360m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJB5GUp8mOQQ0RAZ9Miuj087k) |
| cercanias_056 | Leganés | Leganés Central | 993m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJF-jagSeKQQ0RuymcxlyPSNs) |
| cercanias_058 | Fuenlabrada | Fuenlabrada Central | 732m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJbTQ8UgmLQQ0RFBL7OuOGSzU) |
| cercanias_081 | Mirasierra-Paco de Lucía | Paco de Lucía | 609m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3XkOty4qQg0RczQTYT2nZnU) |
| cercanias_083 | Pitis | Pitis | 52m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJXTFiSx4qQg0RjqEcPSxC6Vw) |
| cercanias_086 | Vallecas | Villa de Vallecas | 470m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_zq1rQAlQg0R8gCWQZInKBo) |
| cercanias_087 | Vicálvaro | Vicálvaro | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJl9WbC28lQg0RFZyJNzOOQ6Q) |
| cercanias_088 | Villaverde Bajo | Villaverde Bajo-Cruce | 967m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJh4VutcImQg0RQXffwqdqvAY) |
| cercanias_089 | Villaverde Alto | Villaverde Alto | 102m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ99N09S8nQg0R7IV_ggFFt4M) |
| metro_001 | Sol | Sol | 75m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJf-YYGX4oQg0RRvnJ0KBzhDM) |
| metro_002 | Gran Vía | Gran Vía | 6m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJofJecocoQg0RSPXAS2CmrzI) |
| metro_003 | Tirso de Molina | Tirso de Molina | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJI5kBZdUnQg0RsfDJDrfChEQ) |
| metro_004 | La Latina | La Latina | 10m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJM1FWdNYnQg0RqexuceK8OVI) |
| metro_005 | Goya | Goya | 36m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJc2ymMLsoQg0RtRQ6-3Bm5a8) |
| metro_006 | Argüelles | Argüelles | 21m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJv5K-rmkoQg0RM7w_cTINTSA) |
| metro_007 | Chueca | Chueca | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJTUSc_oUoQg0RrAraXZMMog0) |
| metro_008 | Embajadores | Embajadores | 41m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6eQxKi0mQg0RpzPMa8LPjJc) |
| metro_009 | Lavapiés | Lavapiés | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0190cCsmQg0RY9JGCic0gg8) |
| metro_011 | Callao | Callao | 57m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6XJ0VHwoQg0RDLS-_d-7IfY) |
| metro_012 | Ópera | Ópera | 29m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJm4wp3HsoQg0R5JKPIWVkVxQ) |
| metro_013 | Príncipe de Vergara | Príncipe de Vergara | 80m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJbR2R2KIoQg0RolNGCond4Es) |
| metro_014 | Alfonso XIII | Alfonso XIII | 3m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJC7i8Z9EoQg0R35y_QjqS0hQ) |
| metro_015 | Gregorio Marañón | Gregorio Marañón | 6m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4Ut95-0oQg0Rb9ofbHZH6jk) |
| metro_016 | Paco de Lucía | Paco de Lucía | 609m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3XkOty4qQg0RczQTYT2nZnU) |
| metro_018 | Príncipe Pío | Príncipe Pío | 67m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJn_Hd820oQg0RgOhjR0WLNbk) |
| metro_019 | Eugenia de Montijo | Eugenia de Montijo | 35m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJz2q-9SSIQQ0REMqzgU6Yp5M) |
| metro_020 | Guzmán el Bueno | Guzmán el Bueno | 153m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJK1xyxVEoQg0Rk1UCDbIr388) |
| metro_021 | Alonso Martínez | Alonso Martínez | 42m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6UwBkI4oQg0RVy4yDVJ-i-M) |
| metro_023 | Vicente Aleixandre | Vicente Aleixandre | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJY6XxFUkoQg0RwZYOd0W6B0U) |
| metro_024 | Concha Espina | Concha Espina | 111m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJkYr1LNkoQg0RCNjl-u-Uknk) |
| metro_025 | Santiago Bernabeu | Santiago Bernabeu | 232m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ06xU_uIoQg0RPrL8BqES33s) |
| metro_026 | Estación del Arte | Estación del Arte | 114m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJNbSXHCYmQg0RUhUT2ytPcTM) |
| metro_027 | Feria de Madrid | Feria de Madrid | 1m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJebEwKFEuQg0Rng0gj_bl5s8) |
| metro_028 | Estadio Metropolitano | Estadio Metropolitano | 114m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJK5RGGOsvQg0RIfL1-A2P_jo) |
| metro_029 | Atocha | Atocha | 98m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJA-pTRiQmQg0RSaADkNa57tI) |
| metro_030 | Pirámides | Pirámides | 82m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD3LgJtAnQg0REkusFhF3_Ew) |
| metro_031 | Tribunal | Tribunal | 16m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_5NFsIkoQg0RfAXGpzkK-AM) |
| metro_032 | Noviciado | Noviciado | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJiYm1emMoQg0RHf6nGz3K1Og) |
| metro_033 | Bilbao | Bilbao | 29m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAWqVEYooQg0RF_BtWEOFyEg) |
| metro_034 | Quevedo | Quevedo | 18m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJK5yy4V8oQg0RmdnLXsE9hyg) |
| metro_035 | Islas Filipinas | Islas Filipinas | 22m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJC_7OuUQoQg0RKoiIjItBEnw) |
| metro_036 | Moncloa | Moncloa | 56m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJQRclnkEoQg0Rp1azo5iACag) |
| metro_040 | Ibiza | Ibiza | 18m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJwTIjXKEoQg0RvaE8c5M3gVQ) |
| metro_042 | Menéndez Pelayo | Menéndez Pelayo | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-3s3ORgmQg0RvCB_yEkDIWs) |
| metro_043 | Ríos Rosas | Ríos Rosas | 26m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJo41Ev_coQg0R2I9y7DImtHY) |
| metro_044 | Iglesia | Iglesia | 52m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJS7SalPQoQg0R4GLSdM1OIKA) |
| metro_045 | Cruz del Rayo | Cruz del Rayo | 36m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJJdy8stwoQg0RY75WB3bP6Qg) |
| metro_047 | Cuatro Caminos | Cuatro Caminos | 22m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJTWzkFFYoQg0RlnOOjyWeBDY) |
| metro_048 | Tetuán | Tetuán | 49m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJCfSmmwYpQg0RabAimogN0UA) |
| metro_049 | Estrecho | Estrecho | 10m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJOb3Ip6opQg0R8NN7JzwBev8) |
| metro_050 | Valdeacederas | Valdeacederas | 13m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJBWa-gw8pQg0R8gFoCdKJuck) |
| metro_051 | Francos Rodríguez | Francos Rodríguez | 10m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJBYoGkK0pQg0Rm6MmlZ8awPs) |
| metro_052 | Carpetana | Carpetana | 24m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD9zQH_UnQg0Rc1kn4cDBF1M) |
| metro_053 | Oporto | Oporto | 59m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJhcovUJInQg0Rp-Pkzh2-i-E) |
| metro_054 | Vista Alegre | Vista Alegre | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ2yuOCosnQg0RoG6hclUmWVc) |
| metro_055 | Carabanchel | Carabanchel | 12m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJG2bh7CCIQQ0RhaD8vIjbs7E) |
| metro_056 | Arturo Soria | Arturo Soria | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJj0QFF9YuQg0RNIev60iWpAA) |
| metro_057 | Esperanza | Esperanza | 47m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJrUGNld4uQg0R3gbIOcd9OVI) |
| metro_058 | Canillas | Canillas | 63m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSQtStuUuQg0R9_1vzL1X_pw) |
| metro_059 | Mar de Cristal | Mar de Cristal | 52m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-3KYFekuQg0RJRA6LI_jzCg) |
| metro_060 | Chamartín | Chamartín | 205m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0ZiXfxUpQg0RAW0xyx-572s) |
| metro_061 | Colombia | Colombia | 14m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJdxJKJScpQg0RsD_IQIMGA_4) |
| metro_063 | Rubén Darío | Rubén Darío | 65m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSzgwMJMoQg0RyeB_mAkFjxE) |
| metro_064 | Núñez de Balboa | Núñez de Balboa | 396m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJGa2HDL8oQg0RlCd1bu0L2Xc) |
| metro_065 | Barajas | Barajas | 2m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFeRYXSAuQg0RALpdT6amn2U) |
| metro_066 | Canillejas | Canillejas | 61m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJrSuAGbEvQg0Rxvswre-3j-c) |
| metro_067 | Torre Arias | Torre Arias | 6m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFZGHfqYvQg0RtqhClFJlZaM) |
| metro_068 | Legazpi | Legazpi | 41m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJT-R8TEgmQg0RJfAxGhoDUtY) |
| metro_069 | Delicias | Delicias | 47m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJf0tZ8jAmQg0RCNfaRO_UW5E) |
| metro_071 | Palos de la Frontera | Palos de La Frontera | 93m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlcuUmC0mQg0RMTxunpxER8M) |
| metro_072 | Pavones | Pavones | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJzZLPOpElQg0RXMS6j65tS4g) |
| metro_073 | Valdebernardo | Valdebernardo | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJIa9e_nUlQg0RXq-Mr9PGK1A) |
| metro_074 | Vicálvaro | Vicálvaro | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJl9WbC28lQg0RFZyJNzOOQ6Q) |
| metro_075 | San Cipriano | San Cipriano | 12m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJZbDfMGglQg0RBw7l8WkWvgQ) |
| metro_076 | Hospital 12 de Octubre | Hospital 12 de Octubre | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJYUo_-FYmQg0RB9MeMhmSFxE) |
| metro_077 | Almendrales | Almendrales | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJdVsp300mQg0RABw82xCmw88) |
| metro_078 | Usera | Usera | 156m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ2wZb9LMnQg0R45jTk6Nxrs0) |
| metro_079 | Plaza Elíptica | Plaza Elíptica | 108m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ13MlfLwnQg0R-YH9kWAiRgU) |
| metro_080 | Puerta de Arganda | Puerta de Arganda | 26m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_-qABEQlQg0RJ3GoE_8GBQo) |
| metro_083 | Tres Olivos | Tres Olivos | 44m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJqVci4tArQg0Ri7k8CmScwls) |
| metro_084 | Montecarmelo | Montecarmelo | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSbEtLs4rQg0RiyNNRvUr-CQ) |
| metro_085 | Las Tablas | Las Tablas | 9m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJe8d-A_ErQg0RfpZQCckcfrQ) |
| metro_086 | Pinar de Chamartín | Pinar de Chamartín | 31m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJofgF-EspQg0RFaHEBttIl48) |
| metro_087 | Antón Martín | Antón Martín | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJs0c7ciomQg0RESKWt1XSy4g) |
| metro_088 | Retiro | Retiro | 74m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJDWKXGZkoQg0RIBjUTC-p43s) |
| metro_089 | Banco de España | Banco de España | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJOZ0IjIQoQg0R30l3FPmBQtY) |
| metro_090 | Sevilla | Sevilla | 69m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4QgoNYEoQg0RWruWQ3Ec1dI) |
| metro_091 | Santo Domingo | Santo Domingo | 137m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJI5YAnnwoQg0R14wi5dk6UmI) |
| metro_092 | San Bernardo | San Bernardo | 34m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJvwHOB2EoQg0RcHRKIIPreuU) |
| metro_093 | Canal | Canal | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJIYkCy1goQg0R_PdahQ_tJHI) |
| metro_094 | Ventura Rodríguez | Ventura Rodríguez | 44m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJcbE8Wm8oQg0Rd5Md362ndPE) |
| metro_095 | Puerta de Toledo | Puerta de Toledo | 37m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJb0FJ0NAnQg0RzMV5ZmZZwMg) |
| metro_096 | Acacias | Acacias | 76m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJsZ0eQNInQg0RAoXdEHMw1B4) |
| metro_097 | Marqués de Vadillo | Marqués de Vadillo | 18m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJGYydKcQnQg0R0hynIjjKnF8) |
| metro_100 | Serrano | Serrano | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJzaDGPJcoQg0REcyjYnGsJ8Y) |
| metro_101 | Velázquez | Velázquez | 37m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJI9cL3pcoQg0R57O6P27ly5c) |
| metro_103 | Colón | Colón | 122m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD0eeT5AoQg0RKmiDgCNgzAQ) |
| metro_104 | República Argentina | República Argentina | 106m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJQRFcdOgoQg0RxBVo0iF5uuk) |
| metro_105 | Alonso Cano | Alonso Cano | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJgbhhIPQoQg0Ry4eZSsMB72Y) |
| metro_106 | Cuzco | Cuzco | 130m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJacixZBwpQg0RTvGJ1kdHr1s) |
| metro_107 | Plaza de Castilla | Plaza de Castilla | 89m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJjXCKHhEpQg0RrYhMTPp19Bg) |
| metro_108 | Alvarado | Alvarado | 14m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJnd9rj1UoQg0R2fRxMzWR_rE) |
| metro_112 | Puerta del Ángel | Puerta del Ángel | 31m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ99i8OQooQg0RYIuxP0Av10A) |
| metro_113 | Alto de Extremadura | Alto de Extremadura | 49m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJre1bcP4nQg0RjwAk8pDITl4) |
| metro_114 | Lucero | Lucero | 36m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJU0XrRwKIQQ0RBsUvma9IamM) |
| metro_115 | Laguna | Laguna | 54m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ2Rq2cB2IQQ0RuoWf41dcqRU) |
| metro_116 | Aluche | Aluche | 64m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD1Y70z6IQQ0Rod6ykz1wisc) |
| metro_117 | Campamento | Campamento | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0TrK72uIQQ0RPMMc3B_dM-I) |
| metro_118 | Batán | Batán | 23m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJOybAJAaIQQ0RVT4ZeBmijd4) |
| metro_119 | Lago | Lago | 3m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSxOOfAYoQg0R7VZdFklbDcM) |
| metro_120 | Casa de Campo | Casa de Campo | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSTZ3qw2IQQ0RXGuKr_hhnNk) |
| metro_121 | Plaza de España | Plaza de España | 25m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ58gOMGUoQg0RD5cSITd7USc) |
| metro_122 | Ciudad Universitaria | Ciudad Universitaria | 60m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJdbFoaTcoQg0RjWSl8mWwAt0) |
| metro_123 | Pío XII | Pío XII | 160m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJKTDW7iQpQg0RJ36JPtrSnqs) |
| metro_124 | Duque de Pastrana | Duque de Pastrana | 137m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJMxtDWzwpQg0RbzDazKziQgo) |
| metro_125 | Herrera Oria | Herrera Oria | 55m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-x1eWoMpQg0R0GCVfDJgkQs) |
| metro_126 | Barrio del Pilar | Barrio del Pilar | 97m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAaI7KZ4pQg0REHaV2J6lXbg) |
| metro_127 | Ventilla | Ventilla | 56m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJO-JELwwpQg0RamdglcrnwyQ) |
| metro_128 | Mirasierra | Mirasierra | 22m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJpd_6CIkpQg0RPuLkicpuH9Y) |
| metro_130 | Suanzes | Suanzes | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJR3W5qg4vQg0RmunnxjHJaZA) |
| metro_131 | Ciudad Lineal | Ciudad Lineal | 35m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJS1jsYBQvQg0RJ1t611jfq0o) |
| metro_132 | Quintana | Quintana | 117m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr4rKNUcvQg0R_X4xaguuTBM) |
| metro_134 | García Noblejas | García Noblejas | 109m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJuz16SG4vQg0RPcOfdNFqEG4) |
| metro_135 | Simancas | Simancas | 313m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJVVFhIHcvQg0ReBIFmxvokp0) |
| metro_136 | Las Musas | Las Musas | 15m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJMUtI7ZYvQg0R99j2u3C3fak) |
| metro_137 | San Blas | San Blas | 59m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSe1Lc5svQg0RfoYQNXiIMro) |
| metro_138 | Pueblo Nuevo | Pueblo Nuevo | 166m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJv2dK8D8vQg0Ro2HfO63SD2Q) |
| metro_139 | Pinar del Rey | Pinar del Rey | 74m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJizn69cQuQg0RMeoBWIgCSiE) |
| metro_140 | Bambú | Bambú | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJi2jxIkcpQg0RIfqPgl3jDzU) |
| metro_142 | Vinateros | Vinateros | 34m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJi3W-5fklQg0RrvZzDm792Ec) |
| metro_143 | Artilleros | Artilleros | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJt0cTUo0lQg0RUZID34izK2o) |
| metro_146 | Antonio Machado | Antonio Machado | 40m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ192QJbwpQg0RMFi7DV-VVPg) |
| metro_147 | Valdezarza | Valdezarza | 66m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJi8Q4XLopQg0R9_cwhJKuxVE) |
| metro_148 | Colonia Jardín | Colonia Jardín | 54m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJacohjmWIQQ0RVjO0Z-ych-c) |
| metro_149 | Opañel | Opañel | 87m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJNYg3AL4nQg0R2IDwcAh-3N0) |
| metro_152 | Juan de la Cierva | Juan de La Cierva | 226m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr-x9a8AgQg0Rmu6Bn84qsYE) |
| metro_155 | Reyes Católicos | Reyes Católicos | 101m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJiQ9PWeIsQg0RTU0qD8nLpmo) |
| metro_156 | Manuel de Falla | Manuel de Falla | 30m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ37qK3pMsQg0Ruyxqp0u7CF8) |
| metro_157 | Marqués de la Valdavia | Marqués de la Valdavia | 96m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJBSYVGfQsQg0Rw-X2oGzfgkQ) |
| metro_158 | Avenida de la Paz | Avenida de La Paz | 33m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJtXFbwCovQg0Rijrm5iyweF0) |
| metro_159 | Alto del Arenal | Alto del Arenal | 47m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJTzcoMMElQg0RqeJBdcjCKLw) |
| metro_161 | Hortaleza | Hortaleza | 52m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJYRk1AsguQg0RuRl6lxvJer4) |
| metro_162 | Manoteras | Manoteras | 20m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHSBqz0opQg0Ree3cRU3nshQ) |
| metro_163 | Empalme | Empalme | 41m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJu5kWnmqIQQ0R96GGJU7QTZw) |
| metro_165 | El Capricho | El Capricho | 15m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHzJoS8wvQg0RCDYvC6Y8EC8) |
| metro_166 | Alameda de Osuna | Alameda de Osuna | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ82DrtywuQg0RzwS3jb5qcjI) |
| metro_167 | Pitis | Pitis | 52m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJXTFiSx4qQg0RjqEcPSxC6Vw) |
| metro_168 | Arroyofresno | Arroyofresno | 16m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJx-ihVPQpQg0R6B9l8lSQ4aY) |
| metro_169 | Lacoma | Lacoma | 18m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3UuHNI0pQg0RWyo8G1wBBi0) |
| metro_170 | La Elipa | La Elipa | 141m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3afgEUUvQg0RX-YYyYu16II) |
| metro_171 | Peñagrande | Peñagrande | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4yy2VZYpQg0Rr_U6Hj6Gr64) |
| metro_173 | Barrio de la Concepción | Barrio de la Concepción | 77m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJhxux4zkvQg0RYH1tCb6EHoA) |
| metro_174 | Ascao | Ascao | 75m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4XVtHmovQg0RjxjghBc6obo) |
| metro_175 | Barrio del Puerto | Barrio del Puerto | 16m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJZ5AJLg8wQg0RYxqDCzChLuw) |
| metro_176 | Coslada Central | Coslada Central | 105m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFVxiygwwQg0R4B6Obpc2090) |
| metro_177 | San Lorenzo | San Lorenzo | 21m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJLdDI4eouQg0R7p6AonsTC2Y) |
| metro_179 | Jarama | Jarama | 84m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFz5mqJ4wQg0R5jsd6XDAAdA) |
| metro_180 | Henares | Henares | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJp7dQI3Y6Qg0RCOLxg5-YXOc) |
| metro_181 | Hospital del Henares | Hospital del Henares | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ7_WTong6Qg0Ry9Bgc_hZfOo) |
| metro_182 | Urgel | Urgel | 105m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr4IWmeonQg0Rte469_zN7Bk) |
| metro_188 | Avenida de la Ilustración | Avenida de la Ilustración | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJb1yt3pMpQg0RUtliRINx6MY) |
| metro_195 | La Rambla | La Rambla | 684m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ8VMZqXswQg0RBCfQynIBspU) |
| metro_200 | Aeropuerto T1-T2-T3 | Aeropuerto T1-T2-T3 | 82m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0RqVaMUxQg0RzmEGI0b6uFs) |
| metro_204 | Puerta del Sur | Puerta del Sur | 12m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJJeApVkaJQQ0Rc-1GxWBJuH0) |
| metro_205 | Joaquín Vilumbrales | Joaquín Vilumbrales | 20m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJkVqqCz-JQQ0RtFxFj3HJIPk) |
| metro_206 | Cuatro Vientos | Cuatro Vientos | 63m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0WiZWfqIQQ0R_69vfZNhrNg) |
| metro_207 | Aviación Española | Aviación Española | 8m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJV06-oViIQQ0RY8O_RMApMCU) |
| metro_208 | Begoña | Begoña | 354m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJF-g-bmkpQg0RrWhIxuFfltw) |
| metro_209 | Fuencarral | Fuencarral | 43m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ8xNn-NcrQg0R-2x5h1TOjDk) |
| metro_210 | Ronda de la Comunicación | Ronda de la Comunicación | 92m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJK5l9UfUrQg0RvCi4thJSoz4) |
| metro_211 | La Granja | La Granja | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6c01vnksQg0RiBj7xLmZITE) |
| metro_212 | La Moraleja | La Moraleja | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaWeA31ssQg0RITg1sTs7_co) |
| metro_213 | Baunatal | Baunatal | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJmztoD-ksQg0RfCWYNZaGGsg) |
| metro_214 | Hospital Infanta Sofía | Hospital Infanta Sofía | 95m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr3aYMz0tQg0RvmQ0pH-KqjM) |
| metro_215 | La Fortuna | La Fortuna | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3-FSx6WJQQ0Rkff0ZWfDijY) |
| metro_216 | La Peseta | La Peseta | 21m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSyhiks6JQQ0Rl8HBqKsm_Ic) |
| metro_217 | Carabanchel Alto | Carabanchel Alto | 14m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJfYCtFy2IQQ0RIqKDgk7BzNg) |
| metro_218 | San Francisco | San Francisco | 12m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6ZTxd4EnQg0RVZ6pcGfB4P4) |
| metro_219 | Pan Bendito | Pan Bendito | 37m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAdzLW4MnQg0RFfHZsaJf0-o) |
| metro_220 | Abrantes | Abrantes | 46m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJdeq48JknQg0RMjHy5YTxsKM) |
| metro_223 | Parque Oeste | Parque Oeste | 39m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJYSDTvZSOQQ0Rri3LuL-djZ0) |
| metro_235 | Getafe Central | Getafe Central | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr88SqKIgQg0RGj23cS1Kmms) |
| metro_240 | Casa del Reloj | Casa del Reloj | 839m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJm-1vjx6KQQ0RnQHGDP8RC2M) |
| metro_241 | Leganés Central | Leganés Central | 145m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJF-jagSeKQQ0RuymcxlyPSNs) |
| metro_244 | Miguel Hernández | Miguel Hernández | 39m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJh2N2ArklQg0RoQ_d9JDcCiM) |
| metro_245 | Sierra de Guadalupe | Sierra de Guadalupe | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJbyBHAqklQg0RO5h2pOkVr1U) |
| metro_246 | Villa de Vallecas | Villa de Vallecas | 28m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_zq1rQAlQg0R8gCWQZInKBo) |
| metro_247 | Congosto | Congosto | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJScxCVv4kQg0RADyNoYd7s0I) |
| metro_248 | Valdecarros | Valdecarros | 118m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJKW0Cd8YkQg0RkfLnDG_Dk-8) |
| metro_249 | Las Rosas | Las Rosas | 31m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJkfISHY0vQg0RyuMLGG_ou6A) |
| metro_250 | Avenida de Guadalajara | Avenida de Guadalajara | 37m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJcVYjjIUvQg0Ru0zfl0MrrQ4) |
| metro_251 | Alsacia | Alsacia | 78m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJJ-LWDn8vQg0R16VMSFKQSU4) |
| metro_252 | La Almudena | La Almudena | 109m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJRexxSWYvQg0RQRwUr1p6xIU) |
| metro_253 | San Fermín-Orcasur | San Fermín-Orcasur | 21m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJyzDiSvgmQg0Rb5GkFblxLcw) |
| metro_254 | Ciudad de los Ángeles | Ciudad de los Ángeles | 55m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJw_TJneUmQg0R_3GR09EpJOc) |
| metro_256 | San Cristóbal | San Cristóbal | 73m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJB5c6BNAmQg0R1qc28DecIQ0) |
| metro_257 | Villaverde Alto | Villaverde Alto | 102m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ99N09S8nQg0R7IV_ggFFt4M) |
| ml_001 | Pinar de Chamartín | Pinar de Chamartín | 31m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJofgF-EspQg0RFaHEBttIl48) |
| ml_009 | Las Tablas | Las Tablas | 9m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJe8d-A_ErQg0RfpZQCckcfrQ) |
| ml_010 | Colonia Jardín | Colonia Jardín | 54m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJacohjmWIQQ0RVjO0Z-ych-c) |

---

## train_station (41) -- will show rail lines

| ID | Our Name | Google Maps Name | Dist | URL |
|----|----------|-----------------|------|-----|
| cercanias_001 | Recoletos | Recoletos | 124m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlWJNnZooQg0RFRoyrFNHp6Y) |
| cercanias_013 | Doce de Octubre | Doce de Octubre | 13m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJJ8F4w1MmQg0RYB6Xo_E11DE) |
| cercanias_014 | Orcasitas | Orcasitas | 816m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJUx3DIAInQg0R260M78Pqg1U) |
| cercanias_015 | Puente Alcocer | Puente Alcocer | 13m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJuaEySiAnQg0Rrvvyixgp41k) |
| cercanias_016 | San Cristóbal de los Ángeles | San Cristóbal de los Ángeles | 31m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJbZ2H4McmQg0RYWW09YmgN94) |
| cercanias_017 | San Cristóbal Industrial | San Cristóbal Industrial | 90m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJNXVEsdQmQg0RDh4k2OgMMTo) |
| cercanias_018 | Getafe Industrial | Getafe Industrial | 24m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFcOv_uMgQg0RyEfGaIfWENE) |
| cercanias_020 | Getafe Sector 3 | Getafe Sector 3 | 0m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJVcl46n0gQg0RLKWf47qokJI) |
| cercanias_021 | Las Margaritas Universidad | Las Margaritas | 15m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJo_Yv37YgQg0RFE7VQRMGtl4) |
| cercanias_022 | El Casar | El Casar | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ1S9OTdogQg0RzPYeKAzSULc) |
| cercanias_023 | Pinto | Pinto | 33m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJKyBlb4IfQg0Rps2eNbyWhTY) |
| cercanias_027 | Parla | Parla | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJV5nQ_DP1QQ0Rvnw6thhNV50) |
| cercanias_029 | Cantoblanco Universidad | Cantoblanco Universidad | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ337eHwMrQg0RbezeFRLxs70) |
| cercanias_030 | Alcobendas-San Sebastián de los Reyes | Alcobendas-San Sebastián de los Reyes | 413m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlVQzxfEsQg0R_wjUqtSJ8Yw) |
| cercanias_031 | El Goloso | El Goloso | 36m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJs1k-P8MqQg0RT6bhya1oGag) |
| cercanias_033 | Asamblea de Madrid-Entrevías | Asamblea de Madrid-Entrevías | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJO2EuJXomQg0RNrajmkhsmns) |
| cercanias_034 | El Pozo | El Pozo | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ7TYNdNMlQg0RRJQQ1wBV-V8) |
| cercanias_035 | Santa Eugenia | Santa Eugenia | 26m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJU0889hAlQg0RGmqYmgfEGq4) |
| cercanias_037 | San Fernando | San Fernando | 25m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJB1H-xfMwQg0RZewT9r6_A84) |
| cercanias_038 | Torrejón de Ardoz | Torrejón de Ardoz | 1m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_6Lbrxg3Qg0RpMFr5i3bXzc) |
| cercanias_039 | Soto del Henares | Soto del Henares | 13m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJcZHQ7Uo2Qg0RiHAeGSko0qI) |
| cercanias_040 | La Garena | La Garena | 22m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlwZGNrxJQg0RoASdnhPVEA0) |
| cercanias_041 | Alcalá de Henares | Alcalá de Henares | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJfVroK2xJQg0RDh30lwqC63g) |
| cercanias_043 | Meco | Meco | 7m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJfzclK01MQg0R-yBKRzBotcg) |
| cercanias_048 | Las Águilas | Las Águilas | 55m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0QtBlVmIQQ0REM_3Z1st4lw) |
| cercanias_053 | Las Retamas | Las Retamas | 869m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJKyqXK7yOQQ0RPGqcQYH6jj4) |
| cercanias_060 | Humanes | Humanes | 656m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJjx_XnqiMQQ0RIwrxYHNLHTU) |
| cercanias_061 | Aravaca | Aravaca | 17m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJK6d64lSGQQ0RXIgc85WI5Hs) |
| cercanias_063 | Pozuelo | Pozuelo | 24m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJGe3K2l6GQQ0R2E6v3H7LWU8) |
| cercanias_064 | Majadahonda | Majadahonda | 35m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJqf89VGuEQQ0RbVWYG4ZJqI0) |
| cercanias_065 | Las Rozas | Las Rozas | 26m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJcwXiJn-DQQ0R1QUY2l3OIn0) |
| cercanias_078 | Cercedilla | Cercedilla | 45m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJQwDNQTVtQQ0RFN6AHGJPud0) |
| cercanias_082 | Ramón y Cajal | Ramón y Cajal | 403m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJe4u_cnspQg0Rb1JlISWrIQk) |
| cercanias_084 | Tres Cantos | Tres Cantos | 45m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJS612_RbVQw0R28J04ohvA98) |
| cercanias_085 | Valdebebas | Valdebebas | 48m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJT3l4BGQuQg0RbjCkqf_c_ZU) |
| cercanias_091 | Valdelasfuentes | Valdelasfuentes | 27m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ11fG25osQg0Rhlh8D0NA5b8) |
| cercanias_092 | Zarzaquemada | Zarzaquemada | 4m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHzqNWeOJQQ0RXyj3kzoqFsI) |
| cercanias_093 | Villalba | Villalba de Guadarrama | 969m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ9QWqVRV0QQ0RICQJoCj0xKc) |
| metro_178 | San Fernando | San Fernando | 25m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJB1H-xfMwQg0RZewT9r6_A84) |
| metro_236 | El Casar | El Casar | 11m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ1S9OTdogQg0RzPYeKAzSULc) |
| ml_041 | Parla Centro-Bulevar Norte | Parla | 512m | [Open](https://www.google.com/maps/place/?q=place_id:ChIJV5nQ_DP1QQ0Rvnw6thhNV50) |

---

## transit_station only (3) -- no line overlay

| ID | Our Name | Google Maps Name | Types | URL |
|----|----------|-----------------|-------|-----|
| ml_042 | Iglesia Centro | Iglesia Centro | ['transit_station'] | [Open](https://www.google.com/maps/place/?q=place_id:ChIJZ01ynDD1QQ0RGK-JDikZrag) |
| ml_043 | Bulevar Sur-Miguel Ángel Blanco | Bulevar Sur | ['transit_station'] | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ2e_nHTv1QQ0RdQR64N4OP3k) |
| ml_045 | Isabel II | Isabel II-Centro de Salud | ['transit_station'] | [Open](https://www.google.com/maps/place/?q=place_id:ChIJOamU7jj1QQ0R4Darq1MGh58) |

---

## Not found in nearby search (132) -- using previous Place IDs

These stations weren't found by the Nearby Search API (search radius may not have covered them). They keep their previously fetched Place IDs.

| ID | Our Name | Previous Google Maps Name | URL |
|----|----------|--------------------------|-----|
| cercanias_005 | Nuevos Ministerios | Nuevos Ministerios - Cercanías | [Open](https://www.google.com/maps/place/?q=place_id:ChIJZ_CdPuUoQg0RzHbOEuQj6SA) |
| cercanias_006 | Fuente de la Mora | Fuente de la Mora | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_RDaRE0pQg0RMVyzc4rP1EI) |
| cercanias_007 | Aeropuerto T4 | Aeropuerto T4 | [Open](https://www.google.com/maps/place/?q=place_id:ChIJiRU8JA8uQg0R23wUDGLmoeo) |
| cercanias_009 | Méndez Álvaro | Méndez Álvaro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaQ2CjxQmQg0RtI6VRGNCR-s) |
| cercanias_019 | Getafe Centro | Getafe Central | [Open](https://www.google.com/maps/place/?q=place_id:ChIJr88SqKIgQg0RGj23cS1Kmms) |
| cercanias_024 | Valdemoro | Valdemoro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJd-yXisweQg0RpfrJ8RPdkgw) |
| cercanias_025 | Ciempozuelos | Ciempozuelos | [Open](https://www.google.com/maps/place/?q=place_id:ChIJufmF7joaQg0RWhezfaRjO3g) |
| cercanias_026 | Aranjuez | Aranjuez | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaVRSsbMFQg0ReZIac8V9SEI) |
| cercanias_032 | Colmenar Viejo | Colmenar Viejo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4Ylp23p-QQ0R3Dici_04giA) |
| cercanias_042 | Alcalá de Henares Universidad | Alcalá de Henares-Universidad | [Open](https://www.google.com/maps/place/?q=place_id:ChIJmRnedapOQg0RIJ0oyEWSZVU) |
| cercanias_044 | Azuqueca | Azuqueca | [Open](https://www.google.com/maps/place/?q=place_id:ChIJMRF1B6RNQg0RnSqOzFkjA7k) |
| cercanias_045 | Guadalajara | Guadalajara | [Open](https://www.google.com/maps/place/?q=place_id:ChIJkXuGKHesQw0R2PcUU9ZT5Is) |
| cercanias_052 | San José de Valderas | San José de Valderas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3R8uaDCJQQ0RgrfnkoZ0EvE) |
| cercanias_054 | Móstoles | Móstoles-El Soto | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHaPui3OOQQ0RbjmDYyzUDrM) |
| cercanias_055 | Móstoles-El Soto | Móstoles-El Soto | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHaPui3OOQQ0RbjmDYyzUDrM) |
| cercanias_057 | Parque Polvoranca | Parque Polvoranca | [Open](https://www.google.com/maps/place/?q=place_id:ChIJVY12uTSKQQ0ROgI669pv33k) |
| cercanias_059 | La Serna-Fuenlabrada | La Serna | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ5Wnqx6-LQQ0RsnJ8_zpKxAY) |
| cercanias_062 | El Barrial-Centro Comercial Pozuelo | El Barrial-Centro Comercial-Pozuelo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJX2UViJOGQQ0RkZfP1jlCYag) |
| cercanias_066 | Pinar | Pinar de Las Rozas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJc1xqExmDQQ0RcaiQjy1qgd4) |
| cercanias_067 | Las Matas | Las Matas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJS4tZaLeCQQ0RIKpfKdUBsAE) |
| cercanias_068 | Torrelodones | Torrelodones | [Open](https://www.google.com/maps/place/?q=place_id:ChIJHzBqdy92QQ0R2PbPyLsKx-0) |
| cercanias_069 | Galapagar-La Navata | Galapagar-La Navata | [Open](https://www.google.com/maps/place/?q=place_id:ChIJn4sVxHt2QQ0R19s0w-gw9V8) |
| cercanias_070 | San Yago | San Yago | [Open](https://www.google.com/maps/place/?q=place_id:ChIJmUAlVfZ0QQ0R64nEMINa5IY) |
| cercanias_071 | El Escorial | El Escorial | [Open](https://www.google.com/maps/place/?q=place_id:ChIJh10BPz8KQQ0Rp1chM0Wy1IU) |
| cercanias_072 | Robledo de Chavela | Robledo de Chavela | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ1acUhWOoQQ0RI0V8x1OTkYA) |
| cercanias_073 | Santa María de la Alameda-Peguerinos | Santa María de la Alameda Peguerinos | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlQYUf5wHQQ0R58NSE16oyQA) |
| cercanias_074 | Los Negrales | Los Negrales | [Open](https://www.google.com/maps/place/?q=place_id:ChIJDf0fp3t0QQ0RkzTtaUYqEQU) |
| cercanias_075 | Alpedrete | Alpedrete | [Open](https://www.google.com/maps/place/?q=place_id:ChIJJc7h33BzQQ0RkPMC0Wpu9RE) |
| cercanias_076 | Collado Mediano | Collado Mediano | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaW1jpPtyQQ0RMxZ0y6BnblI) |
| cercanias_077 | Los Molinos | Los Molinos-Guadarrama | [Open](https://www.google.com/maps/place/?q=place_id:ChIJh7YOqbVyQQ0RQQAKWhWJdRg) |
| cercanias_079 | Puerto de Navacerrada | Puerto de Navacerrada | [Open](https://www.google.com/maps/place/?q=place_id:ChIJIS6BwT5sQQ0RoMCQynY8cAo) |
| cercanias_080 | Cotos | Cotos | [Open](https://www.google.com/maps/place/?q=place_id:ChIJqdGyrjlpQQ0RQdciBCQ7z30) |
| cercanias_090 | Universidad P. Comillas | Universidad Pontificia de Comillas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAybyOhUrQg0R2GIGPSEqnF0) |
| cercanias_094 | Las Zorreras | Las Zorreras | [Open](https://www.google.com/maps/place/?q=place_id:ChIJpR3SLeF0QQ0RRZEx_9m-A9Y) |
| cercanias_095 | Zarzalejo | Zarzalejo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJT0c-OTanQQ0RlXQ1R4Dcke8) |
| metro_010 | Chamberí | Estación de Chamberí (museo) | [Open](N/A) |
| metro_017 | Manuela Malasaña | Manuela Malasaña | [Open](https://www.google.com/maps/place/?q=place_id:ChIJz5rq6DSMQQ0RP4W1OYIm7yI) |
| metro_022 | Diego de León | Estación de Diego de León | [Open](https://www.google.com/maps/place/?q=place_id:ChIJpws-hMcoQg0RfP56Q214KNY) |
| metro_037 | Ventas | Ventas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJWaBp6rQoQg0RJME5wlQxaPo) |
| metro_038 | Manuel Becerra | Manuel Becerra | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ4-DvF7EoQg0Ruliy_HrLLcA) |
| metro_039 | O'Donnell | Metro O Donnell | [Open](https://www.google.com/maps/place/?q=place_id:ChIJE5ak-64oQg0RESqy-67m-VY) |
| metro_041 | Pacífico | Pacífico | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ17cb_xAmQg0RzC3qcBqbg54) |
| metro_046 | Prosperidad | Prosperidad | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaTUbK8UoQg0RDxkUJc8HHRQ) |
| metro_062 | Nuevos Ministerios | Estación de Nuevos Ministerios | [Open](https://www.google.com/maps/place/?q=place_id:ChIJl05g2eQoQg0RxUzptEglylA) |
| metro_070 | Méndez Álvaro | Méndez Álvaro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaQ2CjxQmQg0RtI6VRGNCR-s) |
| metro_081 | Arganda del Rey | Arganda del Rey | [Open](https://www.google.com/maps/place/?q=place_id:ChIJyY49Kw8_Qg0RssvXtF_eIsU) |
| metro_082 | La Poveda | La Poveda | [Open](https://www.google.com/maps/place/?q=place_id:ChIJozaey8E-Qg0R6K8Ue4L1ta8) |
| metro_098 | Conde de Casal | Conde de Casal | [Open](https://www.google.com/maps/place/?q=place_id:ChIJsyyI8AQmQg0R5ZtcMaNcOTw) |
| metro_099 | Sainz de Baranda | Sainz de Baranda | [Open](https://www.google.com/maps/place/?q=place_id:ChIJMcegyakoQg0RspVg2Ts-oGA) |
| metro_102 | Lista | Lista | [Open](https://www.google.com/maps/place/?q=place_id:ChIJKSS0fbkoQg0RLSQJxXlCq0Y) |
| metro_109 | Puente de Vallecas | Estación de Puente de Vallecas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAclCeQ4mQg0Rdv6S3_iX3rk) |
| metro_110 | Nueva Numancia | Nueva Numancia | [Open](https://www.google.com/maps/place/?q=place_id:ChIJG_Gi7womQg0R8ix0fUNK4Dk) |
| metro_111 | Portazgo | Portazgo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJVxyAP94lQg0RWCLK2y3bLcY) |
| metro_129 | Arganzuela-Planetario | Arganzuela-Planetario | [Open](https://www.google.com/maps/place/?q=place_id:ChIJH1zNoDgmQg0R2MvdPzaO72Q) |
| metro_133 | El Carmen | El Carmen | [Open](https://www.google.com/maps/place/?q=place_id:ChIJA0D100svQg0R0VhfGfseY8s) |
| metro_141 | Estrella | Estrella | [Open](https://www.google.com/maps/place/?q=place_id:ChIJTUOhLf4lQg0RNSXX5_Ot934) |
| metro_144 | Avenida de América | Estación de Avenida de América | [Open](https://www.google.com/maps/place/?q=place_id:ChIJSbxOvMYoQg0RklRYC9nHTVM) |
| metro_145 | Cartagena | Cartagena | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAT2oVM8oQg0Ri3in1v9TZ_4) |
| metro_150 | Rivas Vaciamadrid | Rivas Vaciamadrid | [Open](https://www.google.com/maps/place/?q=place_id:ChIJL_Iwy3I8Qg0RR5HzZZb5lCQ) |
| metro_151 | Julián Besteiro | Julián Besteiro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-ebM9fmJQQ0RaFU5JJTuSJk) |
| metro_153 | Alonso de Mendoza | Alonso de Mendoza | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3XjlPJsgQg0R5If5ltjJW9w) |
| metro_154 | Hospital Severo Ochoa | Hospital Severo Ochoa | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ6X_ZnSOKQQ0R-u3KkS1MnMo) |
| metro_160 | Parque de Santa María | Parque de Sta. María | [Open](https://www.google.com/maps/place/?q=place_id:ChIJd9-YEr8uQg0RAT_8zJofkl0) |
| metro_164 | La Gavia | La Gavia | [Open](https://www.google.com/maps/place/?q=place_id:ChIJD6ukRPskQg0RzXV5ZBoEs1U) |
| metro_172 | Parque de las Avenidas | Parque de Las Avenidas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJpf8qWMsoQg0R_VK56I29TzY) |
| metro_201 | Aeropuerto T4 | Estación de Aeropuerto T4 | [Open](https://www.google.com/maps/place/?q=place_id:ChIJrSH10gguQg0RwH8ispgXMmw) |
| metro_202 | Rivas-Urbanizaciones | Rivas Urbanizaciones | [Open](https://www.google.com/maps/place/?q=place_id:ChIJLzzLYQ87Qg0RX9YbWv9BgQc) |
| metro_203 | Rivas Futura | Rivas Futura | [Open](https://www.google.com/maps/place/?q=place_id:ChIJz3M37os7Qg0RfRuBdYDokWU) |
| metro_221 | Parque Lisboa | Parque Lisboa | [Open](https://www.google.com/maps/place/?q=place_id:ChIJleUGuTWJQQ0Ru4W57ZH6sGg) |
| metro_222 | Alcorcón Central | Alcorcon Central | [Open](https://www.google.com/maps/place/?q=place_id:ChIJB5GUp8mOQQ0RAZ9Miuj087k) |
| metro_224 | Universidad Rey Juan Carlos | Universidad Rey Juan Carlos | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFbNTOXuOQQ0R4wMG8MGo_QA) |
| metro_225 | Móstoles Central | Móstoles Central | [Open](https://www.google.com/maps/place/?q=place_id:ChIJmdoSV4COQQ0RU2E-0IzehSA) |
| metro_226 | Pradillo | Pradillo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ92pWRSuMQQ0RpQ46MuZ6I9U) |
| metro_227 | Hospital de Móstoles | Hospital de Móstoles | [Open](https://www.google.com/maps/place/?q=place_id:ChIJlcmlFtCNQQ0RB4llcSkxLtk) |
| metro_228 | Loranca | Loranca | [Open](https://www.google.com/maps/place/?q=place_id:ChIJmT7ZeG-MQQ0Rn0r0G0mcVJU) |
| metro_229 | Hospital de Fuenlabrada | Hospital de Fuenlabrada | [Open](https://www.google.com/maps/place/?q=place_id:ChIJR3lJaHiLQQ0RURkrYGQ5awk) |
| metro_230 | Parque Europa | Parque Europa | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-9EjG3WLQQ0RRlNnKHDs0Yo) |
| metro_231 | Fuenlabrada Central | Estación de Fuenlabrada Central | [Open](https://www.google.com/maps/place/?q=place_id:ChIJoQri4guLQQ0RrA6iH3Ab0rg) |
| metro_232 | Parque de los Estados | Parque de los Estados | [Open](https://www.google.com/maps/place/?q=place_id:ChIJA1uOiwCLQQ0RLi4W5J4CLs0) |
| metro_233 | Arroyo Culebro | Arroyo Culebro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJs1KB14mKQQ0RSXBYknDPfe8) |
| metro_234 | Conservatorio | Conservatorio | [Open](https://www.google.com/maps/place/?q=place_id:ChIJIRF6IX-KQQ0R0zdaIZNeteI) |
| metro_237 | Los Espartales | Los Espartales | [Open](https://www.google.com/maps/place/?q=place_id:ChIJFXOgNMkgQg0RA3wVzMKhjwE) |
| metro_238 | El Bercial | El Bercial | [Open](https://www.google.com/maps/place/?q=place_id:ChIJw9fnFLMgQg0RH9JwgzRTj9A) |
| metro_239 | El Carrascal | El Carrascal | [Open](https://www.google.com/maps/place/?q=place_id:ChIJRbQg7VYnQg0Rpy9aaL5FssA) |
| metro_242 | San Nicasio | San Nicasio | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0w1kpYWJQQ0Rxzl9M70ba2s) |
| metro_243 | Buenos Aires | Buenos Aires | [Open](https://www.google.com/maps/place/?q=place_id:ChIJc4mDHd0lQg0R3_qO05xk5ZI) |
| metro_255 | Villaverde Bajo-Cruce | Villaverde Bajo-Cruce | [Open](https://www.google.com/maps/place/?q=place_id:ChIJh4VutcImQg0RQXffwqdqvAY) |
| ml_002 | Fuente de la Mora | Fuente de la Mora | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_RDaRE0pQg0RMVyzc4rP1EI) |
| ml_003 | Virgen del Cortijo | Virgen del Cortijo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJt6AfGK0uQg0Rp6C60TnNRRk) |
| ml_004 | Antonio Saura | Antonio Saura | [Open](https://www.google.com/maps/place/?q=place_id:ChIJGXa4IbAuQg0Rt0q0LPq7AVc) |
| ml_005 | Álvarez de Villaamil | Álvarez de Villaamil | [Open](https://www.google.com/maps/place/?q=place_id:ChIJN2L7kKUuQg0R8qCQKr_O9D0) |
| ml_006 | Blasco Ibáñez | Blasco Ibáñez | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_05UoqkuQg0Ry2DG9NHLHls) |
| ml_007 | María Tudor | María Tudor | [Open](https://www.google.com/maps/place/?q=place_id:ChIJpXE4uQEsQg0RtK6uSm6TseA) |
| ml_008 | Palas de Rey | Palas de Rey | [Open](https://www.google.com/maps/place/?q=place_id:ChIJowdP1PkrQg0Recnze0GuBJs) |
| ml_011 | Prado de la Vega | Prado de la Vega | [Open](https://www.google.com/maps/place/?q=place_id:ChIJOdaX-3yIQQ0RJIIm08LfhwQ) |
| ml_012 | Colonia de los Ángeles | Colonia de los Ángeles | [Open](https://www.google.com/maps/place/?q=place_id:ChIJZ_Jzg4CIQQ0RIcZItNyhMTg) |
| ml_013 | Prado del Rey | Prado del Rey | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-7oqdyqGQQ0RZV-Dz0qYyfk) |
| ml_014 | Somosaguas Sur | Somosaguas Sur | [Open](https://www.google.com/maps/place/?q=place_id:ChIJM2klMi-GQQ0RACyKAey-5jg) |
| ml_015 | Somosaguas Centro | Somosaguas Centro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJqc8EsCSGQQ0R-7zyHCSQF1U) |
| ml_016 | Pozuelo Oeste | Pozuelo Oeste | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ5dMniD2GQQ0Rkv6Us_6O94k) |
| ml_017 | Bélgica | Bélgica | [Open](https://www.google.com/maps/place/?q=place_id:ChIJaRgSJWuGQQ0RSJ6TJux7pGo) |
| ml_018 | Dos Castillas | Dos Castillas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJLUbi_UCGQQ0RNGgB1pQnRWE) |
| ml_019 | Campus de Somosaguas | Campus de Somosaguas | [Open](https://www.google.com/maps/place/?q=place_id:ChIJgWOxMEaGQQ0RvgmqHXfFELI) |
| ml_020 | Avenida de Europa | Avenida de Europa | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0S2g6k-GQQ0RHONhidcBMKY) |
| ml_021 | Berna | Berna | [Open](https://www.google.com/maps/place/?q=place_id:ChIJkbYmJVGGQQ0RMXn4Z_iqq5c) |
| ml_022 | Estación de Aravaca | Estación de Aravaca | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0zSG4lSGQQ0R4AGjK10cN8s) |
| ml_023 | Ciudad de la Imagen | Ciudad de la Imagen | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ3f79eGKIQQ0RPQKmG72NVps) |
| ml_024 | José Isbert | José Isbert | [Open](https://www.google.com/maps/place/?q=place_id:ChIJeQ2ZpY6IQQ0Rm_wguTE__xE) |
| ml_025 | Ciudad del Cine | Ciudad del Cine | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ84X0H5KIQQ0RJaZ8iAAkKa4) |
| ml_026 | Cocheras | Cocheras | [Open](https://www.google.com/maps/place/?q=place_id:ChIJxbVVLZaIQQ0RAKcXkKh6RRQ) |
| ml_027 | Retamares | Retamares | [Open](https://www.google.com/maps/place/?q=place_id:ChIJoYIuKbCIQQ0RCwQqMtzz7Ro) |
| ml_028 | Montepríncipe | Montepríncipe | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0x__TkWPQQ0RnRXjQqvMn2Q) |
| ml_029 | Ventorro del Cano | Ventorro del Cano | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ899IN0SPQQ0RwbYZG_WEEp4) |
| ml_030 | Prado del Espino | Prado del Espino | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0YNkB2mPQQ0Rj_aJPyC5fG4) |
| ml_031 | Cantabria | Cantabria | [Open](https://www.google.com/maps/place/?q=place_id:ChIJLXSiyXePQQ0RJqj9BUsS9Is) |
| ml_032 | Ferial de Boadilla | Ferial de Boadilla | [Open](https://www.google.com/maps/place/?q=place_id:ChIJbefeyo6PQQ0RM2mkfxOONR8) |
| ml_033 | Boadilla Centro | Boadilla Centro | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ_TAwCGKFQQ0RjHbjUYcR6oQ) |
| ml_034 | Nuevo Mundo | Nuevo Mundo | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ9Tp8tYqPQQ0RdZ38YI9alP8) |
| ml_035 | Siglo XXI | Siglo XXI | [Open](https://www.google.com/maps/place/?q=place_id:ChIJCXW7RvaPQQ0R4hbW9o7WIik) |
| ml_036 | Infante Don Luis | Infante Don Luis | [Open](https://www.google.com/maps/place/?q=place_id:ChIJW-24cviPQQ0RDN-7_MBtvgY) |
| ml_037 | Puerta de Boadilla | Puerta de Boadilla | [Open](https://www.google.com/maps/place/?q=place_id:ChIJIcloClWFQQ0RBPsgoXgdR-c) |
| ml_038 | Plaza de Toros | Plaza de Toros | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ72YNFUz1QQ0Rd6M4oV8mSBY) |
| ml_039 | Julio Romero de Torres | Julio Romero de Torres | [Open](https://www.google.com/maps/place/?q=place_id:ChIJQ-2K9Ur1QQ0RPuhnhgI79MI) |
| ml_040 | La Ballena | La Ballena | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ0SV8HTX1QQ0RqVCy9U2LhjA) |
| ml_044 | Reyes Católicos | Reyes Católicos | [Open](https://www.google.com/maps/place/?q=place_id:ChIJiQ9PWeIsQg0RTU0qD8nLpmo) |
| ml_046 | Parque Parla Este | Parque Parla Este | [Open](https://www.google.com/maps/place/?q=place_id:ChIJL9V7MkD1QQ0RNH_L9BOy0ak) |
| ml_047 | Avenida Sistema Solar | Avenida Sistema Solar | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-7btmWv1QQ0RX7klfiG1uVY) |
| ml_048 | Tierra | Estrella Polar Sur | [Open](https://www.google.com/maps/place/?q=place_id:ChIJ-WZfLEP1QQ0RGQr09VSgsLE) |
| ml_049 | Venus | Venus Norte | [Open](https://www.google.com/maps/place/?q=place_id:ChIJAxDDwGf1QQ0RYoP5Z1wRr4c) |
| ml_050 | Estrella Polar | Estrella Polar Norte | [Open](https://www.google.com/maps/place/?q=place_id:ChIJm9gKql31QQ0Rg2JJrtB8bLY) |
| ml_051 | Jaime I | Jaime I Norte | [Open](https://www.google.com/maps/place/?q=place_id:ChIJebxX6lv1QQ0Rp60WWLFKd2U) |
| ml_052 | Polígono Industrial Ciudad de Parla | Poligono Industrial Ciudad de Parla | [Open](https://www.google.com/maps/place/?q=place_id:ChIJO8q6mlD1QQ0RggL6mK76KPI) |

---

## Notes

- The Nearby Search API has a 60-result limit per request. Multiple overlapping search circles were used to cover the Madrid metro area.
- 132 stations weren't found by nearby search -- these are in less covered areas or have names that didn't match. They retain their previously fetched Place IDs from the Find Place API.
- `subway_station` type guarantees the Google Maps metro line overlay will show.
- `train_station` shows rail line information (Cercanías, AVE, etc.).
- `transit_station` without subway/train shows a generic transit stop without line overlay.
