def getInstruction(block_data):
    if block_data < 1000:
        bank = 0
        tile = block_data
    else:
        block_data = str(block_data)
        bank = int(block_data[:-3])
        tile = int(block_data[-3:])
    if bank == 101:
        return {
            15: "Set Speed",
            21: "Number 0",
            22: "Number 1",
            23: "Number 2",
            24: "Number 3",
            25: "Number 4",
            26: "Number 5",
            27: "Number 6",
            28: "Number 7",
            29: "Number 8",
            30: "Number 9",
            37: "Walk",
            38: "Turn Left",
            39: "Turn Right",
            40: "Baltie Invisible",
            41: "Baltie Visible",
            42: "Wait 0.1 Sec",
            43: "Wait For Input",
            44: "Clear/Load Scene",
            45: "Play A Sound",
            68: "Times [X symbol]",
            69: "Open Bracket [(]",
            70: "Close Bracket [)]",
            71: "Comment",
            72: "Face Right",
            73: "Face Down",
            74: "Face Left",
            75: "Face Up",
            82: "Empty Space",
            83: "Next Line",
            88: "Disable Cloud",
            89: "Enable Cloud",
        }[tile]
    else:
        if tile <= 150:
            return "Place tile "+str(tile)+" from bank "+str(bank)
        else:
            return "Corrupted block"