from ..basic_game import BasicGame

class StalkerCSGame(BasicGame):
    Name = "S.T.A.L.K.E.R.: Clear Sky EE Support Plugin"
    Author = "DIGIT4L_RA7EN"
    Version = "0.1"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Clear Sky EE."

    GameName = "S.T.A.L.K.E.R.: Clear Sky EE"
    GameShortName = "stalkerclearskyee"
    GameNexusName = "stalkerclearskyee"

    GameBinary = "%GAME_PATH%/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%USERPROFILE%\Saved Games\STALKER Clear Sky - EE\STEAM"
    GameIniFiles= "%USERPROFILE%\Saved Games\STALKER Clear Sky - EE\STEAM/user.ltx"
    GameSaveExtension = "scs"
    GameSavesDirectory = "%USERPROFILE%\Saved Games\STALKER Clear Sky - EE\STEAM/savedgames"

    GameSteamId = 2427420