import sqlite3

conn = sqlite3.connect('animation.db')
c = conn.cursor()


footStepsList = []
footStepsLegList = []
footStepsMoveList = []
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")

footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])

id = 1
for line in footStepsLegList:
    c.execute("insert into boxsteplist values (%d,'','')"%(id))
    id = id + 1

chaStepsLegList = []
chaStepsMoveList = []
chaStepsLegList.append("LLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")

chaStepsMoveList.append([0.16, 0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([0.00, -0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([-0.04, -0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.00, 0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.16, 0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([0.00, -0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([-0.04, -0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.00, 0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])