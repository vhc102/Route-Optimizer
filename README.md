
# Route Optimizer


## Run Locally

Go to the project directory

```bash
  cd route_optimizer
```
### Google Maps API Key Setup

Follow the [Google Maps API Key documentation](https://developers.google.com/maps/documentation/javascript/get-api-key) to generate and integrate your API key.

Edit Setting.py for API Key

```bash
  GOOGLE_MAPS_API_KEY=""
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Migrate models in Default DB 

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver

  output: http://127.0.0.1:8000/
```

Swagger UI

```bash
  http://127.0.0.1:8000/swagger/
```



## API Reference

#### Post Route

```http
  POST api/fuel-route/
```
 ### Request Body
| Parameter | Type     | Description                                                     |
| :-------- | :------- |:----------------------------------------------------------------|
| `start` | `string` | **Required**. e.g. Los+Angeles,+CA / 34.058151,-118.2464767     |
 |
| `finish` | `string` | **Required**. e.g.  San+Francisco,+CA / 37.7749552,-122.4195329 |

### Output 
```output
    {
  "route": {
    "total_distance": 381.8117986255235,
    "steps": [
      {
        "location": {
          "lat": 34.058151,
          "lng": -118.2464767
        },
        "distance": 502
      },
      {
        "location": {
          "lat": 34.0598748,
          "lng": -118.2447034
        },
        "distance": 252
      },
      {
        "location": {
          "lat": 34.0601384,
          "lng": -118.2448707
        },
        "distance": 44
      },
      {
        "location": {
          "lat": 34.1484369,
          "lng": -118.3723822
        },
        "distance": 16028
      },
      {
        "location": {
          "lat": 34.1495184,
          "lng": -118.3734971
        },
        "distance": 159
      },
      {
        "location": {
          "lat": 34.2283241,
          "lng": -118.410259
        },
        "distance": 9690
      },
      {
        "location": {
          "lat": 34.3009935,
          "lng": -118.4772619
        },
        "distance": 10390
      },
      {
        "location": {
          "lat": 34.3035685,
          "lng": -118.4792575
        },
        "distance": 345
      },
      {
        "location": {
          "lat": 34.3029659,
          "lng": -118.4803761
        },
        "distance": 124
      },
      {
        "location": {
          "lat": 34.315192,
          "lng": -118.4908635
        },
        "distance": 1676
      },
      {
        "location": {
          "lat": 34.3327093,
          "lng": -118.5062132
        },
        "distance": 2561
      },
      {
        "location": {
          "lat": 34.3343205,
          "lng": -118.5046857
        },
        "distance": 228
      },
      {
        "location": {
          "lat": 35.0069583,
          "lng": -118.9516054
        },
        "distance": 93861
      },
      {
        "location": {
          "lat": 37.5934953,
          "lng": -121.3365778
        },
        "distance": 363366
      },
      {
        "location": {
          "lat": 37.6907284,
          "lng": -122.0936911
        },
        "distance": 74592
      },
      {
        "location": {
          "lat": 37.8267344,
          "lng": -122.2868635
        },
        "distance": 25119
      },
      {
        "location": {
          "lat": 37.770568,
          "lng": -122.4058951
        },
        "distance": 13270
      },
      {
        "location": {
          "lat": 37.7696913,
          "lng": -122.4164776
        },
        "distance": 1082
      },
      {
        "location": {
          "lat": 37.7719067,
          "lng": -122.4233536
        },
        "distance": 696
      },
      {
        "location": {
          "lat": 37.7749552,
          "lng": -122.4195329
        },
        "distance": 480
      }
    ]
  },
  "fuel_costs": {
    "stops": [
      {
        "location": {
          "lat": 37.7749552,
          "lng": -122.4195329
        },
        "cost": 133.63412951893324
      }
    ],
    "total_cost": 133.63412951893324
  },
  "gas_stations": [
    {
      "location": {
        "lat": 34.3343205,
        "lng": -118.5046857
      },
      "stations": [
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 34.3678654,
              "lng": -118.5094662
            },
            "viewport": {
              "northeast": {
                "lat": 34.3692061302915,
                "lng": -118.5079854197085
              },
              "southwest": {
                "lat": 34.3665081697085,
                "lng": -118.5106833802915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Shell",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 1193,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/112103543697727637279\">Shell</a>"
              ],
              "photo_reference": "AWYs27wEDis8gZJ0f9kmnkC7-Zx_rPV1lSU8ny395RqWkR1p1ERdV3GONp588a9OEZIBRkHCwwAIPvUNQaES-Kdjd8yiW0wa9fo8iEbDQHhGxW775ddW-zClCQwrUdn3i3_2ZqCuKTrPPPSCe608KWBz0hIiy8kl0_BApkD_heDZUJrR_StS",
              "width": 2119
            }
          ],
          "place_id": "ChIJyaB9DOCFwoARaV3u8bfwzds",
          "plus_code": {
            "compound_code": "9F9R+46 Newhall, Santa Clarita, CA, USA",
            "global_code": "85639F9R+46"
          },
          "price_level": 2,
          "rating": 3.3,
          "reference": "ChIJyaB9DOCFwoARaV3u8bfwzds",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "convenience_store",
            "atm",
            "finance",
            "food",
            "store",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 88,
          "vicinity": "23502 Newhall Avenue, Newhall"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 34.3657433,
              "lng": -118.5068982
            },
            "viewport": {
              "northeast": {
                "lat": 34.3671221802915,
                "lng": -118.5053761697085
              },
              "southwest": {
                "lat": 34.3644242197085,
                "lng": -118.5080741302915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Chevron",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 4032,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/100533358893010931826\">Ayu yukie</a>"
              ],
              "photo_reference": "AWYs27yA-yWX8lKPoMeajO35-Qd8Vwnkwj1TP6F7JuK79swdlUiHdeIkYTmRnqm_IGItNCK4UjW-XW0GDOanDC9vBdkSpuxJezZ92rL-gG-4khE-7777gakWRdkmHxoSULMCN-BUzr8UiHUdcCWv9T2GVZ6Nk3ocjB0bTIrYzvVlA7h-fiGM",
              "width": 3024
            }
          ],
          "place_id": "ChIJZ-PSuaSFwoARAp4NxMRo8wA",
          "plus_code": {
            "compound_code": "9F8V+76 Newhall, Santa Clarita, CA, USA",
            "global_code": "85639F8V+76"
          },
          "rating": 2.7,
          "reference": "ChIJZ-PSuaSFwoARAp4NxMRo8wA",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "convenience_store",
            "food",
            "store",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 53,
          "vicinity": "20500 Newhall Avenue, Newhall"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 34.30350310000001,
              "lng": -118.4786573
            },
            "viewport": {
              "northeast": {
                "lat": 34.3049289302915,
                "lng": -118.4774242697085
              },
              "southwest": {
                "lat": 34.3022309697085,
                "lng": -118.4801222302915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Roxford Chevron",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 3024,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/113712288539694305322\">C S</a>"
              ],
              "photo_reference": "AWYs27wjvlA1Qlc_PQX6MXzmNfEqjdwbughyqzO4OXqsyy1XAbye5WTuiD1ARvsqgQgMKSsDwYx8dYtY-OEvcRpWwHEBSptzxGrCV309VPFFXxKda-idGapBJUKWD2LqlbLb3LS6Wi4lD8c_JhlEbdJ7pA_sTPlSFFbYh9kfJchiy2dduXl2",
              "width": 4032
            }
          ],
          "place_id": "ChIJpXufSPqPwoARGKnTGmiF68U",
          "plus_code": {
            "compound_code": "8G3C+CG Sylmar, Los Angeles, CA, USA",
            "global_code": "85638G3C+CG"
          },
          "rating": 3.3,
          "reference": "ChIJpXufSPqPwoARGKnTGmiF68U",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "convenience_store",
            "car_repair",
            "food",
            "store",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 43,
          "vicinity": "12881 Encinitas Avenue, Sylmar"
        },
        
    {
      "location": {
        "lat": 37.6907284,
        "lng": -122.0936911
      },
      "stations": [
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 37.69995009999999,
              "lng": -122.1214083
            },
            "viewport": {
              "northeast": {
                "lat": 37.7013370302915,
                "lng": -122.1200977197085
              },
              "southwest": {
                "lat": 37.6986390697085,
                "lng": -122.1227956802915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "76",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 2353,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/107721404123505875377\">Trap Speed 1320</a>"
              ],
              "photo_reference": "AWYs27ycFbZgz75PySr_Isz0BaBExz2uUjtO-obGGtwDQEZTowYJ0tzbJyLK3GNPIEagzZTPMvGSMojkvGfQukrPPRUle_6t0AgriQ639B-o56_C_rfMi40wkdIBE_uC8XMoRZuYZ8gW_-FTBu4LvQFJds004pr5tzW-Wo-k-GoPSw7ibpC1",
              "width": 3948
            }
          ],
          "place_id": "ChIJBSEROM6Rj4ARKME5f3SEVmk",
          "plus_code": {
            "compound_code": "MVXH+XC San Leandro, CA, USA",
            "global_code": "849VMVXH+XC"
          },
          "price_level": 2,
          "rating": 4.2,
          "reference": "ChIJBSEROM6Rj4ARKME5f3SEVmk",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 87,
          "vicinity": "15803 East 14th Street, San Leandro"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 37.6671195,
              "lng": -122.0787729
            },
            "viewport": {
              "northeast": {
                "lat": 37.6684549302915,
                "lng": -122.0774882697085
              },
              "southwest": {
                "lat": 37.6657569697085,
                "lng": -122.0801862302915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Chevron",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 3024,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/104853529503706238407\">spider91 fc</a>"
              ],
              "photo_reference": "AWYs27wEfZ534Od95cPf4OjN-BySMj2uHvhom-yvg1_dR2FcjsQduQ7-vHXM7Lyyv2jXKmg9HbXN2LJqpv1-Byevt34e40KXtCEUFbQgKAOSN0T6OSNbHo6BafBW-Cndk6RInfxJdS5Iuqw50ocZarmexKufqIf8EGZW2TsR0gwGo5YP4mSF",
              "width": 4032
            }
          ],
          "place_id": "ChIJIZv8E96Tj4ARokXUw5YUjCw",
          "plus_code": {
            "compound_code": "MW8C+RF Hayward, CA, USA",
            "global_code": "849VMW8C+RF"
          },
          "rating": 3.8,
          "reference": "ChIJIZv8E96Tj4ARokXUw5YUjCw",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "convenience_store",
            "car_repair",
            "store",
            "food",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 25,
          "vicinity": "24086 Mission Boulevard, Hayward"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 37.6949484,
              "lng": -122.0853653
            },
            "viewport": {
              "northeast": {
                "lat": 37.6963419302915,
                "lng": -122.0840395697085
              },
              "southwest": {
                "lat": 37.6936439697085,
                "lng": -122.0867375302915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
          "icon_background_color": "#4B96F3",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/convenience_pinlet",
          "name": "ampm",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 490,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/110180128269318512569\">ampm</a>"
              ],
              "photo_reference": "AWYs27zC-MVY5JwWmQWh9izzPur0CWALI-hFsMBGraqQE7NUWRoqbskjXNnjMqqrAseZbsU3tKTM8mISyzd48TkalqSJX-lvcIQHBZlFa4wQTgAokgEZbZREBX_fCcP3RrzpsZtG09Se86ODhMXM_1yYmppZ-wKjSrtdM5j7nlNY1ew-XOUh",
              "width": 863
            }
          ],
          "place_id": "ChIJp797SoiRj4ARcwp5YQkPc9g",
          "plus_code": {
            "compound_code": "MWV7+XV Castro Valley, CA, USA",
            "global_code": "849VMWV7+XV"
          },
          "price_level": 1,
          "rating": 3.5,
          "reference": "ChIJp797SoiRj4ARcwp5YQkPc9g",
          "scope": "GOOGLE",
          "types": [
            "convenience_store",
            "atm",
            "supermarket",
            "gas_station",
            "grocery_or_supermarket",
            "cafe",
            "finance",
            "store",
            "restaurant",
            "food",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 8,
          "vicinity": "2770 Castro Valley Boulevard, Castro Valley"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 37.6931612,
              "lng": -122.110783
            },
            "viewport": {
              "northeast": {
                "lat": 37.6944532302915,
                "lng": -122.1094411197085
              },
              "southwest": {
                "lat": 37.6917552697085,
                "lng": -122.1121390802915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Chevron",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 4032,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/105045503580080596728\">Frank Peyton</a>"
              ],
              "photo_reference": "AWYs27wUE04tmLwzEVXqR22qaqh-EWqclFrysA5UEj_yncMnvYJvXXCSk4G3BCMxB-taXbYdF43wVz_N6v7toWQVHc44zzsH-268HfFowP9JD_TK5QPtTXRXeSaLwb0SkHEdoHmdv7t7cQF5GdbuPBB844gXRH6_q_5ynBjx6UEnM1fjGL8U",
              "width": 3024
            }
          ],
          "place_id": "ChIJDQzrOL-Rj4ARpkbFXepPwXc",
          "plus_code": {
            "compound_code": "MVVQ+7M San Leandro, CA, USA",
            "global_code": "849VMVVQ+7M"
          },
          "rating": 3.1,
          "reference": "ChIJDQzrOL-Rj4ARpkbFXepPwXc",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "convenience_store",
            "store",
            "food",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 24,
          "vicinity": "16552 East 14th Street, San Leandro"
        },
        {
          "business_status": "OPERATIONAL",
          "geometry": {
            "location": {
              "lat": 37.79853019999999,
              "lng": -122.4445552
            },
            "viewport": {
              "northeast": {
                "lat": 37.7999861802915,
                "lng": -122.4431288197085
              },
              "southwest": {
                "lat": 37.7972882197085,
                "lng": -122.4458267802915
              }
            }
          },
          "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
          "icon_background_color": "#909CE1",
          "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
          "name": "Fuel 24:7 - Lombard",
          "opening_hours": {
            "open_now": true
          },
          "photos": [
            {
              "height": 1545,
              "html_attributions": [
                "<a href=\"https://maps.google.com/maps/contrib/107721404123505875377\">Trap Speed 1320</a>"
              ],
              "photo_reference": "AWYs27zDr1z8koTLIud2sq5y5K_MTJ89qN0ECyUyK4yXj3jgd0wIJEMQo91Y8CHUGwMiJcX8S-GDQspJ0v9LIz-8XpnEXrleaUf1jya3d0BwIz_Q3o8OV8lEDYpKp5pZGSmtoPRI1xksHb-fCLozwGDUseAHv4_ceaxRmIRD_UNBKS12MLOQ",
              "width": 2060
            }
          ],
          "place_id": "ChIJ-ThdjtSAhYARQA0ggZORD1w",
          "plus_code": {
            "compound_code": "QHX4+C5 Cow Hollow, San Francisco, CA, USA",
            "global_code": "849VQHX4+C5"
          },
          "rating": 3.7,
          "reference": "ChIJ-ThdjtSAhYARQA0ggZORD1w",
          "scope": "GOOGLE",
          "types": [
            "gas_station",
            "atm",
            "convenience_store",
            "finance",
            "store",
            "food",
            "point_of_interest",
            "establishment"
          ],
          "user_ratings_total": 61,
          "vicinity": "2601 Lombard Street, San Francisco"
        }
      ]
    }
  ]
}
```








