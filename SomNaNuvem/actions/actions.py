from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDeterminarAjuda(Action):

    def name(self) -> Text:
        return "action_determinar_ajuda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        problema = tracker.get_slot("problema")

        if problema:
            dispatcher.utter_message(text=f"Entendi que o problema é '{problema}'. Um momento, analisando a melhor forma de ajudar.")
        else:
            dispatcher.utter_message(text="Você pode me dizer qual é o problema para que eu possa ajudar melhor?")

        return []
