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
            ("543",None)
        ]
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
            ("345", None)
        ]
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
            ("234", "country", None)
        ],
        ids=["222_s_WR", "333_s_CR", "444_s_NR", "222_s_TR", "234_s_NR",]
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
            ("234", "country", None)
        ],
        ids=["222_a_WR", "333_a_CR", "444_a_NR", "222_a_TR", "234_a_NR",]
)

def test_get_rank_average(wca_person_atl, event_id, level, expected):
    assert wca_person_atl.get_rank_average(event_id, level) == expected
