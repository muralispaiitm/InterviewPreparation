
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ======================================================== ForestPath  ================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ForestPath_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]

        self.EastEnd = f"{self.Name}.EastEnd"
        self.Well = f"{self.Name}.Well"
        self.Plant = f"{self.Name}.Plant"
        self.DirtPile = F"{self.Name}.DirtPile"
        self.PathBlock = f"{self.Name}.PathBlock"
        self.WestEnd = f"{self.Name}.WestEnd"

    # Creating a Place ======================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========================================================= Bridge  ===================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Bridge_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]

        self.NorthEnd = f"{self.Name}.NorthEnd"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Flowers = f"{self.Name}.Flowers"
        self.SouthEnd = f"{self.Name}.SouthEnd"
        self.Woods = f"{self.Name}.Woods"
        self.SouthSign = f"{self.Name}.SouthSign"
        self.WestSign = f"{self.Name}.WestSign"
        self.NorthSign = f"{self.Name}.NorthSign"

    # Creating a Place =====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF
    
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ====================================================== CastleBedroom  ==============================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class CastleBedroom_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"] # BobHouse
        self.Type = place["Type"]
        self.Door = f"{self.Name}.Door" # BobHouse.Door
        self.Chest = f"{self.Name}.Chest"
        self.Couch = f"{self.Name}.Couch"
        self.Couch_Left = f"{self.Name}.Couch.Left"
        self.Couch_Right = f"{self.Name}.Couch.Right"
        self.Couch_Middle = f"{self.Name}.Couch.Seat"
        self.Fireplace = f"{self.Name}.Fireplace"
        self.Table = f"{self.Name}.Table"
        self.Table_Left = f"{self.Name}.Table.Left"
        self.Table_Right = f"{self.Name}.Table.Right"
        self.Table_FrontLeft = f"{self.Name}.Table.FrontLeft"
        self.Table_FrontRight = f"{self.Name}.Table.FrontRight"
        self.Table_BackLeft = f"{self.Name}.Table.BackLeft"
        self.Table_BackRight = f"{self.Name}.Table.BackRight"
        self.Chair_Right = f"{self.Name}.RightChair"
        self.Chair_Left = f"{self.Name}.LeftChair"
        self.SmallTable = f"{self.Name}.SmallTable"
        self.Bed = f"{self.Name}.Bed"
        self.Bed_Left = f"{self.Name}.Bed.Left"
        self.Bed_Middle = f"{self.Name}.Bed"
        self.Bed_Right = f"{self.Name}.Bed.Right"
        self.Closet = f"{self.Name}.Closet"


    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========================================================== City  ====================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class City_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"] # BobHouse
        self.Type = place["Type"]

        self.NorthEnd = f"{self.Name}.NorthEnd"
        self.GreenHouseDoor = f"{self.Name}.GreenHouseDoor"
        self.Bench = f"{self.Name}.Bench"
        self.Bench_Left = f"{self.Name}.Bench.Left"
        self.Bench_Right = F"{self.Name}.Bench.Right"
        self.Fountain = f"{self.Name}.Fountain"
        self.EastEnd = f"{self.Name}.EastEnd"
        self.BrownHouseDoor = f"{self.Name}.BrownHouseDoor"
        self.RedHouseDoor = f"{self.Name}.RedHouseDoor"
        self.BlueHouseDoor = f"{self.Name}.BlueHouseDoor"
        self.Barrel = f"{self.Name}.Barrel"
        self.Horse = f"{self.Name}.Horse"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Plant = f"{self.Name}.Plant"
        self.Alley = f"{self.Name}.Alley"
        self.Alley2 = f"{self.Name}.Alley2"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ================================================  CastleCrossRoads  =================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class CastleCrossroads_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]
        self.Gate = f"{self.Name}.Gate"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Right = f"{self.Name}.Right"
        self.Left = f"{self.Name}.Left"
        self.EastEnd = f"{self.Name}.EastEnd"
        self.Gate = f"{self.Name}.Gate"
        self.WestSign = f"{self.Name}.WestSign"
        self.EastSign = f"{self.Name}.EastSign"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF


