import pytest


def test_init(wca_person_atl):
    assert wca_person_atl.wca_id == "2015LUNA02"
    assert wca_person_atl.name == "Alexis Tepale Luna"
    assert wca_person_atl.country == "MX"
    assert wca_person_atl.number_of_competitions == 6
    assert wca_person_atl.competitions == [
        "CubeCentralYucatan2024",
        "LosFuertesPuebla2024",
        "PuebladeZaragozaOpen2024",
        "SIGI2015",
        "VolcanoinPuebla2023",
        "ZaragozaOpen2023",
    ]


def test_categories(wca_person_atl):
    assert wca_person_atl.categories == {"222", "333", "444", "555", "666", "777"}


@pytest.mark.parametrize(
    "event_id, expected",
    [
        ("222", 183),
        ("333", 888),
        ("444", 2991),
        ("555", 7232),
        ("666", 13886),
        ("777", 33250),
        ("888", None),
        ("543", None),
    ],
)
def test_get_best_single(wca_person_atl, event_id, expected):
    assert wca_person_atl.get_best_single(event_id) == expected


@pytest.mark.parametrize(
    "event_id, expected",
    [
        ("222", 485),
        ("333", 1168),
        ("444", 4196),
        ("555", 8218),
        ("666", 15679),
        ("777", None),
        ("888", None),
        ("345", None),
    ],
)
def test_get_best_average(wca_person_atl, event_id, expected):
    assert wca_person_atl.get_best_average(event_id) == expected


@pytest.mark.parametrize(
    "event_id, level, expected",
    [
        ("222", "world", 5722),
        ("333", "continent", 2821),
        ("444", "country", 40),
        ("222", "town", None),
        ("234", "country", None),
    ],
    ids=[
        "222_s_WR",
        "333_s_CR",
        "444_s_NR",
        "222_s_TR",
        "234_s_NR",
    ],
)
def test_get_rank_single(wca_person_atl, event_id, level, expected):
    assert wca_person_atl.get_rank_single(event_id, level) == expected


@pytest.mark.parametrize(
    "event_id, level, expected",
    [
        ("222", "world", 5722),
        ("333", "continent", 2821),
        ("444", "country", 40),
        ("222", "town", None),
        ("234", "country", None),
    ],
    ids=[
        "222_a_WR",
        "333_a_CR",
        "444_a_NR",
        "222_a_TR",
        "234_a_NR",
    ],
)
def test_get_rank_average(wca_person_atl, event_id, level, expected):
    assert wca_person_atl.get_rank_average(event_id, level) == expected


@pytest.mark.parametrize(
    "event_id, expected",
    [
        (
            "333",
            {
                "CubeCentralYucatan2024": 974,
                "PuebladeZaragozaOpen2024": 888,
                "LosFuertesPuebla2024": 1084,
                "VolcanoinPuebla2023": 1133,
                "ZaragozaOpen2023": 1290,
                "SIGI2015": 1334,
            },
        ),
        (
            "444",
            {
                "CubeCentralYucatan2024": 2991,
                "PuebladeZaragozaOpen2024": 3626,
                "VolcanoinPuebla2023": 4026,
                "SIGI2015": 4153,
            },
        ),
        ("666", {"PuebladeZaragozaOpen2024": 13886}),
        (
            "777",
            {
                "PuebladeZaragozaOpen2024": 37999,
                "VolcanoinPuebla2023": 33250,
                "ZaragozaOpen2023": 36036,
            },
        ),
        ("123", {}),
    ],
)
def test_get_competition_best_singles(wca_person_atl, event_id, expected):
    assert wca_person_atl.get_competition_best_singles(event_id) == expected


@pytest.mark.parametrize(
    "event_id, expected",
    [
        (
            "222",
            {
                "CubeCentralYucatan2024": 485,
                "LosFuertesPuebla2024": 571,
                "ZaragozaOpen2023": 597,
                "SIGI2015": 550,
            },
        ),
        (
            "333",
            {
                "CubeCentralYucatan2024": 1272,
                "PuebladeZaragozaOpen2024": 1168,
                "LosFuertesPuebla2024": 1184,
                "VolcanoinPuebla2023": 1253,
                "ZaragozaOpen2023": 1332,
                "SIGI2015": 1543,
            },
        ),
        (
            "444",
            {
                "CubeCentralYucatan2024": 4196,
                "PuebladeZaragozaOpen2024": 4325,
                "VolcanoinPuebla2023": 4310,
                "SIGI2015": 4828,
            },
        ),
        ("555", {"LosFuertesPuebla2024": 8218, "ZaragozaOpen2023": 9825}),
        ("666", {"PuebladeZaragozaOpen2024": 15679}),
        (
            "777",
            {
                "PuebladeZaragozaOpen2024": 0,
                "VolcanoinPuebla2023": 0,
                "ZaragozaOpen2023": 0,
            },
        ),
        ("888", {}),
    ],
)
def test_get_best_averages_of_all_competitions(wca_person_atl, event_id, expected):
    assert wca_person_atl.get_best_averages_of_all_competitions(event_id) == expected

@pytest.mark.parametrize(
    "event_id, expected",
    [
        ("333", {
            "CubeCentralYucatan2024": [974, 1394, 2238, 1835, 1137, 1165, 1220, 1427, 1406, 1189],
            "LosFuertesPuebla2024": [1119, 1162, 1275, 1113, 1300, 1085, 1270, 1393, 1084, 1196],
            "PuebladeZaragozaOpen2024": [1277, 1200, 1051, 1262, 1205, 1266, 1088, 1526, 888, 1150],
            "SIGI2015": [1800, 1522, 1611, 1497, 1480, 1334, 1759, 1546, 1744, 1663],
            "VolcanoinPuebla2023": [1228, 1352, 1133, 1256, 1274, 1417, 1253, 1933, 1665, 1216],
            "ZaragozaOpen2023": [1347, 1324, 1290, 1389, 1326, 1672, 1353, 1471, 1478, 1504],
        })
    ]
)
def test_get_all_singles_by_competition(wca_person_atl, event_id, expected):
    assert wca_person_atl.get_all_singles_by_competition(event_id) == expected