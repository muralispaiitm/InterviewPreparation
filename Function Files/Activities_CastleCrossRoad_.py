
class Activities_CastleCrossRoad_:
    def __int__(self, V):
        self.V = V
        self.Status_CCR = ""

        # -------------------------------------------------- Creating Place
        self.Place_CastleCrossroads = self.V.Place_CastleCrossroads
        TF = self.Place_CastleCrossroads.CreatePlace()
        if TF!=True:
            self.V.Display.Menu_Quit()

        # -------------------------------------------------- Characters
        self.Char_Bob = self.V.Char_Bob

        # -------------------------------------------------- Sounds
        self.SEffect_Danger1 = self.V.SEffect_Danger1

        # -------------------------------------------------- Camera Settings
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.CameraFocus(self.Place_CastleCrossroads.WestEnd)
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)
        self.Status_Bridge = " --> Bridge_Setup "

    def SC_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.Char_Bob.Enter(self.Place_CastleCrossroads.WestEnd)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.V.Char_Bob.Exit(self.Place_CastleCrossroads.EastEnd)
        TF = self.V.Set.Wait(1)
        TF = self.V.Set.FadeOut()
        TF = self.V.Display.Menu_Title_Set("To be Continued....")
        TF = self.V.Display.Menu_Show()
        TF = self.V.Set.EnableInput()
        return " --> Startup completed "

