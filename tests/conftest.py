from pathlib import Path
import sys

import pytest

sys.path.append(
    Path(__file__).absolute().parent.parent.__str__()
)

from src.wca import WCAPerson

wca_data_atl: dict = {
    "id": "2015LUNA02",
    "name": "Alexis Tepale Luna",
    "slug": "alexis-tepale-luna",
    "country": "MX",
    "numberOfCompetitions": 6,
    "competitionIds": [
        "CubeCentralYucatan2024",
        "LosFuertesPuebla2024",
        "PuebladeZaragozaOpen2024",
        "SIGI2015",
        "VolcanoinPuebla2023",
        "ZaragozaOpen2023",
    ],
    "numberOfChampionships": 0,
    "championshipIds": [],
    "rank": {
        "singles": [
            {
                "eventId": "222",
                "best": 183,
                "rank": {"world": 5722, "continent": 1551, "country": 96},
            },
            {
                "eventId": "333",
                "best": 888,
                "rank": {"world": 10749, "continent": 2821, "country": 189},
            },
            {
                "eventId": "444",
                "best": 2991,
                "rank": {"world": 1769, "continent": 455, "country": 40},
            },
            {
                "eventId": "555",
                "best": 7232,
                "rank": {"world": 4302, "continent": 1108, "country": 122},
            },
            {
                "eventId": "666",
                "best": 13886,
                "rank": {"world": 2732, "continent": 753, "country": 83},
            },
            {
                "eventId": "777",
                "best": 33250,
                "rank": {"world": 7194, "continent": 2028, "country": 241},
            },
        ],
        "averages": [
            {
                "eventId": "222",
                "best": 485,
                "rank": {"world": 24002, "continent": 6753, "country": 444},
            },
            {
                "eventId": "333",
                "best": 1168,
                "rank": {"world": 14973, "continent": 3847, "country": 275},
            },
            {
                "eventId": "444",
                "best": 4196,
                "rank": {"world": 5386, "continent": 1330, "country": 135},
            },
            {
                "eventId": "555",
                "best": 8218,
                "rank": {"world": 4707, "continent": 1207, "country": 136},
            },
            {
                "eventId": "666",
                "best": 15679,
                "rank": {"world": 3256, "continent": 910, "country": 103},
            },
        ],
    },
    "results": {
        "CubeCentralYucatan2024": {
            "333": [
                {
                    "round": "Second round",
                    "position": 12,
                    "best": 974,
                    "average": 1455,
                    "format": "Average of 5",
                    "solves": [974, 1394, 2238, 1835, 1137],
                },
                {
                    "round": "First round",
                    "position": 5,
                    "best": 1165,
                    "average": 1272,
                    "format": "Average of 5",
                    "solves": [1165, 1220, 1427, 1406, 1189],
                },
            ],
            "222": [
                {
                    "round": "Final",
                    "position": 4,
                    "best": 498,
                    "average": 506,
                    "format": "Average of 5",
                    "solves": [500, 498, 501, 517, 561],
                },
                {
                    "round": "Second round",
                    "position": 4,
                    "best": 391,
                    "average": 485,
                    "format": "Average of 5",
                    "solves": [475, 550, 429, 591, 391],
                },
                {
                    "round": "First round",
                    "position": 7,
                    "best": 431,
                    "average": 498,
                    "format": "Average of 5",
                    "solves": [561, 431, 502, 647, 431],
                },
            ],
            "444": [
                {
                    "round": "Final",
                    "position": 2,
                    "best": 2991,
                    "average": 4196,
                    "format": "Average of 5",
                    "solves": [2991, 4098, 4249, 4242, 4433],
                },
                {
                    "round": "First round",
                    "position": 4,
                    "best": 3511,
                    "average": 4446,
                    "format": "Average of 5",
                    "solves": [4196, 5316, 4324, 3511, 4817],
                },
            ],
        },
        "PuebladeZaragozaOpen2024": {
            "333": [
                {
                    "round": "Second round",
                    "position": 22,
                    "best": 1051,
                    "average": 1222,
                    "format": "Average of 5",
                    "solves": [1277, 1200, 1051, 1262, 1205],
                },
                {
                    "round": "First round",
                    "position": 22,
                    "best": 888,
                    "average": 1168,
                    "format": "Average of 5",
                    "solves": [1266, 1088, 1526, 888, 1150],
                },
            ],
            "444": [
                {
                    "round": "First round",
                    "position": 19,
                    "best": 3626,
                    "average": 4325,
                    "format": "Average of 5",
                    "solves": [4479, 4076, 4854, 3626, 4419],
                }
            ],
            "666": [
                {
                    "round": "Final",
                    "position": 18,
                    "best": 13886,
                    "average": 15679,
                    "format": "Mean of 3",
                    "solves": [16692, 16459, 13886, 0, 0],
                }
            ],
            "777": [
                {
                    "round": "First round",
                    "position": 31,
                    "best": 37999,
                    "average": 0,
                    "format": "Mean of 3",
                    "solves": [37999, 0, 0, 0, 0],
                }
            ],
        },
        "LosFuertesPuebla2024": {
            "333": [
                {
                    "round": "Second round",
                    "position": 27,
                    "best": 1113,
                    "average": 1185,
                    "format": "Average of 5",
                    "solves": [1119, 1162, 1275, 1113, 1300],
                },
                {
                    "round": "First round",
                    "position": 24,
                    "best": 1084,
                    "average": 1184,
                    "format": "Average of 5",
                    "solves": [1085, 1270, 1393, 1084, 1196],
                },
            ],
            "222": [
                {
                    "round": "First round",
                    "position": 53,
                    "best": 183,
                    "average": 571,
                    "format": "Average of 5",
                    "solves": [694, 488, 183, 624, 600],
                }
            ],
            "555": [
                {
                    "round": "First round",
                    "position": 19,
                    "best": 7232,
                    "average": 8218,
                    "format": "Average of 5",
                    "solves": [8221, 8525, 9478, 7909, 7232],
                }
            ],
        },
        "VolcanoinPuebla2023": {
            "333": [
                {
                    "round": "Second round",
                    "position": 31,
                    "best": 1133,
                    "average": 1253,
                    "format": "Average of 5",
                    "solves": [1228, 1352, 1133, 1256, 1274],
                },
                {
                    "round": "First round",
                    "position": 39,
                    "best": 1216,
                    "average": 1445,
                    "format": "Average of 5",
                    "solves": [1417, 1253, 1933, 1665, 1216],
                },
            ],
            "444": [
                {
                    "round": "Second round",
                    "position": 18,
                    "best": 4044,
                    "average": 4323,
                    "format": "Average of 5",
                    "solves": [4614, 4548, 4190, 4044, 4231],
                },
                {
                    "round": "First round",
                    "position": 17,
                    "best": 4026,
                    "average": 4310,
                    "format": "Average of 5",
                    "solves": [4026, 4190, 4135, 5128, 4604],
                },
            ],
            "777": [
                {
                    "round": "Final",
                    "position": 32,
                    "best": 33250,
                    "average": 0,
                    "format": "Mean of 3",
                    "solves": [33250, 0, 0, 0, 0],
                }
            ],
        },
        "ZaragozaOpen2023": {
            "333": [
                {
                    "round": "Second round",
                    "position": 24,
                    "best": 1290,
                    "average": 1332,
                    "format": "Average of 5",
                    "solves": [1347, 1324, 1290, 1389, 1326],
                },
                {
                    "round": "First round",
                    "position": 32,
                    "best": 1353,
                    "average": 1484,
                    "format": "Average of 5",
                    "solves": [1672, 1353, 1471, 1478, 1504],
                },
            ],
            "222": [
                {
                    "round": "First round",
                    "position": 31,
                    "best": 367,
                    "average": 597,
                    "format": "Average of 5",
                    "solves": [607, 665, 367, 632, 551],
                }
            ],
            "555": [
                {
                    "round": "First round",
                    "position": 26,
                    "best": 9599,
                    "average": 9825,
                    "format": "Average of 5",
                    "solves": [10755, 9615, 10005, 9599, 9856],
                }
            ],
            "777": [
                {
                    "round": "First round",
                    "position": 26,
                    "best": 36036,
                    "average": 0,
                    "format": "Mean of 3",
                    "solves": [36036, 0, 0, 0, 0],
                }
            ],
        },
        "SIGI2015": {
            "333": [
                {
                    "round": "Second round",
                    "position": 11,
                    "best": 1480,
                    "average": 1543,
                    "format": "Average of 5",
                    "solves": [1800, 1522, 1611, 1497, 1480],
                },
                {
                    "round": "First round",
                    "position": 16,
                    "best": 1334,
                    "average": 1651,
                    "format": "Average of 5",
                    "solves": [1334, 1759, 1546, 1744, 1663],
                },
            ],
            "222": [
                {
                    "round": "Final",
                    "position": 10,
                    "best": 372,
                    "average": 550,
                    "format": "Average of 5",
                    "solves": [596, 709, 527, 527, 372],
                },
                {
                    "round": "First round",
                    "position": 14,
                    "best": 456,
                    "average": 555,
                    "format": "Average of 5",
                    "solves": [516, 456, 568, 684, 581],
                },
            ],
            "444": [
                {
                    "round": "Final",
                    "position": 5,
                    "best": 4772,
                    "average": 5325,
                    "format": "Average of 5",
                    "solves": [5490, 5105, 5381, 5631, 4772],
                },
                {
                    "round": "First round",
                    "position": 3,
                    "best": 4153,
                    "average": 4828,
                    "format": "Average of 5",
                    "solves": [4418, 5272, 4794, 5334, 4153],
                },
            ],
        },
    },
    "medals": {"gold": 0, "silver": 1, "bronze": 0},
    "records": {"single": [], "average": []},
}

@pytest.fixture
def wca_person_atl() -> WCAPerson:
    return WCAPerson(wca_data_atl)
