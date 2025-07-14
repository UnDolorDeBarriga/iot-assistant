from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

def parser_text(parser, text, min_confidence=0.6):
    last_intent = None
    for intent in parser.determine_intent(text):
        confidence = intent.get("confidence", 1.0)
        print(f"[INTENT] Parsed: {intent} (confidence: {confidence:.2f})")
        if confidence >= min_confidence:
            last_intent = intent
    return last_intent


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
    engine.register_entity("door", "Device")
    engine.register_entity("window", "Device")
    return engine
