from typing import Dict, Set, List, Any


class CompetitionResults:
    def __init__(self, competition_id: str, all_event_results: Dict):
        """
        Represents the competition results for a WCAPerson.

        Args:
            competition_id (str): Competition ID.
            all_event_results (dict): Dictionary with results of all
                events, and all rounds.
        """
        self.competition_id: str = competition_id
        self.event_ids: Set[str] = set(all_event_results.keys())
        self._all_event_round_results: Dict[List[Dict]] = all_event_results

    @property
    def all_event_round_results(self) -> Dict:
        """
        Returns all event results.
        """
        return self._all_event_round_results

    @all_event_round_results.setter
    def all_event_round_results(self, new: Any):
        raise AttributeError("It is not allowed overwrite results!")

    @all_event_round_results.deleter
    def all_event_round_results(self):
        raise AttributeError("It is not allowed delete results!")

    def get_event_results(self, event_id: str) -> List[Dict]:
        """
        Returns the results for a given event for all rounds.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.

        Returns:
            List[Dict]: List of results for all rounds, and `[]` if no participation.
        """
        return self.all_event_round_results.get(event_id, [])

    def get_round_results(self, event_id: str, round_name: str) -> Dict:
        """
        Returns the results for a given event and for a given round.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.
            round_name (str, optional): Name of the round.

        Returns:
            dict: Result, and `{}` if there is no participacion.
        """
        event_result: List[Dict] = self.get_event_results(event_id)

        for round_result in event_result:
            if round_result["round"] == round_name:
                return round_result

        return {}

    def get_best_single_overall(self, event_id: str) -> int:
        """
        Returns the best single of competition by event.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.

        Returns:
            int: Best result overall, -1 if DNF and `None` if not participation.
        """
        event_result: List[Dict] = self.get_event_results(event_id)

        if event_result == []:
            return None

        bests_by_round = [r.get("best") for r in event_result]
        not_dnf_bests = [b for b in bests_by_round if b > 0]

        if not_dnf_bests:
            return min(not_dnf_bests)
        else:
            return -1

    def get_best_single_by_round(self, event_id: str, round_name: str) -> int:
        """
        Returns the best single for a given event and round.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.
            round_name (str): Name of the round.

        Returns:
            dict: Result, and return `None` if not participation.
        """
        round_results: dict = self.get_round_results(event_id, round_name)

        if round_results == {}:
            return None

        return round_results.get("best")

    def get_best_average_overall(self, event_id: str) -> int:
        """
        Returns the best single of competition by event.

        Args:
            event_id (str): WCA event ID, such as "222", "333", etc.

        Returns:
            int: Best average overall
        """

        event_result: List[Dict] = self.get_event_results(event_id)

        if event_result == []:
            return None

        avgs_by_round = [r.get("average") for r in event_result]
        not_dnf_avgs = [b for b in avgs_by_round if b > 0]

        if not_dnf_avgs:
            return min(not_dnf_avgs)
        else:
            return -1
