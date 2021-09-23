from typing import DefaultDict


def getInstruction(x,y):
    if y == 138:
        return {
            151: "Set Speed",
            157: "Number 0",
            158: "Number 1",
            159: "Number 2",
            160: "Number 3",
            161: "Number 4",
            162: "Number 5",
            163: "Number 6",
            164: "Number 7",
            165: "Number 8",
            166: "Number 9",
            173: "Walk",
            174: "Turn Left",
            175: "Turn Right",
            176: "Baltie Invisible",
            177: "Baltie Visible",
            178: "Wait 0.1 Sec",
            179: "Wait For Input",
            180: "Clear/Load Scene",
            181: "Play A Sound",
            204: "Times [X symbol]",
            205: "Open Bracket [(]",
            206: "Close Bracket [)]",
            207: "Comment",
            208: "Face Right",
            209: "Face Down",
            210: "Face Left",
            211: "Face Up",
            218: "Empty",
            219: "Next Line",
            224: "Disable Cloud",
            225: "Enable Cloud",
            DefaultDict: "Unknown Block"
        }[x]
    else:
        return "Place "+str(x)