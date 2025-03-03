from collections import defaultdict
from typing import Dict, List
from objectives.violation_number.oracles.OracleInterface import OracleInterface


class OracleManager:
    __topic_oracle_mapping: Dict[str, List[OracleInterface]]
    __registered_oracles: List[OracleInterface]

    def __init__(self) -> None:
        self.__topic_oracle_mapping = defaultdict(lambda: list())
        self.__registered_oracles = list()

    def register_oracle(self, oracle: OracleInterface):
        self.__registered_oracles.append(oracle)
        for topic in oracle.get_interested_topics():
            self.__topic_oracle_mapping[topic].append(oracle)

    def on_new_message(self, topic, message, t):
        for oracle in self.__topic_oracle_mapping[topic]:
            oracle.on_new_message(topic, message, t)

    def get_results(self):
        result = list()
        for oracle in self.__registered_oracles:
            result += oracle.get_result()

        failure_type_list = [violation.main_type for violation in result if "Failure" in violation.main_type]

        filtered_result = []
        for violation in result:
            if violation.main_type == "ModuleDelayOracle" and violation.key_label + "Failure" in failure_type_list:
                pass
            else:
                filtered_result.append(violation)

        return filtered_result

    def get_counts_wrt_oracle(self) -> dict:
        result = dict()
        for oracle in self.__registered_oracles:
            result[oracle.__class__.__name__] = len(oracle.get_result())
        return result
