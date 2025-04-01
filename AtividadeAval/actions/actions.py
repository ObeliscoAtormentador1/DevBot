from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSolucionarProblema(Action):
    def name(self) -> Text:
        return "action_solucionar_problema"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        problema = tracker.get_slot("problema")
        setor = self.obter_solucao(problema)
        if setor:
            dispatcher.utter_message(text=f"Em caso de problema sobre {problema}, entre em contato com {','.join(setor)}")
        else:
            dispatcher.utter_message(text="Desculpe, não consigo te ajudar, irei te transferir para um atendente humano.")

        return []
    


    def obterSolucoes(self, problema: Text) -> List[Text]:
        setorporproblema = {
            "app": ["Em caso de problemas com o app, tente limpar o cache de seu navegador, se o problema persistir entre em contato com o número 0800 777666"],
            "conta": ["Caso sua conta não esteja logando, cheque as credenciais, se persistir, entre em contato com o número 0800 888999"],
            "plano": ["Para a mudança de plano, entre em contato com o número 0800 111222"] 
        }
        return obterSolucoes.get(problema.lower(), [])
