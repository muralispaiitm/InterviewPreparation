class Activities_CastleBedRoom_:
    def __init__(self, V):
        self.V = V
        self.Status_CBR = ""
        Task_Dress_Limit = 1
        Task_Money_Limit = 1
        Task_FirePlace_Limit = 1
        Task_City_Limit = 5         # Going City from Home is infinite but I kept temporarily 5 since, no one can go those many times.

        # -------------------------------------------------- Place
        self.Place_BobHouse = self.V.Place_BobHouse
        TF = self.Place_BobHouse.CreatePlace()
        if TF!=True:
            self.V.Display.Menu_Quit()
        # -------------------------------------------------- Character
        self.Char_Bob = V.Char_Bob

        self.Char_Candy = self.V.Char_Candy
        TF = self.Char_Candy.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        self.Char_Lilly_S = self.V.Char_Lilly_S
        TF = self.Char_Lilly_S.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        # -------------------------------------------------- Positions of Characters
        self.V.Set.Position(self.Char_Candy.Name, self.Place_BobHouse.Closet)
        self.Char_Candy.Sleep(self.Place_BobHouse.Bed_Right)

        # -------------------------------------------------- Items
        # Clothes, Money, Key

        # -------------------------------------------------- Creating Visual Effects
        self.VEffect_Campfire = self.V.VEffect_Campfire
        self.VEffect_Campfire.CreateEffect(self.Place_BobHouse.Fireplace)

        # -------------------------------------------------- Creating Sound Effects
        self.SEffect_Fireball = self.V.SEffect_Fireball
        self.SEffect_Pocket = self.V.SEffect_Pocket
        self.SEffect_Fireplace = self.V.SEffect_Fireplace
        self.SEffect_Dramatic = self.V.SEffect_Dramatic

        self.SEffect_DarkMagic = self.V.SEffect_DarkMagic
        self.SEffect_Ominous = self.V.SEffect_Ominous
        self.SEffect_Potion = self.V.SEffect_Potion
        self.SEffect_Spell2 = self.V.SEffect_Spell2
        self.SEffect_Error = self.V.SEffect_Error
        self.SEffect_Spooky = self.V.SEffect_Spooky

        # -------------------------------------------------- Icons
        self.Icon_Dress = self.V.Icon_Dress
        self.Icon_Money = self.V.Icon_Money
        self.Icon_FirePlace = self.V.Icon_FirePlace
        self.Icon_City = self.V.Icon_City

        # -------------------------------------------------- Enable Icons
        TF = self.Icon_Dress.EnableIcon(self.Place_BobHouse.Closet, True)
        TF = self.Icon_Money.EnableIcon(self.Place_BobHouse.Closet)

        TF = self.Icon_FirePlace.EnableIcon(self.Char_Lilly_S.Name, True)

        TF = self.Icon_City.EnableIcon(self.Place_BobHouse.Door, True)


        # -------------------------------------------------- Camera Setting
        TF = self.V.Set.CameraFocus(self.Place_BobHouse.Door)
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)
        self.Status_CBR = "CastleBedRoom Setup "

        # ============================================================================================================== Calling Show Menu Function

    def SC_ACBR_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.Char_Bob.Enter(self.Place_BobHouse.Door)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.V.Set.CameraMode('focus')
        TF = self.Char_Bob.SetExpression('scared')
        TF = self.SEffect_Dramatic.Play()
        TF = self.V.Set.CameraMode('track')
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.SmallTable)
        TF = self.Char_Bob.Face(self.Char_Candy.Name)
        TF = self.Char_Bob.Kneel(False)

        D_CBR01_Bob_Candy = self.V.D_CBR01_Bob_Candy_Talk_1
        TF = D_CBR01_Bob_Candy.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)
        #if ("Key" in camelotMessage) & ("Pause" in camelotMessage):
        #    D_CBR01_Bob_Candy.ClearDialog()
        #    D_CBR01_Bob_Candy.HideDialog()
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Door)
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Table)
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Bed)
        TF = self.Char_Bob.Face(self.Place_BobHouse.Door)
        TF = self.Char_Bob.Clap()
        TF = self.V.Set.CameraFocus(self.Place_BobHouse.Door)
        TF = self.Char_Lilly_S.Enter(self.Place_BobHouse.Door)
        TF = self.Char_Lilly_S.WalkTo(self.Char_Bob.Name)

        D_CBR02_Bob_LillyS = self.V.D_CBR02_Bob_LillyS_Talk
        TF = D_CBR02_Bob_LillyS.ShowDialogs(self.Char_Bob.Name, self.Char_Lilly_S.Name)
        #if ("Key" in camelotMessage) & ("Pause" in camelotMessage):
        #    D_CBR02_Bob_LillyS.ClearDialog()
        #    D_CBR02_Bob_LillyS.HideDialog()
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraMode('follow')
        self.Status_CBR += " --> SC_Task01_Start "
        TF = self.SEffect_Dramatic.Stop()
        return self.Status_CBR

    def UC_Task00_Select_Task(self):
        TF = self.V.Set.EnableInput()
        TF = self.V.SEffect_Ominous.Play()
        count = 0
        while True:
            camelotMessage = input()
            if ("Icon Dress" in camelotMessage) or ("Dress" in camelotMessage):
                self.Status_CBR += " --> Dress "
                self.Status_CBR += self.SC_Task03_CBR_Closet_Task_Dress()
                count += 1
            if ("Icon Money" in camelotMessage) or ("Money" in camelotMessage):
                self.Status_CBR += " --> Money "
                self.Status_CBR += self.SC_Task04_CBR_Closet_Task_Money()
                count += 1
            if ("Icon FirePlace" in camelotMessage) or ("FirePlace" in camelotMessage):
                self.Status_CBR += self.SC_Task05_CBR_LillyS_Task_FirePlace()
                self.Status_CBR += " --> FirePlace "
                count += 1
            if ("Icon City" in camelotMessage) or ("City" in camelotMessage):
                self.Status_CBR += self.SC_Task06_CBR_Door_Task_City()
                self.Status_CBR += " --> City "
                count += 1
                TF = self.V.SEffect_Ominous.Stop()
                return self.Status_CBR

    def SC_Task03_CBR_Closet_Task_Dress(self):
        TF = self.V.Set.DisableInput()
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Closet)
        TF = self.Char_Bob.SetClothing("Noble")
        TF = self.SEffect_Pocket.Play()
        TF = self.V.Icon_Dress.DisableIcon()
        TF = self.V.Set.EnableInput()
        return " --> Dress Changed "

    def SC_Task04_CBR_Closet_Task_Money(self):
        TF = self.V.Set.DisableInput()
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Closet)
        TF = self.Char_Bob.SetClothing("Noble")
        TF = self.SEffect_Pocket.Play()
        TF = self.Icon_Money.DisableIcon()
        TF = self.V.Set.EnableInput()
        return " --> Money Taken "

    def SC_Task05_CBR_LillyS_Task_FirePlace(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Set.CameraFocus(self.Char_Lilly_S.Name)
        TF = self.V.Set.CameraMode('track')

        TF = self.Char_Lilly_S.WalkTo(self.Place_BobHouse.Fireplace)
        TF = self.Char_Lilly_S.Kneel()
        TF = self.SEffect_Fireball.Play()
        TF = self.VEffect_Campfire.EnableEffect()
        TF = self.SEffect_Fireplace.Play()
        TF = self.Icon_FirePlace.DisableIcon()

        TF = self.Char_Lilly_S.WalkTo(self.Place_BobHouse.SmallTable)
        TF = self.Char_Lilly_S.Kneel(True)

        TF = self.V.Set.EnableInput()
        return " --> FirePlace Enabled Fire "

    def SC_Task06_CBR_Door_Task_City(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.Char_Bob.Exit(self.Place_BobHouse.Door)
        return " --> Exit from Door to City "


'''from GlobalVariables import Variables
V = Variables()
S = ""
ABFC = Activities_CastleBedRoom_(V)
S += ABFC.SC_Task01_Start()
print(S)
S += ABFC.UC_Task02_CBR_Tasks()
print(S)'''