from matchingEngine import *

engine = MatchingEngine()
engine.process_input("limit buy 10 100")
engine.process_input("limit sell 20 100")
engine.process_input("limit sell 20 200")
engine.process_input("market buy 150")
engine.process_input("market buy 200")
engine.process_input("market sell 200")