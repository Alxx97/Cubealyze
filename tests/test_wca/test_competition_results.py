import pytest


def test_init(competition_results_atl_sigi, competition_results_atl_cube_central):
    assert competition_results_atl_sigi.competition_id == "SIGI2015"
    assert competition_results_atl_sigi.event_ids == {"333", "222", "444"}

    # fmt: off
    assert competition_results_atl_cube_central.competition_id == "CubeCentralYucatan2024"
    assert competition_results_atl_cube_central.event_ids == {"333", "222", "444", "555", "666"}
    # fmt: on


def test_setter_all_event_round_result(
    competition_results_atl_sigi, competition_results_atl_cube_central
):
    with pytest.raises(expected_exception=AttributeError):
        competition_results_atl_sigi.all_event_round_results = []
        competition_results_atl_cube_central.all_event_round_results = []


def test_deleter_all_event_round_result(
    competition_results_atl_sigi, competition_results_atl_cube_central
):
    with pytest.raises(expected_exception=AttributeError):
        del competition_results_atl_sigi.all_event_round_results
        del competition_results_atl_cube_central.all_event_round_results


@pytest.mark.parametrize(
    "event_id, expected",
    [
        (
            "333",
            [
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
        ),
        (
            "222",
            [
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
        ),
        (
            "444",
            [
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
        ),
        (
            "555",
            [
                {
                    "round": "Final",
                    "position": 10,
                    "best": 4242,
                    "average": -1,
                    "format": "Average of 5",
                    "solves": [-1, -1, 4249, 4242, 4433],
                },
            ],
        ),
        ("777", []),
        ("123", []),
    ],
)
def test_get_event_result(competition_results_atl_cube_central, event_id, expected):
    assert competition_results_atl_cube_central.get_event_results(event_id) == expected


@pytest.mark.parametrize(
    "event_id, round_name, expected",
    [
        (
            "333",
            "First round",
            {
                "round": "First round",
                "position": 5,
                "best": 1165,
                "average": 1272,
                "format": "Average of 5",
                "solves": [1165, 1220, 1427, 1406, 1189],
            },
        ),
        ("333", "Final", {}),
        (
            "222",
            "Second round",
            {
                "round": "Second round",
                "position": 4,
                "best": 391,
                "average": 485,
                "format": "Average of 5",
                "solves": [475, 550, 429, 591, 391],
            },
        ),
    ],
)
# fmt: off
def test_get_round_results(competition_results_atl_cube_central, event_id, round_name, expected):
    assert (competition_results_atl_cube_central.get_round_results(event_id, round_name)== expected)
# fmt: on


@pytest.mark.parametrize(
    "event_id, expected",
    [
        ("222", 391),
        ("333", 974),
        ("444", 2991),
        ("555", 4242),
    ],
)
# fmt: off
def test_get_best_single_overall(competition_results_atl_cube_central, event_id, expected):
    assert competition_results_atl_cube_central.get_best_single_overall(event_id) == expected
# fmt: on


@pytest.mark.parametrize(
    "event_id, round_name, expected",
    [
        ("333", "Final", None),
        ("333", "First round", 1165),
        ("222", "Third round", None),
        ("555", "Final", 4242),
        ("666", "Final", -1),
    ],
)
# fmt: off
def test_get_best_single_by_round(competition_results_atl_cube_central, event_id, round_name, expected):
    assert competition_results_atl_cube_central.get_best_single_by_round(event_id, round_name) == expected
# fmt: on


@pytest.mark.parametrize(
    "event_id, expected",
    [
        ("222", 485),
        ("333", 1272),
        ("444", 4196),
        ("555", -1),
        ("666", 15679),
    ],
)
# fmt: off
def test_get_best_average_overall(competition_results_atl_cube_central, event_id, expected):
    assert competition_results_atl_cube_central.get_best_average_overall(event_id) == expected
# fmt: on
