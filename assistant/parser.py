from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

def build_parser():
    engine = IntentDeterminationEngine()

    # Intent: Turn on light
    intent_on = IntentBuilder("TurnOnIntent") \
        .require("Action") \
        .require("Device") \
        .build()

    engine.register_intent_parser(intent_on)

    # Entity registrations
    engine.register_entity("turn on", "Action")
    engine.register_entity("turn off", "Action")
    engine.register_entity("close", "Action")
    engine.register_entity("open", "Action")
    engine.register_entity("light", "Device")
    engine.register_entity("lamp", "Device")
    engine.register_entity("door", "Device")ç
    return engine
