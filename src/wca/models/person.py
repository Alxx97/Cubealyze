from typing import List, Dict, Set


class WCAPerson:
    def __init__(self, wca_data: dict):
        """
        Initialize a `Person` object which stores WCA official results
        and shows results.

        Args:
            wca_data (dict): Response from WCA no-official
                API for person by id.

        Notes:
            All results are presented in centiseconds.
        """
        self.wca_id: str = wca_data.get("id")
        self.name: str = wca_data.get("name")
        self.slug: str = wca_data.get("slug")
        self.country: str = wca_data.get("country")

        self.competitions: List[str] = wca_data.get("competitionIds", [])
        self.number_of_competitions: int = wca_data.get("numberOfCompetitions", 0)
        self.results_raw: Dict = wca_data.get("results", {})

        self.rank_singles = {
            r["eventId"]: r for r in wca_data.get("rank", {}).get("singles", [])
        }
        self.rank_averages = {
            r["eventId"]: r for r in wca_data.get("rank", {}).get("averages", [])
        }

        self.medals = wca_data.get("medals")

    @property
    def categories(self) -> Set[str]:
        """
        Returns the categories which person has compited.

        Returns:
            set:
        """
        return set(self.rank_averages.keys()).union(self.rank_singles.keys())

    def get_best_single(self, event_id: str) -> int:
        """
        Returns the best single for a given event (in centiseconds).

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.

        Returns:
            int: Best single. Returns `None` if competitor has no participations
                in that event.
        """
        return self.rank_singles.get(event_id, {}).get("best")

    def get_best_average(self, event_id: str) -> int:
        """
        Returns the best average for a given event (in centiseconds).

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.

        Returns:
            int: Best average. Returns `None` if competitor has no participations
                in that event.
        """
        return self.rank_averages.get(event_id, {}).get("best")

    def get_rank_single(self, event_id: str, level: str) -> int:
        """
        Returns the rank of single by even, and by level, e.g.,
        by World, Continent, or Country.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.
            level (str): Level of rank, "world", "continent", "country".

        Returns:
            int: Rank of single. Returns `None` if competitor has no participations
                or event_id/level is not valid.
        """
        return self.rank_singles.get(event_id, {}).get("rank", {}).get(level)

    def get_rank_average(self, event_id: str, level: str) -> int:
        """
        Returns the rank of average by event, and by level, e.g.,
        by World, Continent, or Country.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.
            level (str): Level of rank, "world", "continent", "country".

        Returns:
            int: Rank of average. Returns `None` if competitor has no participations
                or event_id/level is not valid.
        """
        return self.rank_singles.get(event_id, {}).get("rank", {}).get(level)
