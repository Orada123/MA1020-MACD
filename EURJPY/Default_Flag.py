import json

Trigger_Flags = {}

Trigger_Flags["Buy_flag"] = False
Trigger_Flags["Sell_flag"] = False

file_name = "Trigger_Flags.json"
with open(file_name, "w") as f_obj:
    json.dump(Trigger_Flags, f_obj)

Crossing_Flags_EMA = {}

Crossing_Flags_EMA['Cross_Up'] = False
Crossing_Flags_EMA['Cross_Down'] = False

file_name = "Crossing_Flags_EMA.json"

with open(file_name, "w") as f_obj:
    json.dump(Crossing_Flags_EMA, f_obj)

Crossing_Flags_MACD = {}

Crossing_Flags_MACD['Cross_Up'] = False
Crossing_Flags_MACD['Cross_Down'] = False

file_name = "Crossing_Flags_MACD.json"

with open(file_name, "w") as f_obj:
    json.dump(Crossing_Flags_MACD, f_obj)