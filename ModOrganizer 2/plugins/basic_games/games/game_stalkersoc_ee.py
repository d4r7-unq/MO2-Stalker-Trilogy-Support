from ..basic_game import BasicGame

class StalkerSoCGame(BasicGame):
    Name = "S.T.A.L.K.E.R. Shadow of Chernobyl EE Support Plugin"
    Author = "DIGIT4L_RA7EN"
    Version = "0.1"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Shadow of Chernobyl EE."

    GameName = "S.T.A.L.K.E.R.: Shadow of Chernobyl EE"
    GameShortName = "stalkershadowofchernobylee"
    GameNexusName = "stalkershadowofchernobylee"

    GameBinary = "%GAME_PATH%/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%USERPROFILE%\Saved Games\STALKER Shadow of Chornobyl - EE\STEAM"
    GameIniFiles= "%USERPROFILE%\Saved Games\STALKER Shadow of Chornobyl - EE\STEAM/user.ltx"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%USERPROFILE%\Saved Games\STALKER Shadow of Chornobyl - EE\STEAM/savedgames"

    GameSteamId = 2427410